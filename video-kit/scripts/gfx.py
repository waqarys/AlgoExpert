"""Animated brand graphics: intro, outro, stingers, section cards, overlays, thumbnails.
Every function returns (path, sfx_cues) where sfx_cues = [(seconds, 'name.wav', gain_db)]."""
import math, os, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from brand import *
import brand as B

def _particles(n=140, seed=3):
    r = random.Random(seed)
    return [(r.uniform(0, W), r.uniform(0, H), r.uniform(-40, 40), r.uniform(-25, 25), r.uniform(1.5, 4.5),
             r.choice([SKY, PINK, TEXT, SKY]), r.uniform(0, 6.28)) for _ in range(n)]

def _draw_particles(img, parts, t, converge=0.0, cx=W/2, cy=H/2, alpha=1.0):
    d = ImageDraw.Draw(img, "RGBA")
    for x, y, vx, vy, s, c, ph in parts:
        px, py = (x + vx * t) % W, (y + vy * t) % H
        px, py = px + (cx - px) * converge, py + (cy - py) * converge
        a = int(255 * alpha * (0.35 + 0.65 * (0.5 + 0.5 * math.sin(ph + t * 3))))
        d.ellipse([px - s, py - s, px + s, py + s], fill=c + (a,))

def _base(t, drift=40):
    im = bg_gradient(); grid(im, offset=t * drift); return im

_BASE = None
def base_frame(t):
    global _BASE
    if _BASE is None: _BASE = bg_gradient()
    im = _BASE.copy(); grid(im, offset=t * 40); return im

def _vignette():
    y, x = np.ogrid[:H, :W]; r = np.sqrt(((x - W/2) / (W/2)) ** 2 + ((y - H/2) / (H/2)) ** 2)
    a = np.clip((r - 0.7) * 160, 0, 170).astype(np.uint8)
    v = np.zeros((H, W, 4), np.uint8); v[..., 3] = a; return Image.fromarray(v, "RGBA")
VIG = None
def vignette():
    global VIG
    if VIG is None: VIG = _vignette()
    return VIG

def mux(video, cues, out, dur, music=False):
    """Attach a synthesized SFX mix (and optional music bed) to a silent clip."""
    from mixer import mix_cues
    wav = out + ".wav"; mix_cues(cues, dur, wav, music=music)
    os.system(f'ffmpeg -loglevel error -y -i "{video}" -i "{wav}" -c:v copy -c:a aac -b:a 192k -shortest "{out}"')
    os.remove(wav)


def comp(im, layer, pos=(0, 0)):
    """Alpha-blend an RGBA layer onto an RGB frame (ImageDraw on RGBA would overwrite alpha)."""
    im.paste(layer, pos, layer)
