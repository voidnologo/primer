# Proposal 0002 — Deterministic state layer (scripts + SQLite) & habit-formation

**Date:** 2026-06-15
**Status:** decided & built (D-0020, Session 3). Source of truth = **markdown** (no DB); scheduler = **SM-2**;
Python stdlib; state layer before intake. `tools/primer_state.py` + tests shipped and wired into the engine.
Habit-formation track (§4) partly in place (Elicit-step anchor + proactive review offer); the rest rides real use.
**Author:** Session 3 (emerged from the Wave-D review discussion)
**Depends on / extends:** D-0018 (self-contained; bookkeeping is code), D-0019 (Goal 5: cultivate learning),
D-0015 (external anchor + decay), Proposal 0001.

> Two linked decisions surfaced while resolving Proposal 0001's Wave D, both from maintainer direction:
> (1) deterministic bookkeeping should be **code, not in-context LLM work** — scripts + an optional local
> SQLite DB are in-scope (D-0018); (2) **cultivating better learning habits is a project goal** (D-0019), so a
> self-contained review/retrieval capability is justified — to *build* the habit, not assume it. This proposal
> lays out the state-layer architecture and the habit-formation track, with the choices that need a decision.

---

## 1. Why this exists

Proposal 0001's Wave B added real arithmetic to the feedback loop: confidence **decay** (a time formula),
recalibration **triggers** (counting misses / lessons), review **scheduling** (interval math), and
miss-aggregation. Having the model do this by reading and rewriting markdown every session is the token/context
cost the maintainer flagged — and LLMs miscount and mis-date, so it's also *less reliable* than code.

Separately (Goal 5), the system should grow the learner's review/retrieval habit over time rather than require
it or abandon it. That needs a cheap, reliable record of *what is due*, *what's been recalled*, and *how the
learner's retention is trending* — exactly the structured state a script + DB handles well and an LLM handles
expensively.

## 2. What is deterministic vs. what is judgment

The split that decides what becomes code:

| Deterministic (→ scripts/DB) | Judgment (→ stays LLM + markdown) |
|---|---|
| Review scheduling: due dates, intervals (SM-2-lite / FSRS) | Whether a recall answer was *correct* (graded in-conversation) |
| Confidence decay over time | What a depth marker's prose *says* |
| Recalibration triggers: count misses / lessons since last | Which misses are a *pattern* worth promoting to a trait |
| Miss/score aggregation, "what's due", trend stats | Lesson content, framing, the Q&A narrative |
| Promotion bookkeeping (canon floor, status flips) | Whether a source is *load-bearing* / stale |

Rule of thumb: **counting, dating, and interval math are code; meaning is the model.** The model *calls* the
scripts (or reads their output) instead of recomputing state in-context.

## 3. The inspectability tension (the crux)

