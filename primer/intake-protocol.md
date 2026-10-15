# Intake Protocol — Cold-Start Interview

The interview the skill runs once, the first time a new learner initializes an instance (`/primer init`). It takes a stranger and produces the first profile — rich, private, and honest about its own confidence.

A cold profile is mostly assumption. The job of intake is to replace as much assumption as possible with *demonstrated* signal in ~30–45 minutes, and to clearly mark what's left as a guess so later lessons and `recalibrate` can correct it.

## Principles

- **This is a conversation with a spine, not a form.** The phases are the spine. Follow tangents that surface signal; return to the spine.
- **Intake follows the Primer's own philosophy.** Intake is the place where derivation-first questions have a job: the Phase 3 probes exist to gauge level, so they may ask before showing (D-0032). Everywhere else, don't lecture and don't interrogate. Senior-peer register by default; read whether that fits and adjust live. No quizzing, no infantilizing.
- **Self-report is the cheap signal; the probe is the real one.** Self-rated skill level is unreliable in both directions. Always ground it with one live probe per domain.
- **Discover, don't assume — broad ability *and* goal.** Do not presuppose the learner's field, their target, or even which domains matter. The spine is the same for a backend lead, a frontend dev wanting MCP, or someone learning their first new language in a decade; the content is *discovered*. Two things get discovered together: how broadly capable they already are (so transferable skill is found, not re-taught), and what they're actually trying to do (so the calibration starts in the right place). The goal decomposes into the skill map; the broad-ability scan says which parts of that map are new.
- **Everything here is private.** The profile *and* the lessons it shapes live only in the learner's private data repo. Collect real context — real stack, real stakes, real anxieties. Nothing here faces a public-safe constraint; publishing a lesson is a separate, deliberate derivation step (planned).

## Phase 0 — Frame (~30s)

Set expectations in three sentences:

> "This is a one-time setup so I calibrate to you instead of guessing. It's about 30–45 minutes, all of it stays private to your own data repo, and you can edit any of it later. A couple of times I'll ask you to *show me* rather than rate yourself — not a test, just so the first lessons land where you actually are."

Then start. Don't over-explain.

## Phase 1 — Broad ability discovery (~5–7 min)

Map the *whole* learner, not just the target. The point is to find what already transfers, so the lesson plan teaches what's new and skips what isn't.

- "Tell me what you do and how long you've been doing it."
- "What have you actually built? What are you good at — the things that feel easy now?"
- "What's your real toolkit — languages, frameworks, paradigms, domains you've worked in?"
- "When you've picked up something new before, how did it go and how did you do it?" (Surfaces learning style early and ramp speed.)
- "Self-taught, formal, a mix? Doesn't change quality — it changes where the gaps usually sit."

Capture richly and unsanitized — this is private. Real employer/domain context is allowed and useful. The skill still never *auto-reads* a work codebase (`~/Work/*`); context arrives through what the learner says.

The breadth matters because most goals lean on adjacent skill. Someone learning a new language already knows programming — calibrate against their *existing* paradigm fluency, not from zero. Someone learning MCP already builds software — the question is which adjacent pieces (HTTP, tool-calling, JSON-RPC, client/server models) they hold. The broad scan is what makes the goal decomposition in Phase 3 honest.

## Phase 2 — Goals & stakes — "why now" (~5–7 min)

The highest-leverage signal and the one most learning tools skip. Motivation drives lesson selection and pacing.

- "Why now? What can you not do today that you want to be able to do?"
- "Is there a forcing function — an interview, a promotion, a migration, a project, or is this curiosity?"
- "What does success look like in three months? Be concrete."
- **"What's the scary thing — the conversation or task you're quietly avoiding?"** This is often the most useful single answer in the whole interview. It rarely survives in a public profile, which is one reason the private repo exists.

Record goals as semi-stable (they evolve; `recalibrate` reviews them). Record the scary thing verbatim — it anchors early lessons.

## Phase 3 — Goal decomposition & calibration (~15–20 min, the core mechanism)

This is where broad ability and goal meet. Don't ask the learner to enumerate domains — most can't, and a learner often doesn't know what their goal depends on. *Derive* the map from the goal, cross it against Phase 1, then probe only the load-bearing unknowns.

### 0. Decompose the goal into a skill map

