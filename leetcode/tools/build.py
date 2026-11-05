#!/usr/bin/env python3
"""Extract Java sources/tests from content/*/explanation.md and render slides.

Each explanation.md has:  # NNNN. Title  /  a meta line  /  ## sections  /
```java file=<pkg>/<Class>.java``` (solution) and ```java test=<pkg>/<Class>Test.java``` blocks.
Usage: python build.py [--slides] [slug-filter]
"""
import os, re, sys, glob, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); LC = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(LC, "..", "lectures", "pipeline"))
BLOCK = re.compile(r"```java (file|test)=(\S+)\n(.*?)```", re.S)

def parse(md):
    text = open(md).read()
    title = re.search(r"^# (.+)$", text, re.M).group(1)
    meta = re.search(r"^\*\*Difficulty:\*\*.*$", text, re.M).group(0).replace("**", "")
    secs = {}
    for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        secs[m.group(1).strip()] = m.group(2).strip()
    return text, title, meta, secs

def extract(text):
    out = []
    for kind, rel, body in BLOCK.findall(text):
        base = "main" if kind == "file" else "test"
        p = os.path.join(LC, "java", "src", base, "java", rel)
        os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w").write(body)
        out.append((kind, rel, body))
    return out

def bullets_of(s):
    items, cur = [], None
    for line in s.splitlines():
        if line.startswith("```"): break
        t = re.sub(r"[*`]", "", line).strip()
        if not t: cur = None; continue
        if re.match(r"^([-*]|\d+\.)\s", line.strip()):
            t = re.sub(r"^([-*]|\d+\.)\s+", "", re.sub(r"[`*]", "", line.strip())); items.append(t); cur = len(items) - 1
        elif cur is not None: items[cur] += " " + t
        else: items.append(t); cur = len(items) - 1
    return [i.replace("$", r"\$") for i in items]

def fenced(s):
    m = re.search(r"```(?:text)?\n(.*?)```", s, re.S); return m.group(1) if m else None

def strip_doc(code):
    code = re.sub(r"[ \t]*/\*\*.*?\*/\n", "", code, flags=re.S)
    return re.sub(r"^(package|import) .*\n", "", code, flags=re.M).strip("\n")

def chunks(code, n=34):
    lines = code.splitlines(); out, cur = [], []
    for l in lines:
        cur.append(l)
        if len(cur) >= n and (l.strip() == "}" or l.strip() == ""): out.append("\n".join(cur)); cur = []
    if any(x.strip() for x in cur): out.append("\n".join(cur))
    return out

def slides(md):
    import make_lecture as ml
    from PIL import Image
    text, title, meta, secs = parse(md)
    sol = [b for k, r, b in BLOCK.findall(text) if k == "file"]
    S = [dict(kind="title", heading=title, subtitle=meta)]
    for name in ["Problem", "Intuition", "Brute Force", "Optimal Approach"]:
        if name in secs: S.append(dict(kind="bullets", heading=name, bullets=bullets_of(secs[name])))
    if "Worked Example" in secs:
        pre = bullets_of(secs["Worked Example"]); f = fenced(secs["Worked Example"])
        if f: S.append(dict(kind="code", heading="Worked Example", code="\n".join(p.replace("\\$", "$") for p in pre) + "\n\n" + f, lang="text", font_size=26))
        elif pre: S.append(dict(kind="bullets", heading="Worked Example", bullets=pre))
    for i, c in enumerate(chunks(strip_doc(sol[0])) if sol else []):
        S.append(dict(kind="code", heading="Java Solution" + (f" ({i+1})" if i else ""), code=c, lang="java", font_size=24))
    for name in ["Complexity", "Pitfalls", "Key Takeaway"]:
        if name in secs: S.append(dict(kind="bullets", heading=name, bullets=bullets_of(secs[name])))
    d = os.path.join(os.path.dirname(md), "slides"); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    paths = []
    for i, s in enumerate(S, 1):
        p = os.path.join(d, f"{i:02d}.png"); ml.render(s, p, i, len(S), title); paths.append(p)
    ims = [Image.open(p).convert("RGB") for p in paths]
    ims[0].save(os.path.join(os.path.dirname(md), "slides.pdf"), save_all=True, append_images=ims[1:], resolution=150)

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    mds = sorted(glob.glob(os.path.join(LC, "content", "*", "explanation.md")))
    if args: mds = [m for m in mds if any(a in m for a in args)]
    for md in mds:
        extract(open(md).read())
        if "--slides" in sys.argv:
            slides(md); print("slides", os.path.basename(os.path.dirname(md)), flush=True)
main()
