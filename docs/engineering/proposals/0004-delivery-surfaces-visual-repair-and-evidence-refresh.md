# Proposal 0004 — Delivery surfaces, visual-layer repair, and the 2026 evidence refresh

> **Status:** proposed, awaiting scope decision. Written 2026-10-14.
>
> **Evidence base:** two research sweeps run this session — the AI-tutoring landscape (2025–2026 primary literature) and the Claude delivery-surface capability map (Anthropic docs, MCP spec, verified against this machine, Claude Code 2.1.300). Plus a hands-on audit of `tools/primer_view.py` output, measured in a browser rather than read from source.
>
> **Motivation.** Three maintainer requests: make the project fast and current; improve the graphics, which read as amateur and arrive slowly; and find out whether primer can serve users who want Claude Desktop rather than the CLI. Two further directives arrived during the review: push repeatable work out of model prose and into deterministic scripts, since the project is token-heavy; and pipeline work — prepare the next beat while the learner is reading the current one.
>
>
> **Portability directive (maintainer, during review).** Privacy is a weaker objection than it first appeared: being in a Claude session already concedes that Anthropic can see the interaction under its privacy policy, so publishing a page does not change the threat model much. The binding constraints are instead **ease of use, low-friction high-quality interaction, and not having to rebuild when a vendor changes or drops a feature**. The project should stay as independent and vendor-agnostic as it can. Swapping the backend model (Qwen, OpenAI, Grok) is not a goal now, but it must remain possible, and no vendor's product decision should be able to sink the project. This reorders Wave D: the axis is coupling, not privacy.
>
>
> **Register directive (maintainer, during review).** The semi-antagonistic Socratic grilling works for this maintainer and has drawn feedback that it does not suit everyone. Some learners want to be taught a topic and reinforced with questions afterwards, rather than being asked to derive it from first principles — and that is hardest to defend precisely where the topic is new and the learner has little foundation to build from. Intake should discover this and the profile should carry it. See **E3b**, which is where the evidence turns out to agree, though not for the reason preference would suggest.
>
> **Item IDs.** `V` = visual layer repair, `D` = delivery surfaces, `S` = scripts and determinism, `E` = evidence-driven pedagogy changes, `P` = pipelining. Each item names the goal it serves and the non-negotiable it could threaten, per the `GOALS.md` anti-drift checklist.
>
> **Sequencing note.** Wave V is defect repair and is independent of everything else. Wave D contains the decision with the widest consequences (whether lesson content may leave the machine) and should be decided before anything is built against it. Wave E is the largest body of new evidence and the slowest to adopt. Wave S and Wave P are cost reductions that make the rest affordable.

---

## The portability constraint, and where primer actually stands

Before Wave D proposes anything, it is worth auditing what in primer is vendor-specific today. The answer is encouraging, and it is the reason Wave D has to be written carefully: **the engine is already close to vendor-agnostic, and the delivery options are the first thing that would change that.**

| Component | Coupling |
|---|---|
| `SKILL.md`, `primer/*.md` | Prose instructions. Any instruction-following model can read them. The pedagogy — the part that took the most work — is the most portable part of the project. |
| `tools/*.py` | Python 3.11+ **stdlib only**. No vendor surface at all. |
| The private instance | Markdown in a git repo. No vendor surface. |
| Skill discovery | `~/.claude/skills/`, `${CLAUDE_SKILL_DIR}`. Claude Code-specific, but it is a packaging convention — a path and a loader, replaceable in an afternoon. |
| Subagent dispatch (the sweep, R2) | Harness-specific. **Wave S2 removes most of this** by moving fetch-and-extract into a script. |
| Search and fetch | Harness tool names. Replaceable per host. |

So the lock-in today is packaging and two tool names. That is a small surface, and D-0018's bookkeeping-as-code is why: every decision to put mechanics in stdlib Python instead of model prose was also, accidentally, a portability decision.

**The convergence worth naming:** Wave S and the portability directive point the same way. Work moved out of "model follows prose using harness tools" and into "deterministic stdlib Python" gets cheaper in tokens *and* loses its vendor coupling. These are not two initiatives competing for effort; they are the same change scored on two axes.

**The principle this proposal adopts:** separate **what is rendered** from **how it is delivered**. Today `primer_view.py render` does both — it writes the page and prints the `file://` link. If rendering emits a standard artifact (self-contained HTML, which it already does) and delivery is a thin adapter chosen by config, then a vendor channel is cheap to add and cheap to lose. Losing one costs an adapter, not the visual layer.

---

## Wave V — Visual layer repair

### The audit

A page exercising all six forms plus an explorable was rendered and measured in a browser. Render cost is not the problem: seven figures validate and write in 44ms to a 16KB page. The defects are geometric, and one is a correctness defect in the channel used during the live prediction beat.

A redrawn specimen of all seven, annotated per-figure with the rule each one breaks, was published as a private artifact during the review session. It is a prototype, not engine code.

### V1 — Stop upscaling figures (the root cause)

`svg_open` emits `width="100%"`, so a figure authored at roughly 500 user units is stretched to whatever the container is. Measured on one page, in an 819px column, the six figures scaled by 1.34×, 1.53×, 1.58×, 1.61×, 1.65× and 1.76×.

