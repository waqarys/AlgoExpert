"""Reusable visual primitives for worked-example slides.

A viz slide: {"kind": "viz", "heading", "panels": [panel, ...], "caption", "narration"}.
Panels are stacked top to bottom. Panel types and fields:
  array     values, hl {idx: color}, ptr {name: idx}, window [lo, hi], label, dim [idx...]
  table     rows (2D), hl {"r,c": color}, rowh, colh, label
  tree      nodes {id: [value, left_id|null, right_id|null]}, root, hl {id: color}, label
  graph     nodes {id: [x, y]} (0..1), edges [[a, b, w?]], directed, hl {id: color}, ehl [[a,b]], label
  stack     items (bottom→top), label, hl {idx: color}
  queue     items (front→back), label
  linked    values, ptr {name: idx}, hl {idx: color}, cycle_to (idx or null), label
  text      lines [str], label     (monospace key/value panel)
Colours may be names: cur, ok, bad, done, warn, or hex.
"""
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse
BG, FG, ACCENT, MUTED, PANEL = "#0f172a", "#e2e8f0", "#38bdf8", "#94a3b8", "#1e293b"
COL = {"cur": "#f59e0b", "ok": "#22c55e", "bad": "#ef4444", "done": "#475569", "warn": "#f472b6", "acc": "#38bdf8", None: PANEL}
c = lambda x: COL.get(x, x)

def _fs(n, base=20):  # font size for n cells
    return base if n <= 10 else max(10, int(base * 10 / n))

def _ratio(ax):
    b = ax.get_position(); f = ax.figure.get_size_inches(); return (b.width * f[0]) / (b.height * f[1])

def Circle(xy, r, **kw):
    kw.pop("transform", None); ax = kw.pop("ax"); return Ellipse(xy, 2 * r, 2 * r * _ratio(ax), **kw)

def _label(ax, t):
    if t: ax.text(0.0, 1.0, t, transform=ax.transAxes, fontsize=16, color=MUTED, va="bottom")

def array(ax, p):
    v = p["values"]; n = max(len(v), 1); hl = {int(k): x for k, x in p.get("hl", {}).items()}
    w = min(0.09, 0.96 / n); x0 = (1 - w * n) / 2; fs = _fs(n, 22)
    if p.get("window"):
        lo, hi = p["window"]; ax.add_patch(Rectangle((x0 + lo * w - 0.005, 0.38), (hi - lo + 1) * w + 0.01, 0.44, fc="none", ec=COL["warn"], lw=3))
    dim = set(p.get("dim", []))
    for i, val in enumerate(v):
        ax.add_patch(FancyBboxPatch((x0 + i * w + 0.004, 0.42), w - 0.008, 0.36, boxstyle="round,pad=0,rounding_size=0.01",
                                    fc=c(hl.get(i)), ec=ACCENT if i not in dim else "#334155", lw=1.5))
        ax.text(x0 + (i + .5) * w, 0.6, str(val), ha="center", va="center", fontsize=fs, color=MUTED if i in dim else FG)
        if p.get("idx", True): ax.text(x0 + (i + .5) * w, 0.86, str(i), ha="center", fontsize=max(10, fs - 8), color=MUTED)
    by = {}
    for name, i in p.get("ptr", {}).items():
        if i is None or i < 0 or i > n: continue
        k = by.setdefault(i, 0); by[i] += 1
        ax.annotate(name, xy=(x0 + (i + .5) * w, 0.4), xytext=(x0 + (i + .5) * w, 0.18 - 0.16 * k), ha="center", fontsize=16,
                    color=COL["cur"], arrowprops=dict(arrowstyle="-|>", color=COL["cur"], lw=2))
    _label(ax, p.get("label"))

