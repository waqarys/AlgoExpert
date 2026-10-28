"""Helpers for writing slide specs compactly."""
import ast, os
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def title(h, sub, n): return dict(kind="title", heading=h, subtitle=sub, narration=n)
def bullets(h, b, n, **kw): return dict(kind="bullets", heading=h, bullets=b, narration=n, **kw)
def eqs(h, e, b, n, **kw): return dict(kind="equations", heading=h, equations=e, bullets=b, narration=n, **kw)
def plot(h, draw, b, n): return dict(kind="plot", heading=h, draw=draw, bullets=b, narration=n)
def code(h, c, n, lang="python", filename=None, **kw):
    d = dict(kind="code", heading=h, code=c, narration=n, lang=lang, **kw)
    if filename: d["filename"] = filename
    return d
def diagram(h, edges, n): return dict(kind="diagram", heading=h, edges=edges, narration=n)

def src(rel, *names):
    """Source of top-level functions/classes (or Class.method) from a repo file, joined."""
    text = open(os.path.join(REPO, rel)).read(); tree = ast.parse(text); lines = text.splitlines(); out = []
    for name in names:
        cls, _, meth = name.partition(".")
        node = next(n for n in tree.body if getattr(n, "name", None) == cls)
        if meth: node = next(n for n in node.body if getattr(n, "name", None) == meth)
        seg = lines[node.lineno - 1 - len(node.decorator_list): node.end_lineno]
        ind = len(seg[0]) - len(seg[0].lstrip())
        out.append("\n".join(l[ind:] for l in seg))
    return "\n\n".join(out)