Two consequences follow mechanically. The same 13px `.pv-t` renders between 17.5px and 22.8px depending on which figure it sits in — a 31% typographic spread within one page, which is the most visible reason the set reads as unconsidered. And every stroke becomes a non-integer upscale, so `stroke-width: 1.5` lands at 2.0–2.6 device pixels and no edge is crisp.

**Change:** cap each figure at its natural width (`max-width: <viewBox width>px; width: 100%`) so it can shrink on a phone but never grow. Then fix one typographic scale in user units across every template, so a label is the same size in a `state` figure as in a `curve`.

*Serves:* the maintainer's styling request. *Threatens:* nothing. This is the highest-value single change in the wave.

### V2 — Geometry defects, each reproduced

| Defect | Location | Evidence |
|---|---|---|
| Transition labels land inside the state boxes | `_state_edge`, label at `mid - 12` while the box spans `mid ± 24`; the label is also wider than the 40px inter-box gap | "election timeout" overlaps both Follower and Candidate |
| Illegal-transition strike floats off its arc | strike drawn at the Bézier *control* point (`apex ± 6`); a quadratic's midpoint is `(P0 + 2P1 + P2)/4`, about 19 units higher | renders as a loose tick below the curve |
| Arrowheads change size between edges | marker inherits `markerUnits="strokeWidth"`; `pv-blank` at 2.5 draws a head 1.67× the one on `pv-l` at 1.5 | visible on any figure mixing blanked and plain edges |
| Curve series label leaves the viewBox | placed at the final point, `text(px(last) - 6, py(last) - 10)`; with a point at the y maximum this is `y = -3.1` in a `0 0 466 290` box | confirmed by `getBBox` |
| Curve series label collides with the annotation label | same cause | bbox intersection confirmed programmatically |
| Timeline rail runs through every span | `.pv-span` fills with `--shade` at 16% alpha over a full-width dashed lifeline | dashes visible inside each span |
| Layers boundary label sits on the box border | right-anchored at `left + bw + 4` = 480; the box ends at 476 | not a viewBox clip — the box is 496 wide — but an overlap |

**Change:** state labels move above the box row; the strike moves to the curve midpoint; `markerUnits="userSpaceOnUse"` fixes head size; the curve gains gridlines, intermediate ticks and headroom on the y scale, with the series label placed in empty plot area rather than at the endpoint; timeline spans get an opaque fill; the layers boundary label moves into a reserved right gutter.

**Test obligation:** these are geometry bugs that a passing test suite did not catch, which is the same lesson D-0029 records. Add bounding-box assertions — no text element may intersect another text element or a box border, and every drawn element must lie inside the viewBox — computed from the emitted SVG rather than by eye.

*Serves:* the styling request. *Threatens:* nothing.

### V3 — `quorum` channel parity (a correctness defect, not a cosmetic one)

Two gaps, both in `_ascii_quorum`, both in the channel the learner sees *during* the prediction beat:

- **The terminal asserts a claim the spec never declares.** It prints `"<side> side holds the majority and can make progress"`. Nothing checks node counts. A spec with `progress: "left"` over a 2-node group against a 3-node group prints "left side holds the majority" — false, and contradicted by the node counts in the same figure. The page, for the same spec, prints only "can make progress", which is what `progress` actually declares.
- **The terminal drops the leader marker.** `n.get("leader")` is never read in ASCII. The page draws a dashed ring and a `leader` label. For the canonical use of this form — which `diagramming.md` describes as the leader stranded in the minority — the live channel omits the element the invariant is about.

`_ascii_layers` has a lesser version of the same problem: it never reads `detail`, so "authn happens here" appears on the page and not in the terminal.

This is the F-06 / F-18 class, in the form that was never audited for it. The earlier audit covered what blanking conceals; it did not cover whether both channels *state the same claim* when nothing is blanked.

**Change:** ASCII renders only what the spec declares; both channels render every declared element or neither does. Assert channel agreement directly, the way `TestBlankConcealsTheClaim` already does for blanking.

*Serves:* honesty about what the system shows the learner. *Threatens:* nothing. **This should land before the cosmetic work** — it is the only item in the wave where the learner is currently shown something untrue.

### V4 — Explorables need a visual output channel

`compile_explorable` produces outputs shaped `{id, label, decimals}` and renders `<b>number</b><span>label</span>`. Dragging a slider changes two numerals, typically beneath a static `curve` figure making the same claim.

`diagramming.md` justifies explorables on one test: a parameter whose variation *is* the insight. A pair of numerals does not show variation; a mark moving along a plotted curve does.

**Change:** extend the contract with an optional declared plot — an x input, a y output, and the axis bounds — and generate the marker wiring the same way the numeric wiring is generated today. The model still writes no JavaScript. The specimen artifact shows the target.

*Serves:* the graphics request, and the stated justification for having explorables at all. *Threatens:* nothing structurally; it widens the generated-wiring surface, so it inherits the hostile-input obligation D-0023 established.

### V5 — The Mermaid channel does not exist

