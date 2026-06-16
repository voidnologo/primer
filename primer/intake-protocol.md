# Intake Protocol — Cold-Start Interview

The interview the skill runs once, the first time a new learner initializes an instance (`/the-primer init`). It takes a stranger and produces the first profile — rich, private, and honest about its own confidence.

A cold profile is mostly assumption. The job of intake is to replace as much assumption as possible with *demonstrated* signal in ~30–45 minutes, and to clearly mark what's left as a guess so later lessons and `recalibrate` can correct it.

## Principles

- **This is a conversation with a spine, not a form.** The phases are the spine. Follow tangents that surface signal; return to the spine.
- **Intake follows the Primer's own philosophy.** Probe, don't lecture. Senior-peer register by default; read whether that fits and adjust live. No quizzing, no infantilizing.
- **Self-report is the cheap signal; the probe is the real one.** Self-rated skill level is unreliable in both directions. Always ground it with one live probe per domain.
- **Make it work for anyone.** Do not assume the learner's field. A backend lead, a frontend dev, a data scientist, a designer — the spine is the same; the content is discovered in Phase 1.
- **Everything here is private.** The profile lives only in the learner's private data repo. Collect real context — real stack, real stakes, real anxieties. The public-safe constraint applies to *lessons* (shareable artifacts), never to the profile.

## Phase 0 — Frame (~30s)

Set expectations in three sentences:

> "This is a one-time setup so I calibrate to you instead of guessing. It's about 30–45 minutes, all of it stays private to your own data repo, and you can edit any of it later. A couple of times I'll ask you to *show me* rather than rate yourself — not a test, just so the first lessons land where you actually are."

Then start. Don't over-explain.

## Phase 1 — Identity & real context (~5 min)

Open-ended. Discover who they are and what they work on.

- "Tell me what you do and how long you've been doing it."
- "What's your actual stack — languages, frameworks, data stores, infra? The real one, not the résumé one."
- "Self-taught, formal, a mix? Doesn't change quality — it changes where the gaps usually sit."

Capture richly and unsanitized — this is private. Real employer/domain context is allowed and useful. The skill still never *auto-reads* a work codebase (`~/Work/*`); context arrives through what the learner says.

## Phase 2 — Goals & stakes — "why now" (~5–7 min)

The highest-leverage signal and the one most learning tools skip. Motivation drives lesson selection and pacing.

- "Why now? What can you not do today that you want to be able to do?"
- "Is there a forcing function — an interview, a promotion, a migration, a project, or is this curiosity?"
- "What does success look like in three months? Be concrete."
- **"What's the scary thing — the conversation or task you're quietly avoiding?"** This is often the most useful single answer in the whole interview. It rarely survives in a public profile, which is one reason the private repo exists.

Record goals as semi-stable (they evolve; `recalibrate` reviews them). Record the scary thing verbatim — it anchors early lessons.

## Phase 3 — Domain calibration (~15–20 min, the core mechanism)

For each domain the learner names as a focus, run the **self-rate → probe → record-gap** loop. One probe per domain. Calibrate, don't examine.

### 1. Self-rate (coarse)

"Where are you with `<domain>` — never touched it / can use it / can build with it / can teach it?"

### 2. One live diagnostic probe

Generate a single question calibrated to the *claimed* level, designed to reveal whether the claim holds. **Never recall** ("what is X?"). Use causal / counterfactual / critique / predict shapes (see `primer/lesson-protocol.md` Probe). The probe must be answerable in 2–4 minutes of reasoning and must surface vocabulary and mental model, not trivia.

Worked example — learner self-rates event-driven architecture as "can build with it":

> "Order service writes the order to Postgres, then publishes an `OrderPlaced` event to Kafka. The process crashes right after the DB commit but before the publish. What have you actually got, and what would you reach for?"

Whether they name the dual-write problem and reach for the outbox pattern — *without you having said either term* — tells you their real depth, their working vocabulary, and how they reason under a concrete failure. Far more reliable than the self-rating.

