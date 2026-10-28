#!/usr/bin/env python3
"""Build specs in order, in groups; commit after each group and push in the background (never force)."""
import glob, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PY = sys.executable; GROUP = 16
specs = sorted(glob.glob(f"{HERE}/specs/mlexpert/*.py")) + sorted(glob.glob(f"{HERE}/specs/systemsexpert/*.json")) + \
        sorted(glob.glob(f"{HERE}/specs/algoexpert/*/*.json"))
push = None
def build(f):
    r = subprocess.run([PY, "make_lecture.py", "--skip-existing", f], cwd=HERE, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    if out: print(out, flush=True)
for i in range(0, len(specs), GROUP):
    grp = specs[i:i + GROUP]
    with ThreadPoolExecutor(8) as ex: list(ex.map(build, grp))
    subprocess.run([PY, "build_index.py"], cwd=HERE, capture_output=True)
    subprocess.run(["git", "add", "lectures"], cwd=REPO)
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO).returncode:
        done = len(glob.glob(f"{REPO}/lectures/**/transcript.md", recursive=True))
        subprocess.run(["git", "commit", "-qm", f"Lectures: batch up to {os.path.basename(grp[-1])} ({done} lectures total)"], cwd=REPO)
        print(f"COMMIT {done} lectures, last={grp[-1]}", flush=True)
    if push is None or push.poll() is not None:
        push = subprocess.Popen(["git", "push", "-q", "origin", "lectures-pilot"], cwd=REPO)
if push: push.wait()
subprocess.run(["git", "push", "-q", "origin", "lectures-pilot"], cwd=REPO)
print("ALL DONE", flush=True)
