# Open Questions

Threads pulled-on during sessions and set down for later. The Primer surfaces relevant entries when a new lesson naturally connects.

Format: `<date> | <domain> | <one-line question or thread, with enough hook to revisit>`

---

- 2026-05-09 | event-driven-architecture | Broker selection: Kafka vs NATS-JetStream vs Redis Streams vs SQS for realtime-feeds — needs decision framework weighted by lag observability and durability. Lesson 4.
- 2026-05-09 | event-driven-architecture | CQRS read-model patterns: sealed/ready markers, freshness stamps, read-your-writes redirection — the actual fix for customer-visibility staleness. Lesson 3.
- 2026-05-09 | event-driven-architecture | Saga patterns (orchestrated vs choreographed) — when feed processing grows multi-stage with compensation logic. Lesson 2.
- 2026-05-09 | event-driven-architecture | Event sourcing decision framework — when audit/replay is genuinely first-order vs hype. Lesson 3.
- 2026-05-09 | event-driven-architecture | Migration sequencing for realtime-feeds shift: per-stage SLOs, deployment ordering, rollback strategy across the 6-stage plan in lesson 1.
- 2026-05-09 | event-driven-architecture | The "lead with vocabulary in new domains" meta-lesson — already encoded as a profile anti-preference; revisit if it surfaces again.
