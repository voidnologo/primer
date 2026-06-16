# `primer` — Requirements & Project Structure

> **Historical design contract.** This is the original v1 requirements doc, written when primer was a single-repo, single-user system. The architecture has since moved to a public-core / private-instance split with an intake interview and a multi-timescale feedback cycle. The **living** design record is now [`docs/engineering/GOALS.md`](docs/engineering/GOALS.md) (north star), [`docs/engineering/DECISIONS.md`](docs/engineering/DECISIONS.md) (decisions + rationale), and the protocols in [`primer/`](primer/). Read this for original intent; read those for current behavior.

A personal, Primer-style learning system. Implemented as a Claude Code skill (`/primer`) that produces interactive, adaptive lessons in the terminal, captures each session as a markdown artifact, and maintains a persistent learner model that evolves over time.

> "A book that knew her, that adapted itself to what she needed, that wove instruction into story." — *The Diamond Age*, paraphrased

---

## 1. Vision

The Primer in *The Diamond Age* is bonded to one reader. It is not a curriculum; it is a relationship. Three properties matter most:

1. **It knows the learner.** Voice, gaps, stack, prior sessions, current edge.
2. **It teaches just-in-time, not on a syllabus.** Topics surface when the learner pulls on them; prerequisites are offered, not enforced.
3. **It uses narrative.** Concepts are explained the way a senior engineer explains things over coffee — analogies grounded in things the learner already knows, building toward independent reasoning.

This system is the working approximation: a skill that, given a topic, generates an interactive lesson in the voice of a senior staff engineer, calibrated to the learner's current depth, and that captures every session into an evolving knowledge graph the learner owns and can revisit.

---

## 2. Design Principles

Drawn from adaptive-tutoring research and the strongest existing curricula in software engineering. A note on effect sizes, since currency cuts both ways: **Bloom's "2-sigma" is folklore** — it traces to unpublished dissertations and has never replicated; the 96-study tutoring meta-analysis pools to ~0.37σ (Nickow et al. 2020), and even live human tutoring tops out near 0.79σ (VanLehn 2011). Intelligent-tutoring-system medians land around 0.42–0.66σ (Ma et al. 2014; Kulik & Fletcher 2016), the upper end inflated by locally-authored tests. The headline generative-AI-tutor RCT (Kestin et al. 2025) is **0.63σ** honest — widely-cited "0.73–1.3σ" figures are quantile-derived, not the average effect. **The defensible design target is ~0.4–0.7σ on transfer-valid (not self-authored) assessments.** See [`docs/engineering/research/2026-06-15-ai-tutoring-and-learning-science.md`](docs/engineering/research/2026-06-15-ai-tutoring-and-learning-science.md) for the verified citations and `primer/source-canon.md` for the source canon.

**P1 — Senior peer, not teacher.** The lesson register is a senior engineer talking to a colleague. Terse, opinionated, allowed to disagree, defends correct positions under pushback. No cheerleading. No "Great question!". No motivational fluff.

**P2 — Productive struggle over fluent answers.** The "LLM Fallacy" — fluent prose making the learner feel competent without becoming so — is the failure mode. Every lesson includes moments where the learner is asked to predict, derive, or critique *before* the explanation lands.

