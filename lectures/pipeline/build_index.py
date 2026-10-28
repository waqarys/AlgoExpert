#!/usr/bin/env python3
"""Regenerate lectures/README.md: an index of every built lecture."""
import os, re, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SECTIONS = [("mlexpert", "MLExpert"), ("systemsexpert", "SystemsExpert"), ("algoexpert", "AlgoExpert")]

def dur(p):
    s = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]))
    return f"{int(s // 60)}:{int(s % 60):02d}"

lines = ["# Video lectures", "",
         "Narrated lectures (720p MP4) with reusable slide assets for recording your own videos: "
         "`slides/NN.png` (1920x1080), `slides.pdf`, `transcript.md` (narration per slide) and `code/` snippets.",
         "Built with [`pipeline/`](pipeline/README.md).", ""]
for key, name in SECTIONS:
    base = os.path.join(ROOT, key)
    items = sorted(dp for dp, _, fs in os.walk(base) if "transcript.md" in fs and "slides.pdf" in fs) if os.path.isdir(base) else []
    if key == "algoexpert":
        order = {"easy": 0, "medium": 1, "hard": 2, "veryhard": 3, "very_hard": 3}
        items.sort(key=lambda p: (order.get(os.path.relpath(p, base).split(os.sep)[0], 9), p))
    lines += [f"## {name} ({len(items)})", "", "| Lecture | Length | Video | Slides | Transcript |", "|---|---|---|---|---|"]
    for d in items:
        rel = os.path.relpath(d, ROOT)
        t = open(os.path.join(d, "transcript.md")).readline().lstrip("# ").strip()
        t = re.sub(r"^\w+Expert · ", "", t)
        if key == "algoexpert": t = f"{rel.split('/')[1]} / {rel.split('/')[2]} / {t}"
        lines.append(f"| {t} | {dur(os.path.join(d, 'lecture.mp4'))} | [mp4]({rel}/lecture.mp4) | [pdf]({rel}/slides.pdf) | [md]({rel}/transcript.md) |")
    lines.append("")
open(os.path.join(ROOT, "README.md"), "w").write("\n".join(lines))
print("index updated")
