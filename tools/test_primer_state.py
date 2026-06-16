#!/usr/bin/env python3
"""Unit tests for primer_state. Stdlib unittest — run: python3 tools/test_primer_state.py"""
import tempfile
import unittest
from datetime import date
from pathlib import Path

import primer_state as ps

TODAY = date(2026, 6, 16)


class TestSM2(unittest.TestCase):
    def test_first_success_is_one_day(self):
        s = ps.sm2(reps=0, interval=0, ef=2.5, quality=4, today=TODAY)
        self.assertEqual(s.reps, 1)
        self.assertEqual(s.interval, ps.FIRST_INTERVAL)
        self.assertEqual(s.due, date(2026, 6, 17))

    def test_second_success_is_six_days(self):
        s = ps.sm2(reps=1, interval=1, ef=2.5, quality=4, today=TODAY)
        self.assertEqual(s.reps, 2)
        self.assertEqual(s.interval, ps.SECOND_INTERVAL)

    def test_third_success_grows_by_ease(self):
        # reps>=2: interval = round(prev_interval * ef)
        s = ps.sm2(reps=2, interval=6, ef=2.5, quality=4, today=TODAY)
        self.assertEqual(s.interval, 15)  # round(6 * 2.5) before ef adjust; ef at q4 unchanged
        self.assertEqual(s.reps, 3)

    def test_lapse_resets(self):
        s = ps.sm2(reps=5, interval=100, ef=2.2, quality=1, today=TODAY)
        self.assertEqual(s.reps, 0)
        self.assertEqual(s.interval, ps.FIRST_INTERVAL)
        self.assertEqual(s.due, date(2026, 6, 17))

    def test_ease_floor(self):
        # Repeated hard grades must not drive ef below the floor.
        ef = 1.3
        for _ in range(5):
            ef = ps.sm2(reps=2, interval=6, ef=ef, quality=3, today=TODAY).ef
        self.assertGreaterEqual(ef, ps.EF_MIN)

    def test_quality_from_label(self):
        self.assertEqual(ps.quality_from_label("good"), 4)
        self.assertEqual(ps.quality_from_label("FAIL"), 1)
        self.assertEqual(ps.quality_from_label("5"), 5)
        with self.assertRaises(ValueError):
            ps.quality_from_label("nope")


class TestPromptRoundTrip(unittest.TestCase):
    def test_parse_format_roundtrip(self):
        line = ("- due:2026-06-20 | int:6 | ef:2.50 | reps:3 | distributed-systems "
                "| Q:: What does Raft guarantee? | A:: At most one leader per term.")
        p = ps.parse_prompt(line)
        self.assertIsNotNone(p)
        self.assertEqual(p.domain, "distributed-systems")
        self.assertEqual(p.reps, 3)
        self.assertEqual(ps.format_prompt(p), line)

    def test_non_prompt_line_ignored(self):
        self.assertIsNone(ps.parse_prompt("## Prompts"))
        self.assertIsNone(ps.parse_prompt("- 2026-06-16 | 5/7 correct"))

    def test_new_prompt_due_today_unseen(self):
        p = ps.new_prompt("docker", "Q?", "A.", TODAY)
        self.assertEqual(p.due, TODAY)
        self.assertEqual(p.reps, 0)
        self.assertEqual(p.ef, ps.EF_DEFAULT)


class TestQueueOps(unittest.TestCase):
    def setUp(self):
        self.lines = [
            "# Review Queue", "", "## Prompts", "",
            "- due:2026-06-10 | int:6 | ef:2.50 | reps:2 | docker | Q:: q-old | A:: a",
            "- due:2026-07-01 | int:30 | ef:2.50 | reps:4 | docker | Q:: q-future | A:: a",
            "", "## Review history", "",
        ]

    def test_due_excludes_future(self):
        due = ps.due_prompts(self.lines, TODAY)
        self.assertEqual(len(due), 1)
        self.assertEqual(due[0][1].question, "q-old")

    def test_insert_prompt_under_header(self):
        out = ps.insert_prompt(self.lines, ps.new_prompt("ai", "newq", "newa", TODAY))
        prompts = [p for _, p in ps.find_prompts(out)]
        self.assertIn("newq", [p.question for p in prompts])
        # placed in the Prompts section, before Review history
        self.assertLess(out.index(ps.format_prompt(ps.new_prompt("ai", "newq", "newa", TODAY))),
                        out.index("## Review history"))


