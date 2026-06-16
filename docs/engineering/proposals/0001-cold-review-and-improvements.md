# Proposal 0001 — Cold review, research synthesis, and improvement plan

**Date:** 2026-06-15
**Status:** Wave A & B implemented (Session 3, D-0014–D-0016). Wave C queued; Wave D awaiting decisions marked ⚑ below.
**Author:** fresh-eyes review (Session 2)
**Scope:** the public core (engine + docs). No personal-instance changes. No work code read.

> A fresh-view audit of the whole engine against its own `GOALS.md`, cross-checked against the current
> AI-tutoring / learning-science literature and the landscape of comparable LLM-learning projects. It
> records what the research validated, what contradicts a stated goal, what is loose, and what could be
> added — then sequences the work. Findings map to `GOALS.md` goals (G1–G4) and non-negotiables (NN).

---

## 1. How this was produced

Reviewed in full: `SKILL.md`, all eight `primer/*` protocols, `templates/learner/*`, the `session-start` /
`session-end` skills, `README.md`, `REQUIREMENTS.md`, `GOALS.md`, and `DECISIONS.md` (D-0001…D-0013).

Two research sweeps (web, 2026-06-15), each captured in full as a durable artifact under
[`docs/engineering/research/`](../research/) so the work isn't repeated:

- **Sweep A — AI-tutoring & learning-science state of the art.** 13 load-bearing quantitative claims
  re-verified against primary sources (VanLehn 2011; Kulik & Fletcher 2016; Ma et al. 2014; Nickow et al.
  2020; Kestin et al. 2025; Khajah et al. 2016; Settles & Meeder 2016; Tetzlaff et al. 2025).
  → [`2026-06-15-ai-tutoring-and-learning-science.md`](../research/2026-06-15-ai-tutoring-and-learning-science.md)
- **Sweep B — comparable projects.** Letta/MemGPT, Generative Agents, Reflexion, DeepTutor, llm-knowledge-base,
  Karpathy "LLM-wiki", Andy Matuschak's body of work (mnemonic medium, prompt quality, situated ideas),
  Orbit, Cursor Memory Bank, and the Boucle "Optimism Feedback Loop" post.
  → [`2026-06-15-comparable-llm-learning-projects.md`](../research/2026-06-15-comparable-llm-learning-projects.md)

Confidence note: claims in §2 below are flagged **[strong]** (RCT / replicated meta-analysis / primary doc)
or **[weak]** (vendor / non-RCT / self-selected sample) per the sweeps' own verification.

---

## 2. Research synthesis (the parts that bear on primer)

**What the field converged on — and primer already does:**

- **"AI assists + tools + vetted content," not LLM-as-oracle, is the only well-evidenced pattern.** [strong]
  Every robust win routes around raw generation: Stanford *Tutor CoPilot* (Wang/Demszky 2024, preregistered
  RCT, +4pp overall / +9pp for weaker tutors) nudges *human* tutors; Khanmigo's math fix was *architectural*
  (a calculator tool + forced retrieval of human-authored content), not prompt-tuning. → primer's mandatory
  per-lesson **source-discovery pass + claim tagging** is exactly this shape.
- **Stable/volatile memory split** is the current best practice. [strong] Letta/MemGPT pins small,
  char-capped `persona`/`human` blocks and searches archival memory on demand; Letta's own writeup says it
  "translates directly to frontmatter markdown with editable metadata sections." → primer's
  `profile.md` (stable) vs `learner/*` (volatile) is the same design.
- **Reflection on accumulated evidence** (Generative Agents, Park et al. 2023) ≈ primer's three-timescale loop.
- **Open Learner Models** (Bull & Kay, SMILI 2007): inspectable / editable / negotiable. → primer's
  learner-editable markdown profile with *visible confidence* at intake is a textbook OLM.
