import sys, os
f = None
for line in sys.stdin:
    if line.startswith("@@@ "):
        p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", line[4:].strip(), "explanation.md")
        os.makedirs(os.path.dirname(p), exist_ok=True); f = open(p, "w"); continue
    if f: f.write(line)
