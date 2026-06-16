# Session 3: Implement Proposal 0001 — Waves A & B

**Date:** 2026-06-15
**Goal:** Implement the corrections and the loop-closing fix from Proposal 0001 — Wave A (C4, C3, C1) and
Wave B (C2, T1, E1, T7). De-personalize the public engine, fix the overstated research claims, and give the
feedback loop an external anchor + forgetting-aware confidence decay.

## Overview

Implemented both waves. The public engine no longer hardcodes a learner — `system-prompt.md` reads the
learner from the profile, senior-peer is now an overridable default register, the canon is framed as a domain
starter pack, and the lesson-template domain list is per-instance. The design docs stop citing folklore
effect sizes and state a defensible ~0.4–0.7σ target. Most consequentially, the feedback loop now has an
external anchor (cold retrieval in `/primer review` feeds confidence both ways and logs misses) and
forgetting-aware decay (untouched high-confidence markers drift toward reprobe), closing the
closed-self-assessment drift that was the review's top structural finding. Three decisions promoted
(D-0014–D-0016). No personal data touched, no work code read.

## Changes Made

**Wave A — corrections**
- **C4** — `REQUIREMENTS.md §2` rewritten with verified effect sizes + ~0.4–0.7σ target; `lesson-protocol.md`
  AutoTutor claim tagged `[from-training, verify]` and the "assist + retrieve, don't withhold by willpower"
  evidence added.
- **C3** — `source-canon.md` floor entries with edition/year claims tagged `[edition — verify]`; preamble now
  applies the verify-tag discipline to floor metadata.
- **C1** — `system-prompt.md` de-personalized (reads profile; default-vs-override register; universal
  non-negotiables called out); `source-canon.md` reframed as a *starter pack*, not a universal canon;
  `lesson-template.md` domain enum → per-instance; `anti-patterns.md` #4 generalized off the hardcoded
  "15+-year" learner and fixed a stale `profile.md`→`topic-index.md` depth-marker path (+ added the
  expertise-reversal under-scaffold default).

**Wave B — close the loop**
- **C2** — `feedback-protocol.md`: confidence is bidirectional; new *Confidence decays with time
  (forgetting-aware)* and *External anchor* subsections; minor-recalibrate step 3 now decays stale
  high-confidence markers; *defending-against* list gains an Optimism-drift entry.
- **T1** — `SKILL.md` `/primer review` rewritten to feed misses back (calibration-log + confidence drop) and
  confirm on clean old answers.
- **E1** — `/primer review` records a score; `review-queue.md` template gains a *Review history* section with
  the self-authored-test caveat.
- **T7** — explicit "just show me" escape hatch gated on productive-struggle tolerance, in `system-prompt.md`
  refusal patterns and `lesson-protocol.md` Probe.

## Files Modified

| File | Change |
|------|--------|
| `REQUIREMENTS.md` | C4 — verified effect sizes + target |
| `primer/lesson-protocol.md` | C4 tag + assist-evidence; T7 escape hatch in Probe |
| `primer/source-canon.md` | C3 edition tags + verify discipline; C1 starter-pack framing |
| `primer/system-prompt.md` | C1 de-personalize; T7 escape hatch |
| `primer/anti-patterns.md` | C1 generalize learner; fix stale depth-marker path |
| `primer/lesson-template.md` | C1 per-instance domain list |
| `primer/feedback-protocol.md` | C2 decay + external anchor + bidirectional confidence |
| `SKILL.md` | T1/E1 — `/primer review` feedback wiring + score recording |
| `templates/learner/review-queue.md` | E1 — Review history section |
| `docs/engineering/DECISIONS.md` | D-0014, D-0015, D-0016 |
| `docs/engineering/proposals/0001-…md` | status → Wave A & B implemented |
| `docs/engineering/pending-tasks.md` | checked off Wave A & B |
| `docs/engineering/continuation.md` | updated last-session pointer |

## Key Design Decisions

Promoted to `DECISIONS.md`: **D-0014** (no hardcoded learner in the public engine), **D-0015** (external
anchor + forgetting-aware decay), **D-0016** (~0.4–0.7σ target; 2σ is folklore). Rationale and rejected
alternatives are recorded there.

## Open Threads

- Wave C queued: T2 (prompt-quality rubric), T5 (resume/artifact path reconcile), T6 (settings.json privacy
  deny-list), T4 (evidence-triggered recalibration).
- Wave D needs ⚑ decisions: T3 (Anki export vs FSRS metadata — recommend Anki first), E2 (situated-idea
  prompts), E4 (`/primer synthesize`). Defer E2/E4 until post-use data.
- D-0015's decay is coarse (drift high→med at recalibrate). If real review data shows it's too blunt, revisit
  a per-marker half-life (T3 territory).

## Next Session

- Wave C (T2 → T5 → T6 → T4), then settle the Wave D ⚑ decisions.
- Still pending from before: run a real `/primer init` intake against the de-personalized engine.

## Drift check

No non-negotiable violated. C1 *strengthens* the sharable-without-leaking goal (removed personal data from
the public core); C2/T1/E1 *strengthen* the "profile gets truer with use" goal and confidence-honesty; C3/C4
*strengthen* the currency non-negotiable; T7 preserves productive struggle while removing a measured failure
mode. No personal data moved toward the core; no work codebase read. Scope stayed within the approved plan.
