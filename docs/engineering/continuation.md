# Continuation — fast resume

> Lean pointer for picking up primer dev. Read first at `session-start`. Kept short and current; history lives in `sessions/` and `DECISIONS.md`.

**Project:** primer — adaptive Primer-style learning system. Class/instance: public core (engine) + private per-user data repo (profile + lessons).

## Last session (3) — Cold review + implementation (Proposal 0001 Waves A & B)

- **Session 2** (review): fresh-eyes audit + two web research sweeps → durable research artifacts in
  `docs/engineering/research/` and `docs/engineering/proposals/0001-…md` (findings C1–C4, T1–T7, E1–E4 + plan).
- **Session 3** (implement): shipped Wave A (C4 effect-size correction, C3 canon edition tags, C1
  de-personalize the public engine) and Wave B (C2 forgetting-aware confidence decay, T1 review→calibration
  external anchor, E1 review-score recording, T7 "just show me" escape hatch). Decisions D-0014–D-0016.
- The engine is now learner-agnostic and the feedback loop has an external anchor (cold retrieval feeds
  confidence both ways; untouched high-confidence markers decay) — closing the closed-self-assessment drift.

## Next up

- **Wave C** (`pending-tasks.md`): T2 prompt-quality rubric → T5 resume/artifact path → T6 settings.json
  privacy deny-list → T4 evidence-triggered recalibration.
- **Wave D** needs ⚑ decisions: T3 (Anki export vs FSRS), E2 (situated-idea prompts), E4 (`/primer synthesize`).
- Still pending: run a real `/primer init` against the de-personalized engine.

## Don't re-litigate

`DECISIONS.md` D-0001…D-0016 are settled (privacy via repo split, one-probe intake, three-timescale feedback,
currency floor, `primer` naming, symlink-determines-command, no-hardcoded-learner, external-anchor+decay,
~0.4–0.7σ target). Touch them only with new evidence.