- **Aggressive fade / default-terse is correct.** [strong] The expertise-reversal effect is *asymmetric*
  (Tetzlaff et al. 2025, 60 experiments, N=5,924): high assistance helps novices (d≈0.51) but *harms*
  experts (d≈−0.43). Under-scaffolding is the right default. → primer's "fade fast" matches.
- **Probe-before-answer is validated, not just stylistic.** [strong] MathTutorBench (2025): models best at
  being *correct* are systematically worst at *withholding* (GPT-4o ~90% solving / ~50% scaffolding). The
  default failure is revealing the full solution — exactly the tendency anti-pattern #7 resists.

**What the field warns about — and primer is exposed to:**

- **Closed self-assessment loops drift optimistic, imperceptibly.** [weak-but-mechanistic] The Boucle
  "Optimism Feedback Loop" post documents an agent that read its own prior summary as ground truth and
  inflated each cycle to a fabricated "99.8%." And the standard learner model (BKT, Corbett & Anderson 1995)
  has **no forgetting** — mastery is monotonic. The field's fix is *forgetting-aware* models (Half-Life
  Regression, Settles & Meeder 2016, drives Duolingo; DAS3H, Choffin et al. 2019) where estimates **decay
  toward "needs review."** → primer's depth-marker confidence only ratchets up. See C2.
- **LLMs produce "prompt-shaped text."** [strong, Matuschak] Surface-correct retrieval prompts that test
  phrasing, not understanding — especially for conceptual material. Fix is a pattern-language + a
  taste-trained filter, not better base generation. → primer auto-generates prompts with no quality bar. See T2.
- **Auto-generating all material removes the generation effect.** [strong] The encoding work *is* the
  learning (SmartFlash; Matuschak). → primer authors every prompt for the learner. See E3.
- **Self-authored tests inflate measured gains** (local-test alignment; Kulik & Fletcher 2016). → if primer
  ever grades itself on its own prompts, it inflates. See E1 caveat.
- **Effect sizes are far smaller than folklore.** [strong] 2σ never replicated (pooled tutoring 0.37 SD,
  Nickow 2020; human tutoring ~0.79, VanLehn 2011); ITS median 0.66 (Kulik & Fletcher) is inflated by local
  tests; the headline gen-AI tutor RCT (Kestin 2025) is **0.63 SD** honest, not the cited 0.73–1.3. See C4.

**Closest analogs worth studying directly:** Letta memory-block model (stable/volatile mechanics);
Matuschak's "How to write good prompts" + "situated ideas" (Nov 2024); llm-knowledge-base (markdown schema +
SR + `confidence:` / `status: quarantined` flags); DeepTutor (L1→L2→L3 editable memory distillation).

---

## 3. Findings

Each finding: what it is, the goal/non-negotiable at stake, and the fix. IDs are referenced by the plan in §4.

### Corrections — contradict a stated goal or non-negotiable