def table(ax, p):
    R = p["rows"]; nr = len(R); nc = max(len(r) for r in R); hl = p.get("hl", {})
    rh, ch = p.get("rowh"), p.get("colh"); off_r = 1 if ch else 0; off_c = 1 if rh else 0
    W, H = nc + off_c, nr + off_r; cw = min(0.08, 0.98 / W); chh = min(0.16, 0.95 / H); x0 = (1 - cw * W) / 2; y0 = 1 - (1 - chh * H) / 2
    fs = min(_fs(W, 20), _fs(H * 1.2, 20))
    def cell(r, cc, txt, fc, col=FG, ec=ACCENT):
        x, y = x0 + cc * cw, y0 - (r + 1) * chh
        ax.add_patch(Rectangle((x + .002, y + .004), cw - .004, chh - .008, fc=fc, ec=ec, lw=1))
        ax.text(x + cw / 2, y + chh / 2, str(txt), ha="center", va="center", fontsize=fs, color=col)
    if ch:
        for j, t in enumerate(ch): cell(0, j + off_c, t, BG, MUTED, BG)
    for i, row in enumerate(R):
        if rh: cell(i + off_r, 0, rh[i], BG, MUTED, BG)
        for j, t in enumerate(row): cell(i + off_r, j + off_c, "" if t is None else t, c(hl.get(f"{i},{j}")))
    _label(ax, p.get("label"))

def tree(ax, p):
    N = p["nodes"]; hl = p.get("hl", {}); pos = {}; order = []
    def walk(i, d):
        if i is None or str(i) not in N: return
        i = str(i); walk(N[i][1], d + 1); pos[i] = [len(order), d]; order.append(i); walk(N[i][2], d + 1)
    walk(p["root"], 0)
    if not pos: _label(ax, p.get("label")); return
    D = max(d for _, d in pos.values()) + 1; n = len(order)
    r = min(0.045, 0.4 / n); ry = r * _ratio(ax); top, bot = 1 - ry - 0.03, ry + 0.03
    xy = {i: ((k + .5) / n, top - d * ((top - bot) / max(D - 1, 1)) if D > 1 else 0.5) for i, (k, d) in pos.items()}
    for i in pos:
        for ch in N[i][1:3]:
            if ch is not None and str(ch) in xy: ax.plot(*zip(xy[i], xy[str(ch)]), color=MUTED, lw=1.5, zorder=1)
    for i, (x, y) in xy.items():
        ax.add_patch(Circle((x, y), r, ax=ax, fc=c(hl.get(i)), ec=ACCENT, lw=1.5, zorder=2, transform=ax.transData))
        ax.text(x, y, str(N[i][0]), ha="center", va="center", fontsize=_fs(n, 18), color=FG, zorder=3)
    for k, t in p.get("notes", {}).items():
        if k in xy: ax.text(xy[k][0] + r + 0.008, xy[k][1], t, ha="left", va="center", fontsize=16, color=COL["cur"], zorder=4)
    _label(ax, p.get("label"))

def graph(ax, p):
    P = p["nodes"]; hl = p.get("hl", {}); ehl = {tuple(map(str, e)) for e in p.get("ehl", [])}
    for e in p.get("edges", []):
        a, b = str(e[0]), str(e[1]); (x1, y1), (x2, y2) = P[a], P[b]; on = (a, b) in ehl or (not p.get("directed") and (b, a) in ehl)
        col, lw = (COL["cur"], 3) if on else (MUTED, 1.5)
        if p.get("directed"):
            ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, shrinkA=22, shrinkB=22))
        else: ax.plot([x1, x2], [y1, y2], color=col, lw=lw, zorder=1)
        if len(e) > 2: ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.03, str(e[2]), fontsize=15, color=ACCENT, ha="center")
    for i, (x, y) in P.items():
        ax.add_patch(Circle((x, y), 0.045, ax=ax, fc=c(hl.get(i)), ec=ACCENT, lw=1.5, zorder=2))
        ax.text(x, y, str(p.get("names", {}).get(i, i)), ha="center", va="center", fontsize=16, color=FG, zorder=3)
    for k, t in p.get("notes", {}).items():
        ax.text(P[k][0], P[k][1] - 0.09, t, ha="center", va="top", fontsize=14, color=COL["cur"])
    _label(ax, p.get("label"))