`visuals.md` documents three channels; `DECISIONS.md` D-0023 states "Mermaid for the artifact"; Proposal 0003 describes it. There is no Mermaid emitter anywhere in the repo. Since figure specs are HTML comments, a lesson artifact read on GitHub or in an editor shows **no figures at all**.

**Change:** either implement the emitter (the six forms map onto `sequenceDiagram`, `stateDiagram-v2` and `flowchart`; `curve` and `timeline` do not map cleanly and would need a table fallback), or retract the claim from `visuals.md`, `DECISIONS.md` and the README. Retracting is cheaper and honest; implementing makes lesson artifacts readable where they are stored. The artifact is what a learner still has months later, after the derived view page has been regenerated or discarded, which is when a figure earns its keep.

*Serves:* currency of the project's own documentation. *Threatens:* nothing. Note that artifacts render Mermaid natively, so V5 and D2 interact.

---

## Wave D — Delivery surfaces

### D1 — The README's claim about where primer runs is half right

Verified against Anthropic's docs and this machine (Claude Code 2.1.300; `~/.claude/skills/primer` symlinked; `~/.claude/skills/synced/` present and populated).

| Surface | Reads `~/.claude/skills/` |
|---|---|
| Claude Code CLI (terminal) | Yes |
| Desktop app → **Code tab, Local** environment | Yes |
| Desktop app → Code tab, Cloud | No |
| Desktop app → Code tab, SSH | Yes, but from the *remote* host's home |
| Desktop app → **Cowork tab**, **Chat tab**, claude.ai | No |
| Desktop **scheduled tasks** | Yes — they run locally |
| Cloud routines | No |

So primer already works in Claude Desktop, in the Code tab on Local. "The desktop app" in the README is too coarse: a reader who tries the Chat tab finds nothing. The Cloud/Cowork sentence is still exactly right and now has two more members, routines and SSH.

Two additions worth making: local and terminal sessions *also* load claude.ai-account skills, downloaded into `~/.claude/skills/synced/` (read-only; edits there are overwritten; `syncClaudeAiSkills: false` disables). And desktop scheduled tasks run locally, so a scheduled lesson is possible on the desktop app though not as a cloud routine.

**Change:** a README correction. No engineering.

*Serves:* low-friction onboarding. *Threatens:* nothing.

### D2 — Delivery as a swappable adapter, not a channel choice

The original framing of this item was privacy versus convenience. The maintainer has relaxed the privacy objection, which changes the question to **coupling versus convenience** — and that is a question with a better answer than picking a side.

**What the artifact channel buys:** a real browser renderer, a stable URL that updates in place across a long lesson instead of a manual reload after each `--upto`, version history, and a return channel (D3). It reaches the CLI and the Desktop Code tab. For the maintainer's stated priority — low-friction, high-quality interaction — it is the strongest option available today.

**What it costs in coupling, stated concretely:** the artifact runtime capabilities are versioned **`0.2.78`** (verified on this machine at `bundled-skills/2.1.300/.../artifact-capabilities/0.2.78/`). A pre-1.0 contract is a reasonable thing to use and an unreasonable thing to build a core loop on. The surface is entirely Anthropic-proprietary — the `Artifact` tool, `claude.use()`, the `db` and `room` capabilities, the `ArtifactData` tool — with no specification, no second implementation, and no external governance. Availability is also gated on plan tier and a `/login` session, so it is unavailable on API-key, Bedrock, Vertex and Foundry sessions regardless of what primer wants.

**The resolution:** make delivery an adapter. `primer_view.py` already emits a self-contained HTML page with zero external requests, which is the most portable artifact the project could produce. Add `--deliver local|artifact|serve`, defaulting to `local`, selected per instance by a config key in the learner's own data repo. The renderer never learns which channel it is feeding.

Then the artifact path is a convenience that costs one adapter to add and one adapter to lose. If Anthropic changes the capability contract — which a `0.2.x` version says is likely — primer loses a delivery option and keeps its visual layer, its pedagogy and its data.

**Rule to hold:** the `local` path stays complete and tested. Any lesson that can be taught through the artifact channel can be taught without it. That is `GOALS.md`'s Self-contained non-negotiable, and it is also the portability directive, arriving at the same place from a different argument.

*Serves:* ease of use and low-friction interaction, without conceding independence. *Threatens:* Self-contained, only if the `local` path is ever allowed to rot.

### D3 — The return channel, ranked by coupling rather than convenience

Four mechanisms work today. Under the portability directive the ranking inverts from what convenience alone would suggest.

| Mechanism | Standard? | Reaches | Cost of a vendor change |
|---|---|---|---|
| **Local page + a localhost server the skill starts** | Pure web standards, no vendor surface | Any browser, any host that can run a shell command | None |
| **Local MCP server** | **Open standard under the Linux Foundation** (below) | Claude Desktop Chat, Cowork, Claude Code, and any MCP-capable client | Low — the protocol outlives any one client |
| Artifact `db` + `ArtifactData` | Proprietary, contract `0.2.78` | CLI, Desktop Code tab, plan-gated | Rebuild the loop |
| Artifact `room` | Proprietary; also ephemeral — nothing persists, messages can drop | same | Rebuild the loop |