**C1 — The engine is over-fit to one learner.**
`primer/system-prompt.md` hardcodes *"The learner has 15+ years … He is technical lead …"*; `source-canon.md`'s
domains are entirely backend/distsys/AI-agentic; `lesson-template.md` hardcodes a five-value domain-slug enum.
The README and intake promise "any learner and any goal." The public engine shipped to a stranger asserts it
is tutoring *you*.
*At stake:* **G4** (sharable without leaking — the maintainer's bio is personal data in the public core) and
**G3** (onboarding a stranger). Also *pedagogical*: per expertise reversal, a hardcoded-expert engine
**under-scaffolds any novice** who adopts it.
*Fix:* de-personalize `system-prompt.md` (pull learner specifics from `$DATA_DIR/learner/profile.md` at
runtime); reframe the canon as one *seed pack* among domain packs (ship a thin starter; the backend-heavy
floor can seed the maintainer's instance); replace the hardcoded domain enum with "domains as defined in the
learner's `topic-index.md`."

**C2 — The feedback loop is a closed self-assessment loop with no external anchor, and confidence only
ratchets up.** The Primer writes depth markers and reads its own prior assessment next session as ground
truth; confidence rises on each confirming lesson and never decays. This is the Boucle drift + the BKT
monotonicity gap.
*At stake:* **G2** (the profile should get *more true* with use) and **NN: honesty about confidence**.
*Fix (with T1, E1):* add **forgetting-aware decay** — a high-confidence marker untouched for N weeks drifts
back toward "reprobe"; and **wire cold-retrieval misses back into the model** (the external anchor). The
minor-recalibrate already surfaces *stale low-confidence* markers; extend it to decay *stale high-confidence*
ones.

**C3 — The canon floor carries untagged unverified specifics** (e.g., edition/year claims like "DDIA 2nd ed.
(… 2026)") while the system mandates `[verified]` / `[from-training, verify]` tags on every claim. The floor
is loaded as authority but exempt from the rule it enforces.
*At stake:* **NN: currency** (self-inconsistent).
*Fix:* tag floor entries; flag the date-bearing ones for verification at the next freshness check.

**C4 — The design-rationale effect sizes are overstated.** `REQUIREMENTS.md §2` cites "Bloom's 2-sigma; ITS
… 0.66σ; recent generative-AI tutors landing 0.73–1.3σ." 2σ is folklore; 0.66σ is inflated by local tests;
0.73–1.3σ generalizes one ~2-week Harvard RCT whose honest ATE is **0.63 SD** (higher figures are
quantile-derived). `lesson-protocol.md:3`'s AutoTutor "one letter grade" claim is also untagged.
*At stake:* **NN: currency / source-grounding** — primer preaches it; its own docs should obey it.
*Fix:* restate the target as **~0.4–0.7 SD on transfer-valid (not self-authored) assessments**, drop 2σ, tag
the AutoTutor claim.

### Tightenings — no goal violation, but loose

- **T1 — Close the review→calibration loop.** A miss on an N-week-old `/primer review` prompt should append a
  calibration-log entry and lower the relevant depth-marker confidence. This is the external anchor for C2 and
  what makes "a reinforcement cycle on ourselves" literally true. *(Pairs with C2, E1.)*
- **T2 — Retrieval-prompt quality bar.** Encode Matuschak's five attributes (focused, precise, consistent,
  tractable, effortful) + a small pattern-language (definition / why-it-matters / contrast / application) as a
  generation spec in `lesson-template.md`, plus a self-check line in `anti-patterns.md`. Counters "prompt-shaped text."
- **T3 — ⚑ Decide the spaced-repetition story.** `/primer review` weights "toward older entries" (a proxy)
  while §11 punts scheduling to Anki. It is currently neither. *Decision needed:* (a) commit to Anki export
  (prompts are already `Q::A`), or (b) add FSRS-style `next_due` / `interval` metadata to `review-queue.md`.
- **T4 — Evidence-triggered recalibration.** Replace fixed N=5 with a trigger on accumulated calibration-log
  misses (Generative-Agents importance threshold), capped at a max lesson count. (Already noted in
  pending-tasks as "tune N"; this supersedes the tuning with a mechanism.)
- **T5 — Resume path inconsistency.** `lesson-template.md` writes flat `…/<date>-<slug>.md`; `/primer resume`
  looks for `…/<slug>/STATE.md` (a directory). Reconcile to one form.
- **T6 — Privacy hard guardrail.** "Never read `~/Work/*`" is instruction-only, but the skill has `Bash`+`Read`.
  Add a `settings.json` deny rule for work/proprietary paths — defense-in-depth for an **NN** at near-zero cost.
- **T7 — Explicit "just show me" escape hatch**, gated on the profile's productive-struggle tolerance, distinct
  from `/explain-deeper`. Socratic pressure misaligned to readiness induces overload (Sweep A §1); the bail-out
  closes it without weakening the default probe-first rule.

### Enhancements — optional; lean into the "adaptive model on yourself" framing

- **E1 — Treat cold-retrieval accuracy as the system's own eval** (measures success-criterion #2, currently
  unmeasured). *Caveat:* prompts are self-authored, so this is a **calibration** signal, not a clean effect
  size — weight it accordingly and prefer signal the system didn't author (the learner reporting real-world
  application) where available. Don't let primer grade itself on its own exam and call it mastery.