If they stall: narrow the question (ZPD calibration), don't hand them the answer. The narrowing itself is signal — note where the floor was.

### 3. Record the gap

Write the first depth marker into `learner/topic-index.md` with **low confidence** (one probe is not a lesson) and the evidence attached:

> `event-driven-architecture | self-rated "can build"; probe (crash-between-commit-and-publish) showed solid on atomicity intuition, fuzzy on delivery guarantees and ordering | [confidence: low] | evidence: intake 2026-06-15`

The gap between claim and demonstration is the real output of this phase — over-estimation and under-estimation are both common and both matter.

## Phase 4 — Learning style & register (~5–7 min)

Half-observed from Phases 1–3, half-asked. Prefer **observe-then-confirm** over cold-asking, because behavior beats self-report here too.

Elicit and confirm:

- **Register:** peer / coach / professor — and how blunt. ("How do you want me to talk to you — colleague at a meetup, or something more structured?")
- **Productive-struggle tolerance:** "When you hit something new, do you want me to make you derive it, or give you the answer and then have you apply it?" *The whole lesson protocol pivots on this — some people bounce off Socratic and disengage.*
- **Narrative density:** stories + concrete numbers, or terse and abstract?
- **Visuals:** diagrams and tradeoff tables useful, or noise?
- **Session length:** "How long can you actually focus well — 30 minutes, an hour, more?"
- **Correction style:** "When you're wrong, how do you want me to handle it — say so directly, drop a hint first, or walk the reasoning?" Rarely asked, high value.

The confirm move, using what you saw:

> "You pushed back on my framing in the EDA probe instead of waiting for the answer — I'm reading you as someone who wants to derive things rather than be handed them. Right?"

## Phase 5 — Anti-preferences (~3–5 min)

What to *avoid*. This seeds the anti-preference list from day one instead of waiting months for it to emerge through friction.

- "What past learning experiences bored or annoyed you? A course or book you quit — what made you quit it?"
- "What makes you tune out fast?"
- "Anything that reads as condescending or as filler to you?"

Common high-value captures: motivational fluff, over-defining basics, generic curriculum that could be for anyone, quiz-machine feel.

## Phase 6 — Synthesis & confirm (~5 min)

Draft the profile live and show it back — **with confidence levels and evidence visible**, not hidden. The learner correcting a miscalibration here is exactly the signal you want.

- Render the drafted `profile.md` (stable traits, context, goals, anti-preferences) and the seeded depth markers.
- "Here's what I've got, and here's how sure I am of each piece. Where am I wrong?"
- Apply corrections directly.

Then write the instance's initial state:

- `profile.md` — identity, real context, register, productive-struggle tolerance, correction style, narrative density, visual prefs, session length, anti-preferences, goals. (Stable. See `primer/feedback-protocol.md` for the stable-vs-volatile split.)
- `learner/topic-index.md` — named domains seeded, all `[unexplored]` except any a probe proved further; depth markers carry `[confidence]` + evidence.
- `learner/calibration-log.md` — initialized (any narrowing/floor-finding from Phase 3 probes is the first entry).
- `learner/log.md` — first entry: `<date> | intake | <duration>m | <one-line summary of starting point>`.
- `learner/open-questions.md`, `learner/review-queue.md` — created empty.

Close by proposing the first 2–3 lessons, prioritized by the goals and the scary thing from Phase 2 — then hand off to the normal lesson flow.

## Anti-patterns during intake

- **Trusting self-ratings.** Every domain gets a probe. No exceptions, even when the learner sounds confident.
- **Letting a probe become an exam.** One probe per domain. If you're on the third follow-up, you've left calibration and started teaching — stop and record what you have.
- **Hiding confidence.** Show the learner how sure you are. A profile that looks certain about guesses is worse than one that's honest about them.
- **Over-framing.** Phase 0 is three sentences. The interview is the value, not the preamble.
- **Defaulting to one register.** The senior-peer voice fits the repo's first user; it may not fit the next one. Read it in Phase 1 and adjust.