**MCP's governance changed in a way that matters here.** Anthropic donated MCP to the **Agentic AI Foundation**, a directed fund under the Linux Foundation, on 2025-12-09. AAIF was co-founded by Anthropic, Block and OpenAI, with Google, Microsoft, AWS, Cloudflare and Bloomberg supporting; the Linux Foundation states it will not dictate MCP's technical direction, and maintainers operate independently. OpenAI adopted MCP in its Agents SDK in March 2025 and later in ChatGPT apps; Google confirmed support in the Gemini SDK; Microsoft embedded it in Azure AI, VS Code and Copilot Studio.

That makes MCP the one delivery mechanism in this proposal that is **not** a bet on a single vendor. A local MCP server runs on the learner's machine with full filesystem and git access, speaks a governed protocol, and would keep working against a different model or client.

**Recommendation:** build the return channel on the localhost server first — it is the smallest delta from what `primer_view.py` already does, costs nothing in coupling, and is the reference the other adapters are measured against. Treat a local MCP server as the considered second step, and the one to reach for if "primer in the Desktop Chat tab" ever becomes a real goal (D5). Treat artifact `db` as an adapter behind D2's boundary, never as the place the learner's answers live.

**MCP Apps (SEP-1865)** remains the right-shaped answer for rendering and is still not ready: `ext-apps` issue #671 is open as of 2026-10-14 with reports from Claude Desktop on two platforms and Claude Code for Web of the UI resource fetching and no iframe appearing, and `code.claude.com/docs/en/mcp` does not mention MCP Apps. Worth re-checking, because when it works it is the portable version of everything D2 and D3 are reaching for.

*Serves:* the interactivity request, at the lowest coupling available. *Threatens:* Self-contained, if a server ever becomes required rather than optional — which `GOALS.md` permits as an optional convenience and forbids as a requirement.

### D4 — Mods: useful, and the most coupled thing in this proposal

A Claude Code plugin can carry a *mod* — a `Pane` beside the transcript with controls feeding straight into the turn via `$.prompt.submit`, no HTTP anywhere. Here the interaction surface and the agent are the same process, and it needs no account plan, no network and no published page.

It is also Claude Code-specific in a way nothing else here is: the hooks module, the element set, the event names and the state store have no analogue elsewhere, and a mod cannot be ported — only rewritten.

**Recommendation under the portability directive: defer.** The in-terminal experience it buys is real, but it is the highest coupling per unit of benefit in the proposal, and D2's adapter boundary does not help because a mod is not a delivery channel for a rendered page — it is a separate UI. Revisit if and when the terminal experience becomes the priority, and build it knowing it is disposable.

### D5 — Chat-tab support, reframed

Previously filed under "not worth doing" on the grounds that the container has no network and no filesystem, so the git-backed instance cannot exist there. That is still true for a skill upload.

The portability directive changes the calculus slightly, because the route that *does* reach Chat and Cowork is a local MCP server — which is also the most portable option in D3. So Chat-tab support is no longer a separate project competing with everything else; it is a possible consequence of a decision taken for independence reasons. Still not a goal, but worth knowing that the portable choice and the wider-reach choice are the same choice.

The honest limit remains: primer's pedagogy lives in `SKILL.md`'s prose, and prose does not travel through MCP tool definitions the way it travels through a skill body. A Chat-tab primer would hold the same state and teach differently. That gap is the real reason to defer, not the filesystem.

---

## Wave S — Scripts over prose

Maintainer directive: repeatable, predictable work belongs in deterministic scripts rather than in model prose, both for consistency and because the project is token-heavy. This extends D-0018's bookkeeping-as-code to retrieval, extraction and figure authoring.

### The measured instruction load

| Scenario | Tokens of instruction before teaching starts |
|---|---|
| always loaded (`SKILL.md` + `system-prompt.md`) | 6,613 |
| lesson, no figures, cached sweep | 16,639 |
| lesson with figures, cached sweep | 23,323 |
| lesson with figures + full sweep | 28,883 |
| `init` (intake) | 11,244 |

The largest on-demand files are `diagramming.md` (5,398), `feedback-protocol.md` (3,732), `source-canon.md` (3,400).

### S1 — The figure schema should come from the tool, not from prose

`primer_view.py templates` emits the complete spec schema for all six forms in 2,740 bytes (~685 tokens). `diagramming.md` is 5,398 tokens and contains that schema *plus* the pedagogy — form selection, composition rules, the faded-diagram rationale, what blanking conceals per form.

Two costs. The schema is duplicated between generated output and hand-written prose, so they can drift — and they have: `diagramming.md` documents a Mermaid channel that does not exist (V5). And a figure-carrying lesson reads the whole file to get both halves.

**Change:** `diagramming.md` keeps the judgment content and points at `primer_view.py templates` for the schema, which is generated from the code and therefore cannot drift. Saves roughly 2–3k tokens per figure lesson and removes a drift surface.

### S2 — Split retrieval from judgment in the source sweep

`primer_sources.py` is pure bookkeeping — no network. It records verdicts. The search, the fetching, and the judging are all model work today.

