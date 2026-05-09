# Learner Profile

> The Primer reads this file at session start. Keep it accurate. Edit freely. Public-safe — no employer names, no proprietary scenarios.

**Last updated:** 2026-05-09 (after lesson 1 — outbox-pattern-and-why-it-comes-first)

---

## Identity

- **GitHub:** voidnologo
- **Total backend experience:** 15+ years
- **Senior-level experience:** ~10 years
- **Languages:** Python (primary, daily), Elixir (Phoenix experience)
- **Self-taught:** yes

## Stack & current responsibilities

Public-safe abstraction of the kind of systems shipped:

- **Frameworks:** Django (most of career — primary), Flask (some), Falcon (current). **No FastAPI experience yet** — team is migrating off Falcon to FastAPI this year.
- **Data:** Postgres as primary store; Redis for cache/locks; queue-backed async work (SQS-like).
- **Architecture pattern in use:** Product consumes multiple external data feeds; current implementation is **cron-driven batch SQL sync jobs**. These produce timing gaps that are now the load-bearing problem to solve (see Current Scenarios).
- **Infra:** Docker (light familiarity — explicit learning area); AWS (ECS, Lambda).
- **Service contracts:** OpenAPI-driven; some spec-first design.
- **Day-2 concerns:** observability via metrics/logs/traces; on-call rotation; capacity planning at small-to-medium scale.

**Role:** Backend team technical lead. Responsible for modernizing and growing the team's web backend.

## Depth markers

One line per top-level domain, with date. Calibrates how aggressively the Primer fades introductory material.

| Domain | Date | Current depth |
|---|---|---|
| ai-agentic | 2026-05-09 | Comfortable consuming LLM APIs from application code; experimenting with prompt engineering; not yet shipped a production agent or formal eval harness; fuzzy on the 2024–26 framework landscape (LangGraph, Pydantic AI, MCP). |
| distributed-systems | 2026-05-09 | Comfortable with Postgres replication and queue-based async; CAP at conceptual level; no production consensus-protocol experience; hasn't read Jepsen reports closely. |
| event-driven-architecture | 2026-05-09 | Solid grasp of the dual-write primitive, outbox mechanics (atomicity invariants, frozen-JSONB payloads, partial-index optimization), polling-vs-CDC tradeoff with the inflection point, and pattern boundaries (saga / CQRS / event-sourcing as successors). Implementation-ready for stage 1 of the realtime-feeds migration. New edge: broker selection and the operational layer (consumer-lag SLOs, freshness stamps in read paths). Hasn't operated Kafka/NATS in production yet. |
| docker | 2026-05-09 | **Really light — explicit learning gap.** Comfortable enough to read a Dockerfile and run Compose, but needs depth on multi-stage builds, BuildKit cache mounts, distroless/Chainguard, image internals, and modern container best practices. Deploys via ECS, no Kubernetes in prod. |
| backend-engineering | 2026-05-09 | 15+ years total, ~10 years senior. Comfortable with day-2 ops, capacity, on-call at small-to-medium scale. **Goal: move from senior backend IC to staff-comfortable** — scope, leverage, glue work, RFC writing, cross-team influence. Specific known gap: cannot currently pass a system-design-at-scale interview confidently. |

## Current scenarios

Problem shapes the learner is actively working through. The Primer should reach for these when grounding lessons; they're generic enough for a public repo and concrete enough to anchor analogies.

- **Realtime from batch feeds.** Product consumes multiple external data feeds. Current implementation: cron-driven batch SQL queries that "sync and associate" the feed data into the application stores. The batch cadence produces timing gaps that are no longer acceptable. Goal: move to realtime / near-realtime event-driven processing of feed events. Active motivation for the EDA learning track — outbox, CDC, sagas, broker selection, idempotency.
- **Falcon → FastAPI migration in flight.** The team is migrating off Falcon onto FastAPI this year. Active context for backend modernization decisions — patterns for new code should anticipate FastAPI idioms (Pydantic models, dependency injection, async).

## Preferences

- **Register:** Senior peer — meetup-after-the-talk. No motivational fluff. No cheerleading. Disagree when correct.
- **Narrative density:** Welcome — "senior engineer explaining at a meetup." Short stories with named characters and concrete numbers beat abstract frameworks.
- **Visuals:** Mermaid for artifacts, ASCII inline during the live conversation. Tables for tradeoffs.
- **Time budget per session:** 60–90 minutes typical. Lesson 1 ran ~75 min and felt right.
- **Sources to trust:** the canon (`primer/source-canon.md`).

## Anti-preferences

Things that don't land — the Primer should avoid them:

- Motivational closers ("Hopefully this was helpful!").
- Over-explaining basics ("Let me first define what a queue is...") — fade fast.
- Pre-2024 LangChain content; pre-2nd-edition DDIA; "event-source everything" content.
- Generic curriculum drift (lesson reads like a Wikipedia article).
- Claiming experience the learner doesn't have. The profile is the source of truth — don't infer FastAPI fluency from "Python web backend" etc.
- **When entering a new technical domain (especially one where the learner has light familiarity in adjacent areas), lead with a brief vocabulary calibration before any conceptual probe.** The "senior depth in adjacent areas may transfer" assumption is unsafe — surfaced when "outbox" was used several times in lesson 1 before being defined; learner had to flag the calibration miss. *Glossary the first 4–8 terms before the first probe lands. Always.*

## Active goals

1. **Modernize the team's backend with current best practices.** Includes the Falcon → FastAPI migration; raising the team's container hygiene; shifting from cron-batch syncs to realtime event-driven data processing.
2. **Grow from senior backend IC to staff-comfortable.** Scope, leverage, glue work; reading Reilly + Larson. Specific milestone: confident in system-design-at-scale conversations and interviews.
3. **Build production fluency in event-driven architecture** — specifically, replacing batch-SQL-sync cron jobs with realtime event-driven data processing.
4. **Build production fluency in agentic workflows** — area where shipping, not just consuming.

## Open ZPD edges

The Primer's snapshot of where the learner is currently being stretched. Updated each session.

- **Broker selection** — Kafka vs NATS-JetStream vs Redis Streams vs SQS for the realtime-feeds migration. Decision framework needed; weighted heavily by lag observability + durability.
- **Operational layer for event-driven systems** — consumer-lag SLOs (Kafka consumer-group lag, JetStream pending counts, SQS ApproximateAgeOfOldestMessage), alerting thresholds, lag dashboards.
- **CQRS read-model patterns** — sealed/ready markers, freshness stamps, read-your-writes redirection. Direct fix for the customer-visibility pain in the realtime-feeds scenario.
- **Saga patterns** (choreographed vs orchestrated) — relevant once feed-processing has multi-stage workflows with compensation logic.
