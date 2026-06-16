---
name: session-start
description: "Start a primer engineering session — load design context, reaffirm the north star (GOALS.md), read recent decisions and open threads, and open a numbered session log. For developing primer itself, not for running a learning lesson."
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
---

# Start Dev Session

Resume engineering work on primer: load design context, reaffirm the north star, and open a new session log. This tracks the **why** of development alongside git's **what**.

> Scope: this is for *developing primer* (the engine/core), not for running a learning lesson. For lessons, that's the `primer` skill itself.

## Workflow

### 1. Determine session number

```bash
ls -1 docs/engineering/sessions/session-*-notes.md 2>/dev/null | sort -t- -k2 -n | tail -3
```

New session is N+1 of the highest existing number.

### 2. Load fast-resume context

Read `docs/engineering/continuation.md` — the lean ("what was done last, what's next") pointer.

### 3. Reaffirm the north star (always)

Read `docs/engineering/GOALS.md`. This is the anti-drift anchor — the goals and non-negotiables every change must serve and none may violate. Carry it through the session; if a proposed change conflicts, surface it.

### 4. Read recent history (as needed)

- `docs/engineering/sessions/session-{N}-notes.md` (most recent) for immediate context and open threads.
- `docs/engineering/DECISIONS.md` (top entries) if the work touches a prior decision — don't silently re-litigate a settled one.
- `docs/engineering/pending-tasks.md` for queued work.

### 5. Create the new session notes file

Create `docs/engineering/sessions/session-{N}-notes.md`:

```markdown
# Session {N}: {Title TBD}

**Date:** {YYYY-MM-DD}
**Goal:** {filled once the user states the objective}

## Overview

{filled as work progresses}

---

## Changes Made

{by feature area, as work progresses}

## Files Modified

| File | Change |
|------|--------|

## Key Design Decisions

{non-obvious choices + rationale. Promote substantive ones to DECISIONS.md at session end.}

## Open Threads

## Next Session
```

### 6. Brief the user

- Last session: 1–3 sentence highlight.
- Next up: from `pending-tasks.md`.
- Ask what to work on. Fill the session Goal once they respond.

## Notes

- Don't update `continuation.md` at start — that's a session-end step.
- `GOALS.md` is always read; `DECISIONS.md`/session notes are read on demand.
- If the user dives into work without invoking this, create the session file when you notice.
