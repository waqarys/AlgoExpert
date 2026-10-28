"""Helpers for per-problem enrichment: viz panels, slide builders, step picking, tree builders."""
def S(heading, panels, caption, narration, layout="rows"):
    return dict(kind="viz", heading=heading, panels=panels, caption=caption, narration=narration, layout=layout)
def A(values, hl=None, ptr=None, window=None, label=None, dim=None, h=1, w=None, idx=True):
    d = dict(type="array", values=list(values), hl={str(k): v for k, v in (hl or {}).items()}, ptr=ptr or {}, label=label, h=h, idx=idx)
    if window: d["window"] = list(window)
    if dim: d["dim"] = list(dim)
    if w: d["w"] = w
    return d
def T(rows, hl=None, rowh=None, colh=None, label=None, h=1, w=None):
    d = dict(type="table", rows=[list(r) for r in rows], hl={f"{r},{c}": v for (r, c), v in (hl or {}).items()}, rowh=rowh, colh=colh, label=label, h=h)
    if w: d["w"] = w
    return d
def TR(nodes, root, hl=None, label=None, notes=None, h=1, w=None):
    d = dict(type="tree", nodes=nodes, root=str(root) if root is not None else None, hl={str(k): v for k, v in (hl or {}).items()}, label=label, notes={str(k): v for k, v in (notes or {}).items()}, h=h)
    if w: d["w"] = w
    return d
def G(pos, edges, hl=None, ehl=None, directed=False, label=None, notes=None, names=None, h=1, w=None):
    d = dict(type="graph", nodes={str(k): v for k, v in pos.items()}, edges=[[str(e[0]), str(e[1])] + list(e[2:]) for e in edges],
             hl={str(k): v for k, v in (hl or {}).items()}, ehl=[[str(a), str(b)] for a, b in (ehl or [])], directed=directed, label=label,
             notes={str(k): v for k, v in (notes or {}).items()}, names=names or {}, h=h)
    if w: d["w"] = w
    return d
def ST(items, label=None, hl=None, h=1, w=None):
    d = dict(type="stack", items=list(items), label=label, hl={str(k): v for k, v in (hl or {}).items()}, h=h)
    if w: d["w"] = w
    return d
def Q(items, label=None, h=1, w=None):
    d = dict(type="queue", items=list(items), label=label, h=h)
    if w: d["w"] = w
    return d
def LL(values, ptr=None, hl=None, cycle_to=None, label=None, h=1, w=None):
    d = dict(type="linked", values=list(values), ptr=ptr or {}, hl={str(k): v for k, v in (hl or {}).items()}, cycle_to=cycle_to, label=label, h=h)
    if w: d["w"] = w
    return d
def TX(lines, label=None, h=0.6, w=None, size=None):
    d = dict(type="text", lines=list(lines), label=label, h=h)
    if w: d["w"] = w
    if size: d["size"] = size
    return d
def pick(steps, k=5):
    """Keep first, last and evenly spaced steps (max k)."""
    if len(steps) <= k: return steps
    idx = sorted({round(i * (len(steps) - 1) / (k - 1)) for i in range(k)})
    return [steps[i] for i in idx]
def bst(values):
    """Insert values into a BST; return (nodes, root) with ids '0','1',… by insertion order."""
    nodes, root = {}, None
    for i, v in enumerate(values):
        nid = str(i); nodes[nid] = [v, None, None]
        if root is None: root = nid; continue
        cur = root
        while True:
            side = 1 if v < nodes[cur][0] else 2
            if nodes[cur][side] is None: nodes[cur][side] = nid; break
            cur = nodes[cur][side]
    return nodes, root
def heap_tree(arr):
    """Array-as-binary-tree (heap layout) → nodes dict keyed by index."""
    n = len(arr); return {str(i): [arr[i], str(2 * i + 1) if 2 * i + 1 < n else None, str(2 * i + 2) if 2 * i + 2 < n else None] for i in range(n)}, "0" if n else None
def level_tree(vals):
    """Level-order list with None gaps → nodes dict keyed by index."""
    nodes = {}
    for i, v in enumerate(vals):
        if v is None: continue
        l, r = 2 * i + 1, 2 * i + 2
        nodes[str(i)] = [v, str(l) if l < len(vals) and vals[l] is not None else None, str(r) if r < len(vals) and vals[r] is not None else None]
    return nodes, "0"
def E(brute, brute_narr, example, pitfalls, pit_narr, tips, tips_narr, code, problem=None):
    return dict(brute=(brute, brute_narr), example=example, pitfalls=(pitfalls, pit_narr), tips=(tips, tips_narr), code=code, problem=problem)
