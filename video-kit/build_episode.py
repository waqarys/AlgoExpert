#!/usr/bin/env python3
"""One-command episode builder for Build with Waqar.

  python build_episode.py --slides <slides_dir> --script episodes/33-saga.md --out out/demo.mp4 [--title "..."]

Script format: YAML-ish front matter (title, subtitle, series, lower_name, lower_topic, next, repo,
thumb_big, thumb_small, thumb_tag), then:
  # Section name            -> animated section card (glitch stinger + swoosh/pop)
  [NN] narration ...        -> slide NN.png with Ken Burns + voice-over (swipe stinger + whoosh between slides)
  [face-pip NN] narration   -> same, with the facecam PiP placeholder (bottom-right)
  [face] narration          -> full-frame talking-head placeholder (use under '# Hook')
  {key: text}               -> gold KEY POINT callout + ding while the line is spoken
Outputs: MP4 (H.264 1080p30, AAC, -14 LUFS), .srt next to it, and a 1280x720 thumbnail.
"""
import argparse, asyncio, os, re, shutil, subprocess, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts"))
import numpy as np
import edge_tts
from brand import W, H, FPS, ASSETS
import gfx, mixer, brand

VOICE = "en-US-GuyNeural"
STING = {"slide": "swipe", "card": "glitch", "big": "lightleak"}

def parse(path):
    txt = open(path, encoding="utf-8").read(); meta = {}
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    if m:
        for ln in m.group(1).splitlines():
            if ":" in ln: k, v = ln.split(":", 1); meta[k.strip()] = v.strip()
        txt = txt[m.end():]
    items = []
    for ln in txt.splitlines():
        ln = ln.strip()
        if not ln: continue
        if ln.startswith("# "): items.append({"kind": "card", "label": ln[2:].strip()}); continue
        m = re.match(r"\[(face-pip\s+|face)?\s*(\d+)?\]\s*(.*)", ln)
        if not m: continue
        mode, num, body = m.groups(); key = None
        km = re.search(r"\{key:\s*(.*?)\}", body)
        if km: key = km.group(1); body = body.replace(km.group(0), "").strip()
        kind = "face" if (mode or "").strip() == "face" else "slide"
        items.append({"kind": kind, "slide": num, "pip": bool(mode and "pip" in mode), "text": body, "key": key})
    return meta, items

async def _tts(text, mp3, rate):
    c = edge_tts.Communicate(text, VOICE, rate=rate); bounds = []
    with open(mp3, "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio": f.write(ch["data"])
            elif ch["type"] in ("SentenceBoundary", "WordBoundary"):
                bounds.append((ch["offset"] / 1e7, ch["duration"] / 1e7, ch["text"]))
    return bounds

def dur_of(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]))

def ken_burns(png, out, dur, idx, overlays=(), still=False):
    """Gentle zoom (1.0->1.06 or reverse) with a slow pan; overlays = [(png, t_in, t_out, anim)]."""
    n = int(round(dur * FPS)); zin = idx % 2 == 0
    z = f"1+0.04*on/{n}" if zin else f"1.04-0.04*on/{n}"  # gentle: max 4% so slide titles at the edge never clip
    if still: z = "1.0"
    px = "iw/2-(iw/zoom/2)"
    cmd = ["ffmpeg", "-loglevel", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-i", png]
    fc = f"[0]scale=3840:2160:flags=lanczos,zoompan=z='{z}':x='{px}':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS}[v0]"
    last = "v0"
    for k, (ov, t0, t1, anim) in enumerate(overlays):
        cmd += ["-loop", "1", "-framerate", str(FPS), "-i", ov]; i = k + 1
        if anim == "slide":  # lower third: slide in from left, out to left
            x = f"'if(lt(t,{t0}),-W,if(lt(t,{t0}+0.5),-W+W*(1-pow(1-(t-{t0})/0.5,3)),if(lt(t,{t1}-0.4),0,-W*pow((t-({t1}-0.4))/0.4,2))))'"
            fc += f";[{i}]format=rgba[o{i}];[{last}][o{i}]overlay=x={x}:y=0:enable='between(t,{t0},{t1})'[v{i}]"
        elif anim == "drop":  # key badge: fade + drop in
            fc += (f";[{i}]format=rgba,fade=t=in:st={t0}:d=0.3:alpha=1,fade=t=out:st={t1-0.4}:d=0.4:alpha=1[o{i}];"
                   f"[{last}][o{i}]overlay=x=0:y='if(lt(t,{t0}+0.3),60-60*(t-{t0})/0.3,0)':enable='between(t,{t0},{t1})'[v{i}]")
        else:  # fade
            fc += f";[{i}]format=rgba,fade=t=in:st={t0}:d=0.5:alpha=1[o{i}];[{last}][o{i}]overlay=0:0:enable='gte(t,{t0})'[v{i}]"
        last = f"v{i}"
    cmd += ["-filter_complex", fc + f";[{last}]format=yuv420p[out]", "-map", "[out]", "-frames:v", str(n),
            "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-r", str(FPS), out]
    subprocess.run(cmd, check=True)

def srt_time(t):
    h, r = divmod(max(t, 0), 3600); m, s = divmod(r, 60); return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",")

