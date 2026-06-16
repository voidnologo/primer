---
name: learn-me-up
description: "Primer-style adaptive learning skill — runs interactive lessons calibrated to a persistent learner profile and captures each session as a durable markdown artifact"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
  - Task
  - AskUserQuestion
  - WebSearch
  - WebFetch
---

<objective>
The Young Lady's Illustrated Primer for one backend engineer.

Run a Primer-style learning session: read the persistent learner profile, calibrate to current depth, run the lesson protocol (Elicit → Probe → Diagnose → Deepen → Recap), and capture the session as a structured `LESSON.md` artifact.

Lessons feel like a senior staff engineer talking to a colleague. Productive struggle over fluent answers. Source-current, never stale. Stack-aware via the public-safe profile; never reads proprietary work code.
</objective>

<execution_context>
The `primer/*` files below are the **engine** — they ship with the public core and are loaded statically.

@$HOME/personal/learning/knowledge/primer/system-prompt.md
@$HOME/personal/learning/knowledge/primer/lesson-protocol.md
@$HOME/personal/learning/knowledge/primer/intake-protocol.md
@$HOME/personal/learning/knowledge/primer/feedback-protocol.md
@$HOME/personal/learning/knowledge/primer/lesson-template.md
@$HOME/personal/learning/knowledge/primer/source-canon.md
@$HOME/personal/learning/knowledge/primer/anti-patterns.md
@$HOME/personal/learning/knowledge/primer/visuals.md

Learner state is **instance data** — it lives in the learner's private data repo, not the core, and is read at runtime from the resolved data dir (see *Resolve the data dir* in `<process>`). It is **not** statically included here.
</execution_context>

<process>
## Resolve the data dir (every invocation, before routing)

Learner state lives in a private data repo whose path differs per machine. Resolve it first:

1. Read `~/.config/primer/config`. It contains `DATA_DIR=<absolute path>` — the root of the private data repo. State files live under `$DATA_DIR/learner/` (`profile.md`, `topic-index.md`, `calibration-log.md`, `log.md`, `review-queue.md`, `open-questions.md`); lesson artifacts under `$DATA_DIR/lessons/`. This mirrors the public core's own layout.
2. If the config is absent, the instance isn't initialized — route to `init` regardless of the argument (except `help`).
3. Dev fallback: if no config but a `learner/` dir exists at the core repo root, use the core repo root as `$DATA_DIR` (transitional / pre-split).

Then read `$DATA_DIR/learner/profile.md` and `$DATA_DIR/learner/topic-index.md` to calibrate before any lesson flow.

## The argument

The skill takes one argument. Route on it:

## `/primer init` — First-time setup (intake interview)

Run when no instance exists. Execute the intake interview in `primer/intake-protocol.md`: the 6-phase cold-start interview (frame → identity → goals & stakes → per-domain calibration with one live probe each → learning style → anti-preferences → synthesis). On completion, scaffold `$DATA_DIR` from `templates/learner/` and write the initial profile, seeded topic-index (with confidence + evidence), calibration-log, and first log entry. Close by proposing the first 2–3 lessons. If `~/.config/primer/config` doesn't exist yet, walk the learner through `tools/init-instance.sh` first.

## `/primer recalibrate` — Correct the model

Deep, user-invoked recalibration per `primer/feedback-protocol.md`: mine `calibration-log.md` for patterns, detect goal/depth drift, audit low-confidence markers, re-confirm stable traits, compact volatile churn, flag stale canon entries. Output a "what changed and why" diff; apply on confirmation. (The *minor* recalibrate runs automatically every 5 lessons at lesson start — not invoked here.)

## `/learn-me-up <topic>` — Run a lesson

