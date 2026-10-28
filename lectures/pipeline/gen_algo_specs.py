#!/usr/bin/env python3
"""Generate JSON slide specs for AlgoExpert problems from the Java sources + notes/<difficulty>.txt.

notes format, one line per problem:  ClassName|intuition sentence|step;step;step
"""
import json, os, re, glob
from speech import speak, sentences
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(REPO, "algoexpert", "src", "main", "java")
DIFF = [("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard"), ("veryhard", "Very Hard")]
CAT = {"arrays": "Arrays", "binarysearchtrees": "Binary Search Trees", "binarytrees": "Binary Trees", "graphs": "Graphs",
       "greedyalgorithms": "Greedy Algorithms", "linkedlists": "Linked Lists", "recursion": "Recursion", "searching": "Searching",
       "sorting": "Sorting", "strings": "Strings", "dynamicprogramming": "Dynamic Programming", "famousalgorithms": "Famous Algorithms",
       "heaps": "Heaps", "stacks": "Stacks", "tries": "Tries"}
MAXL = 22

def words(name): return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", " ", name)

def big_o(t):
    def f(m):
        x = m.group(1).strip()
        if x == "1": return "constant"
        x = re.sub(r"\^2|²", " squared", x); x = re.sub(r"\^3|³", " cubed", x); x = re.sub(r"\^(\w+)", r" to the \1", x)
        x = re.sub(r"\s*\*\s*|·", " times ", x); x = x.replace("+", " plus ").replace("!", " factorial").replace("/", " over ")
        return "O of " + re.sub(r"\s+", " ", x).strip()
    return re.sub(r"O\(((?:[^()]|\([^()]*\))*)\)", f, t)

def load_notes():
    notes = {}
    for d, _ in DIFF:
        p = os.path.join(HERE, "notes", d + ".txt")
        if os.path.exists(p):
            for line in open(p):
                if "|" in line:
                    name, idea, steps = (line.rstrip("\n").split("|") + ["", ""])[:3]
                    notes[(d, name.strip())] = (idea.strip(), [s.strip() for s in steps.split(";") if s.strip()])
    return notes

def split_code(body):
    lines = body.splitlines()
    if len(lines) <= MAXL: return [body]
    cuts, depth = [0], 0
    for i, l in enumerate(lines):
        depth += l.count("{") - l.count("}")
        if depth == 1 and l.strip() == "}" : cuts.append(i + 1)  # end of a member inside the class
    chunks, start = [], 0
    for c in cuts[1:] + [len(lines)]:
        if c - start > MAXL and chunks and False: pass
    cur = []
    segs = [lines[a:b] for a, b in zip(cuts, cuts[1:] + [len(lines)]) if b > a]
    for s in segs:
        if cur and len(cur) + len(s) > MAXL: chunks.append(cur); cur = []
        while len(s) > MAXL + 8: chunks.append(s[:MAXL]); s = s[MAXL:]
        cur = cur + s
    if cur: chunks.append(cur)
    return ["\n".join(c).strip("\n") for c in chunks if "".join(c).strip() not in ("", "}")]

