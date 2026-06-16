# Research — Landscape of comparable LLM-learning projects (2023–2026)

> **Durable research artifact.** Captured 2026-06-15 (Session 2) so we don't repeat this search soon.
> **Fresh until ~2026-09**; re-verify links/activity past that. Feeds Proposal 0001 (validates the
> class/instance + stable/volatile architecture; sources C2, E2, E4).
>
> **Provenance:** web sweep (GitHub, blogs, HN, arXiv, personal sites). Each item flagged **[verified]**
> (page/repo fetched) or **[snippet]** (search-result summary only). ⭐ = most relevant to a primer-style
> design (markdown profile + generated lessons + class/instance split).

---

## 1. LLM-as-tutor projects with persistent learner models

- ⭐ **tutor-gpt (Plastic Labs)** — github.com/plastic-labs/tutor-gpt — [verified]. Reasons about the
  learner's mental state (Theory of Mind), rewrites its own prompts from a user representation; learner model
  offloaded to a service (Honcho) + Supabase. *Borrow:* model the learner's beliefs, not just right/wrong.
  *Pitfall:* a service-backed model is opaque — opposite of a hand-editable markdown profile.
- ⭐ **OpenTutor (zijinz456)** — github.com/zijinz456/OpenTutor — [verified]. Local-first; layered state in
  SQLite: **FSRS 4.5** (scheduling), **BKT** (mastery), behavioral signals (fatigue, error patterns) for
  depth, prerequisite knowledge graph for ordering. *Pitfall:* four overlapping subsystems are a lot to keep
  consistent solo.
- ⭐ **llm-knowledge-base (arturseo-geo)** — github.com/arturseo-geo/llm-knowledge-base — [verified] —
  **closest spiritual match.** A markdown *schema standard* (AGENTS.md spec) with an SR layer:
  `raw/` → LLM compile → `wiki/` → `learning/` (`_review.md` FSRS queue, auto flashcards, `gaps.md` open
  questions). Frontmatter flags `confidence: speculative`, `status: quarantined` to keep low-confidence
  content out of the profile. *Names the pitfall directly:* "once agent-compiled articles mix with your
  personal notes, [the vault] stops being a representation of your knowledge" — **validates primer's
  public-core/private-data split.** *Borrow:* confidence/quarantine frontmatter flags; explicit `gaps.md`.
- ⭐ **DeepTutor (HKUDS)** — github.com/HKUDS/DeepTutor — [verified] — 24.8k★, Apache-2.0. **Three-layer
  file-based memory:** L1 raw turn logs (`.jsonl`) → L2 per-surface summaries (`.md`) → L3 cross-surface
  synthesis (`profile`, `preferences`, `scope`). Human-editable "memory workbench." *Borrow:* L1→L2→L3
  distillation maps onto primer's session-log → DECISIONS/profile promotion (→ **E4**). *Pitfall:* many
  "surfaces" + versioned indexes = heavy bookkeeping.
- **OATutor-LLM-Learner (UC Berkeley CAHLR)** — github.com/CAHLR/OATutor-LLM-Learner — [verified base].
  Pre-LLM ITS (BKT, 4 params/skill, local-first) with an LLM learner-modeling fork. *Borrow:* a tiny per-skill
  probability table is far lighter than embeddings. *Pitfall:* how BKT state and the LLM reconcile is
  under-specified.
- **IntelliCode** (arXiv:2512.18669) — [verified abstract]. Multi-agent tutor with **versioned central learner
  state under a single-writer policy** (one Orchestrator writes; six agents are pure read/transform). *Borrow:*
  single-writer + versioned-state + pure transforms = strong auditability.
- *Snippet-only research designs:* **TASA** (forgetting-aware dynamics, arXiv:2511.15163), **LOOM**
  (learner-memory graph, 2511.21037), **Agent4Edu** (generative-agent learners, 2501.10332).
  **vertesia/large-language-tutor** [verified] — negative example: persistence is future work, not built.

---

## 2. Andy Matuschak (the intellectual center of this space)

- **"Why books don't work"** — andymatuschak.org/books — [verified]. Books assume *transmissionism*; the
  metacognitive work is offloaded to a reader who lacks the skill. Prescription: design mediums where
  *engaging in the obvious fashion* produces understanding. **Mandate for primer: the system, not the learner,
  owns the metacognitive scaffolding** (what/when/how-deep to review).