class TestDecay(unittest.TestCase):
    def test_stale_high_decays(self):
        line = "| dist | 2026-01-01 | solid on raft | high | lesson 2026-01-01 |"
        new_line, change = ps.decay_marker_line(line, TODAY, ps.DECAY_THRESHOLD_DAYS)
        self.assertIn("| med |", new_line)
        self.assertIn("reprobe", new_line)
        self.assertIsNotNone(change)
        # 'updated' date must not be bumped — decay is absence of evidence.
        self.assertIn("2026-01-01", new_line)

    def test_recent_high_unchanged(self):
        line = "| dist | 2026-06-10 | x | high | y |"
        new_line, change = ps.decay_marker_line(line, TODAY, ps.DECAY_THRESHOLD_DAYS)
        self.assertEqual(new_line, line)
        self.assertIsNone(change)

    def test_low_confidence_untouched(self):
        line = "| dist | 2026-01-01 | x | low | y |"
        _, change = ps.decay_marker_line(line, TODAY, ps.DECAY_THRESHOLD_DAYS)
        self.assertIsNone(change)


class TestRecalibrate(unittest.TestCase):
    def test_fires_on_misses(self):
        calib = [f"2026-06-1{i} | dist | too-advanced | x | y" for i in range(4)]
        d = ps.recalibrate_check(log_lines=[], calib_lines=calib)
        self.assertTrue(d.fire)
        self.assertEqual(d.misses, 4)

    def test_fires_on_lesson_cap(self):
        log = [f"2026-06-{10 + i:02d} | lesson | 60m | x" for i in range(8)]
        d = ps.recalibrate_check(log_lines=log, calib_lines=[])
        self.assertTrue(d.fire)
        self.assertEqual(d.lessons, 8)

    def test_below_thresholds_no_fire(self):
        log = ["2026-06-11 | lesson | 60m | x", "2026-06-12 | lesson | 60m | x"]
        calib = ["2026-06-11 | dist | pacing | x | y"]
        d = ps.recalibrate_check(log_lines=log, calib_lines=calib)
        self.assertFalse(d.fire)

    def test_counts_only_after_last_recalibrate(self):
        log = [
            "2026-06-01 | lesson | 60m | x",
            "2026-06-05 | recalibrate-minor | 3m | reset",
            "2026-06-10 | lesson | 60m | x",
        ]
        calib = ["2026-06-02 | d | x | y | z", "2026-06-11 | d | x | y | z"]
        d = ps.recalibrate_check(log_lines=log, calib_lines=calib)
        self.assertEqual(d.lessons, 1)  # only the 06-10 lesson, after the recalibrate
        self.assertEqual(d.misses, 1)   # only the 06-11 miss


class TestCLI(unittest.TestCase):
    """End-to-end: grade a due prompt through the CLI and confirm it reschedules."""
    def test_grade_reschedules_in_file(self):
        with tempfile.TemporaryDirectory() as d:
            data = Path(d)
            (data / "learner").mkdir()
            q = data / "learner" / "review-queue.md"
            q.write_text(
                "# Review Queue\n\n## Prompts\n\n"
                "- due:2026-06-10 | int:6 | ef:2.50 | reps:2 | docker | Q:: q | A:: a\n\n"
                "## Review history\n\n"
            )
            rc = ps.main(["--data-dir", str(data), "--on", "2026-06-16",
                          "review-grade", "--index", "0", "--quality", "good"])
            self.assertEqual(rc, 0)
            after = ps.due_prompts(q.read_text().splitlines(), date(2026, 7, 1))
            self.assertEqual(len(after), 1)
            self.assertGreater(after[0][1].interval, 6)   # interval grew
            self.assertEqual(after[0][1].reps, 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
