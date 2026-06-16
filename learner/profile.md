# Learner Profile — Stable Traits

> The Primer reads this file at session start. It holds **stable traits only** — things that change deliberately (at `recalibrate`) or when you edit, not every session. Volatile state lives elsewhere: depth markers and ZPD edges in `learner/topic-index.md` (with confidence + evidence), calibration misses in `learner/calibration-log.md`. See `primer/feedback-protocol.md` for the split.
>
> **Privacy:** this file lives in your *private* data repo. It can hold real context — real stack, real stakes, the things that make tailoring sharp. The public-safe constraint applies to *lessons* (shareable artifacts), never to this profile. (Until the class/instance split lands, this copy still sits in the public core, so it remains public-safe; enrich it with real context once it moves to the private repo — a deep `recalibrate` is the natural moment.)

**Last updated:** 2026-06-15 (restructured: stable/volatile split; depth markers moved to topic-index)

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

> **Depth markers moved.** Per-domain depth, confidence, and evidence now live in `learner/topic-index.md`. This file no longer carries them — they churned every session and dragged the stable traits with them.

## Current scenarios

Problem shapes the learner is actively working through. The Primer should reach for these when grounding lessons; they're generic enough for a public repo and concrete enough to anchor analogies.

- **Realtime from batch feeds.** Product consumes multiple external data feeds. Current implementation: cron-driven batch SQL queries that "sync and associate" the feed data into the application stores. The batch cadence produces timing gaps that are no longer acceptable. Goal: move to realtime / near-realtime event-driven processing of feed events. Active motivation for the EDA learning track — outbox, CDC, sagas, broker selection, idempotency.
- **Falcon → FastAPI migration in flight.** The team is migrating off Falcon onto FastAPI this year. Active context for backend modernization decisions — patterns for new code should anticipate FastAPI idioms (Pydantic models, dependency injection, async).

## Preferences

- **Register:** Senior peer — meetup-after-the-talk. No motivational fluff. No cheerleading. Disagree when correct.
- **Productive-struggle tolerance:** High. Wants to derive invariants, not be handed them. Probe-first is the right default; pushes back on framing, which is engagement, not resistance.
- **Correction style:** Direct. State the error and the reasoning; no hint-laddering, no softening. Offer a concrete test to settle it.
- **Narrative density:** Welcome — "senior engineer explaining at a meetup." Short stories with named characters and concrete numbers beat abstract frameworks.
- **Visuals:** Mermaid for artifacts, ASCII inline during the live conversation. Tables for tradeoffs.
- **Time budget per session:** 60–90 minutes typical. Lesson 1 ran ~75 min and felt right.
- **Sources to trust:** the canon's vetted floor (`primer/source-canon.md`) plus the per-lesson discovery pass — currency is non-negotiable.

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

> **Open ZPD edges moved** to `learner/topic-index.md` (volatile — they're the Primer's per-session snapshot of where you're being stretched, not a stable trait).
