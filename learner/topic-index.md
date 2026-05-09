# Topic Index

The map of what's been covered, what's in progress, and what's next-suggested. The Primer reads this at session start to choose suggestions and to avoid re-covering ground.

Status legend: `[unexplored]` `[in-progress]` `[covered]` `[mastered]`

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

- `[unexplored]` outbox-pattern-and-why-it-comes-first — default before sagas
- `[unexplored]` sagas-orchestrated-vs-choreographed — when to reach for either
- `[unexplored]` when-to-actually-event-source — the field has cooled on this
- `[unexplored]` kafka-vs-nats-vs-redis-streams — picking the broker

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

The Primer updates this section after each session. Currently, after the seed `agent-patterns-vs-frameworks` reference lesson:

- `mcp-as-the-tool-calling-protocol` — natural follow-on; the patterns above mostly assume tools, MCP is how tools attach in 2026.
- `evals-as-the-real-product` — Evaluator-Optimizer is the entry point; move from "I built an agent" to "I know it's working."
