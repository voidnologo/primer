# Continuation — fast resume

> Lean pointer for picking up primer dev. Read first at `session-start`. Kept short and current; history lives in `sessions/` and `DECISIONS.md`.

**Project:** primer — adaptive Primer-style learning system. Class/instance: public core (engine) + private per-user data repo (profile + lessons).

## Last session (1) — Feedback cycle, intake, class/instance redesign

- Built the onboarding interview (`primer/intake-protocol.md`, discovery-first: broad ability + goal decomposition + one probe per load-bearing sub-skill) and the feedback cycle (`primer/feedback-protocol.md`, three timescales, two-tier recalibrate).
- Reframed currency: canon = vetted floor + mandatory per-lesson source discovery.
- Restructured profile (stable vs volatile; depth markers → topic-index with confidence + evidence).
- Added this engineering-log system (GOALS, DECISIONS, sessions, two session skills).
- **Migrated**: `voidnologo/primer-data` (private) created + pushed; all personal data (profile + lessons) removed from the public core — it now lives only in the private instance. Lessons are private-by-default (D-0013); `examples/` removed.
- **Renamed** to `primer`: skill (symlink + `${CLAUDE_SKILL_DIR}` includes, reinstalled as `/primer`), GitHub repo (`voidnologo/primer`, remote updated), local dir. Work merged to `main` and pushed.

## Next up

- Run `/primer init` for a real intake (replace the generic migrated profile with a rich, evidence-backed one).
See `pending-tasks.md`.

## Don't re-litigate

`DECISIONS.md` D-0001…D-0012 are settled (privacy via repo split, one-probe intake, three-timescale feedback, currency floor, `primer` naming, symlink-determines-command). Touch them only with new evidence.
