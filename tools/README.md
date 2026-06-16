# tools

Helper scripts for primer. All are self-contained (no third-party installs).

| Script | What it does |
|--------|--------------|
| `install.sh` | Symlinks this repo into `~/.claude/skills/primer`. |
| `init-instance.sh` | Scaffolds the private data repo, writes the per-machine pointer (`~/.config/primer/config`), prints the git/gh commands to push it private. |
| `primer_state.py` | **Deterministic learner-model bookkeeping** — the parts of the feedback loop that are pure arithmetic over dates/counts (so the LLM doesn't do them in-context). |
| `test_primer_state.py` | Unit tests for `primer_state.py`. Run: `python3 tools/test_primer_state.py`. |

## `primer_state.py`

Python 3.11+ stdlib only — runs on mac/linux/windows with nothing to install. It reads and rewrites the
learner's **markdown** state files (the source of truth; D-0018/D-0020), so state stays hand-editable and
git-syncs cleanly across machines. No database.

```
python3 tools/primer_state.py --data-dir "$DATA_DIR" <command>
```

Commands:

- `review-due [--limit N]` — list prompts due today (SM-2 schedule), weakest/oldest first.
- `review-grade --index <i> --quality again|hard|good|easy` — grade a due prompt and reschedule it.
- `review-add --domain D --question Q --answer A` — add a new prompt (initial schedule, due today).
- `review-history --correct N --total M [--note ...]` — record a review session's score.
- `markers-decay [--days N]` — drift stale `[high]` depth markers to `[med]` + flag reprobe (forgetting-aware).
- `recalibrate-check` — is a minor recalibrate due? (fires on 4+ misses or 8+ lessons since the last one).

`--on YYYY-MM-DD` overrides "today" (for testing or back-dating). `--data-dir` overrides the path otherwise
read from `~/.config/primer/config`.

Scheduler: **SM-2** (SuperMemo-2) — chosen over FSRS for transparency and zero training data (D-0020).
