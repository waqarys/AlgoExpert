#!/usr/bin/env python3
"""Build a narrated lecture (720p MP4) plus reusable slide assets from a slide spec.

Usage: python make_lecture.py SPEC [SPEC ...] [--voice en-US-GuyNeural] [--skip-existing]

A spec is a Python module (TITLE, OUT, SLIDES) or a JSON file {"title", "out", "slides"}.
Outputs in lectures/<OUT>/: lecture.mp4, transcript.md, slides/NN.png (1920x1080), slides.pdf, code/*.
"""
import argparse, asyncio, textwrap, importlib.util, json, os, re, shutil, subprocess, sys, tempfile
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch
from PIL import Image
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from pygments.styles import get_style_by_name

W, H, DPI = 1920, 1080, 150          # 12.8 x 7.2 inch figure
S = W / 1280                          # pixel scale vs the original 720p design
BG, FG, ACCENT, MUTED, PANEL = "#0f172a", "#e2e8f0", "#38bdf8", "#94a3b8", "#1e293b"
for f in ["/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"]:
    if os.path.exists(f): font_manager.fontManager.addfont(f)
plt.rcParams.update({"font.family": ["Inter", "DejaVu Sans"], "mathtext.fontset": "cm",
                     "text.color": FG, "axes.labelcolor": FG, "xtick.color": MUTED, "ytick.color": MUTED})
import logging; logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXT = {"python": "py", "java": "java", "sql": "sql", "json": "json", "text": "txt", "bash": "sh"}

def canvas(heading, idx, total, title):
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    if heading:
        fig.text(0.05, 0.9, heading, fontsize=34 if len(heading) < 40 else 28, color=FG)
        fig.add_artist(plt.Line2D([0.05, 0.2], [0.87, 0.87], color=ACCENT, lw=4))
    fig.text(0.05, 0.03, title, fontsize=12, color=MUTED)
    fig.text(0.95, 0.03, f"{idx}/{total}", fontsize=12, color=MUTED, ha="right")
    return fig

def draw_diagram(fig, edges, rect=(0.03, 0.08, 0.94, 0.76)):
    """Layered left-to-right box diagram from [(src, dst, label?)]."""
    nodes = []
    for e in edges:
        for n in e[:2]:
            if n not in nodes: nodes.append(n)
    adj = {n: [] for n in nodes}
    for e in edges: adj[e[0]].append(e[1])
    state, back = {}, set()
    def dfs(u):
        state[u] = 1
        for v in adj[u]:
            if state.get(v) == 1: back.add((u, v))
            elif v not in state: dfs(v)
        state[u] = 2
    for n in nodes:
        if n not in state: dfs(n)
    level = {n: 0 for n in nodes}
    for _ in range(len(nodes)):
        for e in edges:
            if (e[0], e[1]) not in back: level[e[1]] = max(level[e[1]], level[e[0]] + 1)
    L = max(level.values()) + 1
    cols = {l: [n for n in nodes if level[n] == l] for l in range(L)}
    ax = fig.add_axes(rect); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    pos, bw = {}, min(0.75 / L, 0.2)
    for l, ns in cols.items():
        for j, n in enumerate(ns):
            pos[n] = ((l + 0.5) / L, 1 - (j + 0.5) / len(ns))
    bh = min(0.16, 0.85 / max(len(c) for c in cols.values()))
    for e in edges:
        (x1, y1), (x2, y2) = pos[e[0]], pos[e[1]]
        ax.annotate("", xy=(x2 - bw / 2 if x2 > x1 else x2, y2), xytext=(x1 + bw / 2 if x2 > x1 else x1, y1),
                    arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.5, shrinkA=0, shrinkB=2,
                                    connectionstyle="arc3,rad=0" if x2 > x1 else "arc3,rad=0.35"))
    for n, (x, y) in pos.items():
        ax.add_patch(FancyBboxPatch((x - bw / 2, y - bh / 2), bw, bh, boxstyle="round,pad=0.005,rounding_size=0.015",
                                    fc=PANEL, ec=ACCENT, lw=1.5))
        ax.text(x, y, "\n".join(textwrap.wrap(n, max(10, int(bw * 95)))), ha="center", va="center",
                fontsize=14 if len(n) < 16 else 12 if len(n) < 34 else 10, color=FG, linespacing=1.1)

