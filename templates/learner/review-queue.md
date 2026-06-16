# Review Queue

Spaced retrieval prompts pulled from prior lesson `Retrieval prompts` sections. The Primer surfaces these during `/primer review` (and as the Elicit-step recall). **Scheduling is owned by `tools/primer_state.py` (SM-2), not the model** — it parses and rewrites these lines deterministically. You can still hand-edit them; just keep the field format.

Prompt line format (under `## Prompts`):

`- due:<YYYY-MM-DD> | int:<days> | ef:<ease> | reps:<n> | <domain> | Q:: <question> | A:: <answer>`

- `due` = next review date · `int` = current interval (days) · `ef` = SM-2 ease factor · `reps` = successful recalls in a row.
- New prompts start `int:0 | ef:2.50 | reps:0`, due the day they're added. Add via `primer_state.py review-add`; grade via `review-grade` (it reschedules).

---

## Prompts

<prompts appended here>

---

## Review history

Cold-retrieval scores from each `/primer review` run — the feedback loop's external anchor
(`primer/feedback-protocol.md`). A **calibration** signal, not a mastery metric: prompts are
Primer-authored, so a high score means "the model's estimate survived delayed recall," not "mastered."
Watch the trend, not any single run.

Format: `<date> | <n>/<m> correct | <by-age note, e.g. "missed 2 of 3 older-than-3wk">`

---
