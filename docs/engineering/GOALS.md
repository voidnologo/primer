# Primer — Engineering Goals & North Star

> Read this at the start of every working session (`/session-start`). It is the anti-drift anchor: every change should serve one of these goals and violate none of the non-negotiables. If a proposed change doesn't, stop and reconsider.

## What primer is

A personal, Primer-style learning system (after the Young Lady's Illustrated Primer in Neal Stephenson's *The Diamond Age*): an adaptive tutor that runs interactive lessons calibrated to a persistent, evidence-backed learner profile, and captures each session as a durable artifact.

**Scope, stated so it stops being re-litigated:** primer is general-purpose. It was prompted by one maintainer's need to stay current in a fast-moving technical field, and that origin is honest, but it is not the boundary. The target is a learner who wants to be *educated* rather than *schooled* — any subject, over years, driven by curiosity rather than by a syllabus or a resume gap. Geology, orbital mechanics, a language, game design, distributed systems. A change that only makes sense for a software-engineering learner is out of scope unless it generalizes.

**Architecture is class/instance:**
- **Public core ("the class")** — this repo. The engine: skill, protocols, templates, examples. Sharable, community-improvable. Holds **zero** personal data.
- **Private instance** — each user's own private data repo: profile, depth markers, calibration log, lessons. Synced across their machines via git. Spawned from the core by `init`.

## Goals (what every change should serve)

1. **A genuinely personal trainer.** Lessons calibrated to *this* learner — depth, vocabulary, register — not a generic curriculum. The profile is the instrument; keep it sharp and honest.
2. **A real feedback cycle.** The system learns the learner over time: intake bootstraps, every lesson adds evidence, recalibration corrects drift. The profile should get *more* true with use, not staler.
3. **Low-friction onboarding for a stranger.** A new user reaches a useful first lesson via a structured intake, not a blank profile they have to hand-author.
4. **Sharable without leaking.** The core is public and useful to others; personal data never touches it.
5. **Cultivate better learning, not just deliver content.** primer should gradually make the learner *better at learning* — building good habits (spaced retrieval, active recall, metacognition) over time, not just answering well in the moment. The system owns the metacognitive scaffolding (what to review, when, how deeply); it models and gently grows good practice rather than assuming the learner already has it or nagging them into it. (Matuschak: the medium, not the learner, must own the metacognitive work.)

## Non-negotiables (a change that breaks one of these is wrong)

- **Currency.** Knowledge must be current. The canon is a *vetted floor*, never a ceiling; every lesson runs a source-discovery pass; the stale-list and stale-criteria are the guardrail. Never freeze knowledge at list-authoring time.
- **Privacy.** All personal data — profile *and* lessons — lives only in the private instance repo and may be rich. The public core holds none. Publishing a lesson is a deliberate, separate derivation step (planned) that sanitizes at that point; lessons are not shareable-by-default. The skill never auto-reads a work codebase.
- **Productive struggle over fluent answers.** The learner reasons before the next explanation lands — on unfamiliar material that means presenting enough to reason from and then asking them to apply or extend it, not withholding until they guess (D-0032). The "LLM Fallacy" (fluent prose that feels like learning but isn't) is the enemy. **What adapts is the delivery, never the demand** — see the register non-negotiable below. A lesson is not made easier because the learner found it hard.
- **No sycophancy.** Hold correct positions under pushback. No motivational fluff. This never flexes, for any learner, at any register setting, and it is what the sycophancy eval tests.
- **Register adapts; rigor does not.** Senior-peer is the *default* voice, not a requirement. How a lesson sounds — directness, pushback, warmth, whether an unfamiliar topic opens with a worked example or a derivation — is a per-learner dimension that intake seeds and the feedback cycle sharpens with use, carrying confidence and evidence exactly as depth markers do. What may **not** move is how much the learner has to decide before help arrives. Vary how much work the Primer does; hold the learner's decision point fixed. (D-0031.)
- **Honesty about confidence.** Depth markers carry confidence + evidence. The system distinguishes what it *knows* about the learner from what it *assumed*. No certain-looking guesses.
- **Stable vs. volatile separation.** Stable traits and volatile state live apart, so churn doesn't corrupt traits and traits get deliberately revisited.
- **Self-contained.** primer delivers its full core loop — lessons, spaced review, the learner model — with nothing but the skill and the user's own data repo. No external tool or service is ever a *requirement*. Integrations (e.g., exporting retrieval prompts to an SRS app) are optional conveniences, never load-bearing.

## Anti-drift checklist

Before adding anything, ask:
- Which goal does this serve? Which non-negotiable could it violate?
- Is this engine (core) or data (instance)? Put it in the right place.
- Does it add currency risk (a closed list, a stale default)?
- Does it move personal data toward the public core?
- Is it scope the user asked for, or feature creep? (Default: don't add unrequested features.)
