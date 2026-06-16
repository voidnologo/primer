# Research — AI/LLM tutoring & learning science: state of the art (2024–2026)

> **Durable research artifact.** Captured 2026-06-15 (Session 2) so we don't repeat this search in this
> session or near ones. Treat as **fresh until ~2026-09** (3-month horizon, matching the canon's freshness
> rule); re-verify quantitative claims past that. Feeds Proposal 0001 (findings C2, C4, T2, T7, E1, E3).
>
> **Provenance:** web sweep + adversarial re-verification of 13 load-bearing claims against primary sources.
> Effect sizes are Cohen's *d* / Hedges' *g* (SD units) unless noted. Each section flags **[strong]**
> (RCT / replicated meta-analysis / primary doc) vs **[weak]** (vendor / non-RCT / self-selected sample).

---

## 1. Socratic / answer-refusing LLM tutors (Khanmigo et al.)

- **The strongest positive RCT is AI-assists-human, not AI-refuses-student.** Stanford *Tutor CoPilot*
  (Wang, Demszky et al., arXiv:2410.03017, 2024) — preregistered RCT, ~900 tutors / ~1,800 K-12 students —
  raised topic mastery +4pp overall (p<0.01), +9pp for lower-rated tutors, at ~$20/tutor/yr. It nudged
  *human* tutors toward Socratic questioning. Does **not** transfer to a student-facing bot that withholds answers.
- **Capability and pedagogy trade off.** MathTutorBench (arXiv:2502.18940, 2025): GPT-4o ~90% problem-solving
  but ~50% scaffolding; a math-specialist model 88% solving / 6% scaffolding. Models best at being *correct*
  are systematically worst at *withholding* — they default to revealing the full solution.
- **Current LLM tutors are "generic," not adaptive.** "Discerning Minds or Generic Tutors?"
  (arXiv:2508.06583, 2025): models affirm correct answers but give vague feedback on wrong ones; most score
  <0.55 on redirecting confused learners; handle *explicit* confusion ("I'm lost") far better than *implicit*
  error signals. Socratic questioning misaligned with readiness can induce cognitive overload (argued
  theoretically, not yet measured via dropout).
- **Khanmigo's math errors were real and systematic** (WSJ, 2024): miscalculated 343−17, disputed
  15²−9²=144, typically failed to self-correct on recheck. Fix was **architectural** — a dedicated calculator
  tool, forced retrieval of human-authored exercises/hints before answering, text representations of graphics.
  No before/after accuracy numbers published.
- Socratic dialogue *can* win when well-aligned: 94-student RCT (Zhang et al., *Computers & Education*, 2025)
  — Socratic agent beat non-Socratic on achievement and critical thinking. Small, single-context.