def build(args):
    meta, items = parse(args.script)
    if args.preset:
        pr = json.load(open(args.preset)); brand.set_accent(pr.get("accent", brand.SKY))
        for k2, v in pr.get("defaults", {}).items(): meta.setdefault(k2, v)
        if not args.pip_shape_set: args.pip_shape = pr.get("pip_shape", args.pip_shape)
    title = args.title or meta.get("title", "Episode")
    work = os.path.join(os.path.dirname(os.path.abspath(args.out)), "_work_" + os.path.splitext(os.path.basename(args.out))[0])
    os.makedirs(work, exist_ok=True); J = lambda *p: os.path.join(work, *p)
    # ---- brand clips for this episode
    intro_cues = gfx.intro(J("intro.mp4"), meta.get("series", ""), title, meta.get("subtitle")) if not os.path.exists(J("intro.mp4")) or args.force else gfx_cache(J, "intro")
    save_cues(J, "intro", intro_cues)
    outro_cues = gfx.outro(J("outro.mp4"), meta.get("next", "Next episode"), meta.get("repo", "github.com/waqarys")) if not os.path.exists(J("outro.mp4")) or args.force else gfx_cache(J, "outro")
    save_cues(J, "outro", outro_cues)
    gfx.lower_third(J("lower.png"), meta.get("lower_name", "Waqar Shaikh"), meta.get("lower_topic", title))
    gfx.facecam_frame(J("pip.png"), args.pip_shape, placeholder=True)
    stings = {s: (os.path.join(ASSETS, "stingers", f"stinger_{s}.mov")) for s in STING.values()}
    sting_cues = {"swipe": [(0.0, "whoosh.wav", -6)], "glitch": [(0.05, "glitch.wav", -6)], "lightleak": [(0.0, "shimmer.wav", -8)]}
    # ---- TTS
    rate = args.rate
    for k, it in enumerate(items):
        if it["kind"] in ("slide", "face"):
            mp3 = J(f"vo_{k:02d}.mp3")
            if not os.path.exists(mp3) or args.force:
                it["bounds"] = asyncio.run(_tts(it["text"], mp3, rate)); json.dump(it["bounds"], open(mp3 + ".json", "w"))
            else: it["bounds"] = json.load(open(mp3 + ".json"))
            it["mp3"] = mp3; it["vo"] = dur_of(mp3)
    # ---- timeline
    clips, cues, voices, subs, cuts = [], [], [], [], []
    t = 0.0; sec_no = 0; slide_idx = 0; first_slide = True
    timeline = []
    def add_clip(path, d, kind):
        nonlocal t
        if clips: cuts.append((t, kind))
        clips.append(path); t0 = t; t += d; timeline.append({"start": round(t0, 2), "dur": round(d, 2), "clip": os.path.basename(path)}); return t0
    for k, it in enumerate(items):
        if it["kind"] == "card":
            if it["label"].lower() == "hook": continue
            sec_no += 1; p = J(f"card_{sec_no:02d}.mp4")
            cc = gfx.section_card(p, it["label"], sec_no, title)
            t0 = add_clip(p, 2.2, "card"); cues += [(t0 + a, n, g) for a, n, g in cc]
            continue
        lead = 0.5; d = it["vo"] + lead + 0.9
        if it["kind"] == "face":
            p = J(f"face_{k:02d}.mp4"); gfx.facecam_full(p, it["text"], d)
            t0 = add_clip(p, d, "big")
            if k == next(i for i, x in enumerate(items) if x["kind"] != "card") :  # hook first, then intro
                pass
        else:
            png = os.path.join(args.slides, f"{int(it['slide']):02d}.png"); p = J(f"seg_{k:02d}.mp4"); ovs = []
            if it["pip"]:  # safe layout: slide shrinks into the content box, camera sits in the right column (never over code)
                comp_png = J(f"safe_{k:02d}.png"); gfx.safe_frame(comp_png, args.pip_shape, meta.get("series", ""), placeholder=True, content_png=png); png = comp_png
            if first_slide: ovs.append((J("lower.png"), 0.6, min(d - 0.2, 6.5), "slide")); first_slide = False
            if it["key"]:
                kb = J(f"key_{k:02d}.png"); gfx.key_badge(kb, it["key"]); ka = lead + it["vo"] * 0.45
                ovs.append((kb, ka, min(d - 0.1, ka + 4.0), "drop"))
            ken_burns(png, p, d, slide_idx, ovs, still=it["pip"]); slide_idx += 1
            t0 = add_clip(p, d, "slide")
            if first_slide is False and len([c for c in clips if "seg_" in c]) == 1: cues.append((t0 + 0.6, "swoosh.wav", -12))
            if it["key"]: cues.append((t0 + lead + it["vo"] * 0.45, "ding.wav", -9))
        voices.append((t0 + lead, it["mp3"]))
        for (o, du, tx) in it["bounds"]: subs.append((t0 + lead + o, t0 + lead + o + du, tx))
        if k == 1 and items[0]["label"].lower() == "hook" if items[0]["kind"] == "card" else False: pass
        # put the intro right after the hook segment
        if it["kind"] == "face" and not any("intro.mp4" in c for c in clips):
            t0 = add_clip(J("intro.mp4"), 6.5, "big"); cues += [(t0 + a, n, g) for a, n, g in intro_cues]
    if not any("intro.mp4" in c for c in clips):  # no hook -> intro first
        clips.insert(0, J("intro.mp4")); raise SystemExit("Add a '# Hook' with a [face] line, or extend builder for intro-first")
    t0 = add_clip(J("outro.mp4"), 9.5, "big"); cues += [(t0 + a, n, g) for a, n, g in outro_cues]
    total = t
    # ---- concat video
    with open(J("concat.txt"), "w") as f:
        for c in clips: f.write(f"file '{c}'\n")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", J("concat.txt"), "-c", "copy", J("base.mp4")], check=True)
    # ---- audio
    voice = np.zeros((int(total * mixer.SR) + mixer.SR, 2), np.float32)
    for t0, mp3 in voices: mixer.place(voice, mixer.load(mp3), t0, mixer.db(args.voice_db))
    sfx = np.zeros_like(voice)
    for c, kind in cuts:
        st = STING[kind]; s0 = c - gfx.STING_DUR / 2
        for a, n, g in sting_cues[st]: mixer.place(sfx, mixer.load(n), s0 + a, mixer.db(g))
    for a, n, g in cues: mixer.place(sfx, mixer.load(n), a, mixer.db(g))
    music = mixer.duck(mixer.music_track(len(voice) / mixer.SR, args.music_db), voice, -8)
    mixer.write(J("mix.wav"), voice + sfx * mixer.db(-3) + music)
    # two-pass loudnorm to -14 LUFS
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", J("mix.wav"), "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(r[r.rfind("{"): r.rfind("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    # ---- final: overlay stingers + mux
    cmd = ["ffmpeg", "-loglevel", "error", "-y", "-i", J("base.mp4"), "-i", J("mix.wav")]
    fc, last = "", "0:v"
    for i, (c, kind) in enumerate(cuts):
        cmd += ["-i", stings[STING[kind]]]; s0 = max(0, c - gfx.STING_DUR / 2)
        fc += f"[{i+2}:v]setpts=PTS+{s0:.3f}/TB[s{i}];[{last}][s{i}]overlay=eof_action=pass:format=auto[x{i}];"; last = f"x{i}"
    fc += f"[{last}]format=yuv420p[vout];[1:a]{ln},aresample=48000[aout]"
    cmd += ["-filter_complex", fc, "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-preset", "slow", "-crf", "18",
            "-profile:v", "high", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{total:.3f}", args.out]
    subprocess.run(cmd, check=True)
    # ---- SRT
    srt = os.path.splitext(args.out)[0] + ".srt"
    with open(srt, "w", encoding="utf-8") as f:
        n = 0
        for a, b, tx in subs:
            words = tx.split(); chunks = [words] if len(tx) <= 84 else [words[: len(words) // 2], words[len(words) // 2:]]
            span = (b - a) / len(chunks)
            for j, ch in enumerate(chunks):
                n += 1; f.write(f"{n}\n{srt_time(a + j * span)} --> {srt_time(a + (j + 1) * span)}\n{' '.join(ch)}\n\n")
    json.dump({"timeline": timeline, "cuts": cuts, "duration": total}, open(os.path.splitext(args.out)[0] + ".timeline.json", "w"), indent=1)
    # ---- thumbnail
    if args.thumb:
        thumb_slide = os.path.join(args.slides, f"{int(args.thumb_slide or next(x['slide'] for x in items if x['kind']=='slide')):02d}.png")
        gfx.thumbnail(args.thumb, thumb_slide, meta.get("thumb_big", title.upper()), meta.get("thumb_small", ""), meta.get("thumb_tag", "JAVA"), meta.get("series", ""))
    print(json.dumps({"out": args.out, "duration": round(total, 2), "srt": srt, "cuts": len(cuts), "sections": sec_no}, indent=1))

def save_cues(J, name, cues): json.dump(cues, open(J(name + ".cues.json"), "w"))
def gfx_cache(J, name): return json.load(open(J(name + ".cues.json")))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slides", required=True); ap.add_argument("--script", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--title"); ap.add_argument("--thumb"); ap.add_argument("--thumb-slide")
    ap.add_argument("--pip-shape", default=None, choices=["rounded", "circle"])
    ap.add_argument("--preset", help="presets/algoexpert.json or presets/leetcode.json")
    ap.add_argument("--rate", default="+4%"); ap.add_argument("--voice-db", type=float, default=0.0)
    ap.add_argument("--music-db", type=float, default=-13.0); ap.add_argument("--force", action="store_true")
    a = ap.parse_args(); a.pip_shape_set = a.pip_shape is not None; a.pip_shape = a.pip_shape or "rounded"; build(a)
