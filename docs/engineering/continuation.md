# Continuation — fast resume

> Lean pointer for picking up primer dev. Read first at `session-start`. Kept short and current; history lives in `sessions/` and `DECISIONS.md`.

**Project:** primer — adaptive Primer-style learning system. Class/instance: public core (engine) + private per-user data repo (profile + lessons).

## Last session (3) — Cold review + implementation (Proposal 0001 Waves A & B)

- **Session 2** (review): fresh-eyes audit + two web research sweeps → durable research artifacts in
  `docs/engineering/research/` and `docs/engineering/proposals/0001-…md` (findings C1–C4, T1–T7, E1–E4 + plan).
- **Session 3** (implement): shipped Wave A (C4 effect-size correction, C3 canon edition tags, C1
  de-personalize the public engine), Wave B (C2 forgetting-aware confidence decay, T1 review→calibration
  external anchor, E1 review-score recording, T7 "just show me" escape hatch), and Wave C (T2 prompt-quality
  bar, T5 resume-path reconcile, T6 README privacy hardening, T4 evidence-triggered recalibration). Also added
  a "What's a Primer?" framing section to the README. Decisions D-0014–D-0017. Branch
  `proposal-0001-review-and-fixes` (Waves A–C committed).
- The engine is now learner-agnostic and the feedback loop has an external anchor (cold retrieval feeds
  confidence both ways; untouched high-confidence markers decay) — closing the closed-self-assessment drift.

Then a design conversation (still Session 3) added two goals and an architecture proposal:
- **D-0018** self-contained (no required external tools; scripts + local SQLite are in-scope; deterministic
  bookkeeping is code, not in-context LLM work). **D-0019 / Goal 5** cultivate better learning *habits*, not
  just content. Anchor reworked onto the lesson flow (Elicit-step recall); `/primer review` is now optional +
  habit-building. T3 resolved into self-contained in-repo scheduling (not Anki).
- **Proposal 0002** written *and decided & built* (D-0020): markdown stays source of truth (no SQLite —
  binary-in-git breaks cross-machine sync), SM-2 scheduler, Python stdlib. Built `tools/primer_state.py`
  (review scheduling, marker decay, recalibrate-check) + 19 passing tests + `tools/README.md`; wired into
  SKILL.md / feedback-protocol.md / review-queue template. E3 (generation effect) also shipped.

## Next up

- **Run a real `/primer init`** intake against the de-personalized engine, writing into the new state layer —
  the first true end-to-end exercise. Verify `init-instance.sh` seeds the new `review-queue.md` format.
- E2/E4 still deferred until post-use data; remaining habit-formation surface grows with use.
- Branch `proposal-0001-review-and-fixes` (pushed); **not yet merged to `main`** — rebase first, `origin/main`
  advanced to `1188833` while we worked.

## Don't re-litigate

`DECISIONS.md` D-0001…D-0019 are settled (privacy via repo split, one-probe intake, three-timescale feedback,
currency floor, `primer` naming, symlink-determines-command, no-hardcoded-learner, external-anchor+decay,
~0.4–0.7σ target, evidence-triggered recalibration, self-contained/bookkeeping-as-code, cultivate-learning
Goal 5). Touch them only with new evidence.