**Divergence flag (popular vs evidence):** the repeated failure modes — learner frustration ("just tell me"),
gaming/shortcut-seeking, drop-off — appear almost entirely in **vendor-adjacent reviews and pilot anecdotes**,
**[weak]** not rigorous studies. No peer-reviewed RCT quantifies frustration rate, jailbreak frequency, or
dropout for answer-refusing tutors. Vendor figures ("23% improvement in 4 weeks", "frustration subsides after
3–4 sessions") have no published methodology — marketing.

**Design implication:** don't make the LLM compute or withhold by willpower — route to tools, retrieve vetted
content; gate Socratic pressure on a readiness signal; provide an explicit "just show me" escape hatch (the
frustration mode is plausible but unmeasured). → **primer: T7, and validates anti-pattern #7.**

---

## 2. Bloom's 2-sigma & honest ITS effect sizes  [all primary-verified]

- **2σ has never been replicated.** Bloom (1984) claimed ~2.0 SD for mastery tutoring; traces to unpublished
  dissertations. 96-study tutoring meta-analysis (Nickow, Oreopoulos & Quan, NBER 2020 / AERJ 2024): pooled
  **0.37 SD** — none near 2.0.
- **Even live human tutoring is ~0.79.** VanLehn (*Educational Psychologist*, 2011): human tutoring d≈**0.79**,
  ITS d≈**0.76** — nearly equal; explicitly "did not confirm" the believed 1.0/2.0 figures.
- **ITS median ≈ 0.66, test-dependent.** Kulik & Fletcher (*RER*, 2016): median **0.66 SD** across 50
  evaluations — but larger on locally-developed than standardized tests, so 0.66 is upper-leaning.
- **Conservative anchor: g≈0.42.** Ma, Adesope, Nesbit & Liu (*JEP*, 2014; 107 effect sizes, N=14,321): ITS
  beat large-group teaching at g≈**0.42**; **no significant difference vs individual human tutoring**
  (g≈−0.11, n.s.). At-scale real-world tutoring is far smaller (~0.06–0.37).
- **Headline AI-tutor RCT** (Kestin et al., *Scientific Reports* 2025, N=194 Harvard physics): GPT-4 tutor
  beat in-class active learning. Honest number is **0.63 SD** (plain linear regression). "0.73–1.3 SD / over
  double learning" figures are **entirely quantile-regression-derived** medians, not the average treatment effect.

**Divergence flag:** "2 sigma" is a myth; even human tutoring tops near 0.8. "0.66σ for ITS" defensible *as a
median* but inflated by local-test alignment. **"Gen-AI tutors deliver 0.73–1.3σ" is cherry-picked** — one
~2-week, single-topic, Harvard-only RCT whose own point estimate is 0.63; the 1.3 is a specific quantile.

**Design implication:** target **~0.4–0.7 SD on transfer-valid (not self-authored) assessments**; treat 2σ as
folklore; measure against delayed post-tests, not vendor headlines. → **primer: C4, E1 caveat.**

---

## 3. Spaced repetition + retrieval practice in narrative learning

**Robust [strong]:**
- **Testing effect:** retrieval beats restudy at 2-day/1-week delays; restudy wins only at ~5-min delays
  (Roediger & Karpicke, *Psychological Science*, 2006).
- **Spacing effect:** distributed > massed across 839 assessments / 317 experiments (Cepeda et al., *Psych
  Bulletin*, 2006). Optimal gap is a *shrinking fraction* of the target retention interval (~10–20% at 1 week
  → ~5–10% at 1 year; Cepeda et al. 2008) — no single fixed interval is optimal.
- **Interleaving** roughly doubled next-day scores while *hurting* in-session performance (Rohrer & Taylor,
  2007/2010).
- **Desirable difficulties** (Bjork & Bjork, 2011): spacing/interleaving/testing slow apparent learning but
  improve retention/transfer; learners reliably *misjudge* them (prefer blocking/massing) — a metacognitive illusion.
- **Mnemonic medium:** Matuschak & Nielsen embed expert-authored SRS prompts in prose (*Quantum Country*;
  "How to write good prompts," 2020 — **focused, precise, consistent, tractable, effortful**). Orbit
  generalizes it; explicitly a **research vehicle, not a validated product**.

**Divergence flags (overreach):**
- **"Interleaving always helps" is false.** Helps similarity-based / low-discriminability category learning;
  **blocking can beat it for rule-based learning and high-discriminability categories** (Carvalho & Goldstone;
  Firth et al. 2021 review).
- **"Testing effect transfers to everything" is overstated.** Robust for near transfer / simple material;
  **mixed for far transfer and complex material** (Pan & Rickard; Springer 2024).
- **Mnemonic-medium evidence is thin [weak]:** *Quantum Country* 2019 data — only ~29% who finished in-text
  review reached the 1-month level; self-selected, **no control group**; ~35–50% reading-time overhead.
- **LLM-auto-generated cards are not uniformly reliable** — quality varies by hallucination rate and
  objective-coverage; improves markedly when the model is given explicit learning objectives (medRxiv 2025).

**Design implication:** build retrieval + expanding-interval scheduling (highest-confidence levers); author
prompts against explicit objectives, not blind auto-generation; apply interleaving selectively; don't promise
far transfer from SRS alone. → **primer: T2, T3, E1; tempers success-criterion #3 (far-transfer) to aspiration.**

---

## 4. Learner modeling & open learner models (OLM)  [verified]

- **BKT** (Corbett & Anderson, UMUAI 1995): 4 params — prior P(L0), learn P(T), guess P(G), slip P(S).
  **No forgetting** — mastery is monotonic non-decreasing. Structural limitation for any long-horizon tutor.
- **Deep Knowledge Tracing** (Piech et al., NeurIPS 2015): one LSTM over the interaction sequence, no
  hand-coded skill structure.
- **Performance Factors Analysis** (Pavlik, Cen & Koedinger, AIED 2009): interpretable logistic model counting
  prior successes/failures per skill; **AFM** counts opportunities only.
- **Attention/transformer KT:** SAKT (Pandey & Karypis, EDM 2019); AKT (Ghosh/Heffernan/Lan, KDD 2020) —
  monotonic exponential-decay attention + Rasch/IRT embeddings.
- **Forgetting-aware models** (the fix for stale estimates): **Half-Life Regression** (Settles & Meeder, ACL
  2016), p=2^(−Δ/h), trained on ~13M Duolingo traces, drives Duolingo's scheduler; **DASH / DAS3H**
  (Lindsey; Choffin et al., EDM 2019) add time-window features to logistic KT for distributed practice.
- **Open Learner Models** (Bull & Kay SMILI framework, IJAIED 2007): inspectable / editable / negotiable;
  analyzed by *what* is disclosed, *to whom*, and *how* the learner can interact.

**Divergence flag (big one):** **"Deep learning crushes BKT" does not survive replication.** Khajah, Lindsey &
Mozer ("How Deep is Knowledge Tracing?", EDM 2016): BKT + forgetting + skill-discovery + individualization is
**"indistinguishable from DKT"**. Xiong et al. (EDM 2016): DKT's ASSISTments-2009 gains were inflated by data
issues (threefold, incl. duplicated rows); on cleaned data no clear edge over PFA. SAKT's claimed superiority
**didn't replicate** in AKT's own experiments.

**Design implication:** an interpretable forgetting-aware model (augmented BKT / PFA+DASH or HLR) matches deep
KT, is far cheaper, and is inspectable enough to expose as an editable OLM; **add decay so estimates lapse
toward "needs review" instead of staying mastered forever.** → **primer: C2 (decay), validates the
editable-markdown profile as a textbook OLM.**

---

## 5. Expertise reversal & adaptive fading  [all verified]

- **Expertise reversal effect** (Kalyuga, Ayres, Chandler & Sweller, *Ed. Psychologist*, 2003): guidance that
  helps novices loses value and can **harm** experts — redundant guidance becomes extraneous working-memory
  load (Kalyuga, *Ed. Psych. Review*, 2007).
- **Worked-example effect** (Sweller & Cooper, 1985): novices learn faster from worked examples than equivalent
  problem-solving.
- **Guidance-fading effect** (Renkl & Atkinson, 2003): fade **full worked example → completion problem →
  independent problem solving** as expertise grows.
- **Adaptivity works through efficiency:** Kalyuga & Sweller (ETR&D 2005) — rapid expertise + cognitive-load
  assessment to adapt. In a Geometry Cognitive Tutor, **adaptive** fading beat fixed fading and standard
  tutored problem-solving on delayed transfer, in less time (Salden, Aleven, Renkl & Schwonke).
- **2025 meta-analysis** (Tetzlaff, Simonsmeier, Peters & Brod, *Learning and Instruction*; 60 experiments,
  N=5,924): low-prior-knowledge learners benefit from high assistance (**d≈0.505**); high-prior-knowledge
  learners are **harmed** by it (**d≈−0.428**). The effect is **asymmetric — helping novices > harming
  experts** — robust in higher ed, weaker for young children and humanities/language.

**Divergence flags:** "more guidance/hints/feedback = better" contradicts cognitive-load theory — persistent
high assistance for advancing learners *is* the failure mode. "AI tutors automatically realize adaptive fading"
is unsupported; the validated adaptation signal is **expertise level + cognitive load**, not engagement/click
data, and that rapid-assessment mechanism has **not** been shown to transfer to LLM tutors.

**Design implication:** fade scaffolding as the learner model rises; default to *under*-scaffolding (the
asymmetry means a wrong guess hurts experts less than smothering novices); trigger fading off expertise/load
estimates, not engagement. → **primer: validates "fade fast / default-terse"; sharpens C1 (a hardcoded-expert
engine under-scaffolds novice adopters).**

---

## 6. Cross-cutting takeaways

1. The most defensible architecture is **"AI assists + tools + vetted content," not LLM-as-omniscient-oracle.**
   Every well-evidenced win routes around raw LLM generation.
2. **Target ~0.4–0.7 SD on transfer-valid assessments.** 2σ is folklore; the best AI RCT is ~0.63 honest.
3. **Prefer interpretable, forgetting-aware learner models** — match deep KT, cost less, surface as editable OLM.
4. **Build retrieval + expanding-interval spacing + adaptive fading** — the three highest-confidence levers —
   but apply interleaving selectively and don't promise far transfer.
5. **Three popular claims to design *against*:** "interleaving always helps", "deep KT beats BKT",
   "generative AI tutors = 1–2σ".

*Weak-source caveats retained:* §1 frustration/gaming modes and §3 mnemonic-medium retention figures rest on
non-RCT / self-selected / vendor sources — directional, not established.
