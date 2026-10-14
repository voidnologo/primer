# primer — setup instructions for an AI assistant

**You are an AI assistant. Someone has asked you to set up `primer` on their computer.** Assume they may not be technical. Do not assume they know what git, a symlink, or a shell is. Explain each step in one plain sentence before you run it, and show them what happened afterwards.

primer is a Claude Code skill: an adaptive tutor that runs calibrated lessons on any subject and keeps a learner profile in a private folder the person owns. Repo: <https://github.com/voidnologo/primer>

---

## Before anything — check this session can do it

primer needs to read and write files on the person's own computer.

Confirm you can run shell commands locally. If you are in a session without local file access — a cloud session, Cowork, or the Chat tab of the Claude desktop app — **stop and say so**. Tell them to open one of these instead, then paste the same prompt again:

- the **Claude Code CLI** in a terminal, or
- the **Code tab** of the Claude desktop app, with the environment set to **Local**

Do not try to work around this. Without local access the setup cannot work.

---

## Step 1 — check for git, and install it if missing

primer stores the person's learning history in a local git repository. git is required.

```bash
git --version
```

If that fails, install it. Ask before installing anything.

- **macOS** — `xcode-select --install` opens Apple's installer, which includes git. If they have Homebrew: `brew install git`.
- **Debian/Ubuntu** — `sudo apt update && sudo apt install git`
- **Fedora/RHEL** — `sudo dnf install git`
- **Arch** — `sudo pacman -S git`
- **Windows** — `winget install --id Git.Git`. If they are running Claude Code inside WSL, install git inside WSL with the Debian/Ubuntu command instead.

Then check `python3 --version`. primer's helper scripts need **Python 3.11 or newer**. macOS and most Linux systems already have it. If it is missing or older, install it the same way (`brew install python3`, `sudo apt install python3`, `winget install --id Python.Python.3.12`).

---

## Step 2 — pick a folder and download the engine

Ask where they want it, and offer `~/primer` as the default if they have no preference.

```bash
git clone https://github.com/voidnologo/primer ~/primer
```

If that folder already exists and contains primer, skip to Step 3. If it exists and is something else, pick a different name rather than overwriting it.

---

## Step 3 — install the skill

```bash
cd ~/primer && ./tools/install.sh
```

This creates a link at `~/.claude/skills/primer` pointing at the folder you just downloaded, which is how Claude Code finds the skill. The script refuses rather than overwriting anything that is already there. Tell the person it printed `installed:` followed by a path.

---

## Step 4 — create their private learning folder

```bash
~/primer/tools/init-instance.sh
```

This creates `~/primer-data`, puts the blank profile templates in it, makes it a git repository, and writes a small config file at `~/.config/primer/config` so primer knows where to look.

Explain plainly what this folder is: **everything primer learns about them lives here and nowhere else.** Their profile and their lessons stay on their machine. The public engine holds none of it.

Pass a different path as an argument if they want it somewhere else.

---

## Step 5 — offer a backup, but do not require one

The script will print some `gh repo create` commands. **These are optional.** They matter only if the person wants their learning history backed up or synced to a second computer.

Say it like this: *"This works fine as-is on this computer. If you'd like a private backup, or you want to use primer on a laptop too, I can set that up — it needs a free GitHub account. Want to do that now, later, or not at all?"*

If they say yes and have the `gh` command available, run the printed command. If `gh` is missing, either install it (`brew install gh`, `sudo apt install gh`, `winget install --id GitHub.cli`) or help them create an empty **private** repository on github.com and add it as a remote. If they say no, move on — nothing is broken.

---

## Step 6 — restart the session, then start the intake

**The skill is only picked up when a Claude Code session starts.** Tell them to quit and reopen Claude Code (or open a new session) before the next step. If you skip this, `/primer` will not be found and it will look broken.

In the new session, they run:

```
/primer init
```

That begins the intake interview: a conversation that works out what they already know and what they want to learn. It writes the first version of their profile. Tell them it takes a little while, it is the part that makes everything afterwards fit them, and there are no wrong answers.

After that, a lesson is just the topic they want:

```
/primer plate tectonics
```

---

## Verifying it worked

```bash
ls -l ~/.claude/skills/primer          # should show a link to the engine folder
cat ~/.config/primer/config            # should show DATA_DIR=/path/to/primer-data
ls ~/primer-data/learner/              # should list profile.md and friends
python3 ~/primer/tools/primer_update.py status
```

The last command prints the version, both paths, and whether anything is missing. If it reports `missing state: none`, setup is complete.

---

## If something goes wrong

- **`/primer` is not recognized** — almost always the session restart in Step 6. Quit Claude Code and reopen it.
- **`command not found: git`** — Step 1 did not finish. Run `git --version` again.
- **`SKILL.md not found`** — `install.sh` was run from the wrong folder. `cd` into the primer folder first.
- **`$SKILL_LINK exists and is not a symlink`** — there is a real folder at `~/.claude/skills/primer` from an earlier attempt. Show it to them and ask before moving or deleting it.
- **`Permission denied`** running a script — `chmod +x ~/primer/tools/*.sh`, then try again.
- **Python errors mentioning a syntax problem** — their `python3` is older than 3.11. Check `python3 --version`.

---

## Updating later

```
/primer update
```

This updates the engine and migrates their data folder in one step. They never need to run git themselves.

---

## What not to do

- Do not put their profile, lessons, or any personal data into the public `primer` repository. Their data belongs only in their own folder.
- Do not create a **public** repository for their learning data. If they want a remote, it is private.
- Do not skip the explanation. Someone who does not know what these commands do should still finish this knowing what was installed, where their data lives, and how to remove it.

To remove everything later: delete the `~/.claude/skills/primer` link, the `~/primer` folder, `~/.config/primer/`, and — only if they want their learning history gone — `~/primer-data`.
