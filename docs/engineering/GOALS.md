# Primer — Engineering Goals & North Star

> Read this at the start of every working session (`/session-start`). It is the anti-drift anchor: every change should serve one of these goals and violate none of the non-negotiables. If a proposed change doesn't, stop and reconsider.

## What primer is

A personal, Primer-style learning system (after the Young Lady's Illustrated Primer in Neal Stephenson's *The Diamond Age*): an adaptive tutor that runs interactive lessons calibrated to a persistent, evidence-backed learner profile, and captures each session as a durable artifact.

**Architecture is class/instance:**
- **Public core ("the class")** — this repo. The engine: skill, protocols, templates, examples. Sharable, community-improvable. Holds **zero** personal data.
- **Private instance** — each user's own private data repo: profile, depth markers, calibration log, lessons. Synced across their machines via git. Spawned from the core by `init`.

## Goals (what every change should serve)

1. **A genuinely personal trainer.** Lessons calibrated to *this* learner — depth, vocabulary, register, struggle tolerance — not a generic curriculum. The profile is the instrument; keep it sharp and honest.
2. **A real feedback cycle.** The system learns the learner over time: intake bootstraps, every lesson adds evidence, recalibration corrects drift. The profile should get *more* true with use, not staler.
3. **Low-friction onboarding for a stranger.** A new user reaches a useful first lesson via a structured intake, not a blank profile they have to hand-author.
4. **Sharable without leaking.** The core is public and useful to others; personal data never touches it.

## Non-negotiables (a change that breaks one of these is wrong)

- **Currency.** Knowledge must be current. The canon is a *vetted floor*, never a ceiling; every lesson runs a source-discovery pass; the stale-list and stale-criteria are the guardrail. Never freeze knowledge at list-authoring time.
- **Privacy.** Personal/profile data lives only in the private instance repo. The public core holds none. Lessons (shareable) are sanitized; the profile (private) may be rich. The skill never auto-reads a work codebase.
- **Productive struggle over fluent answers.** Probe before answering conceptual questions. The "LLM Fallacy" (fluent prose that feels like learning but isn't) is the enemy.
- **Senior-peer register, no sycophancy.** Hold correct positions under pushback. No motivational fluff. (Default register; intake can recalibrate per learner.)
- **Honesty about confidence.** Depth markers carry confidence + evidence. The system distinguishes what it *knows* about the learner from what it *assumed*. No certain-looking guesses.
- **Stable vs. volatile separation.** Stable traits and volatile state live apart, so churn doesn't corrupt traits and traits get deliberately revisited.

## Anti-drift checklist

Before adding anything, ask:
- Which goal does this serve? Which non-negotiable could it violate?
- Is this engine (core) or data (instance)? Put it in the right place.
- Does it add currency risk (a closed list, a stale default)?
- Does it move personal data toward the public core?
- Is it scope the user asked for, or feature creep? (Default: don't add unrequested features.)
