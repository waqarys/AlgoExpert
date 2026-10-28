#!/usr/bin/env python3
"""Build a narrated MP4 lecture from a slide spec.

Usage: python make_lecture.py specs/mlexpert/linear_regression.py [--voice en-US-GuyNeural]

A spec is a Python module defining TITLE, OUT (path relative to lectures/) and SLIDES,
a list of dicts: {"kind": title|bullets|equations|code|plot, "heading", "narration", ...}.
"""
import argparse, asyncio, importlib.util, json, os, subprocess, sys, tempfile
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from pygments.styles import get_style_by_name

W, H, DPI = 1280, 720, 100
BG, FG, ACCENT, MUTED = "#0f172a", "#e2e8f0", "#38bdf8", "#94a3b8"
for f in ["/usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf"]:
    if os.path.exists(f): font_manager.fontManager.addfont(f)
plt.rcParams.update({"font.family": ["Inter", "DejaVu Sans"], "mathtext.fontset": "cm",
                     "text.color": FG, "axes.labelcolor": FG, "xtick.color": MUTED, "ytick.color": MUTED})
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def canvas(heading, idx, total, title):
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=BG)
    if heading:
        fig.text(0.05, 0.9, heading, fontsize=34, weight="semibold", color=FG)
        fig.add_artist(plt.Line2D([0.05, 0.2], [0.87, 0.87], color=ACCENT, lw=4))
    fig.text(0.05, 0.03, title, fontsize=12, color=MUTED)
    fig.text(0.95, 0.03, f"{idx}/{total}", fontsize=12, color=MUTED, ha="right")
    return fig

def render(s, path, idx, total, title):
    k = s["kind"]
    fig = canvas(None if k == "title" else s["heading"], idx, total, title)
    if k == "title":
        fig.text(0.5, 0.58, s["heading"], fontsize=56, weight="semibold", ha="center", color=FG)
        fig.text(0.5, 0.45, s.get("subtitle", ""), fontsize=24, ha="center", color=ACCENT)
    elif k in ("bullets", "equations"):
        y = 0.76
        for b in s.get("equations", []):
            fig.text(0.5, y - 0.04, b, fontsize=34, ha="center", color=ACCENT); y -= 0.15
        for b in s.get("bullets", []):
            fig.text(0.07, y, "•  " + b, fontsize=s.get("size", 24), color=FG, wrap=True); y -= 0.1
    elif k == "plot":
        ax = fig.add_axes(s.get("rect", [0.08, 0.12, 0.55, 0.68]), facecolor="#1e293b")
        for sp in ax.spines.values(): sp.set_color("#334155")
        s["draw"](ax)
        y = 0.74
        for b in s.get("bullets", []):
            fig.text(0.67, y, b, fontsize=20, color=FG); y -= 0.09
    elif k == "code":
        fmt = ImageFormatter(style=get_style_by_name("monokai"), font_name="DejaVu Sans Mono",
                             font_size=s.get("font_size", 30), line_numbers=False, image_pad=24, line_pad=8)
        tmp = path + ".code.png"
        open(tmp, "wb").write(highlight(s["code"].strip("\n"), get_lexer_by_name(s.get("lang", "python")), fmt))
        im = Image.open(tmp); im.thumbnail((W - 120, H - 190))
        top = H - 140 - max(0, (H - 190 - im.height) // 3)
        ax = fig.add_axes([(W - im.width) / 2 / W, (top - im.height) / H, im.width / W, im.height / H])
        ax.imshow(im); ax.axis("off"); os.remove(tmp)
    fig.savefig(path, dpi=DPI, facecolor=BG); plt.close(fig)

async def tts(text, voice, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate="+5%").save(out)

def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", p]).strip())

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("spec"); ap.add_argument("--voice", default="en-US-GuyNeural")
    a = ap.parse_args()
    m = importlib.util.module_from_spec(sp := importlib.util.spec_from_file_location("spec", a.spec)); sp.loader.exec_module(m)
    out_dir = os.path.join(ROOT, m.OUT); os.makedirs(out_dir, exist_ok=True)
    work = tempfile.mkdtemp(); segs = []; n = len(m.SLIDES)
    for i, s in enumerate(m.SLIDES, 1):
        png, mp3, seg = (os.path.join(work, f"{i:02d}.{e}") for e in ("png", "mp3", "mp4"))
        render(s, png, i, n, m.TITLE)
        words = len(s["narration"].split())
        for t in range(5):  # retry on errors or truncated audio (expect ~2.5 words/sec)
            try:
                asyncio.run(tts(s["narration"], a.voice, mp3))
                if dur(mp3) > words / 4.5: break
                print(f"slide {i}: audio looks truncated, retrying")
            except Exception as e: print("tts retry", e)
        else: sys.exit(f"TTS failed for slide {i}")
        d = dur(mp3) + 0.6  # small pause after each slide
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", "15", "-i", png, "-i", mp3,
                        "-af", "apad", "-t", f"{d:.2f}", "-vf", "fade=in:0:5,format=yuv420p",
                        "-c:v", "libx264", "-preset", "medium", "-crf", "28", "-tune", "stillimage",
                        "-c:a", "aac", "-b:a", "96k", "-ar", "44100", "-ac", "1", seg], check=True)
        segs.append(seg); s["_dur"] = d
    lst = os.path.join(work, "list.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in segs))
    mp4 = os.path.join(out_dir, "lecture.mp4")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy",
                    "-movflags", "+faststart", mp4], check=True)
    t, lines = 0.0, [f"# {m.TITLE}\n", f"Voice: {a.voice}. Video: [lecture.mp4](lecture.mp4)\n"]
    for i, s in enumerate(m.SLIDES, 1):
        lines.append(f"## {i}. {s['heading']} ({int(t//60)}:{int(t%60):02d})\n\n{s['narration']}\n")
        t += s["_dur"]
    open(os.path.join(out_dir, "transcript.md"), "w").write("\n".join(lines))
    print(json.dumps({"mp4": mp4, "seconds": round(dur(mp4), 1), "mb": round(os.path.getsize(mp4) / 1e6, 2), "work": work}))

if __name__ == "__main__":
    main()
