# Pending Tasks

Live checklist for primer engineering. `session-end` checks off / prunes completed items and adds new ones. Completed work lives permanently in the session notes, not here.

## Next Up

- [ ] **Run a real intake** (`/primer init`) to replace the generic migrated profile with a rich, evidence-backed one in primer-data.
- [ ] Confirm `session-start`/`session-end` skills match the house style after first real use.

### From Proposal 0001 (cold review — see `proposals/0001-cold-review-and-improvements.md`)

Wave A — corrections (factual + de-personalization), low risk: **[done — Session 3]**
- [x] **C4** — fixed overstated effect-size claims in `REQUIREMENTS.md §2`; tagged AutoTutor claim.
- [x] **C3** — tagged canon floor edition/date entries `[edition — verify]`; added verify discipline.
- [x] **C1** — de-personalized `system-prompt.md`; canon → starter pack; per-instance domain list; generalized `anti-patterns.md` #4 + fixed stale depth-marker path.

Wave B — close the feedback loop (the structural fix): **[done — Session 3]**
- [x] **C2** — forgetting-aware confidence decay + bidirectional confidence + decay in minor-recalibrate.
- [x] **T1** — `/primer review` miss → calibration-log + confidence drop.
- [x] **E1** — cold-retrieval score recorded; `review-queue.md` Review-history section (self-authored caveat).
- [x] **T7** — "just show me" escape hatch gated on struggle-tolerance.
- [x] Promoted to `DECISIONS.md`: D-0014 (no hardcoded learner), D-0015 (external anchor + decay), D-0016 (effect-size target).

Wave C — quality & hygiene:
- [ ] **T2** — prompt-quality rubric (Matuschak's 5 attributes + pattern language) + self-check.
- [ ] **T5** — reconcile resume/artifact path (flat `<date>-<slug>.md` vs `<slug>/STATE.md`).
- [ ] **T6** — `settings.json` deny-list for `~/Work`/proprietary paths (privacy defense-in-depth).
- [ ] **T4** — evidence-triggered recalibration (replaces the N=5 tuning task below).

Wave D — enhancements & ⚑ decisions (defer until post-use data):
- [ ] **⚑ T3** — decide SRS story: Anki export (recommended first) vs FSRS due metadata.
- [ ] **E3** — generation-effect tweak (learner states invariant before Primer writes prompts).
- [ ] **⚑ E2** — situated-idea dynamic prompts (scope decision).
- [ ] **⚑ E4** — `/primer synthesize <domain>` distillation verb (scope decision).

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
- Tune `N` (minor-recalibrate cadence) after real lesson data; currently 5. *(Superseded by Proposal 0001 T4 — make recalibration evidence-triggered rather than a fixed count.)*
- Possible `/primer config` verb to set N and register without a full recalibrate.
- Consider a "transfer-confirm" micro-probe in the first lesson that touches an assumed-held skill (closes the Phase-3 transfer assumption).
