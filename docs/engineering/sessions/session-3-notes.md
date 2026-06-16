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

**Post-push — unblocked work before the decision point**
- **E3 (generation effect)** — Recap now hands the learner the pen first: they state the key takeaway in their
  own words before the Primer summarizes/writes prompts (preserves the encoding work; also a calibration beat).
  `lesson-protocol.md §5`.
- **Consistency sweep** — grepped for stragglers from the rapid edits and fixed three: `SKILL.md` still said
  the minor recalibrate runs "every 5 lessons" (now evidence-triggered, D-0017); and two spots still routed
  **depth markers to `profile.md`** (`lesson-protocol.md §5` Recap update, `anti-patterns.md` #6) — corrected
  to `topic-index.md` per the D-0003 stable/volatile split. (The latter two predated this session.)

**State layer built (Proposal 0002 decided — D-0020)**

Maintainer answered the ⚑ scope questions: source-of-truth delegated to me on merits, scheduler delegated,
state-layer-first, Python (cross-platform). My calls, with reasoning recorded in D-0020:
- **Markdown stays source of truth; no SQLite.** The instance syncs across machines via git; a binary SQLite
  file can't be merged (lost writes on a forgotten pull), and at one-learner scale it buys no speed. This
  *refines* D-0018's "committed SQLite DB" — DB dropped. (A gitignored rebuildable cache remains a future
  option if scale ever demands.)
- **SM-2** scheduler (transparent, no training data; FSRS deferred). **Python 3.11+ stdlib-only** (portable).
- Built `tools/primer_state.py` — `review-due/grade/add/history`, `markers-decay`, `recalibrate-check` — plus
  `tools/test_primer_state.py` (**19 tests, all passing**) and `tools/README.md`. Smoke-tested end-to-end.
- Wired into the engine: `SKILL.md` (review flow, recalibrate-check + decay, prompt-append, a "call code, don't
  compute in-context" note), `feedback-protocol.md` (bookkeeping-as-code note), `review-queue.md` template
  (scheduled line format).

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
| `tools/primer_state.py` | NEW — SM-2 scheduler, decay, recalibrate-check (stdlib) |
| `tools/test_primer_state.py` | NEW — 19 unit tests (passing) |
| `tools/README.md` | NEW — tools index + `primer_state.py` usage |
| `SKILL.md` | (also) wired `primer_state.py` into review / recalibrate-check / prompt-append; state-helpers note |
| `primer/feedback-protocol.md` | (also) bookkeeping-as-code note |
| `templates/learner/review-queue.md` | (also) scheduled prompt-line format |
| `docs/engineering/GOALS.md` | Goal 5 (cultivate learning); self-contained non-negotiable |
| `docs/engineering/proposals/0002-…md` | NEW + status → decided & built |
| `docs/engineering/DECISIONS.md` | D-0014…D-0020 |
| `docs/engineering/proposals/0001-…md` | status → Waves A–C implemented |
| `docs/engineering/proposals/0002-…md` | new — deterministic state layer + habit-formation |
| `docs/engineering/pending-tasks.md` | checked off Waves A–C |
| `docs/engineering/continuation.md` | updated last-session pointer |

## Key Design Decisions

Promoted to `DECISIONS.md`: **D-0014** (no hardcoded learner), **D-0015** (external anchor + decay),
**D-0016** (~0.4–0.7σ target; 2σ folklore), **D-0017** (evidence-triggered recalibration, supersedes D-0004),
**D-0018** (self-contained; deterministic bookkeeping is code), **D-0019** (Goal 5 — cultivate learning
habits), **D-0020** (markdown source of truth, no SQLite, SM-2, Python stdlib — refines D-0018). Rationale and
rejected alternatives recorded there.

## Open Threads

- Proposal 0002 decided & built (D-0020). Remaining habit-formation surface (proactive nudges, showing the
  retention-trend payoff, meta-learning asides) rides real use rather than being front-loaded.
- Proposal 0001 E2 / E4 still deferred until post-use data.
- `init-instance.sh` scaffolds the data repo from `templates/learner/` — confirm it seeds the new
  `review-queue.md` (Prompts + Review history sections) and the scheduled-line format. (Likely fine since it
  copies templates, but verify on the next real init.)
- D-0015's decay is coarse (drift high→med at recalibrate); a per-marker half-life is a future refinement now
  that the scheduler exists.

## Next Session

- A real `/primer init` intake against the de-personalized engine, writing into the new state layer
  (`primer_state.py`) — the first true end-to-end exercise.
- Consider merging `proposal-0001-review-and-fixes` to `main` (rebase first — `origin/main` advanced).
- Still pending from before: run a real `/primer init` intake against the de-personalized engine.

## Drift check

No non-negotiable violated. C1 *strengthens* the sharable-without-leaking goal (removed personal data from
the public core); C2/T1/E1 *strengthen* the "profile gets truer with use" goal and confidence-honesty; C3/C4
*strengthen* the currency non-negotiable; T7 preserves productive struggle while removing a measured failure
mode. No personal data moved toward the core; no work codebase read. Scope stayed within the approved plan.
