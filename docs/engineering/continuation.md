# Continuation — fast resume

> Lean pointer for picking up primer dev. Read first at `session-start`. Kept short and current; history lives in `sessions/` and `DECISIONS.md`.

**Project:** primer — adaptive Primer-style learning system. Class/instance: public core (engine) + private per-user data repo (profile + lessons).

## Last session (1) — Feedback cycle, intake, class/instance redesign

- Built the onboarding interview (`primer/intake-protocol.md`, discovery-first: broad ability + goal decomposition + one probe per load-bearing sub-skill) and the feedback cycle (`primer/feedback-protocol.md`, three timescales, two-tier recalibrate).
- Reframed currency: canon = vetted floor + mandatory per-lesson source discovery.
- Restructured profile (stable vs volatile; depth markers → topic-index with confidence + evidence).
- Settled architecture: public core + private data repo, `init-instance.sh`, `~/.config/primer/config`. Name = `primer`.
- Added this engineering-log system (GOALS, DECISIONS, sessions, these two skills).
- Work on branch `wave1-intake-and-feedback-cycle`.

## Next up

Wave 2: finish the rename to `primer` (skill name + verbs + install + memory; user does the GitHub rename) and migrate the maintainer's real data into a private instance repo. See `pending-tasks.md`.

## Don't re-litigate

`DECISIONS.md` D-0001…D-0011 are settled (privacy via repo split, one-probe intake, three-timescale feedback, currency floor, `primer` naming, etc.). Touch them only with new evidence.