def stack(ax, p):
    it = p["items"]; hl = {int(k): x for k, x in p.get("hl", {}).items()}; n = max(len(it), 1); h = min(0.14, 0.9 / n)
    for i, v in enumerate(it):
        ax.add_patch(Rectangle((0.38, 0.05 + i * h), 0.24, h * .9, fc=c(hl.get(i)), ec=ACCENT))
        ax.text(0.5, 0.05 + (i + .45) * h, str(v), ha="center", va="center", fontsize=_fs(n, 18), color=FG)
    if not it: ax.text(0.5, 0.1, "(empty)", ha="center", color=MUTED, fontsize=16)
    ax.plot([0.36, 0.36, 0.64, 0.64], [0.95, 0.03, 0.03, 0.95], color=MUTED, lw=2)
    _label(ax, p.get("label") or "stack (top ↑)")

def queue(ax, p):
    array(ax, {"values": p["items"] or ["–"], "idx": False, "label": p.get("label") or "queue (front → back)", "hl": p.get("hl", {})})

def linked(ax, p):
    v = p["values"]; n = max(len(v), 1); w = min(0.12, 0.96 / n); x0 = (1 - w * n) / 2; hl = {int(k): x for k, x in p.get("hl", {}).items()}
    for i, val in enumerate(v):
        x = x0 + i * w
        ax.add_patch(FancyBboxPatch((x + 0.01, 0.45), w * 0.55, 0.3, boxstyle="round,pad=0,rounding_size=0.01", fc=c(hl.get(i)), ec=ACCENT, lw=1.5))
        ax.text(x + 0.01 + w * 0.275, 0.6, str(val), ha="center", va="center", fontsize=_fs(n, 20), color=FG)
        if i < len(v) - 1: ax.annotate("", xy=(x + w + 0.01, 0.6), xytext=(x + 0.01 + w * 0.55, 0.6), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.5))
    if p.get("cycle_to") is not None and v:
        a = x0 + (len(v) - 1) * w + 0.01 + w * 0.275; b = x0 + p["cycle_to"] * w + 0.01 + w * 0.275
        ax.annotate("", xy=(b, 0.75), xytext=(a, 0.75), arrowprops=dict(arrowstyle="-|>", color=COL["warn"], lw=2, connectionstyle="arc3,rad=0.4"))
    by = {}
    for name, i in p.get("ptr", {}).items():
        if i is None or i >= n: continue
        k = by.setdefault(i, 0); by[i] += 1; xx = x0 + i * w + 0.01 + w * 0.275
        ax.annotate(name, xy=(xx, 0.44), xytext=(xx, 0.22 - 0.15 * k), ha="center", fontsize=15, color=COL["cur"], arrowprops=dict(arrowstyle="-|>", color=COL["cur"], lw=2))
    _label(ax, p.get("label"))

def text(ax, p):
    L = p["lines"]; fs = p.get("size", 22 if len(L) <= 6 else 18)
    for i, l in enumerate(L):
        ax.text(0.02, 0.92 - i * (0.9 / max(len(L), 5)), l, fontsize=fs, family="DejaVu Sans Mono", color=FG, va="top")
    _label(ax, p.get("label"))

KINDS = dict(array=array, table=table, tree=tree, graph=graph, stack=stack, queue=queue, linked=linked, text=text)

def render(fig, s):
    panels = s["panels"]; top, bottom = 0.84, 0.17 if s.get("caption") else 0.08
    layout = s.get("layout", "rows")
    n = len(panels)
    for i, p in enumerate(panels):
        if layout == "cols":
            ws = p.get("w") or [1 / n] * n
            x = 0.04 + 0.92 * sum((pp.get("w") or 1 / n) for pp in panels[:i]); wi = 0.92 * (p.get("w") or 1 / n)
            rect = [x, bottom, wi - 0.02, top - bottom]
        else:
            hs = [pp.get("h", 1) for pp in panels]; tot = sum(hs); y = top - (top - bottom) * sum(hs[:i + 1]) / tot
            rect = [0.04, y + 0.01, 0.92, (top - bottom) * hs[i] / tot - 0.04]
        ax = fig.add_axes(rect); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
        KINDS[p["type"]](ax, p)
    if s.get("caption"):
        fig.text(0.5, 0.09, s["caption"], ha="center", fontsize=22, color=FG,
                 bbox=dict(boxstyle="round,pad=0.4", fc=PANEL, ec="#334155"))
