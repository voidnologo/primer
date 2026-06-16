# Pending Tasks

Live checklist for primer engineering. `session-end` checks off / prunes completed items and adds new ones. Completed work lives permanently in the session notes, not here.

## Next Up

- [ ] **Caleb's GitHub repo rename** `knowledge → primer` (Caleb does this in GitHub settings). After renaming, update the local remote: `git remote set-url origin git@github.com:voidnologo/primer.git`.
- [ ] **(Optional, cosmetic) local dir move** `~/personal/learning/knowledge → ~/personal/learning/primer`. Safe now: the skill command comes from the `~/.claude/skills/primer` symlink and engine includes use `${CLAUDE_SKILL_DIR}`, so nothing breaks. Re-run `tools/install.sh` after moving. Best done outside an active session (the move changes the working dir).
- [ ] **Run Caleb's real intake** (`/primer init`) to replace the generic migrated profile with a rich, evidence-backed one in primer-data.
- [ ] Confirm `session-start`/`session-end` skills match the house style after first real use.

## Done (this session)

- [x] Wave 1: intake, feedback cycle, currency reframe, profile restructure.
- [x] init-instance.sh + `~/.config/primer/config` + data-repo layout.
- [x] Engineering logs (GOALS, DECISIONS, sessions, these docs) + session skills.
- [x] Class/instance split + migration: `voidnologo/primer-data` (private) created and pushed; personal data removed from core.
- [x] Rename to `primer` (skill name + verbs, install.sh, README, REQUIREMENTS, memory). Live skill reinstalled as `/primer`.

## Ideas / proposals (not committed)

- Tune `N` (minor-recalibrate cadence) after real lesson data; currently 5.
- Decide whether `examples/` ships 1–2 sanitized sample lessons, or stays empty.
- Possible `/primer config` verb to set N and register without a full recalibrate.
- Consider a "transfer-confirm" micro-probe in the first lesson that touches an assumed-held skill (closes the Phase-3 transfer assumption).
