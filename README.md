# knowledge

A personal, Primer-style learning system for a senior backend engineer.

Inspired by the Young Lady's Illustrated Primer from Neal Stephenson's *The Diamond Age*, implemented as a Claude Code skill that runs interactive, narrative tutorials calibrated to a persistent learner profile and captures every session as a durable markdown artifact.

Goal: stay current as a senior backend engineer; grow into staff-level technical leadership; never waste time on outdated takes.

## How it works

1. Invoke `/learn-me-up <topic>` in Claude Code.
2. The skill reads `learner/profile.md`, calibrates depth, runs the **Elicit → Probe → Diagnose → Deepen → Recap** lesson protocol.
3. The session is captured to `lessons/<domain>/<YYYY-MM-DD>-<slug>.md` per the strict template.
4. Retrieval prompts, open threads, and depth markers feed back into the learner model. Future sessions adapt.

See [`REQUIREMENTS.md`](REQUIREMENTS.md) for the full system contract; [`primer/`](primer/) for the rules and personality; [`learner/`](learner/) for the persistent state; [`lessons/`](lessons/) for the corpus.

## Install

```bash
./tools/install.sh
```

Symlinks the repo into `~/.claude/skills/learn-me-up`. Then in any Claude Code session:

```
/learn-me-up
/learn-me-up index
/learn-me-up <topic>
```

## Subcommands

- `/learn-me-up <topic>` — start an interactive lesson
- `/learn-me-up next` — suggest 2–3 best-next lessons
- `/learn-me-up review` — interleaved spaced-retrieval warm-up from prior lessons
- `/learn-me-up resume` — pick up an in-progress lesson
- `/learn-me-up index` — show topic-index tree with status
- `/learn-me-up profile` — show or update the learner profile
- `/learn-me-up suggest <goal>` — propose a multi-lesson track for a stated goal

## Design principles

8 principles drive the system. The full set is in [`REQUIREMENTS.md` § 2](REQUIREMENTS.md#2-design-principles). The most load-bearing:

- **Senior peer, not teacher.** Lessons read like a senior engineer talking to a colleague. No motivational fluff; no cheerleading.
- **Productive struggle over fluent answers.** Every lesson forces prediction or critique before the explanation lands.
- **Primitives → failure modes → patterns → tradeoffs.** Universal high-quality progression. Never start with a framework.
- **Currency is non-negotiable.** Every lesson cites from a 2026-current allowlist (`primer/source-canon.md`); a stale-list is explicitly avoided.
- **Stack-aware, never proprietary.** No employer names, no work-codebase snippets — ever. Stack awareness comes from the public-safe profile.

## Reading the lessons online

The lesson corpus is markdown — works as-is in any editor or directly on GitHub. A static-site rendering of finalized lessons is a planned v1.2 addition; the SSG choice is deferred until the corpus is large enough to know what the navigation should look like.

## Contributing

This is one engineer's Primer. Other engineers should fork and bring their own profile and corpus. The architecture (skill + primer + learner + lessons) is the reusable part.

## License

MIT — see [`LICENSE`](LICENSE).
