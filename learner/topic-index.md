# Topic Index

The map of what's been covered, what's in progress, and what's next-suggested. The Primer reads this at session start to choose suggestions and to avoid re-covering ground.

Status legend: `[unexplored]` `[in-progress]` `[covered]` `[mastered]`

---

## Depth markers (confidence + evidence)

One row per top-level domain. Calibrates how aggressively the Primer fades introductory material. `confidence` reflects how much is *demonstrated* vs *self-reported* — a marker built only from self-report or a single intake probe stays `low` until a lesson confirms it. See `primer/feedback-protocol.md`.

| Domain | Updated | Depth | Confidence | Evidence |
|---|---|---|---|---|
| ai-agentic | 2026-05-09 | Comfortable consuming LLM APIs from app code; experimenting with prompt engineering; not yet shipped a production agent or formal eval harness; fuzzy on the 2024–26 framework landscape (LangGraph, Pydantic AI, MCP). | med | Reference lesson `agent-patterns-vs-frameworks` (2026-05-09); rest self-reported. |
| distributed-systems | 2026-05-09 | Comfortable with Postgres replication and queue-based async; CAP at conceptual level; no production consensus-protocol experience; hasn't read Jepsen reports closely. | low | Self-reported only — no lesson yet. Candidate for a probe. |
| event-driven-architecture | 2026-05-09 | Solid on the dual-write primitive, outbox mechanics (atomicity invariants, frozen-JSONB payloads, partial-index optimization), polling-vs-CDC tradeoff with the inflection point, and pattern boundaries (saga / CQRS / event-sourcing as successors). Implementation-ready for stage 1 of the realtime-feeds migration. Hasn't operated Kafka/NATS in production. | high (outbox) / low (broker + ops) | Lesson `outbox-pattern-and-why-it-comes-first` (2026-05-09, 75m) — demonstrated, derived invariants under probing. |
| docker | 2026-05-09 | **Really light — explicit learning gap.** Can read a Dockerfile and run Compose; needs depth on multi-stage builds, BuildKit cache mounts, distroless/Chainguard, image internals. Deploys via ECS, no Kubernetes in prod. | low | Self-reported gap — no lesson yet. |
| backend-engineering | 2026-05-09 | 15+ yrs total, ~10 senior. Comfortable with day-2 ops, capacity, on-call at small-to-medium scale. Known gap: cannot currently pass a system-design-at-scale interview confidently. | med | Long real-world experience (self-reported); no lesson yet to confirm the staff-scope edge. |

## Open ZPD edges

The Primer's per-session snapshot of where the learner is currently being stretched. Volatile — updated each session.

- **Broker selection** — Kafka vs NATS-JetStream vs Redis Streams vs SQS for the realtime-feeds migration. Decision framework needed; weighted heavily by lag observability + durability.
- **Operational layer for event-driven systems** — consumer-lag SLOs (Kafka consumer-group lag, JetStream pending counts, SQS ApproximateAgeOfOldestMessage), alerting thresholds, lag dashboards.
- **CQRS read-model patterns** — sealed/ready markers, freshness stamps, read-your-writes redirection. Direct fix for the customer-visibility pain in the realtime-feeds scenario.
- **Saga patterns** (choreographed vs orchestrated) — relevant once feed-processing has multi-stage workflows with compensation logic.

---

## ai-agentic

Building LLM-powered systems, tool use, agent loops, evaluation.

- `[reference]` agent-patterns-vs-frameworks — the Anthropic taxonomy: workflows vs agents → see `lessons/ai-agentic/2026-05-09-agent-patterns-vs-frameworks.md`
- `[unexplored]` evals-as-the-real-product — what actually moves AI quality
- `[unexplored]` mcp-as-the-tool-calling-protocol — the 2026 standard
- `[unexplored]` building-a-stateful-agent-with-langgraph — when durable state demands it

## distributed-systems

Foundational + modern. Consensus, replication, time, failure modes.

- `[unexplored]` consensus-without-implementing-paxos — what to actually internalize
- `[unexplored]` replication-and-the-three-flavors-of-consistency — strong / eventual / causal
- `[unexplored]` time-clocks-and-why-they-lie — Lamport, vector clocks, hybrid
- `[unexplored]` reading-a-jepsen-report — the practitioner skill

## event-driven-architecture

Event-driven patterns, brokers, idempotency.

- `[covered]` outbox-pattern-and-why-it-comes-first → [lesson](../lessons/event-driven-architecture/2026-05-09-outbox-pattern-and-why-it-comes-first.md) *(2026-05-09, 75 min)*
- `[unexplored]` sagas-orchestrated-vs-choreographed — when to reach for either
- `[unexplored]` when-to-actually-event-source — the field has cooled on this
- `[unexplored]` kafka-vs-nats-vs-redis-streams — picking the broker ← **suggested next**

## docker

Modern container workflows.

- `[unexplored]` images-as-filesystems-and-why-it-matters — the mental model
- `[unexplored]` multi-stage-buildkit-and-cache-mounts — current best practice
- `[unexplored]` distroless-and-the-chainguard-shift — what replaced Alpine
- `[unexplored]` compose-v2-as-a-dev-loop — local development

## backend-engineering

Architecture, scalability, reliability, design heuristics; staff-IC scope.

- `[unexplored]` the-staff-engineer-shift — scope, leverage, glue work
- `[unexplored]` capacity-and-failure-budgets — operational thinking
- `[unexplored]` design-decisions-as-tradeoff-tables — the artifact of staff design
- `[unexplored]` on-call-as-a-design-input — how reliability shapes architecture

---

## Suggested next

The Primer updates this section after each session.

**After lesson 1 (outbox-pattern-and-why-it-comes-first), in priority order for the realtime-feeds migration:**

1. **`kafka-vs-nats-vs-redis-streams`** *(EDA, lesson 4)* — broker selection. The migration timeline pressures it; lag observability and durability are now load-bearing selection criteria per the operational layer surfaced in lesson 1.
2. **`sagas-orchestrated-vs-choreographed`** *(EDA, lesson 2)* — multi-stage workflows with compensation; layers on top of outbox. Becomes immediately relevant as feed-processing grows multi-stage.
3. **`when-to-actually-event-source`** *(EDA, lesson 3, optional)* — calibration against hype before encountering it in the wild. Honest answer is "rarely needed for ingest-enrich-expose." ~30 min when curiosity wins.

**Earlier (still active suggestions, lower priority for the migration):**

- `mcp-as-the-tool-calling-protocol` *(ai-agentic)* — natural follow-on from the seed lesson; the workflow patterns mostly assume tools, MCP is how tools attach in 2026.
- `evals-as-the-real-product` *(ai-agentic)* — the move from "I built an agent" to "I know it's working."
