"""Labelled contact sheet of frames from finished demos."""
import subprocess, sys, io
from PIL import Image, ImageDraw
from brand import font, BG, TEXT, SKY
def grab(mp4, t):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", str(t), "-i", mp4, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(raw)).convert("RGB").resize((480, 270), Image.LANCZOS)
def sheet(rows, out):
    cols = max(len(r[1]) for r in rows); cw, ch = 480, 270; pad = 16
    im = Image.new("RGB", (pad + cols * (cw + pad), 70 + len(rows) * (ch + 90)), BG); d = ImageDraw.Draw(im)
    d.text((pad, 18), "Build with Waqar · video-kit demo contact sheet", font=font("display", 34, 800), fill=TEXT)
    y = 70
    for name, shots in rows:
        d.text((pad, y + 4), name, font=font("sans", 26, 700), fill=SKY); y += 40
        for i, (t, lab) in enumerate(shots):
            x = pad + i * (cw + pad); im.paste(grab(name_to[name], t), (x, y))
            d.text((x, y + ch + 6), f"{lab}  @{t:.1f}s", font=font("sans", 20, 500), fill=TEXT)
        y += ch + 50
    im.save(out)
name_to = {}
