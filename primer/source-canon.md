# Source Canon — 2026-Current

The allowlist + stale-list the skill draws from. Every lesson's `sources_consulted` should pull from the allowlist. Anything in the stale-list must be explicitly avoided — the learner has stated that wasted-time-on-outdated-takes is the failure mode they most fear.

This file is itself a living document. Each session checks `freshness_check` in its frontmatter; if the canon is more than ~3 months stale at session start, re-validate before grounding claims.

---

## Allowlist (load-bearing in 2026)

### AI / Agentic Workflows

- **Anthropic — "Building Effective Agents"** — https://www.anthropic.com/research/building-effective-agents — Canonical taxonomy: workflows vs agents; chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.
- **Anthropic Cookbook — patterns/agents** — https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents — Reference implementations of the patterns above; minimal, no-framework code.
- **12-Factor Agents (Dex Horthy / HumanLayer)** — https://github.com/humanlayer/12-factor-agents — The "12-factor for LLM apps." Production checklist.
- **LangGraph** — https://langchain-ai.github.io/langgraph/ — Stateful graph orchestration. Reach for it when durable state demands it; not before.
- **Pydantic AI** — https://ai.pydantic.dev/ — FastAPI-style DX for agents; first-class MCP and structured output. Best fit for Python-heavy stacks.
- **Model Context Protocol (MCP)** — https://modelcontextprotocol.io/ — Tool-calling standard as of 2026. Read the spec, not blog summaries.
- **Chip Huyen — *AI Engineering* (O'Reilly, 2025)** — https://www.oreilly.com/library/view/ai-engineering/9781098166298/ — Eval, RAG, deployment, cost — the systems-engineer view of LLM apps.
- **Hamel Husain on evals** — https://hamel.dev/ — "Your AI Product Needs Evals" is required reading.

### Distributed Systems

- **MIT 6.5840 (formerly 6.824)** — https://pdos.csail.mit.edu/6.824/ — The gold standard. Raft / Spinnaker / CRAQ labs in Go.
- **Designing Data-Intensive Applications, 2nd ed. (Kleppmann & Riccomini, 2026)** — https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/ — Updated for cloud, streaming, modern storage. The book.
- **Jepsen analyses** — https://jepsen.io/analyses — Empirical consistency teardowns; how real systems fail in real ways.
- **aphyr/distsys-class** — https://github.com/aphyr/distsys-class — Practitioner counterpart to 6.5840.
- **Marc Brooker's blog** — https://brooker.co.za/blog/ — AWS principal engineer; current thinking on consensus, durability, formal methods in production.
- **theanalyst/awesome-distributed-systems** — https://github.com/theanalyst/awesome-distributed-systems — Maintained curation of papers, talks, tools.
- **jepsen-io/maelstrom** — https://github.com/jepsen-io/maelstrom — Workbench for writing toy Raft/CRDT impls and getting them checked.

### Event-Driven Architecture

- **microservices.io (Chris Richardson)** — https://microservices.io/patterns/ — Saga, outbox, event sourcing, CQRS. Actively maintained.
- **Oskar Dudycz — Event-Driven.io** — https://event-driven.io/ — Most prolific current voice on event sourcing pragmatics; "should you build it" essays are unusually honest.
- **Confluent — *Kafka: The Definitive Guide*, 2nd ed.** — https://www.confluent.io/resources/kafka-the-definitive-guide/ — Updated for KRaft (no ZooKeeper).
- **Microsoft Azure Architecture Center — patterns** — https://learn.microsoft.com/azure/architecture/patterns/ — Vendor-neutral writeups of CQRS, event sourcing, outbox, saga with tradeoffs.
- **NATS JetStream docs** — https://docs.nats.io/nats-concepts/jetstream — Lightweight Kafka alternative.
- **Debezium docs** — https://debezium.io/documentation/ — CDC + outbox-pattern reference implementation.
- **Martin Fowler — Event Sourcing / CQRS** — https://martinfowler.com/eaaDev/EventSourcing.html — Foundational vocabulary; pair with Dudycz for 2026 reality.

### Docker / Containers

- **Docker official docs — Build with Docker** — https://docs.docker.com/build/ — BuildKit, cache mounts, multi-stage, bake. Source of truth.
- **Nigel Poulton — *Docker Deep Dive*, 2025 ed.** — https://leanpub.com/dockerdeepdive — Updated yearly. Current edition adds Build Cloud, buildx, Model Runner.
- **Google distroless** — https://github.com/GoogleContainerTools/distroless — Canonical minimal runtime images; `:debug` variants for incident response.
- **Chainguard Images** — https://images.chainguard.dev/ — The 2025-26 distroless successor with continuous CVE patching.
- **wagoodman/dive** — https://github.com/wagoodman/dive — Layer-by-layer image inspection; teaches what your Dockerfile actually produces.
- **Docker Compose v2 docs** — https://docs.docker.com/compose/ — Compose v2 (Go rewrite) is the current one.

### Backend Systems Thinking

- **donnemartin/system-design-primer** — https://github.com/donnemartin/system-design-primer — Shared vocabulary for system design.
- **Google SRE Books (free)** — https://sre.google/books/ — *SRE*, *Workbook*, *Building Secure & Reliable Systems*. Canonical reliability/on-call/capacity-planning text.
- ***Software Engineering at Google* (Winters/Manshreck/Wright)** — https://abseil.io/resources/swe-book — Code-as-org-asset; Hyrum's Law; staff-IC mindset at scale.
- **Tanya Reilly — *The Staff Engineer's Path*** — https://www.oreilly.com/library/view/the-staff-engineers/9781098118723/ — The book on staff-level technical leadership.
- **Will Larson — *An Elegant Puzzle* + StaffEng.com** — https://staffeng.com/ — Career/scope/scale patterns.
- **The Pragmatic Engineer (Gergely Orosz)** — https://newsletter.pragmaticengineer.com/ — Current Big-Tech engineering practice.
- **High Scalability** — http://highscalability.com/ — Architecture deep-dives on real systems (Discord, Figma, Notion).
- **Marc Brooker + Cindy Sridharan blogs** — https://brooker.co.za/blog/, https://copyconstruct.medium.com/ — Distributed-systems reliability and observability thinking.

---

## Stale list (explicitly avoid)

- Pre-2024 LangChain monolith tutorials — superseded by Anthropic "Building Effective Agents" + LangGraph + Pydantic AI.
- Designing Data-Intensive Applications, 1st ed. (2017) — noticeably dated on cloud and streaming. Use 2nd ed.
- "Microservices Patterns" book (Richardson, 2018) — use the actively-maintained microservices.io site + Dudycz.
- Burns, "Designing Distributed Systems" (2018) — use Brooker + 6.5840 + Jepsen.
- Alpine-as-default Dockerfiles — distroless / Chainguard are the current default.
- Older Coursera "Cloud Computing Specialization" / Udemy distsys — replaced by 6.5840 + DDIA 2nd ed.
- "Use Paxos" content from before ~2020 — Raft + practical-Paxos variants are the current teaching path.
- "Event-source everything" content — the field has cooled. Outbox-first; sagas only for true cross-service workflows.

---

## Cross-cutting shifts to encode (2024–2026)

- **Agents:** consensus has moved from "use a framework" to "use simple, composable LLM-call patterns; reach for LangGraph/Pydantic AI when you need durable state." MCP is now the tool-calling standard — teach it at the same level as HTTP, not as an optional extra.
- **Distributed systems:** less "implement Paxos," more "understand replication / consistency / failure modes well enough to read a Jepsen report." Formal methods (TLA+, P) are entering practitioner mainstream via Brooker/AWS.
- **Event-driven:** outbox-first; sagas only for true cross-service workflows; full event sourcing only for audit/finance domains.
- **Containers:** distroless/Chainguard have displaced Alpine-as-default; BuildKit features (cache mounts, secrets, bake) are no longer optional.
- **Backend thinking:** the staff-engineer vocabulary (scope, leverage, glue work) has become standard; system design is increasingly *operational* (capacity, on-call, blast radius) rather than purely architectural.

---

## Refreshing this file

When `freshness_check` exceeds ~3 months on a session, the skill should:

1. Spawn a research subagent to verify each domain's allowlist is still load-bearing.
2. Surface any new sources that have entered the conversation (high signal: new books, talks at major conferences, projects with rapid star growth).
3. Update this file and bump the date.

Prefer fewer, higher-quality sources over comprehensive lists. When in doubt, cut.