def render(s, path, idx, total, title):
    k = s["kind"]
    fig = canvas(None if k == "title" else s["heading"], idx, total, title)
    if k == "title":
        fig.text(0.5, 0.58, s["heading"], fontsize=56 if len(s["heading"]) < 28 else 40, ha="center", color=FG)
        fig.text(0.5, 0.45, s.get("subtitle", ""), fontsize=24, ha="center", color=ACCENT)
    elif k in ("bullets", "equations"):
        y = 0.76
        for b in s.get("equations", []):
            fig.text(0.5, y - 0.04, b, fontsize=s.get("eq_size", 34), ha="center", color=ACCENT); y -= 0.15
        bl = s.get("bullets", [])
        avail = y - 0.08
        for size in ([s["size"]] if "size" in s else [24, 22, 20, 18, 16, 14]):
            width = int(1150 / size)                      # ~chars per line at this size
            wrapped = [textwrap.wrap(b, width) or [""] for b in bl]
            lh = size / 72 / (H / DPI) * 1.45             # line height in figure fraction
            need = sum(len(w) for w in wrapped) * lh + len(bl) * lh * 0.45
            if need <= avail: break
        for w in wrapped:
            for j, line in enumerate(w):
                fig.text(0.07, y, ("•  " if j == 0 else "    ") + line, fontsize=size, color=FG); y -= lh
            y -= lh * 0.45
    elif k == "plot":
        ax = fig.add_axes(s.get("rect", [0.08, 0.12, 0.55, 0.68]), facecolor=PANEL)
        for sp in ax.spines.values(): sp.set_color("#334155")
        s["draw"](ax)
        y = 0.74
        for b in s.get("bullets", []):
            fig.text(0.67, y, b, fontsize=20, color=FG); y -= 0.09
    elif k == "diagram":
        draw_diagram(fig, s["edges"])
    elif k == "code":
        fmt = ImageFormatter(style=get_style_by_name("monokai"), font_name="DejaVu Sans Mono",
                             font_size=int(s.get("font_size", 30) * S), line_numbers=False,
                             image_pad=int(24 * S), line_pad=int(8 * S))
        tmp = path + ".code.png"
        open(tmp, "wb").write(highlight(s["code"].strip("\n"), get_lexer_by_name(s.get("lang", "python")), fmt))
        im = Image.open(tmp); im.thumbnail((W - int(120 * S), H - int(190 * S)), Image.LANCZOS)
        top = H - int(140 * S) - max(0, (H - int(190 * S) - im.height) // 3)
        ax = fig.add_axes([(W - im.width) / 2 / W, (top - im.height) / H, im.width / W, im.height / H])
        ax.imshow(im, interpolation="none"); ax.axis("off"); os.remove(tmp)
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)
    im = Image.open(path).convert("RGB")
    im.quantize(colors=256, method=Image.Quantize.MEDIANCUT).save(path, optimize=True)

async def tts(text, voice, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate="+5%").save(out)

def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).strip())

def load(path):
    if path.endswith(".json"):
        d = json.load(open(path)); return d["title"], d["out"], d["slides"]
    sp = importlib.util.spec_from_file_location("spec", path); m = importlib.util.module_from_spec(sp)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sp.loader.exec_module(m)
    return m.TITLE, m.OUT, m.SLIDES

def build(spec, voice):
    title, out, slides = load(spec)
    out_dir = os.path.join(ROOT, out)
    for sub in ("slides", "code"): shutil.rmtree(os.path.join(out_dir, sub), ignore_errors=True)
    os.makedirs(os.path.join(out_dir, "slides"), exist_ok=True)
    work = tempfile.mkdtemp(); segs = []; n = len(slides); pngs = []; codes = []
    for i, s in enumerate(slides, 1):
        png = os.path.join(out_dir, "slides", f"{i:02d}.png"); mp3, seg = (os.path.join(work, f"{i:02d}.{e}") for e in ("mp3", "mp4"))
        render(s, png, i, n, title); pngs.append(png)
        if s["kind"] == "code":
            os.makedirs(os.path.join(out_dir, "code"), exist_ok=True)
            name = s.get("filename") or f"{i:02d}_{re.sub(r'[^a-z0-9]+', '_', s['heading'].lower()).strip('_')}.{EXT.get(s.get('lang', 'python'), 'txt')}"
            open(os.path.join(out_dir, "code", name), "w").write(s["code"].strip("\n") + "\n"); codes.append(name)
        words = len(s["narration"].split())
        for t in range(6):  # retry on errors or truncated audio (expect ~2.5 words/sec)
            try:
                asyncio.run(tts(s["narration"], voice, mp3))
                if dur(mp3) > words / 4.5: break
                print(f"{out} slide {i}: audio looks truncated, retrying", flush=True)
            except Exception as e: print("tts retry", e, flush=True)
        else: raise RuntimeError(f"TTS failed for {out} slide {i}")
        d = dur(mp3) + 0.6
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "15", "-i", png, "-i", mp3,
                        "-af", "apad", "-t", f"{d:.2f}", "-vf", "scale=1280:720:flags=lanczos,fade=in:0:5,format=yuv420p",
                        "-c:v", "libx264", "-preset", "medium", "-crf", "28", "-tune", "stillimage",
                        "-c:a", "aac", "-b:a", "96k", "-ar", "44100", "-ac", "1", seg], check=True)
        segs.append(seg); s["_dur"] = d
    lst = os.path.join(work, "list.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in segs))
    mp4 = os.path.join(out_dir, "lecture.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy",
                    "-movflags", "+faststart", mp4], check=True)
    import img2pdf  # embeds the optimised PNGs losslessly
    open(os.path.join(out_dir, "slides.pdf"), "wb").write(img2pdf.convert(pngs, rotation=img2pdf.Rotation.ifvalid))
    t, lines = 0.0, [f"# {title}\n", "Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: " + voice + "\n"]
    for i, s in enumerate(slides, 1):
        lines.append(f"## {i}. {s['heading']} ({int(t//60)}:{int(t%60):02d}) — `slides/{i:02d}.png`\n\n{s['narration']}\n")
        t += s["_dur"]
    open(os.path.join(out_dir, "transcript.md"), "w").write("\n".join(lines))
    shutil.rmtree(work)
    size = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(out_dir) for f in fs)
    return {"out": out, "seconds": round(dur(mp4), 1), "mp4_mb": round(os.path.getsize(mp4) / 1e6, 2), "folder_mb": round(size / 1e6, 2)}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("specs", nargs="+")
    ap.add_argument("--voice", default="en-US-GuyNeural"); ap.add_argument("--skip-existing", action="store_true")
    a = ap.parse_args(); rc = 0
    for spec in a.specs:
        try:
            if a.skip_existing:
                _, out, _ = load(spec)
                if os.path.exists(os.path.join(ROOT, out, "slides.pdf")): continue
            print(json.dumps(build(spec, a.voice)), flush=True)
        except Exception as e:
            print(json.dumps({"spec": spec, "error": str(e)}), flush=True); rc = 1
    sys.exit(rc)

if __name__ == "__main__":
    main()
