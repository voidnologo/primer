# Primer — Decision Log

Append-only record of engineering decisions: the **why**, the tradeoffs, and what was rejected. Git history is the *what*; this is the *why*. New decisions go at the top. Each entry is dated and numbered.

Format: decision, context, alternatives considered, tradeoff accepted.

---

## D-0016 · 2026-06-15 · Design target is ~0.4–0.7σ on transfer-valid assessments; 2σ is folklore

**Decision:** State the system's evidence-grounded effect-size target as **~0.4–0.7σ on transfer-valid (not self-authored) assessments**, and stop citing Bloom's "2-sigma" and "generative-AI tutors at 0.73–1.3σ" as design grounding.

**Context:** `REQUIREMENTS.md §2` grounded the design in figures that don't survive verification — ironic in a project whose top non-negotiable is currency. 2σ traces to unpublished dissertations and never replicated (pooled tutoring ~0.37σ, Nickow 2020; human tutoring ~0.79σ, VanLehn 2011); ITS medians are ~0.42–0.66σ (Ma 2014; Kulik & Fletcher 2016), inflated by local tests; the headline gen-AI RCT is 0.63σ honest (Kestin 2025), the higher figures quantile-derived.

**Alternatives:** keep the aspirational numbers (rejected — they fail the project's own source-grounding rule); drop effect sizes entirely (rejected — a target is useful, and the honest range still motivates the design).

**Tradeoff:** a less impressive headline, in exchange for a defensible bar. Implication captured in the feedback loop: self-authored retrieval prompts inflate, so cold-review scores are a calibration signal, not a mastery/effect-size claim (see D-0015). Verified citations: `docs/engineering/research/2026-06-15-ai-tutoring-and-learning-science.md`.

## D-0015 · 2026-06-15 · The feedback loop gets an external anchor + forgetting-aware confidence decay

**Decision:** Depth-marker confidence moves **both ways** and **decays with time**. Cold retrieval in `/primer review` is the external anchor: a miss lowers confidence and logs a calibration entry; a clean answer to an old prompt raises it. Untouched `[high]` markers drift toward `[med]`/reprobe at minor-recalibrate. Review scores are recorded as a calibration signal, explicitly *not* a mastery metric.

**Context:** The loop updated the model only from its own prior assessments, and confidence only ratcheted up — a closed self-assessment loop that drifts optimistic imperceptibly (Boucle "Optimism Feedback Loop"), compounding the BKT monotonicity gap (no forgetting). This worked *against* the goal that the profile gets more true with use.

**Alternatives:** a formal forgetting model (FSRS/Half-Life Regression) per marker (rejected for now — heavier than warranted before real lesson data; revisit under Proposal 0001 T3); leave the loop self-referential (rejected — the drift is the core risk a self-training system must defend against).

**Tradeoff:** the anchor is coarse and the prompts are self-authored, so review scores can't be read as effect sizes — accepted, because "the estimate survived delayed recall" is still the strongest non-self-generated signal available without external assessments. Implements Proposal 0001 C2 + T1 + E1.

## D-0014 · 2026-06-15 · The public engine carries no hardcoded learner

**Decision:** The engine (`primer/*`) is learner-agnostic. `system-prompt.md` reads the learner from `$DATA_DIR/learner/profile.md` rather than asserting a fixed bio; senior-peer/meetup is the *default* register, overridable by the profile; the source canon is framed as a domain *starter pack*, not a universal canon; the lesson-template domain list is per-instance, not a fixed enum.

**Context:** The public core hardcoded the maintainer's bio ("15+ years … technical lead …"), a backend-only canon, and a five-value domain enum — while the README promised "any learner and any goal." This put personal data in the public repo (violating the sharable-without-leaking goal) and mis-onboarded a stranger. It is also a pedagogical miscalibration: an engine that assumes an expert under-scaffolds novice adopters, and over/under-scaffolding is a measured harm (expertise reversal, asymmetric — Tetzlaff 2025).

**Alternatives:** physically split the backend canon into the maintainer's instance and ship a thin starter, or ship multiple domain packs (deferred — Proposal 0001 ⚑ decision; this change does the *framing* now and leaves the content move for later); keep the bio and document it as "the reference learner" (rejected — still personal data in the public core).

**Tradeoff:** the senior-peer voice is now explicitly a default rather than the identity, so the engine reads slightly less opinionated up front — accepted, since the non-negotiable register traits (no sycophancy, productive struggle, currency, confidence-honesty) are preserved as universal. Implements Proposal 0001 C1 (and fixed a stale `profile.md`→`topic-index.md` depth-marker path in `anti-patterns.md`).

## D-0013 · 2026-06-15 · Lessons are private/personal, not shareable-by-default

**Decision:** Lesson artifacts are personal — calibrated to the learner — and live only in the private instance, alongside the profile. The public core ships no personal lessons. Publishing is a deliberate, separate step. **Supersedes the lesson-sharing aspect of D-0001** (which framed "only lessons are sanitized," implying lessons were the shareable surface).

**Context:** The point of the project is deep personalization; a lesson is shaped by the learner's profile, gaps, and scenarios, so it's as sensitive as the profile. Calling lessons "shareable" and sanitizing them by default both undercut that and add friction.

**Alternatives:** lessons sanitized-and-public-by-default (rejected — caps personalization, leaks calibration signal); a public/private split per lesson (rejected — premature).

**Tradeoff:** no public lesson corpus for now. A future **derivation skill** will turn a chosen personal lesson into a sanitized, shareable artifact on demand — sanitization happens at that step, not on every lesson. Resolved: `examples/` removed from the public core (no provisional public lessons); samples will come from the derivation skill.

## D-0012 · 2026-06-15 · Rename to `primer`; skill name from symlink; `${CLAUDE_SKILL_DIR}` for engine includes

**Decision:** Skill renamed `learn-me-up` → `primer`. The command name is set by the installed symlink name (`~/.claude/skills/primer`), not frontmatter or the repo dir name. Engine `@`-includes switched from absolute `$HOME/...` paths to `@${CLAUDE_SKILL_DIR}/primer/...`.

**Context:** The Wave-2 rename risked breaking the live skill (frontmatter/symlink/path mismatch) and the local-dir move risked breaking the session working dir.

**Findings (via claude-code-guide):** command name derives from the skill dir/symlink name; `${CLAUDE_SKILL_DIR}` resolves to the skill's install location at runtime.

**Tradeoff:** the physical repo dir name and the local-dir move become cosmetic — nothing depends on them. Engine includes are now location-independent, so the GitHub repo rename and local-dir move carry zero functional impact.

## D-0011 · 2026-06-15 · Engineering session/decision logs in the public core

**Decision:** Track development "why" in `docs/engineering/` — `GOALS.md` (north star), `DECISIONS.md` (this file), `sessions/` (per-session logs) — plus a `/session-start` / `/session-end` mechanism.

**Context:** Git records what changed; the reasoning and rejected alternatives were living only in chat. Need durable design memory to maintain focus and prevent drift across sessions.

**Alternatives:** keep it in commit messages only (rejected — no room for tradeoffs/alternatives, not browsable as a design narrative); a single CHANGELOG (rejected — conflates what/why).

**Tradeoff:** a small per-session documentation cost, paid back as anti-drift and onboarding for future contributors. Logs live in the public core (they document the engine and carry no personal data).

**Format basis:** adapted the maintainer's existing session-skill convention from the public `~/personal/card-game` project (session_start/end + numbered notes + pending-tasks + continuation), with two primer changes: a `GOALS.md` north-star read for anti-drift, and a dedicated ADR-style `DECISIONS.md`. Implemented as **modern skills** (`.claude/skills/<name>/SKILL.md`), not legacy `.claude/commands/`. The proprietary work repos were not read.

## D-0010 · 2026-06-15 · Project name is "primer", not "the-primer"

**Decision:** Name the project/repo/skill `primer`.

**Context:** "the-primer" reads truer to the source material but the leading "the" gets dropped or questioned in practice.

**Tradeoff:** slight loss of fidelity to *The Diamond Age* framing for everyday memorability. Internal engine directory `primer/` and the skill name share the word — acceptable (different namespaces).

## D-0009 · 2026-06-15 · Data-repo layout mirrors the core (`learner/` + `lessons/`)

**Decision:** The private data repo root contains `learner/` (state) and `lessons/` (artifacts); `$DATA_DIR` points at the root.

**Context:** Initial scaffold flattened state to the data-dir root, which contradicted the `learner/…` paths used throughout the protocol docs.

**Alternatives:** flat root with bare filenames (rejected — would have required rewriting ~13 references across the engine docs and lost the state/artifact grouping).

**Tradeoff:** one extra path segment, in exchange for a clean wholesale migration (move existing `learner/` + `lessons/` as-is) and zero protocol-doc churn. Dev-fallback ($DATA_DIR = core repo root) then works unchanged.

## D-0008 · 2026-06-15 · init scaffolds locally and prints commands; never calls GitHub

**Decision:** `tools/init-instance.sh` scaffolds the data dir, git-inits it, writes the per-machine config, and **prints** the `gh`/`git` commands for the user to run.

**Context:** The public core can't assume how others host or auth their private data.

**Alternatives:** auto-create via `gh` (rejected for the core — assumes gh auth and a hosting choice); point-at-existing only (rejected — more manual for the common case).

**Tradeoff:** one manual push step, in exchange for portability across unknown user setups. (For the maintainer's *own* instance migration, using `gh` directly is fine — that's not the core's job.)

## D-0007 · 2026-06-15 · Per-machine data pointer in `~/.config/primer/config` (XDG)

**Decision:** The skill resolves `$DATA_DIR` from `~/.config/primer/config`.

**Context:** The same private data repo is cloned to different paths on personal vs. work machines.

**Alternatives:** gitignored pointer file in the core (rejected — lost on re-clone); env var (rejected — invisible, easy to forget on a new machine).

**Tradeoff:** a config file outside both repos to manage, in exchange for surviving re-clones and being naturally per-machine.

## D-0006 · 2026-06-15 · Currency: canon is a vetted floor, not a ceiling

**Decision:** The allowlist is a pre-vetted *starting set*; every lesson runs a mandatory source-discovery pass beyond it; the stale-list + stale-criteria are the real currency guardrail; load-bearing finds get promoted back into the floor.

**Context:** A closed allowlist would freeze knowledge at list-authoring time — the opposite of the currency goal.

**Alternatives:** strict allowlist (rejected — restricts current info); no canon at all (rejected — discards vetting already done, every lesson re-explores from scratch).

**Tradeoff:** per-lesson search cost, in exchange for non-negotiable currency plus a floor that ages forward through use.

## D-0005 · 2026-06-15 · Micro-feedback is silent (inferred), never asked

**Decision:** The Primer infers engagement/difficulty/style-fit from the conversation and records it; it does not ask end-of-lesson rating questions.

**Context:** Explicit rating prompts read as the fluff the learner profile explicitly rejects.

**Tradeoff:** inference is noisier than a direct answer, but avoids friction and stays in-register. Patterns get confirmed across sessions via the calibration log, not a single self-report.

## D-0004 · 2026-06-15 · Two-tier recalibration (minor auto every 5, deep on demand)

**Decision:** A lightweight minor recalibrate auto-runs every 5 lessons (compacts volatile state, shows a diff); a deep recalibrate the user invokes rewrites stable traits and goals.

**Context:** An append-only loop accretes volatile state and never corrects the model; but stable traits shouldn't be rewritten on one session.

**Alternatives:** only-manual (rejected — drift goes uncaught); only-automatic deep (rejected — too heavy to run often, risks over-fitting traits).

**Tradeoff:** N=5 is a guess to tune. Two mechanisms instead of one, in exchange for cheap continuous hygiene + deliberate, evidence-based trait changes.

## D-0003 · 2026-06-15 · Feedback loop runs at three timescales; stable/volatile split

**Decision:** Capture silently within a lesson, capture signals at lesson end (calibration log + confidence/evidence on depth markers), recalibrate periodically. Stable traits → `profile.md`; volatile state (depth markers, ZPD edges, calibration misses) → `learner/`.

**Context:** The original loop only updated at session end and mixed stable traits with volatile depth markers in one file, so the file churned and traits were never deliberately revisited.

**Tradeoff:** more files and more moving parts, in exchange for a profile that gets more true with use and is honest about confidence.

## D-0002 · 2026-06-15 · Intake = self-report + one live diagnostic probe per domain

**Decision:** The cold-start interview grounds each self-rated domain with a single live diagnostic probe (causal/counterfactual/critique), and records the gap at low confidence.

**Context:** Self-rated skill level is unreliable in both directions; a blank or self-report-only profile mis-calibrates the first lessons.

**Alternatives:** self-report only (rejected — unreliable); placement-exam depth (rejected — too much onboarding friction).

**Tradeoff:** ~30–45 min onboarding and one probe's worth of uncertainty per domain, in exchange for a first profile grounded in demonstrated behavior. Real depth is refined by later lessons.

## D-0001 · 2026-06-15 · Privacy via class/instance repo split, not a public-safe profile

**Decision:** Separate a public core (engine) from a private instance data repo (profile + lessons). The profile is private and may be rich; only lessons are sanitized.

**Context:** The original model made the profile "public-safe," which capped its richness — the genuinely useful tailoring signal (real stack, stakes, anxieties) couldn't be stored. The maintainer also needs profile + lessons synced across two machines.

**Alternatives:** two files (public + gitignored private) in one repo (rejected — superseded; doesn't give cross-machine sync); keep fully public-safe (rejected — caps quality); all data gitignored local-only (rejected — no sync).

**Tradeoff:** managing two repos and a private remote (trust boundary: private GitHub repo, not local-only), in exchange for a rich profile, clean sharing, and git-based multi-machine sync.
