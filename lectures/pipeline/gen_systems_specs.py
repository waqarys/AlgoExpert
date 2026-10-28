#!/usr/bin/env python3
"""Generate JSON slide specs for SystemsExpert from systemsexpert/*.md (narration derived from the notes)."""
import json, os, re, glob
from speech import speak, clean, sentences
from enrich.systems import D as ENRICH
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
OUTD = os.path.join(HERE, "specs", "systemsexpert"); os.makedirs(OUTD, exist_ok=True)
MAXB = 6
end = lambda t: t if t.endswith(('.', '?', '!')) else t + '.'

def chunks(items, n=MAXB, budget=9.0, width=74):
    """Split bullets so each slide fits at >= 20pt (about 74 chars per line, ~9 lines)."""
    out, cur, used = [], [], 0.0
    for b in items:
        cost = -(-len(b) // width) + 0.45
        if cur and (used + cost > budget or len(cur) >= n): out.append(cur); cur, used = [], 0.0
        cur.append(b); used += cost
    if cur: out.append(cur)
    return out or [[]]

def mermaid_edges(src):
    labels, edges = {}, []
    node = r"([A-Za-z0-9_]+)\s*(\[\[.*?\]\]|\[\(.*?\)\]|\[.*?\]|\(.*?\))?"
    for line in src.splitlines():
        line = line.strip()
        if not line or line.startswith(("flowchart", "graph", "subgraph", "end", "%%")): continue
        parts = re.split(r"\s*(?:<-->|-->|---|-\.->|==>)(?:\|[^|]*\|)?\s*", line)
        ids = []
        for p in parts:
            m = re.match(node, p.strip())
            if not m: continue
            nid, lab = m.group(1), m.group(2)
            if lab: labels[nid] = re.sub(r"^[\[\(]+|[\]\)]+$", "", lab).strip()
            ids.append(nid)
        edges += [(a, b) for a, b in zip(ids, ids[1:])]
    name = lambda i: labels.get(i, i)
    return [[name(a), name(b)] for a, b in edges]

def parse(md):
    """-> title, intro, [(section, sub, kind, payload)] where kind in bullets/code/mermaid/para."""
    lines = md.splitlines(); title = clean(lines[0].lstrip("# ")); blocks = []; sec = sub = None; fence = None; buf = []
    label = None
    for line in lines[1:]:
        if fence is not None:
            if line.startswith("```"):
                blocks.append((sec, sub, "mermaid" if fence == "mermaid" else "code", "\n".join(buf))); fence = None; buf = []
            else: buf.append(line)
            continue
        if line.startswith("```"): fence = line[3:].strip(); buf = []; continue
        if line.startswith("## "): sec, sub, label = re.sub(r"^\d+\.\s*", "", line[3:]).strip(), None, None; continue
        if line.startswith("### "): sub, label = line[4:].strip(), None; continue
        if sec is None: continue
        m = re.match(r"^\*\*(.+?)\*\*\s*$", line.strip())
        if m: label = m.group(1); continue
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", line):
            blocks.append((sec, sub or label, "bullets", [clean(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line))]))
        elif line.strip() and not line.startswith(">") and not line.startswith("|"):
            blocks.append((sec, sub or label, "para", clean(line)))
    merged = []
    for b in blocks:  # merge consecutive bullets/paras under the same heading
        if merged and tuple(merged[-1][:2]) == tuple(b[:2]) and b[2] in ("bullets", "para") and merged[-1][2] == "bullets":
            merged[-1][3].extend(b[3] if b[2] == "bullets" else sentences(b[3]))
        else:
            merged.append([b[0], b[1], "bullets" if b[2] in ("bullets", "para") else b[2],
                           (b[3] if b[2] == "bullets" else sentences(b[3])) if b[2] in ("bullets", "para") else b[3]])
    return title, merged

INTRO = {"Clarifying questions": "Start by clarifying the scope with your interviewer. Good questions here are:",
         "Requirements": "Next, pin down the requirements.",
         "Capacity estimates": "Now some rough capacity estimates, which drive the design.",
         "Entities": "Here are the core entities.", "Data model": "Here is the data model.",
         "Deep dives": "Let's go deeper on one of the hard parts:", "Trade-offs & alternatives": "Finally, the key trade-offs.",
         "Trade-offs": "Finally, the key trade-offs."}

def endpoint_speech(code):
    eps = []
    for l in code.splitlines():
        m = re.match(r"\s*(GET|POST|PUT|PATCH|DELETE|WS|WSS)\s+(\S+)", l)
        if m:
            path = re.sub(r"\{(\w+)\}", r"by \1", m.group(2)).replace("/", " ").replace("_", " ").replace("?", " with ").strip()
            eps.append(f"{m.group(1)} {path}")
    return eps

def entity_names(code):
    return [m.group(1) for m in re.finditer(r"^\s*([A-Za-z_]+)\s*[\({]", code, re.M)]