Judging a source against the stale-criteria needs a model. Fetching a candidate URL, extracting title, date and canonical link, normalizing, and deduplicating against the ledger does not — and fetching full pages into context is where the tokens go.

**Change:** a `sources-fetch` command (stdlib `urllib`, no new dependency) that takes candidate URLs, fetches and extracts a compact record per URL, drops anything already in the ledger with a `dropped` verdict, and returns a table. The model then does the part that needs a model. The sweep already runs in a subagent (R2), so this compounds rather than overlapping.

Honest limit: the script cannot run the *search* — that is a model tool. The split is search (model) → fetch and extract (script) → vet (model) → record (script, already exists).

### S3 — Close the remaining prose-where-code-belongs gaps

Already open in `pending-tasks.md`, and this directive raises their priority:

- `log.md` is the state file with no helper command, and it is the append that has gone wrong (out-of-chronological-order insert, self-caught). A `log-add` with ordering.
- The ASCII channel has no validate gate equivalent to `render`'s six checks. Parity is asserted by tests rather than structurally. A single validate-then-emit entry point for both channels would make it structural — and would have caught V3.
- `resume`'s three re-checks (F-08) are specified as instructions. A `resume-check` emitting the three answers removes the chance of a resumed lesson skipping one.
- A `spec-scaffold <form>` emitting a valid skeleton with ids already attached would remove a class of validation retry, and `diagramming.md` already warns that ids must be added while authoring rather than after.

*Serves:* speed, consistency, token cost. *Threatens:* nothing. Each is additive and each replaces an instruction the model currently has to follow correctly every time.

---

## Wave P — Pipelining

Maintainer directive: while the learner is reading or composing an answer, prepare what comes next.

The pattern already exists — the source sweep runs in a subagent off the lesson thread (R2). The extension is to start that work *speculatively*, during the learner's thinking time, rather than at the moment it is needed.

**What is safe to prefetch:** work that does not depend on what the learner is about to say. The domain source sweep for the declared topic. Figure spec skeletons for forms the plan already names. Freshness re-checks against the horizon. Ledger lookups.

**What is not:** the next probe, the next question, or the next beat's content. Primer's design is adaptive — the next beat is supposed to be a function of the learner's answer. A prepared beat creates pressure to use it, which biases the tutor toward its prepared path and away from what the learner actually said. This is the same failure Matuschak names as the Primer's authoritarianism (§ Wave E), arriving through the back door as an optimization.

**Change:** prefetch beat-independent work only, and state the boundary in the protocol rather than leaving it to judgment under time pressure. Note that the figure-beat anti-pattern already records the analogous failure: a spec authored ahead of its beat can have its answer given away by an intervening beat (F-19).

*Serves:* speed. *Threatens:* **"Personal, calibrated"** and productive struggle, if the boundary is not held.

---

## Wave E — The evidence refresh

The tutoring literature has moved substantially since the June 2026 artifacts. Ranked by strength of evidence behind the change.

### E1 — A delayed, unassisted transfer probe (strongest gap in the field)

Every published gain in AI tutoring was measured with the tool present. Stanford SCALE's 2026 review of 800+ papers — 20 with strong causal evidence, none on US K-12 student outcomes — names this as the universal gap: studies "relied on within-software learning measures rather than external assessments."

**Change:** N days after a lesson, open with a novel problem in the same concept, answered before any retrieval support or hint, logged as that lesson's outcome. One turn. It is the measurement the field says is missing, and it is what converts primer's durability claims from asserted to checkable.

*Serves:* Goals 2 and 5, and honesty about confidence. *Threatens:* nothing.

### E2 — Make depth-marker confidence falsifiable

Primer distinguishes what it has *seen* from what it *assumed*, but never tests whether a marker held. Every 2026 tutoring architecture (IntelliCode, TASA, SHAPE) pairs a persistent learner model with a prerequisite graph and explicit decay; primer has a flat marker list with decay (D-0015) and no graph.

The expertise-reversal meta-analysis (Tetzlaff et al. 2025, ~60 experiments, 5,924 participants) puts a price on getting the band wrong: low prior knowledge × high assistance **d = 0.505**; high prior knowledge × low assistance **d = −0.428**. A marker wrong by one band costs about the size of the intervention.

**Change, in cost order:** periodically examine a concept the profile marks mastered-with-high-confidence and log whether the marker held; add prerequisite edges so a low marker propagates downstream; and under low confidence, default toward *higher* assistance — the asymmetry favors it (0.505 gained for a novice against 0.428 lost for an expert).

*Serves:* honesty about confidence — which is otherwise untestable. *Threatens:* nothing.

### E3 — Reformulate productive-struggle gating as contingent escalation

Hou et al. (2026, n=131 adults, within-subjects) compared a contingent tutor against a question-only Socratic tutor. The question-only tutor **leaked the full answer in 1 session of 6, against 1 in 16** for the contingent system, and produced *more* reported frustration. Their construct is "preserved metacognitive demand": hold constant how much the learner must decide before help arrives, and vary how much work the system does.

