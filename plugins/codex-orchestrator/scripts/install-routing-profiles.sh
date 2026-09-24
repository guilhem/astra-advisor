#!/bin/sh
set -eu

codex_home=${CODEX_HOME:-"$HOME/.codex"}
case "$codex_home" in
  '~') codex_home=$HOME ;;
  '~/'*) codex_home=$HOME/${codex_home#\~/} ;;
esac
destination=$codex_home/subagent-router
mkdir -p "$destination"

for profile in "${PLUGIN_ROOT:?}/routing"/codex-orchestrator-*.json; do
  target=$destination/${profile##*/}
  if [ ! -e "$target" ] && [ ! -L "$target" ]; then
    cp -n "$profile" "$target"
  fi
done
