#!/bin/bash
# usage: tools/ship.sh "commit msg" — renders slides for problems missing slides.pdf, rebuilds index, commits, pushes (with retries)
cd "$(dirname "$0")/.." || exit 1
todo=$(for d in content/*/; do [ -f "$d/slides.pdf" ] || basename "$d"; done)
[ -n "$todo" ] && python3 tools/build.py --slides $todo | wc -l
python3 tools/index.py
git add . && git commit -qm "$1"
for i in 1 2 3 4 5; do git push -q origin leetcode 2>&1 && break; sleep 10; done
git log origin/leetcode --oneline -1