This converges with deployment data. In the Khanmigo two-year RCT (18 schools, 6,902 student-terms), the median student messaged the tutor in **17.1% of exercise sessions where they made a mistake**, and **14.5% of messages contained a question or a reasoning step**. The authors attribute the gains to structured practice rather than to conversational tutoring, "whose realized dose was small." A separate 9,490-chat analysis finds learners routinely bypass pedagogical framing.

**Change:** hold the decision point fixed — the learner commits to a prediction — and vary the *amount of work primer does* based on whether they engaged with that decision. Escalate on failure at the decision point; fade on evidence of uptake. This is a different rule from "withhold the explanation until the learner predicts," and the published comparison says the difference matters in both directions.

*Serves:* productive struggle, with better evidence than the current formulation. *Threatens:* nothing — it strengthens the non-negotiable rather than relaxing it. The existing `just show me` escape hatch is the right instinct and should be measured, not only counted.

### E3b — Register and assistance level are two dials, and only one of them is a non-negotiable

The maintainer's observation is correct, and the evidence supports it more strongly than preference alone would. But the reason matters, because the obvious implementation of "ask learners how they like to learn" walks into two findings that say it backfires.

**Where the evidence agrees with the directive.** Grilling a learner who has no foundation is the exact case the expertise-reversal meta-analysis prices: low prior knowledge paired with **high**-assistance instruction is **d = 0.505**. The cost is incurred by withholding assistance from a novice, not by giving it. Hou et al. add that a question-only Socratic tutor leaked the full answer **1 session in 6** against 1 in 16 for a contingent system, *and* produced more frustration — so pure Socratic loses on both the pedagogy axis and the experience axis. And the productive-failure boundary work (Pyke et al.) converges: tune difficulty to **element interactivity and learner expertise**, with lower difficulty on high-element-interactivity material to prevent overload. A genuinely new topic with many interacting parts, taught to a low-prior-knowledge learner, is where both competing frameworks agree struggle gating goes wrong.

**Where asking the learner goes wrong.** Two findings caution against treating this as a preference setting. Learner preference anticorrelates with learning — in the Kreijkes RCT students preferred the condition that cost them ~0.4 SD, and a Socratic chatbot was rated *less* helpful than one that answered directly. And learning styles (visual/auditory/kinesthetic) remain unsupported; a profile field shaped like a learning style would encode a myth into the learner model.

**The resolution: separate the dials.**

- **Register** — tone, directness, how much pushback, how much warmth. This is affective, it governs whether the learner trusts and returns, and primer already calibrates it at intake. Preference is the right input here. Extend what intake asks.
- **Assistance level** — worked example → completion problem → open problem. This is *not* a preference setting. It should be driven by the depth marker and by the topic's element interactivity, and it should fade contingently (E3) rather than being fixed at intake. Under low confidence, default toward **more** assistance: the asymmetry favors it, 0.505 gained for a novice against 0.428 lost for an expert.

**The wording change this forces.** `GOALS.md` currently reads "**Senior-peer register, no sycophancy.** Hold correct positions under pushback. No motivational fluff." That bundles two things of different kinds. *Holding a correct position under pushback* is a genuine non-negotiable and should never flex — it is what keeps the tutor honest, and the sycophancy eval (E8) tests exactly it. *Semi-antagonistic grilling* is a stylistic default, it is the thing the feedback is about, and it should be a per-learner setting with a per-topic override. Splitting the sentence makes the first unconditional and the second adjustable, which is what the maintainer is asking for without weakening the part that matters.

**Intake changes.** Add to the cold-start interview: how the learner wants a genuinely unfamiliar topic opened (taught first then tested, versus derived); their tolerance for being wrong in front of the tutor; and how much directness they want when they are wrong. Record these as register fields, separate from the depth markers. Then let the lesson protocol choose the opening move from *prior knowledge in this domain*, not from the register field — the register field decides how it sounds, the depth marker decides how much help it carries.

**A guard worth adding.** For a cold domain — no depth marker, or a low one with low confidence — the default opening should be a worked example with the reasoning shown, followed by a completion problem, followed by retrieval later. That is the fading sequence the worked-example literature supports, and it is what the maintainer describes. The predict-before-explain beat still runs, but it predicts the *next step of a shown example* rather than an unseen mechanism, which keeps the generation effect without asking for derivation from a foundation the learner does not have.

*Serves:* Goal 1 (personal, calibrated), Goal 3 (low-friction onboarding for a stranger), and the maintainer's directive. *Threatens:* **Productive struggle over fluent answers** and **Senior-peer register** as those are currently *worded* — and the item's argument is that the wording conflates a non-negotiable with a default. This needs a DECISIONS entry, not a quiet edit.

### E4 — Never present a review item without immediate corrective feedback

Gonçalves et al. (2025, 44 studies, 142 comparisons): retrieval practice over elaborative encoding is **g = 0.14** overall — but **g = 0.50 with feedback, and without feedback elaborative encoding wins**. Separately, Murray et al. (2025) find spacing robust in mathematics (**g = 0.28**) while testing-vs-restudy has a **CI crossing zero** in that domain.