- **E2 — "Situated idea" dynamic prompts** (Matuschak, Nov 2024): store *invariant + source + intent* and
  regenerate varied probes over time instead of a frozen `Q::A`. Counters review boredom; tests transfer.
- **E3 — Preserve the generation effect:** at Recap, have the learner state the invariant in their own words
  *before* the Primer writes the retrieval prompts. A small protocol tweak in `lesson-protocol.md §5`.
- **E4 — A distillation layer for the lessons corpus** (DeepTutor L1→L2→L3): a future `/primer synthesize
  <domain>` that turns N lessons into a durable per-domain map. The topic-index is a status map, not a synthesis.

### Validated — name them so we don't churn on settled-good design

Class/instance split; stable/volatile = Letta memory blocks; three-timescale loop ≈ Generative Agents;
editable-markdown OLM; aggressive fade (expertise-reversal asymmetry); source-discovery + tagging; probe-first.
No change. These are the project's strengths and the literature backs them.

---

## 4. Implementation plan

Sequenced by *risk to a non-negotiable* first, then leverage. Effort: S (≤1 edit-pass), M (a few files +
protocol thought), L (new mechanism / design decision). Each wave is independently shippable.

### Wave A — Corrections (factual + de-personalization). Low risk, high goal-alignment.

| ID | Change | Files | Goal | Effort |
|----|--------|-------|------|--------|
| C4 | Replace 2σ/0.66/0.73–1.3 with "~0.4–0.7 SD, transfer-valid"; tag AutoTutor claim | `REQUIREMENTS.md`, `primer/lesson-protocol.md` | NN currency | S |
| C3 | Tag canon floor entries; mark date-bearing ones for verification | `primer/source-canon.md` | NN currency | S |
| C1 | De-personalize `system-prompt.md` (pull from profile); canon → seed pack; drop domain-slug enum | `primer/system-prompt.md`, `primer/source-canon.md`, `primer/lesson-template.md` | G3, G4 | M |

### Wave B — Close the loop (the structural fix). Medium risk; touches the feedback contract.

| ID | Change | Files | Goal | Effort |
|----|--------|-------|------|--------|
| C2 | Forgetting-aware confidence decay; decay stale *high*-confidence markers in minor-recalibrate | `primer/feedback-protocol.md` | G2, NN honesty | M |
| T1 | `/primer review` miss → calibration-log entry + confidence drop | `SKILL.md`, `primer/feedback-protocol.md` | G2 | M |
| E1 | Record cold-retrieval accuracy per review; surface trend (with self-authored caveat) | `SKILL.md`, `templates/learner/review-queue.md` | G2 | M |
| T7 | "just show me" escape hatch gated on struggle-tolerance | `primer/system-prompt.md`, `primer/lesson-protocol.md` | — | S |

### Wave C — Quality & hygiene. Low risk.

| ID | Change | Files | Goal | Effort |
|----|--------|-------|------|--------|
| T2 | Prompt-quality rubric + pattern language + self-check | `primer/lesson-template.md`, `primer/anti-patterns.md` | — | S |
| T5 | Reconcile resume/artifact path | `SKILL.md`, `primer/lesson-template.md` | — | S |
| T6 | `settings.json` deny-list for work/proprietary paths | `.claude/settings*.json`, `README.md` | NN privacy | S |
| T4 | Evidence-triggered recalibration (replaces N=5 tuning) | `primer/feedback-protocol.md`, `SKILL.md` | — | M |

