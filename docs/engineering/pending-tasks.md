# Pending Tasks

Live checklist for primer engineering. `session-end` checks off / prunes completed items and adds new ones. Completed work lives permanently in the session notes, not here.

## Next Up

- [ ] **Run a real intake** (`/primer init`) to replace the generic migrated profile with a rich, evidence-backed one in primer-data.
- [ ] Confirm `session-start`/`session-end` skills match the house style after first real use.

## Done (this session)

- [x] Wave 1: intake, feedback cycle, currency reframe, profile restructure.
- [x] init-instance.sh + `~/.config/primer/config` + data-repo layout.
- [x] Engineering logs (GOALS, DECISIONS, sessions, these docs) + session skills.
- [x] Class/instance split + migration: `voidnologo/primer-data` (private) created and pushed; personal data removed from core.
- [x] Rename to `primer` (skill name + verbs, install.sh, README, REQUIREMENTS, memory). Live skill reinstalled as `/primer`.
- [x] GitHub repo renamed `knowledge → primer` (`voidnologo/primer`), remote updated, pushed. Local dir moved to `~/personal/learning/primer`.
- [x] Lessons reframed as private-by-default (D-0013); `examples/` removed from the public core.

## Ideas / proposals (not committed)

- **Lesson → public-artifact derivation skill** (D-0013): take a personal lesson from the private instance and derive a sanitized, shareable artifact on demand. The only sanctioned path to a public lesson.
- Tune `N` (minor-recalibrate cadence) after real lesson data; currently 5.
- Possible `/primer config` verb to set N and register without a full recalibrate.
- Consider a "transfer-confirm" micro-probe in the first lesson that touches an assumed-held skill (closes the Phase-3 transfer assumption).