- **Mnemonic medium / Quantum Country** (w/ Nielsen) — quantum.country — [verified]. Prose pauses for
  retrieval questions, then expanding-interval reviews; *prompts are author-provided* (no card-writing burden).
  *Pitfalls he names:* poor at producing complex *understanding* (vs recall); SRS is "an onerous habit",
  benefits feel slow; cold-start needs critical mass.
- ⭐ **"How to write good prompts"** — andymatuschak.org/prompts — [verified]. "Prompt design is task design."
  Five attributes: **focused, precise, consistent, tractable, effortful.** Usable as both a generation spec
  *and* a quality classifier/eval. *Pitfall:* conceptual ("explain why") prompts are far harder than factual.
  → **primer: T2.**
- ⭐ **"Wizard-of-Oz learning assistant"** (Feb 2023) — andymatuschak.org/woz-learning — [verified]. He
  hand-played the AI tutor first. Findings: ground prompts in the learner's *actual motivating project*;
  talk-aloud review transcripts are highest-signal; detect the learner's **mode — syllabus / exploration /
  fiery** — and adapt. *Pitfall:* N-of-1 "resists systematization."
- ⭐ **"Situated ideas / machine-generated prompts"** (Nov 2024) — andymatuschak.org/situated-idea-memory-system
  — [verified] — **his most relevant LLM work.** Replaces the static flashcard with a **"situated idea"**
  (source text + highlight + intent), from which the system *synthesizes varied activities over time* (varied
  cues, rising depth). Architecture: generate many prompts, then **filter with a taste-trained classifier**
  (2,000+ hand-labeled samples) rather than make the base generator uniformly good. → **primer: E2.**
  *Pitfall he names:* the classifier "generalizes much less well to out-of-sample texts."
- **The LLM prompt-authoring ceiling** — notes.andymatuschak.org/zGkLPdiEs7Qohkesq7TNiBe — [verified]. GPT-4
  writes usable prompts for *declarative* knowledge given explicit principles, but for *conceptual* material
  produces prompts that "reinforce the surface — what is said, rather than what it means." Fix: feed an
  explicit **pattern language** (definition, example-classification, why-it-matters, application, contrast).
  **Single biggest risk for any LLM prompt-authoring feature: "prompt-shaped text".** → **primer: T2.**
- **Orbit** — github.com/andymatuschak/orbit · withorbit.com — [verified]. Productized SR engine with an open
  authoring API; treat scheduling/retrieval as shared infrastructure. *Pitfall:* "research vehicle"; attrition.

---

## 3. Markdown / file-based "second brain" + LLM

**Read-side (RAG over notes):** Smart Connections [verified] (local embeddings, never writes);
Copilot for Obsidian [verified] (RAG with citations back to notes); Khoj [verified] (35k★, scheduled
automations ≈ spaced nudges); Reor [verified] (auto-links by similarity). *Common pitfall:* similarity-only
links are noisy; stale embeddings → stale answers.

**Write-side (LLM authors markdown back):** obsidian-flashcards-llm [verified] (LLM writes cards into the note
in SR syntax — generation and scheduling decoupled; *pitfall:* no grounding → hallucinated facts into the
deck); ⭐ **AI-powered Zettelkasten (joshylchen)** [verified] (typed bidirectional links supports/refines/
contradicts; **CEQRC loop: Capture → Explain → Question (Feynman) → Refine → Connect**, via an MCP server —
the Feynman "Question" stage is a learning mechanic, not just retrieval).

**"Learning OS" / agent-over-markdown:**
- ⭐ **Karpathy "LLM Wiki" pattern** — aimaker.substack.com — [verified]. Three layers: immutable `sources/`
  → LLM-generated wiki → a **`CLAUDE.md` schema governing how the model reads/writes**. ≈ primer's
  class/instance reach. *Pitfall flagged:* "maintenance-free" is theoretical; semantic drift grows; users
  over-trust auto-links.
- ⭐ **Personal OS + Markdown Wiki (lawyer112)** — github.com/lawyer112/personal-os-wiki — [verified].
  Separates durable **Wiki** from **OS execution state** (runtime data never pollutes version-controlled
  notes) + a claim→evidence→review protocol. *Borrow:* knowledge/execution separation mirrors
  public-core/private-data. *Pitfall:* very early; heavy infra.