def design_spec(path, idx):
    title, blocks = parse(open(path).read())
    short = re.sub(r"\s*\(.*\)$", "", title)
    slug = os.path.basename(path)[:-3]
    slides = [dict(kind="title", heading=short, subtitle="SystemsExpert design walkthrough",
                   narration=f"In this lecture we design {speak(short.replace('Design ', ''))}. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.")]
    seen = set(); comps = []; E = ENRICH.get(slug, {})
    for sec, sub, kind, payload in blocks:
        head = sec if not sub else (f"{sec}: {sub}" if sec not in ("Deep dives",) else sub)
        if sec == "Requirements" and sub: head = f"{sub} requirements"
        intro = "" if (sec, kind) in seen and not sub else INTRO.get(sec, "")
        if sec == "Deep dives" and sub: intro = f"Deep dive: {speak(sub)}."
        if sec == "Requirements" and sub: intro = f"The {sub.lower()} requirements."
        seen.add((sec, kind))
        if kind == "mermaid":
            edges = mermaid_edges(payload)
            if not edges: continue
            nodes = []
            for a, b in edges:
                for n in (a, b):
                    if n not in nodes: nodes.append(n)
            comps = nodes
            outs = {}
            for a, b in edges: outs.setdefault(a, []).append(speak(b))
            flow = " ".join(f"{speak(a)} connects to {' and '.join(bs)}." for a, bs in list(outs.items())[:8])
            slides.append(dict(kind="diagram", heading="High-level architecture", edges=edges,
                               narration=f"Here's the high-level architecture. {flow}"))
            if E.get("flow"):
                rname, steps = E["flow"]
                for node, cap, narr in steps:
                    assert node in nodes, (path, node)
                    slides.append(dict(kind="diagram", heading=f"Request flow: {rname}", edges=edges, highlight=[node], caption=cap, narration=narr))
        elif kind == "code":
            code = payload.strip("\n")
            if not code.strip(): continue
            eps = endpoint_speech(code)
            if eps: narr = f"The API. The main endpoints are: {'; '.join(speak(e) for e in eps[:8])}. Each one is small, resource-oriented and easy to version."
            elif entity_names(code): narr = f"{INTRO.get(sec, 'The core records are')} The main records are {', '.join(entity_names(code)[:8])}. Each one maps to a table or a key-value record, keyed so that the hot queries are single lookups."
            else: narr = f"{intro} Here's a sketch of the {sec.lower()} for reference."
            slides.append(dict(kind="code", heading=head, code=code, lang="text", font_size=26,
                               filename=f"{len(slides) + 1:02d}_{re.sub(r'[^a-z0-9]+', '_', head.lower()).strip('_')}.txt", narration=narr))
        else:
            parts = chunks(payload); ov = E.get("speech", {}).get(sub or "")
            ov_s = sentences(ov) if ov else []
            for j, part in enumerate(parts):
                h = head if j == 0 else f"{head} (cont.)"
                said = [re.sub(r"^([\w ]+?)\s*\((.*)\)\s*(.*)$", lambda m: f"The {m.group(1)} record holds {m.group(2)}. {m.group(3)}", b) if sec == "Data model" else b for b in part]
                narr = (intro + " " if j == 0 else "") + " ".join(end(speak(b)) for b in said)
                if ov_s:
                    k = -(-len(ov_s) // len(parts)); narr = " ".join(ov_s[j * k:(j + 1) * k]) or "Continuing that point."
                if sec.startswith("Trade-offs") and j == 0 and E.get("decisions"):
                    slides.append(dict(kind="bullets", heading="Key decisions", bullets=[f"{a} → {b}" for a, b in E["decisions"]],
                        narration="Let's pull together the key decisions. " + " ".join(f"{speak(a)}, because {speak(b)}." for a, b in E["decisions"])))
                slides.append(dict(kind="bullets", heading=h, bullets=part, narration=narr.strip()))
                if sec == "Capacity estimates" and j == len(parts) - 1 and E.get("capacity"):
                    slides.append(dict(kind="bullets", heading="Capacity: worked out", bullets=[a for a, _ in E["capacity"]],
                        narration="Let's actually work the numbers. " + " ".join(b for _, b in E["capacity"])))
    if E.get("capacity") and not any(x["heading"] == "Capacity: worked out" for x in slides):
        at = next((i for i, x in enumerate(slides) if x["heading"] == "High-level architecture"), len(slides) - 1)
        slides.insert(at, dict(kind="bullets", heading="Capacity: worked out", bullets=[a for a, _ in E["capacity"]],
                               narration="Before drawing boxes, let's estimate the hardest load. " + " ".join(b for _, b in E["capacity"])))
    rec = ["Clarify scope, then functional + non-functional needs", "Estimate load to size storage and fan-out"]
    if comps: rec.append("Core pieces: " + ", ".join(re.sub(r"[:(].*", "", c).strip() for c in comps[:5]))
    rec.append("Know your trade-offs and failure modes")
    slides.append(dict(kind="bullets", heading="Recap", bullets=rec,
                       narration=f"To recap {speak(short.replace('Design ', ''))}: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture" +
                       (f" built around {', '.join(speak(re.sub(r'[:(].*', '', c).strip()) for c in comps[:4])}" if comps else "") +
                       ", and walked through the deep dives and trade-offs. Practise explaining each decision out loud."))
    return dict(title=f"SystemsExpert · {short}", out=f"systemsexpert/{slug}", slides=slides)

def fundamentals_specs(path):
    md = open(path).read(); rows = re.findall(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", md, re.M)
    fw = re.search(r"## Interview framework.*?\n(.*?)\n\n", md, re.S).group(1)
    steps = [clean(s) for s in re.split(r"\s*\d+\.\s+", fw) if s.strip()]
    cheat = [clean(l[2:]) for l in md.split("## Back-of-envelope cheatsheet")[1].splitlines() if l.startswith("- ")]
    specs = [dict(title="SystemsExpert · Interview Framework", out="systemsexpert/00a_interview_framework", slides=[
        dict(kind="title", heading="System Design Interviews", subtitle="Framework and back-of-envelope maths",
             narration="Welcome to the SystemsExpert series. Before the individual designs, here's the framework to run every system design interview, and the numbers you should know for quick estimates."),
        dict(kind="bullets", heading="The 45-minute framework", bullets=steps,
             narration="Run every interview in the same order. " + " ".join(f"Step {i}: {speak(s).rstrip('.')}." for i, s in enumerate(steps, 1)) + " Keep the interviewer involved at every step."),
        dict(kind="bullets", heading="Back-of-envelope numbers", bullets=cheat,
             narration="Some numbers worth memorising. " + " ".join(speak(c).rstrip(".") + "." for c in cheat)),
        dict(kind="bullets", heading="Worked estimate: photo sharing", bullets=[
             "100M DAU × 2 uploads/day = 200M photos/day", "200M ÷ 86,400 s ≈ 2.3k uploads/s (peak ×3 ≈ 7k/s)",
             "× 2 MB ≈ 400 TB/day → ~150 PB/year (× 3 replicas)", "Reads 50× writes ≈ 115k/s → CDN + cache",
             "Conclusion: blob store + CDN; metadata DB sharded"],
             narration="Let's run one estimate end to end, for a photo-sharing app. A hundred million daily users uploading two photos each is two hundred million photos a day. Divide by about eighty-six thousand seconds: roughly twenty-three hundred uploads a second, maybe seven thousand at peak. At two megabytes each that's four hundred terabytes a day, about a hundred and fifty petabytes a year before replication. If reads are fifty times writes, that's over a hundred thousand reads a second. Those numbers tell you immediately: photos go in a blob store behind a CDN, and metadata needs a sharded database."),
        dict(kind="bullets", heading="Recap", bullets=["Same structure every time", "Requirements before boxes", "Estimate, then size the design", "Finish with trade-offs"],
             narration="To recap: use the same structure every time, settle requirements before drawing boxes, let estimates size the design, and always finish with trade-offs and failure modes. Next, the fundamentals, in four parts.")])]
    for part in range(4):
        rs = rows[part * 6:(part + 1) * 6]
        sl = [dict(kind="title", heading=f"Design Fundamentals {part + 1}/4", subtitle=f"Topics {rs[0][0]}–{rs[-1][0]}",
                   narration=f"Design fundamentals, part {part + 1} of 4. We'll cover {', '.join(speak(clean(r[1])) for r in rs[:-1])}, and {speak(clean(rs[-1][1]))}.")]
        for num, topic, pts in rs:
            topic = clean(topic); bl = [b.strip().rstrip(".") for b in re.split(r";\s*|\.\s+", clean(pts)) if b.strip()]
            sl.append(dict(kind="bullets", heading=f"{num}. {topic}", bullets=bl,
                           narration=f"{speak(topic)}. " + " ".join(speak(b) + "." for b in bl)))
        sl.append(dict(kind="bullets", heading="Recap", bullets=[f"{n}. {clean(t)}" for n, t, _ in rs],
                       narration="To recap this part: " + "; ".join(speak(clean(t)) for _, t, _ in rs) + ". Each of these shows up again in the design walkthroughs."))
        specs.append(dict(title=f"SystemsExpert · Fundamentals {part + 1}/4", out=f"systemsexpert/00{'bcde'[part]}_fundamentals_{part + 1}", slides=sl))
    return specs

if __name__ == "__main__":
    specs = fundamentals_specs(os.path.join(REPO, "systemsexpert", "00-fundamentals.md"))
    for i, p in enumerate(sorted(glob.glob(os.path.join(REPO, "systemsexpert", "[0-9][0-9]-design-*.md"))), 1):
        specs.append(design_spec(p, i))
    for s in specs:
        json.dump(s, open(os.path.join(OUTD, os.path.basename(s["out"]) + ".json"), "w"), indent=1, ensure_ascii=False)
    print(len(specs), "systems specs")