### Wave D — Enhancements & decisions. Larger; some need a call.

| ID | Change | Files | Decision? | Effort |
|----|--------|-------|-----------|--------|
| T3 | SRS: Anki export **or** FSRS due metadata | `SKILL.md`, `templates/learner/review-queue.md` | ⚑ yes | M |
| E3 | Generation-effect tweak (learner states invariant first) | `primer/lesson-protocol.md` | no | S |
| E2 | Situated-idea dynamic prompts | `primer/lesson-template.md`, `SKILL.md` | ⚑ scope | L |
| E4 | `/primer synthesize <domain>` distillation verb | `SKILL.md` (+ new protocol) | ⚑ scope | L |

### Decisions required before Wave D (⚑)

1. **T3 — scheduling:** export to Anki (keep primer generation-only, honor §11 / P7), or own a lightweight
   FSRS schedule in-repo (richer `/primer review`, more to maintain)? Recommendation: **Anki export** first —
   it honors the existing out-of-scope decision and is one formatter; revisit FSRS only if review usage is high.
2. **C1 — canon:** ship a *thin* domain-agnostic starter and move the backend-heavy floor into the maintainer's
   instance, or ship *several* domain packs in the core? Recommendation: **thin starter + the backend pack as
   one example pack**, so a stranger isn't handed someone else's syllabus but the vetting work isn't lost.
3. **E2 / E4 scope:** enhancements, not corrections — defer until after a real intake + a handful of lessons
   produce data to design against (mirrors D-0004's "tune after real use" stance).

### Suggested order

C4 → C3 → C1 (Wave A, one session) → C2 + T1 + E1 + T7 (Wave B, the important one) → Wave C → revisit D after use.

---

## 5. Goal & enhancement coverage (every surfaced item has a disposition)

| Item | Disposition |
|------|-------------|
| C1, C3, C4 | Do now (Wave A) |
| C2, T1, E1, T7 | Do next (Wave B) |
| T2, T4, T5, T6 | Queue (Wave C) |
| T3 | ⚑ decide, then Wave D |
| E2, E4 | Defer until post-use data (⚑ scope) |
| E3 | Wave D, no decision needed |
| Validated set | No action — settled-good, leave alone |

Anti-drift check (per `GOALS.md`): every change above serves G1–G4 and none weakens a non-negotiable. C1/C2
*strengthen* G4/G2; C3/C4 *strengthen* the currency NN; T6 *strengthens* the privacy NN; T7 preserves
"productive struggle" while removing a failure mode the literature flags. No personal data moves toward the
core. Nothing here was requested as feature creep — it is a review the maintainer asked for.

---

## 6. Sources

Sweep A primaries: VanLehn 2011 (*Ed. Psychologist*); Kulik & Fletcher 2016 (*RER*); Ma et al. 2014 (*JEP*);
Nickow/Oreopoulos/Quan 2020 (NBER); Kestin et al. 2025 (*Scientific Reports*); Wang/Demszky et al. 2024
(arXiv:2410.03017); MathTutorBench (arXiv:2502.18940); Khajah/Lindsey/Mozer 2016 (EDM); Settles & Meeder 2016
(ACL); Choffin et al. 2019 (EDM); Tetzlaff et al. 2025 (*Learning and Instruction*); Bull & Kay 2007 (IJAIED);
Corbett & Anderson 1995 (UMUAI). Sweep B: Letta/MemGPT (arXiv:2310.08560); Park et al. 2023 (arXiv:2304.03442);
Matuschak (andymatuschak.org — "How to write good prompts", "situated ideas" 2024, "Why books don't work");
llm-knowledge-base, DeepTutor, Karpathy LLM-wiki (repos); Boucle "The Optimism Feedback Loop" (blog).
Weak-source flags retained from the sweeps: Khanmigo frustration/gaming modes and mnemonic-medium retention
figures rest on vendor/non-RCT/self-selected data — treat as directional, not established.