**Dominant community pitfall** (Zettelkasten forums): auto-generating notes short-circuits the thinking that
makes a note worth keeping. Consensus: use the LLM for the *learning phase* (Feynman questioning, spotting
wrong inferences) and *bookkeeping* (linking/tagging), **not** the synthesis itself. → **primer: E3.**

---

## 4. Skills / rules / agent-memory for learning + memory architectures

**Practical (skills & rules):**
- ⭐ **learning-opportunities (DrCatHicks)** — github.com/DrCatHicks/learning-opportunities — [verified]. A
  Claude Code skill injecting evidence-based exercises (prediction→reveal, teach-it-back) at coding moments.
  **No persistent profile, no adaptive difficulty.** *The clearest validation of primer's thesis:* its gap
  (session-scoped, can't escalate) is exactly what an evidence-backed persistent profile fills. Exercise
  formats are borrowable.
- **self-learning-claude (reshadat)** — [verified]. Per-project JSON "playbook", typed categories
  (pitfall/strategy/domain/endpoint/code), updated on success/failure. *Borrow:* typed-category taxonomy.
  *Pitfall:* JSON + no compaction → unbounded noise.
- **claude-reflect** — github.com/BayramAnnakov/claude-reflect — [snippet]. Captures corrections into
  CLAUDE.md/AGENTS.md. Closest existing "markdown-as-profile updated by a reflection loop." *Pitfall:* no
  stable/volatile split → always-loaded bloat.
- ⭐ **Cursor "Memory Bank" (vanzan01)** — [snippet]. Persistent memory as a `memory-bank/` of markdown;
  **stateless commands** (read files → act → write files); core-vs-optional split; `/reflect` + `/archive`
  lifecycle. Structurally ≈ a markdown learner profile. *Pitfall:* files drift/bloat without disciplined
  archiving — **compaction must be first-class.**
- **Cursor rules evolution** (`.cursorrules` → `.cursor/rules/*.mdc` with YAML frontmatter) — [verified]. The
  lesson *is* the evolution: a flat profile doesn't scale; frontmatter + scoping does. *Pitfall:*
  `alwaysApply` overuse blows the context budget.

**Memory architectures (mechanics for stable/volatile + reflection):**
- ⭐ **MemGPT / Letta** — arXiv:2310.08560 · letta.com/blog/agent-memory — [verified] — **canonical design.**
  **In-context memory blocks** (`persona`, `human`; each label+description+value+**char-cap**, agent-editable,
  pinned every prompt) vs **out-of-context** recall/archival (searched on demand). Compaction = memory-pressure
  eviction + recursive summarization; **sleep-time compute** = async agents refine blocks during idle. Letta:
  "translates directly to frontmatter-based markdown files with editable metadata sections." **Strongest match
  to primer:** persona/human ≈ stable traits vs volatile; char-caps force compaction; sleep-time compute =
  batch reflection *between* lessons. *Pitfall:* self-editing memory can overwrite good data — gate on
  caps/structure.
- ⭐ **Generative Agents (Park et al., Stanford 2023)** — arXiv:2304.03442 — [verified abstract]. **Memory
  stream** (recency + LLM-assigned **importance 1–10** + relevance) + **reflection** triggered when cumulative
  importance crosses a threshold (~150 in the paper), synthesizing higher-level conclusions written *back* as
  first-class entries. **primer's reflection blueprint:** score evidence; when importance accumulates,
  synthesize a durable trait ("learner consistently confuses X with Y"). → **T4.** *Pitfall:* each reflection
  is an LLM call; gate promotions on *repeated* evidence to avoid noisy rewrites.
- **Reflexion (Shinn et al., NeurIPS 2023)** — arXiv:2303.11366 — [verified abstract]. Failure → short *verbal*
  lesson in a bounded episodic buffer → carried to next attempt. *Borrow:* cheap, transparent "mistake →
  actionable note → primes next lesson." *Pitfall:* bounded by design — promote recurring lessons to durable
  storage.

---

## 5. "Self-improving" / reinforcement-loop-on-yourself

- **"Talent as a Reinforcement Loop, Not a Gift"** (Goedecke, attrib.) — HN 45683262 — [snippet; reconstructed].
  Talent as a self-reinforcing loop: small win → reward → reinforced behavior. *Borrow:* engineer frequent
  visible early wins so reinforcement fires. *Pitfall:* motivational metaphor with no objective reward signal.
- **QS Primer: Spaced Repetition and Learning** — quantifiedself.com — [verified]. The QS-for-skills lineage
  (Howard, Craig, Winter). *Borrow:* Winter's trick — hold task difficulty constant and treat your score as a
  sensor for cognitive state. *Pitfall (Wozniak):* "Do not learn if you do not understand" — retention metrics
  measure recall, not comprehension; optimizing the proxy diverges from the goal.
- ⭐ **The Optimism Feedback Loop** — blog.boucle.sh/posts/the-optimism-feedback-loop — [verified] — **the
  indispensable cautionary rule.** An agent in a closed self-assessment loop read its own previous summary as
  ground truth and wrote a slightly more positive one each time; over 140 iterations it fabricated "99.8%
  accuracy." "The drift is imperceptible within a single loop." **Design rule for primer:** anchor
  self-assessment to *external* signal (real outcomes, holdback sets, peer review) or a self-grading loop
  drifts optimistic and you won't feel it. → **C2, E1.**
- **HypoCompass (CMU)** — arXiv:2310.05292 — [snippet]. Ericsson-style deliberate practice: learner
  hypothesizes the bug cause while the LLM handles adjacent low-value work. *Borrow:* offload the skill you're
  *not* training so all load lands on the target.
- **Nat Eliason — Deliberate Practice** — nateliason.com/blog/deliberate-practice — [verified]. Ericsson's
  4-step loop; the LLM fills the "frequent feedback" slot. *Pitfall:* "self-devised feedback" is where
  self-grading inflation enters.
- **"Teach Your LLM to Teach You Back"** — medium — [verified]. System prompt instructs the LLM to *suppress
  praise* and tag cognitive state from a fixed lexicon. *Borrow:* observation over encouragement (≈ primer's
  no-fluff register). *Pitfall:* assumes the LLM can distinguish genuine drift from normal variation.
- **skill-eval-harness (adewale)** — github.com/adewale/skill-eval-harness — [verified]. Agent-skill eval, but
  the mechanics transfer: a **holdback set** (unseen problems → test transfer) and **leakage detection** (flag
  when the answer appears before recall). *Gap:* a genuine *human-learning* eval harness appears to be an
  unfilled niche. → **E1.**
- **SmartFlash + testing-effect cluster** — arXiv:2602.14431 — [snippet]. Backs retrieval > restudy and
  interleaving. *Pitfall directly relevant:* automating card *creation* removes the **generation effect** —
  "I spend all my energy preparing" *is* the learning. → **E3.**

---

## 6. The through-line for a primer-style builder

1. **Persistent evidence-backed profile is the real gap.** Every existing *learning skill* is session-scoped
   (learning-opportunities) — that gap is primer's thesis. Architecture papers (Letta, Generative Agents)
   supply the mechanics.
2. **Stable-vs-volatile split, on markdown:** small capped always-loaded **core** (stable traits; Letta
   `persona`/`human`) + larger **archival evidence store** (logs, observations) retrieved not always-loaded.
3. **Layered distillation is the consensus shape:** raw logs → session/surface summaries → consolidated profile
   (DeepTutor L1/L2/L3; primer's session-log → DECISIONS/profile). → **E4.**
4. **Reflection must be gated and batched:** synthesize on a threshold (Generative Agents); gate on *repeated*
   evidence; run as sleep-time/batch work; **compaction is first-class** (Cursor Memory Bank). → **T4.**
5. **Two failure modes to design against:** **optimism drift** (Boucle — anchor to external signal) and
   **"prompt-shaped text" / generation-effect loss** (Matuschak, SmartFlash — taste-classifier + keep *some*
   generation work with the learner). → **C2, T2, E3.**
6. **Validated separations:** keep agent-generated knowledge apart from human notes (llm-knowledge-base,
   Karpathy, Personal OS) — direct support for primer's public-core/private-data and class/instance design.

**Closest analogs to study first:** llm-knowledge-base (markdown schema + SR + confidence flags),
DeepTutor (L1/L2/L3 editable memory), Karpathy LLM-wiki (`CLAUDE.md`-as-schema), Letta memory-block model.
*Re-verify before quoting:* Generative Agents threshold numbers (secondary source); Goedecke post,
claude-reflect, Memory Bank specifics (snippet-only).
