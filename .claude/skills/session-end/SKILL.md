---
name: session-end
description: "Close a primer engineering session — finalize the session log, promote substantive decisions to DECISIONS.md, update pending-tasks and the lean continuation pointer, and run a drift check against GOALS.md. For developing primer itself, not for running a learning lesson."
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
---

# End Dev Session

Finalize the session: complete the log, promote decisions to the durable record, update the live task list and fast-resume pointer, and confirm no drift from the north star.

## Workflow

### 1. Identify the current session

```bash
ls -1 docs/engineering/sessions/session-*-notes.md | sort -t- -k2 -n | tail -1
```

### 2. Finalize the session notes

Update `docs/engineering/sessions/session-{N}-notes.md`:

- **Title / Goal:** replace placeholders.
- **Overview:** 1–2 paragraphs — what was accomplished and *why*.
- **Changes Made:** by feature area.
- **Files Modified:** complete table. Populate from git:
  ```bash
  git diff --name-only HEAD~{commits-this-session} 2>/dev/null
  ```
- **Key Design Decisions:** the non-obvious choices with rationale ("why", not "what").
- **Open Threads / Next Session:** carry-forward.

### 3. Promote decisions to the durable log

For each substantive decision (a tradeoff, a rejected alternative, a constraint), append an entry to the **top** of `docs/engineering/DECISIONS.md` using the next `D-00NN` number and the entry format there (decision · context · alternatives · tradeoff). The session note is the narrative; `DECISIONS.md` is the searchable record.

### 4. Update pending tasks

`docs/engineering/pending-tasks.md`:
- Check off / remove completed items (they now live in the session notes).
- Add tasks/ideas discovered this session.
- Reorder "Next Up" if priorities shifted.

### 5. Update the continuation pointer

`docs/engineering/continuation.md` (keep lean, ~60–80 lines):
- Update "Last session (N)" → number + title.
- 2–4 bullets of what was done.
- Update the "Next up" line.
- Don't accumulate history here — that's what session notes + DECISIONS.md are for.

### 6. Drift check

Re-read `docs/engineering/GOALS.md` and confirm in the session notes: did this session serve a goal and violate no non-negotiable? Record the answer honestly — a flagged drift is more useful than a silent one.

### 7. Report

- Session title + date.
- 3–5 key accomplishments.
- Decisions promoted (D-00NN list).
- Open items carried forward.
- Suggested next focus.
- Remind the user to commit if they haven't.

## Notes

- Session notes are the permanent narrative record — be thorough.
- `DECISIONS.md` is append-only and numbered — never rewrite history, supersede with a new entry.
- `continuation.md` is for fast resumption — short and current.