# ---------------------------------------------------------------- intro
def intro(path, series=None, title=None, subtitle=None, dur=6.5):
    """Logo slam + channel name + episode title slot. series/title None -> generic placeholder slot."""
    parts = _particles(); n = int(dur * FPS); w = Writer(path); L = logo(300)
    fname = font("display", 104, 800); ftag = font("sans", 34, 500)
    for i in range(n):
        t = i / FPS; im = base_frame(t)
        conv = ease_in_out(t / 1.4) if t < 1.4 else 0
        _draw_particles(im, parts, t, converge=conv * 0.92, cy=H/2 - 80, alpha=1 - 0.6 * clamp01((t - 1.4) / 0.6))
        fx = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(fx)
        # diagonal light sweep 0.9-1.5
        if 0.9 < t < 1.6:
            p = ease_in_out((t - 0.9) / 0.7); x0 = -600 + p * (W + 1200)
            d.polygon([(x0, 0), (x0 + 120, 0), (x0 - 300, H), (x0 - 420, H)], fill=SKY + (90,))
        # shockwave ring at 1.4
        if 1.4 < t < 2.3:
            p = ease_out((t - 1.4) / 0.9); r = 160 + p * 900
            cx, cy = W/2 - 0 if t < 2.0 else W/2, H/2 - 80
            d.ellipse([W/2 - r, H/2 - 80 - r, W/2 + r, H/2 - 80 + r], outline=PINK + (int(220 * (1 - p)),), width=int(6 + 10 * (1 - p)))
        # logo: pop in at 1.4, slide left at 2.1
        if t >= 1.4:
            s = back_out((t - 1.4) / 0.5) * 1.0; sz = max(4, int(300 * s))
            mv = ease_in_out((t - 2.1) / 0.6); lx = W/2 + (-560 - 0) * mv * 1.0
            lx = W/2 - 500 * mv - 0; ly = H/2 - 80 - 40 * mv
            li = L.resize((sz, sz), Image.LANCZOS)
            ring = Image.new("RGBA", (sz + 80, sz + 80), (0, 0, 0, 0))
            ImageDraw.Draw(ring).ellipse([40, 40, sz + 40, sz + 40], fill=PINK + (140,))
            fx.alpha_composite(ring.filter(ImageFilter.GaussianBlur(22)), (int(lx - sz/2 - 40), int(ly - sz/2 - 40)))
            fx.alpha_composite(li, (int(lx - sz/2), int(ly - sz/2)))
        # channel name reveal 2.3+
        if t >= 2.3:
            p = ease_out((t - 2.3) / 0.6); tx = int(W/2 - 300 + 60 * (1 - p)); ty = H/2 - 80 - 40
            txt = Image.new("RGBA", (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(txt)
            td.text((tx, ty - 70), "BUILD WITH WAQAR", font=fname, fill=TEXT + (int(255 * p),))
            q = ease_out((t - 2.6) / 0.5)
            td.text((tx + 4, ty + 60), "Java  ·  Algorithms  ·  Design Patterns  ·  System Design", font=ftag, fill=SKY + (int(255 * q),))
            fx.alpha_composite(glow(txt, 14, 0.9) if t < 3.2 else txt)
        # episode slot 3.3+
        if t >= 3.3:
            p = ease_in_out((t - 3.3) / 0.5)
            x1 = int(W/2 - 760 + 1520 * p); d.rectangle([W/2 - 760, 700, x1, 704], fill=SKY + (255,))
            d.rectangle([W/2 - 760, 700, W/2 - 760 + int(300 * p), 704], fill=PINK + (255,))
            q = ease_out((t - 3.6) / 0.6); a = int(255 * q); dy = int(30 * (1 - q))
            if title:
                d.text((W/2 - 760, 726 + dy), series.upper(), font=font("sans", 36, 600), fill=B.ACCENT + (a,))
                ft = fit_font(d, title, "display", 92, 800, 1520)
                d.text((W/2 - 760, 776 + dy), title, font=ft, fill=TEXT + (a,))
                if subtitle:
                    d.text((W/2 - 760, 890 + dy), subtitle, font=font("sans", 40, 400), fill=MUTED + (a,))
            else:
                if series: d.text((W/2 - 760, 712 + dy), series.upper(), font=font("sans", 30, 600), fill=B.ACCENT + (a,))
                for xx in range(int(W/2 - 760), int(W/2 + 760), 28):
                    d.line([(xx, 740), (xx + 14, 740)], fill=MUTED + (a,), width=2); d.line([(xx, 900), (xx + 14, 900)], fill=MUTED + (a,), width=2)
                d.text((W/2 - 740, 770 + dy), "EPISODE TITLE SLOT  —  add text in CapCut", font=font("sans", 52, 600), fill=MUTED + (a,))
        comp(im, fx); comp(im, vignette())
        if t > dur - 0.5:  # fade to slide bg
            k = (t - (dur - 0.5)) / 0.5; im = Image.blend(im, Image.new("RGB", (W, H), BG), ease_in_out(k))
        w.write(im)
    w.close()
    return [(0.0, "riser.wav", -4), (1.38, "impact.wav", -2), (2.25, "swoosh.wav", -8), (3.3, "whoosh.wav", -8), (3.65, "pop.wav", -10), (dur - 0.6, "swoosh.wav", -12)]

# ---------------------------------------------------------------- outro
END_BOXES = [(1060, 150, 1800, 566), (1060, 610, 1800, 1026)]  # YouTube end-screen video slots (16:9)
def outro(path, next_text="Next up · next episode", repo="github.com/waqarys", dur=9.5, show_slots=True):
    parts = _particles(seed=9); n = int(dur * FPS); w = Writer(path); L = logo(150)
    for i in range(n):
        t = i / FPS; im = base_frame(t); _draw_particles(im, parts, t, alpha=0.6)
        d = ImageDraw.Draw(im, "RGBA")
        p = ease_out(t / 0.6); x0 = int(110 - 80 * (1 - p)); a = int(255 * p)
        comp(im, L, (x0, 150)) if p > 0.05 else None
        d.text((x0 + 180, 168), "Thanks for watching!", font=font("display", 60, 800), fill=TEXT + (a,))
        d.text((x0 + 182, 252), "Build with Waqar", font=font("sans", 34, 500), fill=SKY + (a,))
        # subscribe button: pops at 1.0, clicked at 2.2
        if t >= 1.0:
            s = back_out((t - 1.0) / 0.4); bw, bh = int(460 * s), int(110 * s); bx, by = 110 + 230, 430
            clicked = t >= 2.25; col = (60, 66, 82) if clicked else (229, 45, 39)
            btn = Image.new("RGBA", (W, H), (0, 0, 0, 0)); bd = ImageDraw.Draw(btn)
            bd.rounded_rectangle([bx - bw/2, by - bh/2, bx + bw/2, by + bh/2], radius=int(22 * s), fill=col + (255,))
            if s > 0.6:
                lab = "SUBSCRIBED" if clicked else "SUBSCRIBE"; f = font("display", 46, 800)
                tx = bx - text_w(bd, lab, f)/2 - (24 if clicked else 0)
                bd.text((tx, by - 30), lab, font=f, fill=(255, 255, 255, 255))
                if clicked:
                    ex = tx + text_w(bd, lab, f) + 22
                    bd.line([(ex, by + 2), (ex + 12, by + 14), (ex + 34, by - 12)], fill=(255, 255, 255, 255), width=7, joint="curve")
            if not clicked: btn = glow(btn, 16, 0.8)
            comp(im, btn)
            # bell
            if t >= 2.6:
                q = back_out((t - 2.6) / 0.35); r = int(52 * q); cx, cy = bx + 300, by
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=PANEL + (255,), outline=GOLD + (255,), width=4)
                wob = math.sin((t - 2.6) * 25) * 12 * max(0, 1 - (t - 2.6)); fb = font("sans", 50, 700)
                bell = Image.new("RGBA", (120, 120), (0, 0, 0, 0)); ImageDraw.Draw(bell).text((30, 22), "🔔", font=fb, fill=GOLD)
                b2 = Image.new("RGBA", (120, 120), (0, 0, 0, 0)); bdd = ImageDraw.Draw(b2)
                bdd.pieslice([30, 25, 90, 95], 180, 360, fill=GOLD); bdd.rectangle([30, 58, 90, 80], fill=GOLD)
                bdd.rectangle([22, 78, 98, 86], fill=GOLD); bdd.ellipse([52, 86, 68, 102], fill=GOLD)
                b2 = b2.resize((int(80 * q) or 1, int(80 * q) or 1)).rotate(wob, resample=Image.BICUBIC)
                comp(im, b2, (cx - b2.width // 2, cy - b2.height // 2 - 2))
            # cursor
            if 1.5 <= t < 3.0:
                k = ease_in_out((t - 1.5) / 0.7); cx, cy = int(700 - 260 * k), int(700 - 250 * k)
                pr = 0.85 if 2.15 < t < 2.35 else 1.0
                pts = [(0, 0), (0, 46), (12, 35), (21, 56), (29, 52), (20, 32), (36, 32)]
                d.polygon([(cx + x * pr, cy + y * pr) for x, y in pts], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255))
        # next episode + repo
        if t >= 3.2:
            q = ease_out((t - 3.2) / 0.6); a = int(255 * q); dx = int(-40 * (1 - q))
            d.rounded_rectangle([110 + dx, 600, 980 + dx, 760], radius=20, fill=PANEL + (int(200 * q),), outline=B.ACCENT + (a,), width=3)
            d.rectangle([110 + dx, 600, 120 + dx, 760], fill=B.ACCENT + (a,))
            ft = fit_font(d, next_text, "sans", 44, 700, 820)
            d.text((150 + dx, 625), "WATCH NEXT", font=font("sans", 28, 700), fill=B.ACCENT + (a,))
            d.text((150 + dx, 672), next_text, font=ft, fill=TEXT + (a,))
        if t >= 4.0:
            q = ease_out((t - 4.0) / 0.6); a = int(255 * q)
            d.text((112, 810), "CODE + SLIDES", font=font("sans", 28, 700), fill=PINK + (a,))
            ft = fit_font(d, repo, "mono", 40, 600, 880)
            d.text((112, 850), repo, font=ft, fill=TEXT + (a,))
        # end-screen safe slots (YouTube places video cards here)
        if show_slots:
            q = ease_out((t - 0.4) / 0.8)
            for (x0b, y0b, x1b, y1b) in END_BOXES:
                d.rounded_rectangle([x0b, y0b, x1b, y1b], radius=18, fill=(255, 255, 255, int(10 * q)), outline=SKY + (int(60 * q),), width=2)
        comp(im, vignette())
        if t < 0.3: im = Image.blend(Image.new("RGB", (W, H), BG), im, t / 0.3)
        if t > dur - 0.6: im = Image.blend(im, Image.new("RGB", (W, H), (0, 0, 0)), ease_in_out((t - dur + 0.6) / 0.6))
        w.write(im)
    w.close()
    return [(0.0, "whoosh.wav", -8), (1.0, "pop.wav", -6), (2.22, "click.wav", -2), (2.6, "ding.wav", -10), (3.2, "swoosh.wav", -10), (4.0, "pop.wav", -12)]

# ---------------------------------------------------------------- stingers (alpha MOV)
STING_DUR = 0.7
def stinger(path, style):
    n = int(STING_DUR * FPS); w = Writer(path, alpha=True); L = logo(170); r = random.Random(11)
    for i in range(n):
        p = i / (n - 1); im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        if style == "swipe":
            cols = [PINK, SKY, PURPLE, BG]
            for k, c in enumerate(cols):
                q = ease_in_out(clamp01(p * 1.35 - k * 0.08)) ; x = -W - 600 + q * (2 * W + 1200)
                x = x + 0  # band left edge
                d.polygon([(x, 0), (x + W + 300, 0), (x + W, H), (x - 300, H)], fill=c + (255,))
            if 0.38 < p < 0.62: im.alpha_composite(L, (W//2 - 85, H//2 - 85))
        elif style == "glitch":
            cover = 1 - abs(p - 0.5) * 2  # 0..1..0
            iris = ease_in_out(clamp01(cover * 1.6))
            if iris > 0:
                rw, rh = W * 1.1 * iris, H * 1.1 * iris
                d.rectangle([W/2 - rw/2, H/2 - rh/2, W/2 + rw/2, H/2 + rh/2], fill=BG + (255,))
            lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
            for _ in range(int(10 + 50 * cover)):
                y = r.randint(0, H); hh = r.choice([2, 3, 4, 6, 10, 18, 28]); off = r.randint(-300, 300)
                c = r.choice([SKY, PINK, PURPLE, TEXT, SKY]); x0 = r.randint(-200, W); ln = r.randint(80, 700)
                a = int((90 + 150 * cover) * r.uniform(0.5, 1))
                ld.rectangle([x0 + off, y, x0 + off + ln, y + hh], fill=c + (a,))
                ld.rectangle([x0 + off + 8, y + hh, x0 + off + ln + 8, y + hh + 2], fill=(255, 0, 80, a // 2))
            if iris > 0.2:
                for yy in range(0, H, 6): ld.line([(0, yy), (W, yy)], fill=(0, 0, 0, int(60 * iris)), width=2)
            im.alpha_composite(lay); d = ImageDraw.Draw(im)
            if cover > 0.75:
                for dx, c in [(-14, (255, 0, 80)), (14, (0, 220, 255)), (0, TEXT)]:
                    f = font("display", 160, 900); s = "</>"
                    tl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(tl).text((W/2 - text_w(d, s, f)/2 + dx, H/2 - 110), s, font=f, fill=c + (230,)); im.alpha_composite(tl)
        elif style == "lightleak":
            cover = math.sin(math.pi * p) ** 1.5
            y, x = np.ogrid[:H//4, :W//4]; arr = np.zeros((H//4, W//4, 4), np.float32)
            for (cx, cy, rad, col) in [(0.2 + 0.6 * p, 0.3, 0.5, PINK), (0.8 - 0.5 * p, 0.7, 0.55, GOLD), (0.5, 0.5, 0.35 + 0.5 * cover, (255, 245, 235))]:
                g = np.exp(-(((x / (W/4) - cx) ** 2 + (y / (H/4) - cy) ** 2) / (rad ** 2)))[..., None]
                arr[..., :3] += g * np.array(col); arr[..., 3:] += g * 255
            arr[..., :3] /= np.maximum(arr[..., 3:] / 255, 1e-3); arr[..., 3] = np.clip(arr[..., 3] * cover ** 2 * 1.8, 0, 255)
            arr[..., :3] = np.clip(arr[..., :3], 0, 255)
            im = Image.fromarray(arr.astype(np.uint8), "RGBA").resize((W, H), Image.BILINEAR)
        w.write(im)
    w.close()
    return {"swipe": [(0.0, "whoosh.wav", -6)], "glitch": [(0.05, "glitch.wav", -6)],
            "lightleak": [(0.0, "shimmer.wav", -8)]}[style]

def flatten_stinger(mov, mp4, bg=(0, 255, 0), cues=None):
    """MP4 version (no alpha) over chroma green, with SFX baked in, for CapCut chroma-key."""
    tmp = mp4 + ".v.mp4"
    os.system(f'ffmpeg -loglevel error -y -f lavfi -i color=c=0x{bg[0]:02x}{bg[1]:02x}{bg[2]:02x}:s={W}x{H}:r={FPS}:d={STING_DUR} '
              f'-i "{mov}" -filter_complex "[0][1]overlay=format=auto,format=yuv420p" -t {STING_DUR} -c:v libx264 -crf 16 "{tmp}"')
    mux(tmp, cues, mp4, STING_DUR + 0.3); os.remove(tmp)

# ---------------------------------------------------------------- section card
def section_card(path, label, number=1, episode="", dur=2.2):
    n = int(dur * FPS); w = Writer(path); fnum = font("display", 340, 900)
    for i in range(n):
        t = i / FPS; im = base_frame(t); d = ImageDraw.Draw(im, "RGBA")
        p = ease_out(t / 0.5)
        num = f"{number:02d}"; nl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); nd = ImageDraw.Draw(nl)
        nd.text((140 + int(60 * (1 - p)), 300), num, font=fnum, fill=(0, 0, 0, 0), stroke_width=5, stroke_fill=B.ACCENT + (int(140 * p),))
        comp(im, nl)
        q = ease_in_out((t - 0.15) / 0.45); d.rectangle([700, 600, 700 + int(1000 * q), 608], fill=B.ACCENT + (255,))
        d.rectangle([700, 600, 700 + int(180 * q), 608], fill=PINK + (255,))
        r = ease_out((t - 0.3) / 0.5); a = int(255 * r)
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        f = fit_font(ld, label.upper(), "display", 120, 900, 1150)
        ld.text((700 + int(80 * (1 - r)), 450), label.upper(), font=f, fill=TEXT + (a,))
        ld.text((702, 630), f"SECTION {number}" + (f"   ·   {episode}" if episode else ""), font=font("sans", 36, 600), fill=MUTED + (int(255 * ease_out((t - 0.55) / 0.5)),))
        comp(im, glow(lay, 12, 0.6) if t < 1.0 else lay); comp(im, vignette())
        w.write(im)
    w.close()
    return [(0.25, "swoosh.wav", -8), (0.45, "pop.wav", -10)]

# ---------------------------------------------------------------- static overlays
def lower_third(path, name="Waqar Shaikh", topic="Build with Waqar", y=860):
    """y=860 for full-frame slides; y=905 keeps it below the safe-layout content box (ends at 879)."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x, h = 90, 130; f1 = font("display", 50, 800); f2 = font("sans", 32, 500)
    wd = max(text_w(d, name, f1), text_w(d, topic, f2)) + 230
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([x + 6, y + 10, x + wd + 6, y + h + 10], 26, fill=(0, 0, 0, 150))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    d.rounded_rectangle([x, y, x + wd, y + h], 26, fill=(15, 23, 42, 235), outline=SKY + (255,), width=3)
    d.rectangle([x + 150, y + 22, x + 154, y + h - 22], fill=PINK)
    im.alpha_composite(logo(100), (x + 26, y + 15))
    d.text((x + 178, y + 16), name, font=f1, fill=TEXT); d.text((x + 180, y + 80), topic, font=f2, fill=SKY)
    im.save(path)

PIP = (1380, 700, 1860, 1020)  # x0,y0,x1,y1 rounded-rect PiP (480x320 incl. border)
def facecam_frame(path, shape="rounded", placeholder=False, box=PIP, label=True):
    """Brand-coloured facecam frame with soft shadow. placeholder=True fills the hole with a labelled stand-in."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); x0, y0, x1, y1 = box
    if shape == "circle":
        s = min(x1 - x0, y1 - y0); x0, y0 = x1 - s, y1 - s
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    shp = sd.ellipse if shape == "circle" else (lambda b, **k: sd.rounded_rectangle(b, 34, **k))
    shp([x0 + 8, y0 + 16, x1 + 8, y1 + 16], fill=(0, 0, 0, 170)); im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    # gradient border ring
    ring = Image.new("RGBA", (W, H), (0, 0, 0, 0)); rd = ImageDraw.Draw(ring)
    grad = np.zeros((H, W, 4), np.uint8); xs = np.linspace(0, 1, x1 - x0 + 12)[None, :, None]
    g = (np.array(SKY) * (1 - xs) + np.array(PINK) * xs).astype(np.uint8)
    grad[y0 - 6:y1 + 6, x0 - 6:x1 + 6, :3] = g; grad[..., 3] = 255
    mask = Image.new("L", (W, H), 0); md = ImageDraw.Draw(mask)
    if shape == "circle": md.ellipse([x0 - 6, y0 - 6, x1 + 6, y1 + 6], fill=255); md.ellipse([x0 + 2, y0 + 2, x1 - 2, y1 - 2], fill=0)
    else: md.rounded_rectangle([x0 - 6, y0 - 6, x1 + 6, y1 + 6], 38, fill=255); md.rounded_rectangle([x0 + 2, y0 + 2, x1 - 2, y1 - 2], 30, fill=0)
    gi = Image.fromarray(grad, "RGBA"); gi.putalpha(mask)
    # clear the hole (shadow must not darken the camera)
    hole = Image.new("L", (W, H), 0); hd = ImageDraw.Draw(hole)
    (hd.ellipse if shape == "circle" else (lambda b, **k: hd.rounded_rectangle(b, 30, **k)))([x0 + 2, y0 + 2, x1 - 2, y1 - 2], fill=255)
    a = np.asarray(im).copy(); a[np.asarray(hole) > 0] = 0; im = Image.fromarray(a, "RGBA")
    if placeholder:
        ph = Image.new("RGBA", (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(ph)
        pd.rectangle([x0, y0, x1, y1], fill=(36, 30, 70, 255))
        cx, cy = (x0 + x1) // 2, (y0 + y1) // 2 - 30; rr = (y1 - y0) // 7
        pd.ellipse([cx - rr, cy - rr - 20, cx + rr, cy + rr - 20], fill=MUTED + (160,))
        pd.pieslice([cx - 2.2 * rr, cy + rr - 10, cx + 2.2 * rr, cy + 5 * rr], 180, 360, fill=MUTED + (160,))
        if label:
            f = font("sans", 22 if shape == "circle" else 24, 700); s1 = "YOUR FACE CAM GOES HERE"; s2 = "(OBS · Slides + Facecam PiP)"
            pd.rectangle([x0, y1 - 74, x1, y1], fill=(0, 0, 0, 150))
            pd.text((cx - text_w(pd, s1, f) / 2, y1 - 68), s1, font=f, fill=GOLD); f2 = font("sans", 20, 500)
            pd.text((cx - text_w(pd, s2, f2) / 2, y1 - 38), s2, font=f2, fill=TEXT)
        hm = Image.new("L", (W, H), 0); (ImageDraw.Draw(hm).ellipse if shape == "circle" else (lambda b, **k: ImageDraw.Draw(hm).rounded_rectangle(b, 30, **k)))([x0 + 2, y0 + 2, x1 - 2, y1 - 2], fill=255)
        ph.putalpha(Image.fromarray(np.minimum(np.asarray(ph)[..., 3], np.asarray(hm))))
        im.alpha_composite(ph)
    im.alpha_composite(gi); im.save(path)

def key_badge(path, text):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = fit_font(d, text, "sans", 42, 700, 1300); tw = text_w(d, text, f); bw = tw + 330; x0 = (W - bw) // 2; y0 = 900
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([x0, y0 + 10, x0 + bw, y0 + 110], 30, fill=(0, 0, 0, 170))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(16)))
    gl = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(gl).rounded_rectangle([x0, y0, x0 + bw, y0 + 100], 30, outline=GOLD + (255,), width=6)
    im.alpha_composite(gl.filter(ImageFilter.GaussianBlur(10)))
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + 100], 30, fill=(15, 23, 42, 245), outline=GOLD, width=3)
    d.rounded_rectangle([x0 + 14, y0 + 14, x0 + 250, y0 + 86], 20, fill=GOLD)
    d.text((x0 + 36, y0 + 28), "KEY POINT", font=font("display", 36, 900), fill=BG)
    d.text((x0 + 280, y0 + 24), text, font=f, fill=TEXT); im.save(path)

def facecam_full(path, hook_text, dur, name="Waqar Shaikh"):
    """Full-frame talking-head placeholder (hook scene) with kinetic hook caption."""
    n = int(dur * FPS); w = Writer(path); parts = _particles(60, 21)
    base = Image.new("RGB", (W, H), (28, 24, 52))
    bd = ImageDraw.Draw(base)
    for (cx, cy, r, c) in [(300, 250, 260, PURPLE), (1600, 300, 320, (30, 64, 110)), (1500, 900, 240, (120, 50, 120)), (400, 900, 200, (30, 80, 120))]:
        bd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
    base = base.filter(ImageFilter.GaussianBlur(90))  # "background blur" look
    sil = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sil)
    sd.ellipse([W/2 - 150, 230, W/2 + 150, 590], fill=(90, 100, 125, 255)); sd.pieslice([W/2 - 430, 600, W/2 + 430, 1500], 180, 360, fill=(90, 100, 125, 255))
    sil = sil.filter(ImageFilter.GaussianBlur(3))
    words = hook_text.split()
    for i in range(n):
        t = i / FPS; im = base.copy(); _draw_particles(im, parts, t, alpha=0.25); comp(im, sil)
        d = ImageDraw.Draw(im, "RGBA")
        # rule-of-thirds guides + label
        for gx in (W // 3, 2 * W // 3): d.line([(gx, 0), (gx, H)], fill=(255, 255, 255, 28), width=2)
        for gy in (H // 3, 2 * H // 3): d.line([(0, gy), (W, gy)], fill=(255, 255, 255, 28), width=2)
        d.rounded_rectangle([60, 50, 1010, 150], 22, fill=(0, 0, 0, 150), outline=GOLD, width=3)
        d.text((90, 62), "YOUR FACE CAM GOES HERE", font=font("display", 44, 900), fill=GOLD)
        d.text((92, 112), "OBS scene: Full Facecam (talking-head hook) — eyes on the top third line", font=font("sans", 22, 500), fill=TEXT)
        # REC dot
        if int(t * 2) % 2 == 0: d.ellipse([W - 190, 78, W - 160, 108], fill=(239, 68, 68, 255))
        d.text((W - 150, 72), "REC", font=font("sans", 34, 800), fill=TEXT)
        # kinetic caption: words appear across the duration
        k = int(len(words) * clamp01(t / (dur * 0.85))) + 1; shown = words[:k]
        lines, cur = [], ""
        f = font("display", 54, 800)
        for wd in shown[-16:]:
            if text_w(d, cur + " " + wd, f) > 1500: lines.append(cur); cur = wd
            else: cur = (cur + " " + wd).strip()
        lines.append(cur); lines = lines[-2:]
        y = 860 - 70 * (len(lines) - 1)
        for ln in lines:
            tw = text_w(d, ln, f); d.rounded_rectangle([W/2 - tw/2 - 30, y - 8, W/2 + tw/2 + 30, y + 70], 16, fill=(0, 0, 0, 170))
            d.text((W/2 - tw/2, y), ln, font=f, fill=TEXT); y += 82
        # brand frame
        d.rounded_rectangle([18, 18, W - 18, H - 18], 30, outline=SKY + (180,), width=4)
        comp(im, vignette()); w.write(im)
    w.close()

def thumbnail(path, slide, big, small, tag, series):
    """1280x720 thumbnail: face-cam cut-out slot left? -> we keep code/slide right + big text left."""
    Wt, Ht = 1280, 720; im = Image.new("RGBA", (Wt, Ht), BG + (255,))
    bgi = bg_gradient(Wt, Ht, BG2, (40, 20, 90)).convert("RGBA"); im.alpha_composite(bgi)
    sl = Image.open(slide).convert("RGBA").resize((820, 461), Image.LANCZOS).rotate(-6, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", (Wt, Ht), (0, 0, 0, 0)); sh.alpha_composite(Image.new("RGBA", sl.size, (0, 0, 0, 180)), (560, 200))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(20)))
    sl.putalpha(Image.fromarray((np.asarray(sl)[..., 3] * 0.9).astype(np.uint8)))
    im.alpha_composite(sl, (540, 160))
    d = ImageDraw.Draw(im)
    fb = fit_font(d, big, "display", 190, 900, 760)
    lay = Image.new("RGBA", (Wt, Ht), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
    ld.text((60, 150), big, font=fb, fill=TEXT, stroke_width=8, stroke_fill=BG)
    im.alpha_composite(glow(lay, 16, 0.5))
    fs = fit_font(d, small, "display", 64, 800, 720)
    d.rounded_rectangle([56, 400, 76 + text_w(d, small, fs) + 30, 490], 16, fill=GOLD)
    d.text((80, 408), small, font=fs, fill=BG)
    d.rounded_rectangle([60, 40, 60 + text_w(d, tag, font("display", 40, 900)) + 40, 104], 14, fill=(229, 45, 39))
    d.text((80, 46), tag, font=font("display", 40, 900), fill=(255, 255, 255))
    d.text((64, 640), series, font=font("sans", 32, 600), fill=B.ACCENT)
    im.alpha_composite(logo(120), (Wt - 150, 30))
    # facecam slot hint (cut-out goes bottom-right)
    im.convert("RGB").save(path)


# ---------------------------------------------------------------- safe layout (content left, camera right column)
def _rr_mask(box, r, shape="rounded"):
    m = Image.new("L", (W, H), 0); md = ImageDraw.Draw(m)
    (md.ellipse(box, fill=255) if shape == "circle" else md.rounded_rectangle(box, r, fill=255)); return m

def safe_frame(path, shape="rounded", series="", placeholder=False, cam=True, content_png=None, cam_label="YOUR FACE CAM"):
    """Opaque branded frame with a transparent 16:9 content hole (left) and a camera hole (right column).
    content_png: if given, the slide is scaled into the hole (used by build_episode)."""
    im = bg_gradient().convert("RGBA"); grid(im, 0, 12); d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = CONTENT; cx0, cy0, cx1, cy1 = CAM
    # content shadow + accent border
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle([x0 + 6, y0 + 12, x1 + 6, y1 + 12], 18, fill=(0, 0, 0, 170))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(16)))
    ImageDraw.Draw(im).rounded_rectangle([x0 - 4, y0 - 4, x1 + 4, y1 + 4], 20, outline=B.ACCENT + (255,), width=4)
    # right column branding
    col_x = (cx0 + cx1) // 2; im.alpha_composite(logo(120), (col_x - 60, 420))
    d = ImageDraw.Draw(im); f = font("display", 30, 800)
    for k, ln in enumerate(["BUILD WITH", "WAQAR"]): d.text((col_x - text_w(d, ln, f) / 2, 560 + k * 38), ln, font=f, fill=TEXT)
    if series:
        fs = font("sans", 22, 700); words = series.split(" · "); y = 660
        for wd in words:
            d.text((col_x - text_w(d, wd, fs) / 2, y), wd, font=fs, fill=B.ACCENT); y += 30
    # bottom strip hint (captions / lower third live here)
    d.rectangle([x0, y1 + 30, x0 + 160, y1 + 34], fill=B.ACCENT + (255,)); d.rectangle([x0, y1 + 30, x0 + 40, y1 + 34], fill=PINK + (255,))
    # punch holes
    a = np.asarray(im).copy(); a[np.asarray(_rr_mask([x0, y0, x1, y1], 16)) > 0, 3] = 0
    if cam:
        sh2 = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh2)
        (sd.ellipse if shape == "circle" else (lambda b, **k: sd.rounded_rectangle(b, 30, **k)))([cx0 + 6, cy0 + 12, cx1 + 6, cy1 + 12], fill=(0, 0, 0, 170))
        tmp = Image.fromarray(a, "RGBA"); tmp.alpha_composite(sh2.filter(ImageFilter.GaussianBlur(16))); a = np.asarray(tmp).copy()
        a[np.asarray(_rr_mask([cx0, cy0, cx1, cy1], 30, shape)) > 0, 3] = 0
    im = Image.fromarray(a, "RGBA")
    if cam:  # gradient ring
        ring = Image.new("RGBA", (W, H), (0, 0, 0, 0)); grad = np.zeros((H, W, 4), np.uint8)
        xs = np.linspace(0, 1, cx1 - cx0 + 12)[None, :, None]; grad[cy0 - 6:cy1 + 6, cx0 - 6:cx1 + 6, :3] = (np.array(B.ACCENT) * (1 - xs) + np.array(PINK) * xs).astype(np.uint8); grad[..., 3] = 255
        outer = _rr_mask([cx0 - 6, cy0 - 6, cx1 + 6, cy1 + 6], 36, shape); inner = _rr_mask([cx0 + 1, cy0 + 1, cx1 - 1, cy1 - 1], 30, shape)
        m = np.where(np.asarray(inner) > 0, 0, np.asarray(outer)).astype(np.uint8); gi = Image.fromarray(grad, "RGBA"); gi.putalpha(Image.fromarray(m)); im.alpha_composite(gi)
    if content_png or placeholder:
        base = Image.new("RGBA", (W, H), BG + (255,))
        if content_png:
            sl = Image.open(content_png).convert("RGBA").resize((x1 - x0, y1 - y0), Image.LANCZOS); base.paste(sl, (x0, y0))
        if placeholder and cam:
            pd = ImageDraw.Draw(base); pd.rectangle([cx0, cy0, cx1, cy1], fill=(36, 30, 70, 255))
            ccx, ccy = (cx0 + cx1) // 2, (cy0 + cy1) // 2 - 20; rr = 46
            pd.ellipse([ccx - rr, ccy - rr - 20, ccx + rr, ccy + rr - 20], fill=MUTED)
            pd.pieslice([ccx - 2.2 * rr, ccy + rr - 10, ccx + 2.2 * rr, ccy + 5 * rr], 180, 360, fill=MUTED)
            pd.rectangle([cx0, cy1 - 112, cx1, cy1 - 40], fill=(0, 0, 0, 255)); f1 = font("sans", 22, 800); f2 = font("sans", 17, 500)
            pd.text((ccx - text_w(pd, cam_label, f1) / 2, cy1 - 106), cam_label, font=f1, fill=GOLD)
            s2 = "placeholder · OBS camera"; pd.text((ccx - text_w(pd, s2, f2) / 2, cy1 - 72), s2, font=f2, fill=TEXT)
        base.alpha_composite(im); im = base
    im.save(path)

def annotate_layout(path, title, regions, shape="rounded", series="", cam=True, note=""):
    """Annotated layout diagram for the guide: regions = [(box, label, colour)]."""
    tmp = path + ".tmp.png"; safe_frame(tmp, shape, series, placeholder=False, cam=cam)
    im = Image.new("RGBA", (W, H), (20, 26, 40, 255)); im.alpha_composite(Image.open(tmp)); os.remove(tmp)
    d = ImageDraw.Draw(im)
    for box, label, col in regions:
        lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        ld.rectangle(box, fill=col + (55,), outline=col + (255,), width=4); im.alpha_composite(lay)
        f = font("sans", 30 if (box[2] - box[0]) > 500 else 22, 800); lines = label.split("\n"); y = box[1] + 14
        for ln in lines:
            tw = text_w(d, ln, f); d.rounded_rectangle([box[0] + 12, y - 4, box[0] + 30 + tw, y + 38], 8, fill=(0, 0, 0, 200)); d.text((box[0] + 21, y), ln, font=f, fill=col); y += 46
    d.rounded_rectangle([24, 940, 1896, 1060], 16, fill=(0, 0, 0, 210))
    d.text((48, 952), title, font=font("display", 40, 900), fill=TEXT)
    if note: d.text((48, 1008), note, font=font("sans", 26, 500), fill=MUTED)
    im.convert("RGB").save(path)
