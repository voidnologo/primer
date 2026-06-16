#!/usr/bin/env bash
# Install the primer skill into ~/.claude/skills/ via symlink.
# The repo IS the skill dir — this just makes Claude Code find it.
# The skill's command name is the symlink name (primer -> /primer).

set -euo pipefail

REPO_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/.." &> /dev/null && pwd )"
SKILL_LINK="$HOME/.claude/skills/primer"
LEGACY_LINK="$HOME/.claude/skills/learn-me-up"

if [[ ! -f "$REPO_DIR/SKILL.md" ]]; then
  echo "error: $REPO_DIR/SKILL.md not found — are you running from the repo?" >&2
  exit 1
fi

mkdir -p "$HOME/.claude/skills"

# Clean up the pre-rename symlink if present.
if [[ -L "$LEGACY_LINK" ]]; then
  echo "removing legacy symlink: $LEGACY_LINK -> $(readlink "$LEGACY_LINK")"
  rm "$LEGACY_LINK"
fi

if [[ -L "$SKILL_LINK" ]]; then
  existing="$(readlink "$SKILL_LINK")"
  if [[ "$existing" == "$REPO_DIR" ]]; then
    echo "already installed: $SKILL_LINK -> $existing"
    exit 0
  fi
  echo "removing stale symlink: $SKILL_LINK -> $existing"
  rm "$SKILL_LINK"
elif [[ -e "$SKILL_LINK" ]]; then
  echo "error: $SKILL_LINK exists and is not a symlink. Refusing to clobber." >&2
  exit 1
fi

ln -s "$REPO_DIR" "$SKILL_LINK"
echo "installed: $SKILL_LINK -> $REPO_DIR"
echo
echo "First time? Run: /primer init"
echo "Otherwise:    /primer index"
