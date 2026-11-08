"""Shared palette, fonts and drawing helpers for the Build with Waqar video kit.
Palette sampled from the existing dark slides (bg #0F172A, text #E2E8F0, accent #38BDF8,
muted #94A3B8) and the WS avatar (purple #4B198F, pink #FF90E8)."""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

W, H, FPS = 1920, 1080, 30
BG = (15, 23, 42); BG2 = (11, 17, 32); PANEL = (30, 41, 59)
TEXT = (226, 232, 240); MUTED = (148, 163, 184)
SKY = (56, 189, 248); PURPLE = (91, 33, 182); PINK = (255, 144, 232); GOLD = (250, 204, 21)

KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(KIT, "assets")
LOGO = os.path.join(ASSETS, "brand", "avatar.png")
GF = "/usr/share/fonts/truetype/sand-box/google"
_FONTS = {
    "sans": [f"{GF}/Inter/Inter-VariableFont_opsz,wght.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"],
    "display": [f"{GF}/Montserrat/Montserrat-VariableFont_wght.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"],
    "mono": [f"{GF}/JetBrains Mono/JetBrainsMono-VariableFont_wght.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"],
}
_cache = {}
def font(kind="sans", size=48, weight=700):
    key = (kind, size, weight)
    if key in _cache: return _cache[key]
    for p in _FONTS[kind]:
        if os.path.exists(p):
            f = ImageFont.truetype(p, size)
            try:
                f.set_variation_by_axes([weight] if "opsz" not in p else [min(max(size,14),32), weight])
            except Exception:
                try: f.set_variation_by_axes([weight])
                except Exception: pass
            _cache[key] = f; return f
    return ImageFont.load_default()

def ease_out(t):  t = min(max(t, 0), 1); return 1 - (1 - t) ** 3
def ease_in_out(t): t = min(max(t, 0), 1); return 3 * t * t - 2 * t * t * t
def back_out(t, s=1.70158):
    t = min(max(t, 0), 1) - 1; return t * t * ((s + 1) * t + s) + 1
def clamp01(x): return min(max(x, 0.0), 1.0)

def bg_gradient(w=W, h=H, c1=BG2, c2=(24, 18, 60)):
    x = np.linspace(0, 1, w)[None, :, None]; y = np.linspace(0, 1, h)[:, None, None]
    t = np.clip(0.65 * x + 0.35 * y, 0, 1)
    arr = (np.array(c1) * (1 - t) + np.array(c2) * t).astype(np.uint8)
    return Image.fromarray(np.broadcast_to(arr, (h, w, 3)).copy(), "RGB")

def grid(img, offset=0.0, alpha=18, step=80):
    d = ImageDraw.Draw(img, "RGBA")
    for x in range(-step, img.width + step, step):
        xx = int(x + offset % step); d.line([(xx, 0), (xx, img.height)], fill=SKY + (alpha,), width=1)
    for y in range(0, img.height, step):
        d.line([(0, y), (img.width, y)], fill=SKY + (alpha,), width=1)

def text_w(d, s, f):
    b = d.textbbox((0, 0), s, font=f); return b[2] - b[0]

def fit_font(d, s, kind, size, weight, maxw):
    while size > 20 and text_w(d, s, font(kind, size, weight)) > maxw: size -= 2
    return font(kind, size, weight)

def glow(layer, radius=18, strength=1.6):
    """Add a bloom to an RGBA layer."""
    blur = layer.filter(ImageFilter.GaussianBlur(radius))
    a = np.asarray(blur).astype(np.float32); a[..., 3] = np.clip(a[..., 3] * strength, 0, 255)
    out = Image.fromarray(a.astype(np.uint8), "RGBA"); out.alpha_composite(layer); return out

def logo(size):
    im = Image.open(LOGO).convert("RGBA").resize((size, size), Image.LANCZOS)
    m = Image.new("L", (size, size), 0); ImageDraw.Draw(m).ellipse([0, 0, size - 1, size - 1], fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0)); out.paste(im, (0, 0), m); return out

class Writer:
    """Pipe PIL frames into ffmpeg. alpha=True -> MOV (qtrle, keeps transparency)."""
    def __init__(self, path, alpha=False, fps=FPS, size=(W, H), audio=None):
        self.alpha = alpha
        cmd = ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba" if alpha else "rgb24",
               "-s", f"{size[0]}x{size[1]}", "-r", str(fps), "-i", "-"]
        if audio: cmd += ["-i", audio]
        if alpha: cmd += ["-c:v", "qtrle", "-pix_fmt", "argb"]
        else: cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p"]
        if audio: cmd += ["-c:a", "aac", "-b:a", "192k", "-shortest"]
        cmd += [path]
        self.p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    def write(self, im):
        im = im.convert("RGBA" if self.alpha else "RGB"); self.p.stdin.write(im.tobytes())
    def close(self):
        self.p.stdin.close(); assert self.p.wait() == 0

# ---- series presets (accent colour distinguishes AlgoExpert vs LeetCode episodes)
ACCENT = SKY
def set_accent(rgb):
    global ACCENT
    ACCENT = tuple(rgb)

# ---- safe layout: captured content never sits under the camera
CONTENT = (24, 24, 1544, 879)        # 1520x855 (16:9) slides / IntelliJ / whiteboard
CAM = (1568, 24, 1896, 352)          # 328x328 camera box in the right-hand column
