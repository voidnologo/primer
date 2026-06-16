# Session 3: Implement Proposal 0001 — Waves A, B & C (+ README framing)

**Date:** 2026-06-15
**Goal:** Implement the corrections and the loop-closing fix from Proposal 0001 — Wave A (C4, C3, C1),
Wave B (C2, T1, E1, T7), and Wave C (T2, T5, T6, T4). De-personalize the public engine, fix the overstated
research claims, give the feedback loop an external anchor + forgetting-aware decay, then quality/hygiene.
Also added a "What's a Primer?" framing section to the README (the *why*, for readers who haven't read
*The Diamond Age*).

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

**Wave C — quality & hygiene**
- **T2** — retrieval-prompt quality bar (Matuschak's 5 attributes + a conceptual pattern-language) in
  `lesson-template.md`; matching self-check line in `anti-patterns.md`.
- **T5** — reconciled the resume/artifact path: in-progress state is a sidecar
  `<date>-<slug>.STATE.md` next to the flat artifact (was a `<slug>/STATE.md` directory in `/primer resume`
  vs a flat file in the template). Updated `SKILL.md`, `lesson-template.md`, and `.gitignore`
  (`lessons/**/*.STATE.md`).
- **T6** — privacy hardening documented in `README.md`: a recommended `deny` block for the user's *global*
  `~/.claude/settings.json` (the repo's `.claude/*` is gitignored, so a committed repo setting wouldn't apply
  to `/primer` sessions). Defense-in-depth atop the instruction-level rule.
- **T4** — minor recalibrate is now **evidence-triggered with a cap** (M=4 misses OR N=8 lessons), replacing
  fixed N=5. Updated `feedback-protocol.md` and `SKILL.md` step 2.

**README framing (user request)**
- Added "What's a Primer?" — a short, non-academic section on the *Diamond Age* Primer (Nell + the book that
  meets her where she is) and why this project exists, plus a "What this is" implementation paragraph.

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
| `SKILL.md` | T1/E1 review wiring; T5 resume path; T4 recalibrate trigger |
| `templates/learner/review-queue.md` | E1 — Review history section |
| `templates/learner/calibration-log.md` | added `retention-miss` miss-type |
| `primer/lesson-template.md` | C1 domains; T2 prompt-quality bar; T5 sidecar convention |
| `primer/anti-patterns.md` | C1 generalize + path fix; T2 prompt self-check |
| `README.md` | "What's a Primer?" framing; T6 privacy-hardening block |
| `.gitignore` | T5 — `lessons/**/*.STATE.md` |
| `docs/engineering/DECISIONS.md` | D-0014, D-0015, D-0016, D-0017 |
| `docs/engineering/proposals/0001-…md` | status → Waves A–C implemented |
| `docs/engineering/pending-tasks.md` | checked off Waves A–C |
| `docs/engineering/continuation.md` | updated last-session pointer |

## Key Design Decisions

Promoted to `DECISIONS.md`: **D-0014** (no hardcoded learner in the public engine), **D-0015** (external
anchor + forgetting-aware decay), **D-0016** (~0.4–0.7σ target; 2σ is folklore), **D-0017** (evidence-triggered
recalibration, supersedes D-0004's fixed N=5). Rationale and rejected alternatives are recorded there.

## Open Threads

- **Wave D awaits the maintainer's ⚑ decisions** (reiterated to them this session): T3 (Anki export vs FSRS
  metadata — recommend Anki first), E2 (situated-idea prompts — recommend defer until post-use data), E4
  (`/primer synthesize` — recommend defer). E3 (generation-effect tweak) needs no decision and is queued.
- D-0015's decay is coarse (drift high→med at recalibrate). If real review data shows it's too blunt, revisit
  a per-marker half-life — overlaps T3.

## Next Session

- Resolve Wave D ⚑ decisions, then implement what's chosen (+ E3 regardless).
- Still pending from before: run a real `/primer init` intake against the de-personalized engine.

## Drift check

No non-negotiable violated. C1 *strengthens* the sharable-without-leaking goal (removed personal data from
the public core); C2/T1/E1 *strengthen* the "profile gets truer with use" goal and confidence-honesty; C3/C4
*strengthen* the currency non-negotiable; T7 preserves productive struggle while removing a measured failure
mode. No personal data moved toward the core; no work codebase read. Scope stayed within the approved plan.