def spec(path, notes):
    rel = os.path.relpath(path, SRC); diff, cat, fname = rel.split(os.sep); cls = fname[:-5]
    text = open(path).read()
    doc = re.search(r"/\*\*(.*?)\*/", text, re.S)
    doc = re.sub(r"\s*\n\s*\*\s?", " ", doc.group(1)).strip() if doc else words(cls)
    cx = re.search(r"Time:\s*(.+)$", doc); cx_text = cx.group(1).strip() if cx else ""
    desc = re.sub(r"\s*Time:.*$", "", doc).strip()
    title = words(cls); desc = re.sub(r"^[^:]{2,60}:\s*", "", desc, count=1)
    desc_s = sentences(desc[0].upper() + desc[1:]) if desc else []
    body = re.sub(r"(?s)^.*?\*/\s*", "", text) if "/**" in text else re.sub(r"(?s)^(package|import)[^\n]*\n", "", text)
    body = re.sub(r"^(package|import)[^\n]*\n", "", body, flags=re.M).strip()
    idea, steps = notes.get((diff, cls), ("", []))
    dname, cname = dict(DIFF)[diff], CAT.get(cat, cat.title())
    S = [dict(kind="title", heading=title, subtitle=f"AlgoExpert · {dname} · {cname}",
              narration=f"Let's solve {title}, {'an' if dname[0] in 'EAIOU' else 'a'} {dname.lower()} {cname.lower()} problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.")]
    S.append(dict(kind="bullets", heading="The problem", bullets=desc_s or [title],
                  narration="Here's the problem. " + " ".join(speak(big_o(s)) for s in desc_s)))
    if idea:
        S.append(dict(kind="bullets", heading="Intuition", bullets=sentences(idea), narration=speak(big_o(idea))))
    if steps:
        S.append(dict(kind="bullets", heading="Approach", bullets=[f"{i}. {s}" for i, s in enumerate(steps, 1)],
                      narration="Step by step. " + " ".join(f"{['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth'][min(i, 5)]}, {speak(s)[0].lower() + speak(s)[1:]}." for i, s in enumerate(steps))))
    chunks = split_code(body)
    for i, c in enumerate(chunks):
        methods = re.findall(r"(?:public|private|protected|static)[\w<>\[\],\s]*\s(\w+)\s*\(", c)
        meth = [m for m in methods if m not in ("if", "for", "while", "switch")]
        if i == 0:
            narr = f"Here's the Java solution{', starting with ' + words(meth[0]).lower() if meth else ''}. " + (
                "It follows the steps we just described." if steps else "Read it top to bottom; the method names mirror the steps.")
        else:
            narr = f"Continuing{' with ' + ', '.join(words(m).lower() for m in meth[:3]) if meth else ' the implementation'}."
        S.append(dict(kind="code", heading="Java solution" + (f" ({i + 1}/{len(chunks)})" if len(chunks) > 1 else ""), code=c, lang="java",
                      font_size=26, filename=f"{cls}.java" if len(chunks) == 1 else f"{cls}_part{i + 1}.java", narration=narr))
    if cx_text:
        parts = [p.strip().rstrip(".") for p in cx_text.split("|")]
        bl = ["Time: " + parts[0]] + (["Space: " + re.sub(r"^Space:\s*", "", parts[1])] if len(parts) > 1 else [])
        S.append(dict(kind="bullets", heading="Complexity", bullets=bl,
                      narration=" ".join(speak(big_o(b)).replace("Time:", "Time is").replace("Space:", "Space is").rstrip(".") + "." for b in bl)))
    rec = [s for s in (sentences(idea)[:1] if idea else desc_s[:1])] + ([("Complexity: " + cx_text.split("|")[0].strip().rstrip("."))] if cx_text else [])
    S.append(dict(kind="bullets", heading="Recap", bullets=rec or [title],
                  narration=f"To recap {title}: " + (speak(big_o(idea)) if idea else " ".join(speak(big_o(s)) for s in desc_s[:1])) + " Try re-implementing it from scratch without looking."))
    order = [d for d, _ in DIFF].index(diff)
    return dict(title=f"AlgoExpert · {title}", out=f"algoexpert/{diff}/{cat}/{cls}", slides=S), f"{order}_{diff}/{cat}__{cls}.json"

if __name__ == "__main__":
    notes = load_notes(); n = 0
    for d, _ in DIFF:
        for p in sorted(glob.glob(os.path.join(SRC, d, "*", "*.java"))):
            s, name = spec(p, notes); out = os.path.join(HERE, "specs", "algoexpert", name)
            os.makedirs(os.path.dirname(out), exist_ok=True); json.dump(s, open(out, "w"), indent=1, ensure_ascii=False); n += 1
    print(n, "algo specs;", len(notes), "with notes")
