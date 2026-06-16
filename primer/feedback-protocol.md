# Feedback Protocol — How the Primer Learns the Learner

The loop that keeps the profile true after intake. Intake produces a profile that is mostly assumption; this protocol turns lessons into evidence and periodically corrects the model rather than only appending to it.

The core failure of a naive loop is conflating things that change at different rates and only updating at one timescale. This protocol runs at three.

## Stable vs. volatile — the split that makes the loop work

Two kinds of fact live in the profile, and mixing them in one file means the volatile churn drags the stable traits along and the stable traits never get deliberately revisited.

- **Stable traits** → `profile.md`. Identity, real context, register, productive-struggle tolerance, correction style, narrative density, visual prefs, session length, anti-preferences, goals (semi-stable). Changes deliberately — at `recalibrate`, or when the learner edits.
- **Volatile state** → `learner/`. Depth markers (with confidence + evidence), `[status]` tags, ZPD edges → `topic-index.md`. Calibration misses → `calibration-log.md`. These churn every session.

Depth markers live in `topic-index.md`, **not** `profile.md`. Each marker carries `[confidence: low/med/high]` and the evidence that earned it (which session, what was demonstrated). Intake claims start `low`; each lesson that confirms raises confidence. This lets the Primer distinguish what it *knows* about the learner from what it *assumed*.

## Timescale 1 — within a lesson (silent)

The Diagnose step (`primer/lesson-protocol.md`) already adjusts depth live. Add: when a **calibration miss** happens, note it silently and carry it to session end. Never break flow to ask about it.

Miss types to watch for:

- too basic / too advanced
- vocabulary gap (used a term before establishing it)
- dead analogy (the framing didn't connect)
- pacing off (rushed or dragged)
- struggle-tolerance mismatch (learner bounced off a Socratic probe and wanted the answer)

## Timescale 2 — end of each lesson (signal capture)

Beyond the existing depth-marker and topic-index updates:

### Calibration-log entry

Append to `learner/calibration-log.md` any misses observed:

`<date> | <domain> | <miss-type> | <what happened> | <adjustment made / to make>`

This is the routine version of what currently happens by luck. The existing "lead with vocabulary in new domains" rule was a vocabulary-gap miss that got hand-promoted to a trait; this makes that capture systematic so patterns surface instead of being caught ad hoc.

### Confidence + evidence on depth markers

Update each touched marker in `topic-index.md`: adjust the depth description, set `[confidence]`, append the evidence. Strongest possible upgrade signal: **the learner correcting a Primer error** — that demonstrates mastery beyond passive recall, so it raises confidence more than a clean answer does.

### Silent micro-feedback (inferred, never asked)

The Primer does **not** ask "did the difficulty land?" — that crosses into the fluff the protocol elsewhere refuses. Instead it *infers* from the conversation and writes the signals:

| Signal class | Inferred from |
|---|---|
| **Calibration** | Did the learner anticipate points before they were made (too basic) or repeatedly ask for narrowing (too advanced)? |
| **Engagement** | Did they pull on threads and push back (engaged), or give short acknowledgments and stop asking (disengaging)? |
| **Mastery evidence** | Did they derive an invariant, correct an error, or only restate? |
| **Style confirmation** | Did the chosen register / correction style / narrative density fit, or did friction show? |

These feed the calibration-log and, when a pattern is clear, the anti-preferences. If a single lesson contradicts a stable trait, note it — don't rewrite the trait on one data point; that's what `recalibrate` is for.

## Timescale 3 — recalibration (two tiers)

The append-only loop accretes volatile state until it needs compacting and the model needs correcting. Two tiers, by the user's design.

### Minor recalibrate — auto, every 5 lessons

System-triggered (default N = 5; configurable). Lightweight, runs at the start of the 6th/11th/… lesson, takes ~2–3 minutes, shows a short diff and proceeds:

1. Scan `calibration-log.md` since the last recalibrate for **repeated** miss-types in the same domain → fold into the relevant depth marker or anti-preference.
2. Flip any `[status]` that the evidence clearly warrants (e.g., `[in-progress]` → `[covered]`).
3. Surface — don't resolve — any depth marker still at `[confidence: low]` that hasn't been touched in several lessons (a standing assumption worth a probe next time).
4. Show a 3–5 line "changed since last check" diff. Proceed into the lesson.

Minor recalibrate does **not** rewrite stable traits or goals.

### Deep recalibrate — user-invoked (`/primer recalibrate`)

On demand, a full meta-session (not a lesson):

1. **Mine `calibration-log.md` for patterns** across all domains → promote recurring misses to stable traits / anti-preferences. (This is how a one-off observation legitimately becomes a rule.)
2. **Detect drift:** Are the goals in `profile.md` still current? Should any domain flip to `[mastered]`? Are the ZPD edges stale?
3. **Confidence audit:** List low-confidence markers — assumptions never actually tested — as candidates to probe in upcoming lessons.
4. **Re-confirm stable traits** with the learner: has register / struggle tolerance / correction style changed? People change; the profile should be allowed to.
5. **Compact volatile churn:** collapse superseded depth-marker history; archive resolved open-questions.
6. **Flag stale canon:** surface `source-canon.md` floor entries that now fail the stale-criteria (ties into `primer/source-canon.md` refresh).
7. **Output a "what I changed and why" diff** and apply on confirmation.

The distinction that matters: the minor tier keeps volatile state honest cheaply and automatically; the deep tier is the only place stable traits and goals get rewritten, and it does so on accumulated evidence with the learner in the loop — never on a single session.

## What this protocol is defending against

- **Profile rot** — markers that were true at intake and silently went stale. Confidence + evidence + the confidence audit catch it.
- **Lucky-catch dependence** — useful observations (like the vocabulary-calibration rule) being noticed only when someone happens to. The calibration-log makes capture routine.
- **Append-only sprawl** — volatile state piling up until the profile is noise. The two recalibrate tiers compact it.
- **Over-fitting to one session** — rewriting a stable trait because of a single off day. Only deep recalibrate touches stable traits, and only on patterns.