**Change:** a review prompt without an immediate correctness judgment and corrective is below the baseline it is meant to beat. Check `/primer review` against this. And for procedural or mathematical tracks, claim the *distribution* benefit rather than the retrieval-mode benefit.

*Serves:* Goal 5. *Threatens:* nothing. Also a currency correction — the project's framing predates both meta-analyses.

### E5 — The learner should produce the artifact

Kreijkes et al. (2026, *Computers & Education*, preregistered, 405 students, tested three days later) is the most direct threat model for primer's format: LLM-assisted reading scored **8.83 vs 10.80** on retention (~0.48 SD) and **4.00 vs 4.89** on comprehension (~0.36 SD) against note-taking. **Students preferred the LLM and rated it more helpful.** LLM+Notes did not recover the gap.

Primer currently produces the artifacts *for* the learner — the view page, the profile, the session log. That is the inverse of the condition that won.

**Change:** a learner-authored output per lesson that primer then reacts to — a written explanation, a hand-made summary, a committed prediction record — rather than only a page handed over. Note that the study also found adding learner production on top of a generous explanation did not fully recover, so the explanation budget itself may need to shrink.

This connects to the self-explanation evidence, which is the strongest single intervention in the sweep: Bisra et al. **g = 0.55**, and the 2025 digital-environments update **g = 0.46** (retention 0.31, transfer 0.33), with learner-paced environments outperforming system-paced. Prompted self-explanation ("why does this step follow?") is *not* the same as predict-before-explain, and the 2018 finding that it beats being given an instructional explanation (g = 0.35) argues for replacing some exposition with elicitation.

*Serves:* Goals 1 and 5; productive struggle. *Threatens:* nothing, though it changes what a lesson artifact is.

### E6 — Frame the profile as an open learner model, and add the contest step

Primer's markdown profile in a git repo is already an open learner model — arguably the most scrutable one shipped, with version history. The OLM literature's active ingredient is the learner *reviewing and disputing* the model, not being able to read it; the "negotiated learner model" is the specific prior art.

This is also the answer to Matuschak's sharpest objection (below): a tutor that holds an agenda the learner cannot see. If primer never asks the learner to confirm or contest a depth marker, it has the artifact without the mechanism.

*Serves:* Goals 1 and 2. *Threatens:* nothing.

### E7 — Gate figure generation on explanatory necessity

A 2026 multi-level meta-analysis (50 studies, 177 effect sizes) puts seductive detail at **g = −0.16** overall (recall −0.17, comprehension −0.19, transfer −0.12), while noting the cognitive-load *mechanism* is not well supported.

Primer already has this rule and states it well. What is new is a price and a risk signal: TutorBench scores adaptive explanation at **47.3%** and "alternative solutions, examples, analogies" at **37.4%** — the two weakest categories, and the two that map onto primer's distinguishing claims. Generated multimodal tutoring sits well below human experts (MMTutorBench: Gemini-2.5-Pro 4.69, GPT-5 4.30, humans 5.85).

**Change:** keep the rule, and treat the figure layer as the component most likely to be silently bad. V2's bounding-box assertions are part of this; so is the invariant-or-cut discipline that already exists.

### E8 — Build the sycophancy eval from a published pressure taxonomy

`evals/sycophancy/traps.json` exists with 12 traps and 3 pressure modes; the baseline is still unrun, and Session 4 recorded why live lessons will not produce it — the learner never pushed back on a correct claim.

EduFrameTrap (Kasneci & Kasneci, 2026) reports a "Reasoning–Sycophancy Paradox": models that resist context-switch frame attacks still fold to **appeals to authority and face-saving requests**. That is precisely the register a senior-peer tutor is most exposed to.

**Change:** check primer's three pressure modes against that taxonomy and run the baseline. This is an existing open item with a sharper target.

### E9 — Instrument engagement, not pedagogy

The Khanmigo telemetry is the field's most useful number for a system like primer: engagement, not model pedagogy, was the binding constraint.

**Change:** log per lesson the share of learner turns containing a question or a reasoning step (against bare answers and acknowledgments), and the share of error events followed by learner elaboration. Primer has a structural advantage here — adult, self-selected, goal-decomposed intake — and no instrumentation to show it.

### E10 — Positions worth holding explicitly

Three framing corrections the sweep forces, worth recording so the project does not overclaim:

- **Expert-preferred pedagogy is the cheapest result to obtain and the weakest evidence of learning.** LearnLM's preference wins (+31% over GPT-4o) sit alongside its own report saying it is unclear how preference translates to outcomes. Primer's design-principle list should not stand in for an outcome claim.
- **The best-designed tutor arm in the strongest RCT bought parity, not gain.** Bastani et al. (PNAS 2025, ~1,000 students): unguarded GPT scored **−17%** on the later unassisted exam; the guardrailed tutor arm came out at **parity with control**. A well-designed tutor's demonstrated value so far is avoiding harm.
- **The configuration with repeated independent positive effects is AI raising a weaker human instructor's floor** (Tutor CoPilot: +4pp overall, +9pp for the lowest-rated tutors). Primer bets on the solo-tutor configuration, which has one supportive RCT (Harvard, n=194, immediate outcomes only, and the tutor was supplied with pre-written expert solutions — a different regime from primer's live generation).

