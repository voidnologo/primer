# Session 1: Feedback cycle, intake interview, class/instance redesign

**Date:** 2026-06-15

> Per-session development log. Captures the **why** behind the work: goal, decisions (→ `DECISIONS.md`), tradeoffs, and open threads. Pairs with the git history for the **what**. (This first entry is a richer backfill of a long design+build session; later sessions follow the `session-start` template.)

## Goal of the session

Design and build the feedback/learning cycle and the new-user onboarding for the project, and resolve how the sensitive learner profile is stored. Align on process before building; then build.

## Context at start

- Single-user system (`learn-me-up` skill) with a strong lesson engine but: no onboarding interview, a shallow/implicit feedback loop, and a profile deliberately kept shallow because it was committed to a public repo.
- Maintainer is the sole consumer today; friends are interested. Maintainer uses two machines (personal + work) and needs profile + lessons synced.

## What changed (the "what")

- New engine docs: `primer/intake-protocol.md`, `primer/feedback-protocol.md`.
- `primer/source-canon.md` reframed (floor not ceiling) + wired into `lesson-protocol.md` and `system-prompt.md`.
- Profile restructured: stable traits in `profile.md`; depth markers + ZPD edges → `topic-index.md` with confidence + evidence; new `calibration-log.md`.
- `templates/learner/` scaffold; `tools/init-instance.sh`; `SKILL.md` config-driven `$DATA_DIR`, new `init` / `recalibrate` verbs.
- This engineering-log system (`docs/engineering/`).
- Commits on branch `wave1-intake-and-feedback-cycle`: `a7b68af` (Wave 1), `d393f5d` (init tooling + naming + layout).

## Decisions made (the "why")

Recorded in `DECISIONS.md`: D-0001 (class/instance privacy split) through D-0011 (these logs). Highlights:
- Privacy resolved by **repo split**, not a public-safe profile (D-0001) — also gives cross-machine sync.
- Intake = self-report **+ one live probe** per domain (D-0002).
- Feedback at **three timescales** + stable/volatile split (D-0003); **two-tier recalibrate**, minor auto every 5 (D-0004).
- Currency: canon as a **vetted floor** with mandatory per-lesson discovery (D-0006).
- Name: **primer** (D-0010); data layout mirrors core (D-0009).

## Tradeoffs accepted

- More files / more moving parts (two repos, several state files) in exchange for a profile that improves with use, is honest about confidence, and never leaks.
- N=5 for minor recalibrate is an untuned guess.
- One manual `git push` step on init, for portability across unknown user setups.

## Open threads / next

- **Wave 2 (task #7):** finish the rename (skill frontmatter + verb headers `/learn-me-up` → `/primer`, `install.sh` symlink, README/REQUIREMENTS, `~/.claude` memory). Coordinate frontmatter + symlink + reinstall so the live skill doesn't break. GitHub repo rename: **user does it**.
- **Wave 2 (task #5):** migrate the maintainer's real `learner/` + `lessons/` into a private data repo (maintainer's `gh` access is available for this — the maintainer's own instance, not the core).
- `/session-start` / `/session-end` mechanism: format still to confirm against the maintainer's house style (built fresh; `~/Work` not read).
- Tune N after real use; revisit whether examples/ ships sample lessons.

## Drift check

No non-negotiable violated. Privacy strengthened (D-0001), currency strengthened (D-0006). Scope stayed within what was requested (onboarding, feedback cycle, profile storage, rename, dev logs).