**P3 — Primitives → failure modes → patterns → tradeoffs.** The structure shared by the strongest sources (DDIA 2nd ed., MIT 6.5840, Anthropic's "Building Effective Agents", Google SRE). Never start with a framework. Start with the underlying problem; arrive at the framework only after the problem demands it.

**P4 — Currency is non-negotiable.** Every lesson cites sources from a 2026-current allowlist. A "stale-source list" is maintained and explicitly avoided (e.g., pre-2024 LangChain monoliths, DDIA 1st ed., Alpine-as-default Dockerfiles). When a claim is from training rather than tool-grounded, it must be tagged.

**P5 — Adapt, don't generalize.** The learner profile is read at the start of every session and updated at the end. Difficulty, vocabulary, and depth fade based on demonstrated mastery. Default to terse expert register; the learner has 15+ years of backend experience.

**P6 — Two-track output.** Every session produces (a) the in-terminal conversation and (b) a structured `LESSON.md` artifact suitable for re-reading, sharing, or presenting at a meetup. The artifact is *the* unit of value — the conversation is just how it gets made.

**P7 — Embed retrieval, don't gamify it.** Each lesson ends with 5–15 atomic Q/A prompts in a known format (Anki-importable). No points, no streaks, no flashcard UI. Spaced retrieval rides on top of narrative work, not in place of it.

**P8 — Stack-aware, never proprietary.** The repo is public. Lessons never read, quote, or reference proprietary work code — no diffs, no snippets, no scenarios identifiable to a specific employer. Stack awareness comes from `learner/profile.md`, a hand-curated, public-safe statement of the learner's stack, problem shapes, and current responsibilities — plus whatever the learner brings to the live conversation. Examples in lesson artifacts are always canonical, synthesized, or fully anonymized. The work codebase informs *which topics matter* and *how to frame analogies*, never *what code appears in a lesson*.

---

## 3. The Learner (System Context)

This section is the *contract about who the system is for*. The skill reads it before every session.

- **Role:** Backend team technical lead. Currently responsible for updating, modernizing, and growing a Python web backend.
- **Background:** Long-time self-taught developer. 15+ years of production backend experience in Python and Elixir.
- **Goal:** Stay relevant as a senior backend engineer; grow into staff-level technical leadership; modernize the team's stack with current best practices.
- **Initial focus topics:** AI / agentic workflows · distributed systems · event-driven architecture · Docker · "thinking as a backend systems engineer" (architecture, scalability, reliability, design heuristics).
- **Register:** Comfortable in the CLI; comfortable with formal CS vocabulary. Wants narrative depth, not introductions. Prefers conversation over slides — "the way a senior engineer explains things at a meetup."
- **Visuals:** Charts, diagrams, ASCII art, and Mermaid all welcome. Mermaid renders on GitHub; ASCII renders in any terminal; both are used.
- **Failure mode to avoid:** Wasting time on a topic only to discover the world has moved on.

A richer, evolving version of this lives in `learner/profile.md` and is updated by the system after every session. The profile is written at a level of abstraction that is safe for a public repo — no employer name, no proprietary scenarios, no internal service names.

---

## 4. The Skill — `/primer`

### 4.1 Invocation forms

| Form | Behavior |
|---|---|
| `/primer <topic>` | Start an interactive lesson on `<topic>`. The skill checks the topic index for prior coverage, calibrates depth from `learner/profile.md`, and proposes a lesson plan before diving in. |
| `/primer next` | Suggest the 2–3 best next lessons given current profile (filling gaps, reinforcing recent learning, prerequisites for stated goals). User picks. |
| `/primer review` | 60–120 second interleaved retrieval warm-up over recent topics; surfaces from `learner/review-queue.md`. Can stand alone or precede a new lesson. |
| `/primer resume` | Pick up an in-progress lesson (state lives in `lessons/<topic>/<slug>/STATE.md`). |
| `/primer index` | Render `learner/topic-index.md` as a tree with status (covered / in-progress / next-suggested). |
| `/primer profile` | Show or update `learner/profile.md` interactively. |
| `/primer suggest <goal>` | Given a high-level goal ("I'm being asked to design a saga between two services"), suggest a *track* of lessons that gets the learner there. |

**Scenario anchoring is conversational, not flagged.** If the learner wants a lesson framed around a specific problem shape ("we're considering moving an internal reporting flow to event-driven — teach me CQRS with that in mind"), they say so in the opening turn. The skill responds in canonical / anonymized terms — no proprietary code or identifiers reach the artifact.

### 4.2 Lesson protocol — Elicit → Probe → Diagnose → Deepen → Recap

This is the core interaction loop, drawn from AutoTutor / Carnegie Cognitive Tutor research (deep-reasoning questions outperform recall by ≈one letter grade) and Khan Academy's Khanmigo Socratic system prompt (refuses direct answers; pushes the learner to reason first).

1. **Elicit** — Open with what the learner already believes/knows. ("Before we dig in: what's your current mental model of consensus? Where do you think it bites?") Brief; sets the calibration anchor.
2. **Probe** — Ask 1–2 deep-reasoning questions (causal, counterfactual, "what would break if…") that force the learner to derive a key invariant. Wait for an answer. Don't auto-complete.
3. **Diagnose** — Update the working model: which assumptions are sound, which are off, where the ZPD edge is. State this back to the learner briefly. Adjust the rest of the lesson accordingly.
4. **Deepen** — Now teach. Worked example → faded example → free problem. Layer in narrative; reach for the user's stack as analogy where natural. This is the bulk of the session.
5. **Recap** — Summarize the 3–5 invariants worth keeping. Generate the embedded retrieval prompts. Identify open threads to revisit. Update the profile + topic index.

The skill must hold the line under pushback when correct ("sycophancy collapse" is a documented failure mode). It is allowed and encouraged to disagree.

### 4.3 The `LESSON.md` artifact format

Every session writes one of these to `lessons/<topic-slug>/<YYYY-MM-DD>-<lesson-slug>.md`. Strict template:

```markdown
---
topic: distributed-systems
slug: 2026-05-09-consensus-and-raft
duration_minutes: 75
zpd_edge_before: <one line>
zpd_edge_after:  <one line>
sources_consulted: [list of URLs, with [verified] vs [from-training] tags]
freshness_check: <date the source canon was last validated>
---

# <Lesson Title>

## TL;DR
3–5 bullets. The invariants worth keeping.

## Where you started
Restated mental model from the Elicit step. The anchor.

## The problem (primitives → failure modes)
What is the underlying problem, before any tool? What goes wrong without one?

## The patterns
Worked examples, faded examples, free problem. Diagrams (Mermaid + ASCII) inline.

## Tradeoffs
Honest comparison: when does pattern X beat Y? What are the operational costs?

## Q&A
The substantive questions you asked and how they were answered. Verbatim where it matters.

## Open threads
Things we pulled on and set down. Saved to learner/open-questions.md too.

## Retrieval prompts
5–15 atomic Q/A pairs (Anki-import format, two-column or `Q::A`).
Include at least 2 deep-reasoning prompts (causal/counterfactual), not just recall.

## Sources
[Verified] sources with URLs and access dates.
[From-training] claims explicitly flagged.

## Next
2–3 follow-on lesson suggestions written into learner/topic-index.md.
```

### 4.4 Visuals

- **Mermaid first** for sequence diagrams, state diagrams, and flowcharts (renders on GitHub, lossless as code, good for re-reading).
- **ASCII art** for in-terminal moments where Mermaid wouldn't render (the live conversation). Used inline during the session, then a Mermaid version is generated for the artifact.
- **Tables** for tradeoff comparisons.
- **No images** in v1 — keeps the system text-native and grep-friendly.

---

## 5. The Learner Model

Files are markdown so the learner can read and edit them directly. The system reads them at session start and writes them at session end.

```
learner/
  profile.md          The "who you are" file. Role, stack, depth markers per topic, preferences, register. Updated each session.
  topic-index.md      Hierarchical map: domain → topic → sub-topic, with status: [unexplored|in-progress|covered|mastered] and links to lessons/.
  review-queue.md     Orbit-style retrieval prompts pending interleave. Pulled from at /primer review.
  open-questions.md   Threads pulled-on but not chased. Surfaced when relevant to a new lesson.
  log.md              Append-only one-line log of every session. Date · topic · mode · duration · ZPD-edge.
```

`profile.md` schema (markdown sections):

- **Identity** — name, role, repo context.
- **Stack & current responsibilities** — what kind of systems they ship and on what stack, at a level of abstraction safe for a public repo. (E.g., "Python web backend, Postgres + Redis, Docker on AWS, async work via SQS-like queues" — not employer/service names.)
- **Depth markers** — per top-level domain, a 1-line "current depth" claim with date. E.g. `distributed-systems: 2026-05-09 — comfortable with replication, fuzzy on consensus, no production Raft experience`.
- **Preferences** — narrative density, register, visual preferences, time budget per session.
- **Anti-preferences** — things that don't land. ("Don't use sports analogies.")
- **Active goals** — 1–3 multi-month learning goals in plain prose.

The system has explicit permission to update this file at the end of any session. The learner can edit it freely between sessions.

---

## 6. Source Canon

Maintained in `primer/source-canon.md`. Two lists:

**Allowlist (load-bearing in 2026)** — including, per topic:
- *AI / agentic*: Anthropic "Building Effective Agents", anthropic-cookbook patterns, 12-Factor Agents, LangGraph, Pydantic AI, MCP spec, Chip Huyen *AI Engineering*, Hamel Husain on evals.
- *Distributed systems*: MIT 6.5840, DDIA 2nd ed., Jepsen analyses, aphyr/distsys-class, Marc Brooker's blog, jepsen-io/maelstrom.
- *Event-driven*: microservices.io, Oskar Dudycz / event-driven.io, Kafka 2nd ed. (KRaft), Azure architecture patterns, NATS JetStream docs, Debezium.
- *Docker*: docs.docker.com/build, Poulton *Docker Deep Dive* 2025 ed., distroless, Chainguard Images, dive, Compose v2 docs.
- *Backend systems thinking*: system-design-primer, Google SRE books, *Software Engineering at Google*, Reilly *Staff Engineer's Path*, Will Larson / staffeng.com, The Pragmatic Engineer, High Scalability, Brooker + Sridharan blogs.

**Stale list (explicitly avoid)** — pre-2024 LangChain tutorials, DDIA 1st ed., "Microservices Patterns" (2018) book in favor of microservices.io + Dudycz, Burns "Designing Distributed Systems" (2018), Alpine-as-default Dockerfiles, older Coursera distsys.

**Cross-cutting shifts to encode**:
- *Agents*: simple composable LLM-call patterns first; reach for LangGraph/Pydantic AI when durable state demands it; MCP at the level of HTTP, not as optional.
- *Distributed systems*: less "implement Paxos," more "read a Jepsen report well." Formal methods (TLA+, P) entering practitioner mainstream.
- *Event-driven*: outbox-first; sagas only for true cross-service workflows; full event sourcing only for audit/finance domains. The field has cooled on "event-source everything."
- *Containers*: distroless / Chainguard have displaced Alpine; BuildKit features (cache mounts, secrets, bake) are no longer optional.

The canon is itself a living document. Each session checks `freshness_check` and re-validates if stale.

---

## 7. Anti-Patterns the System Must Resist

Encoded in `primer/anti-patterns.md` and enforced via the role contract:

1. **Sycophancy collapse** — folding when the learner pushes back, even when correct. The Primer holds the line on truth and explains why.
2. **The LLM Fallacy** — fluent output that lets the learner feel they understood something they didn't. Counter: every lesson has at least one "predict before reading" beat.
3. **Quiz-machine feel** — endless flashcards. Counter: retrieval prompts are the *exit* of a narrative session, not the session itself.
4. **Expertise reversal** — over-explaining to a senior. Counter: depth markers in profile drive aggressive fading; `--explain-deeper` is opt-in, not default.
5. **Hallucinated authority** on technical detail (APIs, perf numbers, RFCs). Counter: tag every claim as `[verified via docs]` or `[from-training]`; prefer tool-grounded answers.
6. **Generic curriculum drift** — slipping into topic-X-for-everyone mode. Counter: the lesson must reference at least one fact from `learner/profile.md` in its framing.
7. **No direct-answer-on-first-attempt** for conceptual questions. Khanmigo's rule. The first move is always a probe back.

---

## 8. Initial Topic Seed

Five top-level domains, with proposed first lessons. Not a fixed track — these are starting points the system can draw from when the learner asks for `/primer next` and has no other anchor.

- **AI / agentic workflows** — `agent-patterns-vs-frameworks` (the Anthropic taxonomy) → `evals-as-the-real-product` → `mcp-as-the-tool-calling-protocol` → `building-a-stateful-agent-with-langgraph`.
- **Distributed systems** — `consensus-without-implementing-paxos` → `replication-and-the-three-flavors-of-consistency` → `time-clocks-and-why-they-lie` → `reading-a-jepsen-report`.
- **Event-driven architecture** — `outbox-pattern-and-why-it-comes-first` → `sagas-orchestrated-vs-choreographed` → `when-to-actually-event-source` → `kafka-vs-nats-vs-redis-streams`.
- **Docker** — `images-as-filesystems-and-why-it-matters` → `multi-stage-buildkit-and-cache-mounts` → `distroless-and-the-chainguard-shift` → `compose-v2-as-a-dev-loop`.
- **Backend systems thinking** — `the-staff-engineer-shift` → `capacity-and-failure-budgets` → `design-decisions-as-tradeoff-tables` → `on-call-as-a-design-input`.

Order is suggestive. The skill chooses based on profile and pull.

---

## 9. Project Structure

```
knowledge/                       The repo *is* the skill directory.
├── SKILL.md                     The Claude Code skill. Routes args; references primer/* and learner/*.
├── README.md                    Pitch, install instructions, lesson index entry-point.
├── REQUIREMENTS.md              This document. The system contract.
├── LICENSE                      MIT.
│
├── primer/                      The system's "personality" and rules. Read by the skill every session.
│   ├── system-prompt.md         Role contract: senior staff engineer pairing. Negative constraints. Register.
│   ├── lesson-protocol.md       Elicit → Probe → Diagnose → Deepen → Recap, with examples.
│   ├── lesson-template.md       The LESSON.md format spec.
│   ├── source-canon.md          Allowlist + stale-list + cross-cutting shifts.
│   ├── anti-patterns.md         Sycophancy, LLM fallacy, expertise reversal, etc.
│   └── visuals.md               Mermaid + ASCII conventions.
│
├── learner/                     The persistent learner model. Read at start, written at end.
│   ├── profile.md
│   ├── topic-index.md
│   ├── review-queue.md
│   ├── open-questions.md
│   └── log.md
│
├── lessons/                     The accumulating corpus. One folder per top-level domain.
│   ├── ai-agentic/
│   ├── distributed-systems/
│   ├── event-driven-architecture/
│   ├── docker/
│   └── backend-engineering/
│
├── tracks/                      Future: curated multi-lesson sequences. Empty in v1.
│
└── tools/
    └── install.sh               Symlinks the repo into ~/.claude/skills/primer.
```

### Skill installation

The repo *is* the skill directory — `SKILL.md` lives at the root. Install by symlinking the whole repo into `~/.claude/skills/`:

```bash
ln -s "$(pwd)" ~/.claude/skills/primer
```

`tools/install.sh` automates this. The repo is the canonical thing; the user's machine just symlinks.

---

## 10. Repo Plan

- **Host:** `github.com/voidnologo/knowledge`
- **Visibility:** **Public.** Lessons are publishable artifacts (worth sharing with the team); the learner's profile is intentionally written at a public-safe level of abstraction. No proprietary code, scenarios, or identifiers ever land in the repo.
- **First commit contents:** `REQUIREMENTS.md`, `README.md`, `LICENSE`, the `primer/` and `learner/` scaffolding, the skill, `tools/install.sh`, `lessons/` with a README and one hand-authored reference lesson demonstrating the artifact format.
- **gh CLI is already authed as voidnologo with `repo` scope** — `gh repo create` will work.

---

## 11. Out of Scope (v1)

- Multi-user / sharing — this is one learner's Primer.
- Programmatic spaced-repetition scheduler — the system *generates* prompts; an external SRS (Anki/Mochi) does the scheduling. **(Superseded — see D-0018/D-0019 + Proposal 0002.)** Scheduling is now in-scope, self-contained, and deterministic (scripts + an optional local SQLite DB in the private data repo); cultivating the review habit is a project goal (Goal 5); external SRS export is optional, never required.
- Web UI — CLI only.
- Audio/video lessons.
- Pre-planned curriculum tracks — `tracks/` exists as a hook, but v1 ships ad-hoc with curriculum-aware suggestions.
- Reading from work codebases — out of scope. The skill never reads `~/Work/*`. Stack-aware framing comes from `learner/profile.md` (hand-curated by the learner) and from live conversation. Hard rule for a public repo.
- Proprietary scenarios — no employer names, no internal service names, no diffs of work code. The profile and any conversational scenario inputs must be sanitized before they shape an artifact.
- **Static-site rendering of lessons (v1.2 deferred).** The lessons are SSG-ready (markdown + frontmatter + Mermaid). SSG choice — Material for MkDocs, Astro+Starlight, or Jekyll — is deferred until ~5–10 lessons exist and the navigation shape is clear. Plan to deploy to GitHub Pages.

---

## 12. Success Criteria

The system is successful if, after 10 sessions, the learner can:

1. Pull up any `LESSON.md` and use it as a meetup talk outline with minor editing.
2. Answer the embedded retrieval prompts from a 4-week-old lesson with >70% accuracy (cold).
3. Trace at least one real architectural decision (e.g., a step in the realtime-feeds migration, or a backend modernization call) back to insights from a specific lesson in the corpus.
4. Feel that the Primer "knows" them — reads the profile, references prior sessions, calibrates correctly without being told.
5. Trust the source canon: zero "I learned X but it turned out to be a 2022 take" moments.

---

## 13. Resolved Decisions

1. **Repo visibility** — **public.** Profile is written at a public-safe level of abstraction. No proprietary code or identifiers in the repo, ever.
2. **Skill name** — `/primer` (hyphen, matching convention).
3. **Stack grounding** — always-on via profile; never reads `~/Work/*`; scenario anchoring happens conversationally with canonical / anonymized examples in the artifact.
4. **First lesson** — no live sample run today. Refinement happens through real use.
5. **v1 scope** — recommended: skill + `primer/*` + `learner/*` scaffolding + install + repo + one hand-authored reference `LESSON.md` demonstrating the artifact format.

---

## 14. Implementation Order

1. Write `primer/system-prompt.md` and `primer/lesson-protocol.md` — the core voice contract.
2. Write `primer/lesson-template.md`, `primer/source-canon.md`, `primer/anti-patterns.md`, `primer/visuals.md`.
3. Write `SKILL.md` — the skill that ties it together.
4. Scaffold `learner/` — empty `profile.md` (filled interactively in step 6), `topic-index.md` seeded with §8, empty `review-queue.md`, `open-questions.md`, `log.md`.
5. Write `tools/install.sh`, `README.md`, `LICENSE`.
6. Run an interactive profile bootstrap with the learner — fill `profile.md` with real depth markers and preferences (public-safe abstraction).
7. Hand-author one reference `LESSON.md` in `lessons/ai-agentic/` to demonstrate the artifact format. Static, not a live session.
8. `git init`, first commit, `gh repo create voidnologo/knowledge --public`, push.
9. Symlink the skill and verify `/primer index` works end-to-end.