The research that validates primer's design also prizes a **hand-editable, git-diffable, grep-able** learner
model (Open Learner Models — Bull & Kay 2007; llm-knowledge-base's "markdown so it stays *yours*"). A SQLite
DB is none of those by default. So the real question is **source of truth**:

- **Option A — DB is source of truth** for structured volatile state (depth markers, calibration log, review
  schedule/history); markdown stays for narrative (lessons, `profile.md` stable traits, open-questions).
  Scripts render `/primer index`, `/primer profile`, "show my markers" from the DB, and **emit a markdown/CSV
  snapshot on every write** so git diffs and hand-inspection still work. *Lowest run cost; richest queries.*
  *Cost:* hand-editing means editing via a command, not a text file; the snapshot is a view, not the source.
- **Option B — markdown stays source of truth**; SQLite is a **derived cache** scripts rebuild from markdown
  for fast queries/scheduling. *Keeps full editability + git-diff + the OLM property.* *Cost:* a sync step and
  two stores to keep consistent; writes still touch markdown.
- **Option C — hybrid by concern.** Pure-computation state with no editing value (review schedule, score
  history, decay timestamps) lives in SQLite; everything a human reads or edits (depth markers, profile,
  calibration log, lessons) stays markdown, with scripts doing the *counting/dating* over it. *Smallest change;
  preserves editability where it matters; the DB holds only what nobody hand-edits.*

**Recommendation: C**, then revisit A if the markdown-counting scripts prove too fiddly. C captures most of the
cost/reliability win (the heavy arithmetic — scheduling, decay, triggers — leaves the context) while keeping
the learner model the inspectable markdown artifact the whole project is built around. A is the destination if
query needs outgrow markdown; B's dual-write tends to drift.

## 4. The habit-formation track (Goal 5)

Independent of the storage choice, what "cultivate the habit" concretely means:

- **Anchor rides the lesson (built, Proposal 0001):** every lesson opens with a recall of a prior invariant.
  A script picks *which* prior invariant is "due" for that domain; the model just asks and grades.
- **Proactive, in-register offer:** "you've a few recalls due — 90-second warm-up?" with a one-line *why*
  (retrieval > re-reading). Never nag; the desirable-difficulties illusion means learners undervalue it, so
  the system models the payoff rather than pressures.
- **Show the payoff:** surface the retention trend ("you nailed 3 of 3 four-week-old recalls") as a visible
  early win — the reinforcement-loop framing (engineer the win so the habit reinforces itself).
- **Ramp, don't front-load:** start with the in-lesson recall only; expand to optional warm-ups as the learner
  engages. Meta-learning tips (interleaving, spacing, the generation effect) surface as brief asides when
  relevant, not as a curriculum.

## 5. Scope decision needed (⚑)

Before any build:

1. **⚑ Source of truth** — A (DB-of-record + markdown snapshots), B (markdown-of-record + DB cache), or C
   (hybrid: computation in DB, human-readable state in markdown)? *Recommend C.*
2. **⚑ Scheduling algorithm** — SM-2-lite (simple expanding interval; ~20 lines) vs FSRS (better-calibrated,
   heavier; OpenTutor uses FSRS 4.5). *Recommend SM-2-lite first; it's self-contained and upgradeable.*
3. **⚑ Build order** — do this state layer *before* a real `/primer init` intake (so the first lessons write
   into it), or run an intake on the current markdown engine first and migrate after? *Recommend: build C +
   SM-2-lite first* (small), since intake writes the initial markers and review queue and we'd rather it
   write into the final shape.
4. **Language/runtime for scripts** — Python (matches the maintainer's stack; `sqlite3` stdlib, zero deps) vs
   shell. *Recommend Python, stdlib-only, committed in the public core under `tools/`; the DB lives in the
   private data repo.*

## 6. Coverage / disposition

| Item | Disposition |
|------|-------------|
| D-0018 self-contained; bookkeeping-as-code | Settled |
| D-0019 Goal 5 cultivate learning | Settled |
| Lesson-borne anchor (Elicit recall) | Built (Proposal 0001) |
| State-layer architecture (A/B/C) | ⚑ this proposal |
| Scheduler (SM-2-lite vs FSRS) | ⚑ this proposal |
| Proposal 0001 T3 (SRS story) | Resolved *into* this proposal — self-contained + in-repo, not Anki |
| Proposal 0001 E2 (situated-idea prompts), E4 (`/primer synthesize`) | Still deferred until post-use data |
| Proposal 0001 E3 (generation effect) | Queued; no decision needed |

## 7. Sources

OpenTutor (SQLite + FSRS 4.5 + BKT, local-first), DeepTutor (file-based L1→L2→L3 memory), llm-knowledge-base
(markdown-as-DB + confidence flags), Bull & Kay 2007 (Open Learner Models — editability/inspection),
Matuschak ("Why books don't work" — the medium owns the metacognitive scaffolding; situated ideas) — all in
`docs/engineering/research/2026-06-15-*.md`. SM-2 (SuperMemo) / FSRS as the scheduling options.
