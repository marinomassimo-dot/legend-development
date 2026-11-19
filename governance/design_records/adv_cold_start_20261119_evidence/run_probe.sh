#!/bin/sh
# usage: run from a clean detached checkout of main; auto memory disabled; read-only tools
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude -p --model sonnet --effort medium --tools Read,Grep,Glob --max-turns 30 --output-format json --no-session-persistence "$(cat "$1")"
