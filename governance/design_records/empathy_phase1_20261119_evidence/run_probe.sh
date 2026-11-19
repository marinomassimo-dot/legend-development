#!/bin/sh
# usage: run_probe.sh NAME PROMPTFILE  (cwd = clean detached checkout; auto memory disabled; read-only tools)
cd /home/desktop/legend-development/.claude/worktrees/he_probe_e1
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 claude -p --model sonnet --effort medium --tools Read,Grep,Glob --max-turns 30 --output-format json --no-session-persistence "$(cat $2)" > <scratch>/$1.json 2> <scratch>/$1.err
echo "exit=$?" > <scratch>/$1.exit
