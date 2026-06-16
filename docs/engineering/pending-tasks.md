# Pending Tasks

Live checklist for primer engineering. `session-end` checks off / prunes completed items and adds new ones. Completed work lives permanently in the session notes, not here.

## Next Up

- [ ] **Wave 2 — rename to `primer`** (task #7): skill frontmatter `name` + verb headers (`/learn-me-up` → `/primer`) in `SKILL.md`; remaining `learner/` path refs in the older verbs; `tools/install.sh` symlink name; README + REQUIREMENTS; `~/.claude` memory files. Coordinate frontmatter + symlink + reinstall so the live skill doesn't break mid-rename. **GitHub repo rename: user does it.**
- [ ] **Wave 2 — migrate maintainer's instance** (task #5): move real `learner/` + `lessons/` into a private data repo; `init` the pointer. (Maintainer's `gh` access available — own instance, not the core.)
- [ ] Confirm `session-start`/`session-end` skills match the maintainer's house style after first real use.

## Ideas / proposals (not committed)

- Tune `N` (minor-recalibrate cadence) after real lesson data; currently 5.
- Decide whether `examples/` ships 1–2 sanitized sample lessons, or stays empty.
- Possible `/primer config` verb to set N and register without a full recalibrate.
- Consider a "transfer-confirm" micro-probe in the first lesson that touches an assumed-held skill (closes the Phase-3 transfer assumption).