1. **Calibrate.** Read `$DATA_DIR/learner/profile.md` (stable traits) and `$DATA_DIR/learner/topic-index.md` (depth markers with confidence + evidence, open ZPD edges). Note the depth marker and its confidence for the topic's domain — low-confidence markers are assumptions to probe, not facts to fade past. Note prior lessons in this domain and relevant entries in `$DATA_DIR/learner/open-questions.md`.
2. **Minor recalibrate check.** If 5+ lessons have been logged since the last recalibrate (count `$DATA_DIR/learner/log.md`), run the minor recalibrate first (`primer/feedback-protocol.md`): scan `calibration-log.md` for repeated misses, flip warranted statuses, surface stale low-confidence markers, show a 3–5 line diff, then proceed.
3. **Plan.** Propose a one-paragraph lesson plan: framing, key invariants, what you'll skip given their depth. Get a quick acknowledgment or course-correction.
4. **Run the protocol.** Elicit → Probe → Diagnose → Deepen → Recap (`primer/lesson-protocol.md`). The Deepen step's source-discovery pass is mandatory. Use AskUserQuestion sparingly; default to free-form conversation.
5. **Self-check** against `primer/anti-patterns.md` before writing the artifact.
6. **Write the artifact** to `$DATA_DIR/lessons/<domain-slug>/<YYYY-MM-DD>-<lesson-slug>.md` per `primer/lesson-template.md`. Include retrieval prompts. Promote any load-bearing newly-discovered source into the canon floor.
7. **Update state** (`primer/feedback-protocol.md`):
   - Append retrieval prompts to `$DATA_DIR/learner/review-queue.md`.
   - Append open threads to `$DATA_DIR/learner/open-questions.md`.
   - Update the domain's depth marker in `$DATA_DIR/learner/topic-index.md`: depth, `[confidence]`, evidence (this session). Mark the topic covered/in-progress; refresh ZPD edges and suggested next.
   - Append any calibration misses to `$DATA_DIR/learner/calibration-log.md`. Infer the silent micro-feedback signals (calibration / engagement / mastery / style fit) from the conversation and record them — do not ask the learner.
   - Append one line to `$DATA_DIR/learner/log.md`.
   - Stable traits in `profile.md` change only via `recalibrate`, not here.

## `/learn-me-up next` — Suggest next lessons

Read profile + topic-index + open-questions. Propose 2–3 best-next lessons. Use AskUserQuestion to let the learner pick. On selection, jump to `<topic>` flow.

Selection priority: (1) topics tied to active goals, (2) prerequisites for in-progress topics, (3) recent open threads, (4) domain breadth.

## `/learn-me-up review` — Interleaved retrieval

Pull 6–10 prompts from `learner/review-queue.md`, weighted toward older entries (spaced review). Run them as a 60–120 second warm-up. Mark answered prompts; surface ones missed for re-review. Can stand alone or precede a `<topic>` lesson.

## `/learn-me-up resume` — Continue an in-progress lesson

Look for `lessons/<domain>/<slug>/STATE.md` files. If one exists, ask if it should be resumed. Otherwise surface the most recent unfinished lesson.

## `/learn-me-up index` — Render the topic index

Read `learner/topic-index.md` and render as a tree with status flags: `[unexplored] [in-progress] [covered] [mastered]`. Link to lesson files where applicable.

## `/learn-me-up profile` — Show or update the learner profile

Render `learner/profile.md`. Ask if any sections need updating (active goals, anti-preferences, depth markers). On update, edit the file directly.

## `/learn-me-up suggest <goal>` — Suggest a lesson track

Given a high-level goal in plain prose, propose a 3–6 lesson sequence that gets there. Surface the dependency graph briefly. Do not execute the lessons — produce the proposed track and write it to `tracks/<slug>.md` if the learner wants it persisted.

## No argument — Show usage

Render a brief usage block listing the verbs. Don't dump the full requirements doc.
</process>

<constraints>
- **Never auto-read `~/Work/*` or any proprietary work codebase.** Work context reaches the profile only through what the learner says, never by reading code.
- **Lessons are the shareable artifact — sanitize them.** No employer names, internal service names, or work-codebase identifiers in lesson artifacts; examples are canonical, synthesized, or fully anonymized. The *profile* is private (its own data repo) and may hold real context; the sanitization rule is about lessons, not the profile.
- **Currency is non-negotiable.** Cite from the canon's vetted floor *and* the mandatory per-lesson source-discovery pass. Never cite the stale list. See `primer/source-canon.md`.
- **Tag every technical claim** as `[verified via docs]` or `[from-training, verify]`. Default to tool-grounded retrieval for API/version-specific facts.
- **For conceptual questions, probe before answering.** Khanmigo rule.
- **Hold positions under pushback** when correct. Sycophancy is failure.
- **Max one in-progress session at a time** in `lessons/*/STATE.md`. No parallel in-progress sessions.
</constraints>