Take the Phase 2 goal and break it into the sub-skills/domains it actually requires. Mark each against the broad-ability scan: **transfers** (already held — don't re-teach), **adjacent** (partial, worth a probe), or **new** (the real learning surface). Show the learner the map and let them correct it — they'll know if you've mis-scoped.

Worked examples:

- **"Get good at system design."** Decomposes into: data modeling, caching, queues/async, replication/consistency, capacity/failure thinking, the communication craft (tradeoff tables, RFCs). A backend lead transfers most primitives; the new surface is *consistency at scale* and *the staff-level communication*. Probe there.
- **"Learn MCP and AI-assisted development."** Decomposes into: client/server model, JSON-RPC/transport, tool/resource definitions, LLM tool-calling loop, agent patterns, evals. A working dev transfers HTTP and client/server; *tool-calling semantics* and *evals* are usually new. Probe there.
- **"Learn a new programming language (say Rust)."** Decomposes into: syntax (cheap, self-serve), the language's *distinctive model* (ownership/borrowing), its ecosystem/tooling, idioms vs. their current paradigm. Someone fluent in Python transfers control flow and decomposition; the new surface is *ownership* and *thinking in the type system*. Probe there, not on syntax.

The decomposition is what turns "I want to learn X" into a calibrated starting point. Skipping it produces a generic curriculum — the failure mode to avoid.

### Then, for each load-bearing (adjacent / new) sub-skill, run the loop

`self-rate → probe → record-gap`. One probe per sub-skill. Calibrate, don't examine. Skip transfers entirely (note them as assumed-held, low cost to confirm later).

### 1. Self-rate (coarse)

"Where are you with `<sub-skill>` — never touched it / can use it / can build with it / can teach it?"

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

## Phase 4 — Register (~5–7 min)

Half-observed from Phases 1–3, half-asked. Prefer **observe-then-confirm** over cold-asking, because behavior beats self-report here too.

What comes out of this phase is a **starting point, and the learner should hear it described that way.** Register is learned: these answers go into the profile's *Register* table at `low` confidence with "intake, self-report" as the evidence, and lessons revise them (`primer/feedback-protocol.md`, *Register is learned*). Two findings are why it can't be a setting the learner simply picks: preference anticorrelates with learning (students prefer conditions that cost them ~0.4 SD), and learning styles remain unsupported, so a field shaped like one would encode a myth (D-0031). Say so briefly: "I'll start here and adjust as I see what actually works for you."

Elicit and confirm, one dimension at a time:

- **Voice:** peer / coach / professor, and how formal. ("How do you want me to talk to you — colleague at a meetup, or something more structured?")
- **Directness when you're wrong:** "When you're wrong, should I just say so, name it and then walk the reasoning, or drop a hint first?" Rarely asked, high value.
- **Pushback:** "If I think you're wrong and you disagree, do you want me to argue it out with you?" (The Primer holds a correct position under pushback regardless — this sets the tone of the argument, not whether it happens.)
- **Being wrong in front of the tutor:** "Some people like to be corrected immediately; some want a beat to catch it themselves first. Which are you?"
- **Presentation before the first question:** "When a topic is completely new to you, I'll show you something and then ask you to reason about it. How much do you want to see first — the bare rule, a worked example, or a worked example with the numbers?" *Don't offer "make me derive it" as an option for new material.* Whether to show first is decided by the depth marker, not here (`primer/lesson-protocol.md`, *Choosing the opening*); this only shapes what gets shown.
- **Narrative density:** stories + concrete numbers, or terse and abstract?
- **Visuals:** diagrams and tradeoff tables useful, or noise?
- **Session length:** "How long can you actually focus well — 30 minutes, an hour, more?" (A preference, not register; it goes under *Preferences*.)

The confirm move, using what you saw:

> "You pushed back on my framing in the EDA probe instead of waiting for the answer — I'm reading you as someone who wants me to argue with you rather than just explain. Right?"

Where an observation in Phases 1–3 agrees with what they say, the row can start at `low–med` with both pieces cited. Where it disagrees, record the self-report as the setting, note the observation in the evidence column, and keep it at `low`: the next few lessons settle it.

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

- `profile.md` — identity, real context, the *Register* table (each row with its confidence and evidence), preferences (session length, sources), anti-preferences, goals. (Stable. See `primer/feedback-protocol.md` for the stable-vs-volatile split, and *Register is learned* for how the table moves.)
- `learner/topic-index.md` — the goal's skill map seeded (transfers, adjacent, new), statuses `[unexplored]` except where a probe proved further or a skill transfers; depth markers carry `[confidence]` + evidence.
- `learner/calibration-log.md` — initialized (any narrowing/floor-finding from Phase 3 probes is the first entry).
- `learner/log.md` — first entry: `<date> | intake | <duration>m | <one-line summary of starting point>`.
- `learner/open-questions.md`, `learner/review-queue.md` — created empty.

Close by proposing the first 2–3 lessons, prioritized by the goals and the scary thing from Phase 2 — then hand off to the normal lesson flow.

## Anti-patterns during intake

- **Trusting self-ratings.** Every load-bearing (adjacent / new) sub-skill gets a probe. No exceptions, even when the learner sounds confident. Transfers may be assumed-held but get confirmed in the first lesson that touches them.
- **Skipping the decomposition.** Asking "what domains do you want?" instead of deriving the map from the goal. The learner often doesn't know what their goal depends on — that's the Primer's job.
- **Letting a probe become an exam.** One probe per domain. If you're on the third follow-up, you've left calibration and started teaching — stop and record what you have.
- **Hiding confidence.** Show the learner how sure you are. A profile that looks certain about guesses is worse than one that's honest about them.
- **Over-framing.** Phase 0 is three sentences. The interview is the value, not the preamble.
- **Defaulting to one register.** The senior-peer voice fits the repo's first user; it may not fit the next one. Read it in Phase 1 and adjust.
