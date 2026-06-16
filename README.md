# primer

A personal, Primer-style learning system — an adaptive tutor that runs interactive lessons calibrated to *you* and gets sharper the more you use it.

## What's a "Primer"?

In Neal Stephenson's *The Diamond Age*, the *Young Lady's Illustrated Primer* is a book made for a single child. It was commissioned for an aristocrat's granddaughter — but a copy slips into the hands of Nell, a girl from the slums it was never meant for. That turns out not to matter. The Primer meets her where she is.

It isn't a textbook. It pays attention to who's actually reading it, learns her world, and teaches through stories bent to fit her life — smuggling in reading, logic, computation, self-defense, and eventually how to *think* — always pitched just past what she can already do, never lecturing, never bored of her, never talking down. Over years, that book raises a neglected kid into a formidable adult. The teaching works because it's a relationship, not a syllabus.

That's the north star, aimed at one stubborn problem: staying sharp in a field that keeps moving. This project won't write you a fairy tale or raise your children — but it goes after the part that *is* reproducible. A tutor that genuinely knows you: your real depth, your gaps, the register you want to be spoken in. One that teaches when you pull on a thread, not when a curriculum says to. One whose lessons are yours — they live in your own repo, they outlast the session, and the model of you gets a little truer every time you show up.

## What this is

Implemented as a Claude Code skill, primer runs narrative, calibrated lessons against a persistent, evidence-backed learner profile and captures every session as a durable markdown artifact. It works for any learner and any goal — system design, MCP and AI-assisted development, picking up a new language, distributed systems. The intake interview discovers your ability and decomposes *your* goal; it doesn't assume a curriculum.

## Class and instance

primer is split in two:

- **This repo — the public core ("the class").** The engine: the skill, the protocols (`primer/`), and the instance templates. It holds **zero** personal data — including no lessons. Clone it and pull updates as the community improves it.
- **Your private data repo ("the instance").** Your profile, depth markers, calibration log, and lessons. Private, and git-synced across your machines. Created from the core by `init`.

This is why your data can be rich (real stack, real goals) without ever leaking: it lives only in your private repo. **Lessons are personal too** — they're calibrated to you, so they live in the private instance alongside the profile. Publishing a lesson is a deliberate, separate step (a derivation skill that turns a personal lesson into a sanitized public artifact is planned), never the default.

## Install & first run

```bash
git clone <this repo>
cd primer
./tools/install.sh          # symlinks the repo as the `primer` skill
```

Then, in any Claude Code session:

```
/primer init                # one-time: scaffold your private data repo + intake interview
```

`init` walks you through `tools/init-instance.sh` (scaffolds your data repo locally and prints the `git`/`gh` commands to push it private), then runs the cold-start interview to build your first profile. After that:

```
/primer <topic>             # run a lesson
/primer index               # show your topic map
```

### Second machine

Clone your private data repo, then point that machine at it:

```bash
./tools/init-instance.sh <path-to-your-data-repo-clone>
```

It detects the existing instance and only writes that machine's pointer (`~/.config/primer/config`).

### Privacy hardening (recommended)

primer never auto-reads a work codebase — but that is an instruction the model follows, not a wall. For
defense in depth, add a deny rule to your **global** Claude Code settings (`~/.claude/settings.json`) so the
tools physically can't read proprietary paths during a session. Adjust the paths to your machine:

```jsonc
{
  "permissions": {
    "deny": [
      "Read(//Users/you/Work/**)",
      "Edit(//Users/you/Work/**)",
      "Bash(cat //Users/you/Work/**)"
    ]
  }
}
```

This is belt-and-suspenders on top of the skill's own rule (the engine still redirects work-specific
scenarios to canonical analogs). Stack-aware framing comes from your profile and what you say in the
conversation, never from reading the code.

## Subcommands

- `/primer init` — first-time setup: intake interview, builds your profile
- `/primer <topic>` — start an interactive lesson
- `/primer next` — suggest 2–3 best-next lessons
- `/primer recalibrate` — deep profile review (the minor one runs automatically every 5 lessons)
- `/primer review` — interleaved spaced-retrieval warm-up from prior lessons
- `/primer resume` — pick up an in-progress lesson
- `/primer index` — show topic-index tree with status
- `/primer profile` — show or update your profile
- `/primer suggest <goal>` — propose a multi-lesson track for a stated goal

## Design principles

The full set and the engineering rationale live in [`docs/engineering/GOALS.md`](docs/engineering/GOALS.md) and [`docs/engineering/DECISIONS.md`](docs/engineering/DECISIONS.md). The most load-bearing:

- **Personal, calibrated, evidence-backed.** Depth markers carry confidence + evidence; the system knows what it has *seen* you do vs. what it *assumed*. Intake discovers ability and goal; the feedback cycle keeps the profile true.
- **Senior peer, not teacher.** Lessons read like a senior engineer talking to a colleague (register is calibrated per learner). No motivational fluff.
- **Productive struggle over fluent answers.** Every lesson forces prediction or critique before the explanation lands.
- **Currency is non-negotiable.** The canon (`primer/source-canon.md`) is a *vetted floor*, not a ceiling — every lesson searches for current sources beyond it; a stale-list is the guardrail.
- **Private by architecture, never proprietary.** All personal data — profile *and* lessons — lives only in your private instance; the skill never auto-reads a work codebase. Publishing a lesson is a deliberate future derivation step, not a default.

## Developing primer

Engineering happens against the north star in [`docs/engineering/`](docs/engineering/) using the `session-start` / `session-end` skills, which track the *why* (decisions, tradeoffs) alongside git's *what*. See [`REQUIREMENTS.md`](REQUIREMENTS.md) for the original design contract (historical; the living design record is now `docs/engineering/` + `primer/`).

## Contributing

The public core is the reusable part. Other learners clone it and bring their own private instance — fork or PR improvements to the engine; never commit personal data here.

## License

MIT — see [`LICENSE`](LICENSE).
