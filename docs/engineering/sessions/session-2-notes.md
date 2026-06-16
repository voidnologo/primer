# Session 2: Cold-eyes review — research synthesis + improvement proposal

**Date:** 2026-06-15
**Goal:** Fresh-view review of the whole engine against `GOALS.md`, grounded in current AI-tutoring /
learning-science research and the landscape of comparable LLM-learning projects. Produce durable research
artifacts and a sequenced improvement plan. No implementation this session — review + plan only.

## Overview

A from-scratch read of the entire public core (`SKILL.md`, all eight `primer/*` protocols, templates, the two
session skills, README/REQUIREMENTS/GOALS/DECISIONS) plus two web research sweeps. The architecture held up
well against the literature — the class/instance split, stable/volatile memory, three-timescale loop, and
editable-markdown profile each match an independently-arrived-at best practice (Letta memory blocks,
Generative Agents reflection, Bull & Kay open learner models). The work surfaced four corrections that
contradict a stated goal/non-negotiable, seven tightenings, and four enhancements — all recorded in
Proposal 0001 with an implementation plan and a coverage table so nothing is dropped.

Research was captured **in full** as durable artifacts (per the maintainer's instruction this session) so we
don't re-run the searches in near sessions.

## Changes Made

- **New: research artifacts** (`docs/engineering/research/`) — two full sweeps with citations and
  verified/weak source flags, plus an index README and a freshness convention (~3-month horizon).
- **New: proposal system** (`docs/engineering/proposals/`) — Proposal 0001: findings (C1–C4, T1–T7, E1–E4),
  what the research validated, a 4-wave sequenced plan mapping each item to goals/files/effort, decisions
  required (⚑), and a coverage table.

## Files Modified

| File | Change |
|------|--------|
| `docs/engineering/research/2026-06-15-ai-tutoring-and-learning-science.md` | New — Sweep A (full) |
| `docs/engineering/research/2026-06-15-comparable-llm-learning-projects.md` | New — Sweep B (full) |
| `docs/engineering/research/README.md` | New — research index + freshness convention |
| `docs/engineering/proposals/0001-cold-review-and-improvements.md` | New — review + plan |
| `docs/engineering/sessions/session-2-notes.md` | New — this log |
| `docs/engineering/pending-tasks.md` | Added the proposed waves to the queue |

## Key Design Decisions

Held to "review + plan, don't implement" — the maintainer asked for a review and a plan, not edits to the
engine. None of C1–C4 were applied yet; they're sequenced in Proposal 0001 and queued. The two structural
findings worth promoting to `DECISIONS.md` *when implemented* (not before):

- **C2 — the feedback loop has no external anchor and confidence only ratchets up** → optimism drift (Boucle)
  + the BKT monotonicity gap. The fix is forgetting-aware confidence decay + wiring cold-retrieval misses back
  into the model. This is the most important finding; it's also what makes "a reinforcement cycle on
  ourselves" literally true.
- **C1 — the engine is over-fit to one learner** (maintainer's bio hardcoded in `system-prompt.md`; canon and
  domain-slug enum backend-specific) — a G4/G3 violation and, per expertise reversal, a pedagogical
  miscalibration for novice adopters.

## Open Threads

- ⚑ Decisions before Wave D: SRS approach (Anki export vs FSRS metadata — recommend Anki first); canon as thin
  starter + backend example pack vs multiple packs (recommend the former); E2/E4 scope (recommend defer until
  post-use data).
- Sweep A's first agent finished but its full synthesis didn't stream back via TaskOutput — recovered from the
  completion notification; both sweeps are fully captured.

## Next Session

- Implement **Wave A** (C4 → C3 → C1) — low-risk factual + de-personalization edits.
- Then **Wave B** (C2 + T1 + E1 + T7) — the structural loop fix.
- Promote C1/C2 to `DECISIONS.md` (D-0014+) as they land.

## Drift check

No non-negotiable violated this session (review + docs only; no engine change, no personal data near the
core, no work code read). The proposal *strengthens* G2/G4 and the currency/privacy non-negotiables. Scope
stayed within the requested review.
