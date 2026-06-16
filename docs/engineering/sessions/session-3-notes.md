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

**Wave D discussion → two new goals + an architecture proposal**

Resolving Wave D turned into a design conversation that produced new direction (captured durably):
- **Goal 5 (D-0019)** — cultivating better learning *habits* and gradually training better learning is a
  project goal, not just delivering content. Added to `GOALS.md`.
- **Self-contained + bookkeeping-as-code (D-0018)** — no external tool is ever required; scripts and a local
  SQLite DB (in the private data repo) are in-scope so deterministic work (decay, triggers, scheduling) leaves
  the LLM context. Supersedes REQUIREMENTS P7/§11's "external SRS does the scheduling."
- **Anchor reworked** — since the maintainer won't do periodic review (prefers skimming logs), the Wave B
  external anchor was moved onto the lesson flow: a light **recall check at the Elicit step** (always-on),
  with `/primer review` now *optional* and the Primer offering it proactively as habit-building. Time-decay is
  the passive guard. (`lesson-protocol.md`, `feedback-protocol.md`, `SKILL.md`.)
- **Proposal 0001 T3 resolved into Proposal 0002** — self-contained in-repo scheduling, not Anki.
- **Proposal 0002 written** — deterministic state layer (scripts + SQLite) + habit-formation track, with the
  source-of-truth (A/B/C), scheduler (SM-2-lite vs FSRS), and build-order choices left as ⚑ decisions. No
  build started — awaiting the maintainer's scope call.

## Files Modified

| File | Change |
|------|--------|
| `REQUIREMENTS.md` | C4 verified effect sizes + target; §11 superseded note (self-contained scheduling) |
| `primer/lesson-protocol.md` | C4 tag + assist-evidence; T7 escape hatch; Elicit-step recall anchor |
| `primer/source-canon.md` | C3 edition tags + verify discipline; C1 starter-pack framing; generalized currency rationale |
| `primer/system-prompt.md` | C1 de-personalize; T7 escape hatch |
| `primer/anti-patterns.md` | C1 generalize + stale-path fix; T2 prompt self-check |
| `primer/lesson-template.md` | C1 per-instance domains; T2 prompt-quality bar; T5 sidecar convention |
| `primer/feedback-protocol.md` | C2 decay + bidirectional confidence; T1/anchor (2 sources + decay); T4 trigger |
| `SKILL.md` | T1/E1 review wiring; T5 resume path; T4 trigger; review→optional+habit framing |
| `templates/learner/review-queue.md` | E1 — Review history section |
| `templates/learner/calibration-log.md` | added `retention-miss` miss-type |
| `README.md` | "What's a Primer?" framing; T6 privacy-hardening block |
| `.gitignore` | T5 — `lessons/**/*.STATE.md` |
| `docs/engineering/GOALS.md` | Goal 5 (cultivate learning); self-contained non-negotiable |
| `docs/engineering/DECISIONS.md` | D-0014…D-0019 |
| `docs/engineering/proposals/0001-…md` | status → Waves A–C implemented |
| `docs/engineering/proposals/0002-…md` | new — deterministic state layer + habit-formation |
| `docs/engineering/pending-tasks.md` | checked off Waves A–C |
| `docs/engineering/continuation.md` | updated last-session pointer |

## Key Design Decisions

Promoted to `DECISIONS.md`: **D-0014** (no hardcoded learner), **D-0015** (external anchor + decay),
**D-0016** (~0.4–0.7σ target; 2σ folklore), **D-0017** (evidence-triggered recalibration, supersedes D-0004),
**D-0018** (self-contained; deterministic bookkeeping is code, SQLite in-scope), **D-0019** (Goal 5 — cultivate
learning habits). Rationale and rejected alternatives recorded there.

## Open Threads

- **Proposal 0002 awaits the maintainer's ⚑ scope decisions** (the morning's first item): source of truth
  (A/B/C — recommend C, hybrid), scheduler (SM-2-lite vs FSRS — recommend SM-2-lite first), build order
  (recommend build state layer before a real intake), script language (recommend Python stdlib). No build
  started.
- Proposal 0001 E2 / E4 still deferred until post-use data. E3 (generation effect) is queued, needs no
  decision — implementing it tonight if time permits before the decision point.
- D-0015's decay is coarse (drift high→med at recalibrate); revisit a per-marker half-life when the scheduler
  lands (Proposal 0002).

## Next Session (morning)

- **First:** resolve Proposal 0002's ⚑ scope decisions, then build the chosen state layer + scheduler.
- Then a real `/primer init` intake against the de-personalized engine (ideally writing into the new state layer).
- Still pending from before: run a real `/primer init` intake against the de-personalized engine.

## Drift check

No non-negotiable violated. C1 *strengthens* the sharable-without-leaking goal (removed personal data from
the public core); C2/T1/E1 *strengthen* the "profile gets truer with use" goal and confidence-honesty; C3/C4
*strengthen* the currency non-negotiable; T7 preserves productive struggle while removing a measured failure
mode. No personal data moved toward the core; no work codebase read. Scope stayed within the approved plan.