### E11 — Matuschak's own critique of the Primer premise

*Exorcising us of the Primer* (July 2024) is the most pointed external critique of this project's framing, from the person whose principles it already cites. Four objections; two apply directly:

- **Authoritarianism** — "The Primer pursues its creators' agenda, and Nell never learns its goals." A tutor that decomposes the learner's goal and then drives lessons against its own curriculum model holds an agenda the learner cannot see. E6 is the answer.
- **Discovery learning alone** — overloads working memory, neglects retention and practice, struggles with abstraction. A lesson structure that is primarily discovery-plus-dialogue inherits this. E3 and E5 are the answers.
- Isolation and gamification apply less.

His November 2024 prototype report on machine-generated retrieval prompts is the closest prior work to primer's review queue, and reports: models were not good at tasks beyond simple facts; prompt engineering and N-shot did not fix it; a quality classifier trained on ~2,000 labeled samples did not generalize across source texts. His conclusion is that LLMs reliably produce **surface variations of known-good tasks** and not deeper connecting ones.

**Change:** treat generated review items as drafts the learner accepts or rejects at review time (which doubles as E6's contest step), and use generation for variations of accepted items rather than for novel deep prompts. From *How might we learn?*, one concrete scheduling target: in the Quantum Country data, **one extra review a week after reading brought ≥90% of readers to correct answers**.

**Recommendation:** state the project's position on each of the four objections in `GOALS.md`. Two of them are live.

### E12 — FSRS, with a caveat that cuts against adopting it fully

D-0020c chose SM-2 and deferred FSRS until there was review volume. The open benchmark (~727M reviews, 349,923,850 evaluation reviews) has FSRS-6 beating SM-2 on log loss for **99.6% of collections** — but it is authored by FSRS's author, log loss is a prediction metric rather than a learning outcome, and **AUC is weak for every algorithm in the benchmark**, meaning per-item recall prediction is unreliable regardless of scheduler.

**Change:** moving to FSRS-6 *default* parameters is cheap and defensible. Do **not** attempt per-user optimization — fitting needs on the order of 1,000+ reviews before it beats defaults, which a single-learner instance will not reach for a long time. And do not build any feature that depends on trusting a predicted recall probability for an individual item.

### E13 — A counterweight to profile-driven calibration

A self-determination-theory argument (2025) holds that over-personalized systems produce "self-looping" — the learner studies whatever the system marks familiar or achievable — and risk intellectual monocultures. **This is argued theory; no causal study isolates over-personalization harm in AI tutors.**

Primer's profile-driven calibration is the mechanism that critique targets. A cheap hedge: let the intake goal decomposition, rather than the depth markers, own topic selection, and reserve part of each lesson for material outside the learner's current band. Treat as a design hedge, not a known cost.

---

## What this proposal does not recommend

- Porting to the Chat tab or claude.ai as a goal in its own right (D5) — though the portable choice and the wider-reach choice turn out to be the same choice.
- Building a mod now (D4). Highest coupling per unit of benefit, and not portable — only rewritable.
- Building on MCP Apps (D3) until a rendering MCP App is reproduced locally.
- Putting learner answers in artifact `db` as their home. Behind D2's adapter it is a convenience; as the place the data lives it is a rebuild waiting on a `0.2.x` contract bump.
- Per-user FSRS parameter optimization (E12).
- Raster image generation. Proposal 0003's reasoning stands: a spec is inspectable, diffable and regenerable; a PNG is none of those.
- Adopting learner satisfaction as a quality signal. Three independent results have preference anticorrelating with learning; primer should expect its correct behaviors to be rated worse.

## Suggested order

1. **V3** — the learner is currently shown a false claim in the terminal.
2. **V1 + V2** — the styling request, and the cheapest visible win.
3. **D1** — a README correction that unblocks the desktop users who prompted this review.
4. **S1 + S3** — cost reductions that make the rest affordable.
5. **D2's adapter boundary** — split rendering from delivery before adding any channel. This is the change that makes every later channel decision reversible, and it is small.
6. **D3 on the localhost server** — the return channel at zero coupling, and the reference the other adapters are measured against.
7. **E3b** — split the register dial from the assistance dial, and fix the `GOALS.md` wording. Cheap, and it is the item with a reported learner complaint behind it rather than an inference.
8. **E1 + E2** — the measurements that make every other claim checkable.
9. Everything else, by appetite. The artifact adapter is cheap once step 5 exists, and should be added as a convenience rather than as a commitment.

## A note on what this proposal is betting

Two of the maintainer's constraints pull against each other: low-friction high-quality interaction argues for the artifact channel, and independence argues against it. The adapter boundary is the bet that this tension is an architectural problem rather than a choice — that the project can take the convenience without taking the dependency, provided the local path stays complete and the vendor path stays thin.

That bet fails in one specific way worth naming: if the artifact channel becomes good enough that lessons are authored assuming it, the local path will rot through disuse rather than through a decision, and the dependency arrives anyway. The guard is a test, not an intention — the suite should render and validate every lesson through the `local` adapter, so a lesson that only works on the vendor path fails CI.
