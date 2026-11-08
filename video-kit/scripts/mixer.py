"""numpy audio mixer: narration + SFX cues + ducked music bed -> WAV."""
import os, subprocess, wave
import numpy as np
from brand import ASSETS
SR = 48000
AUD = os.path.join(ASSETS, "audio")
_c = {}
def load(path):
    if path in _c: return _c[path]
    if not os.path.isabs(path): path = os.path.join(AUD, path)
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.float32).reshape(-1, 2).copy(); _c[path] = a; return a
def db(x): return 10 ** (x / 20)
def place(buf, clip, t, gain=1.0):
    i = int(round(t * SR)); j = min(len(buf), i + len(clip))
    if i < len(buf) and j > i: buf[i:j] += clip[: j - i] * gain
def write(path, buf):
    buf = np.clip(buf, -1, 1); pcm = (buf * 32767).astype(np.int16)
    with wave.open(path, "wb") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
def music_track(dur, level_db=-24, fade_in=1.5, fade_out=2.5):
    m = load("music_bed_loop.wav"); n = int(dur * SR); reps = n // len(m) + 1
    out = np.tile(m, (reps, 1))[:n] * db(level_db)
    fi, fo = int(fade_in * SR), int(fade_out * SR)
    out[:fi] *= np.linspace(0, 1, fi)[:, None]; out[-fo:] *= np.linspace(1, 0, fo)[:, None]
    return out
def duck(music, voice, depth_db=-12, attack=0.08, release=0.5):
    """Sidechain: lower the music by depth_db while the voice is active (smoothed envelope)."""
    hop = 480; e = np.sqrt(np.mean(voice[: len(voice) // hop * hop].mean(1).reshape(-1, hop) ** 2, 1))
    active = (e > 0.01).astype(float); g = np.empty_like(active); s = 1.0
    a_att, a_rel = np.exp(-hop / (SR * attack)), np.exp(-hop / (SR * release))
    for i, v in enumerate(active):
        target = db(depth_db) if v else 1.0; a = a_att if target < s else a_rel; s = a * s + (1 - a) * target; g[i] = s
    g = np.repeat(g, hop); g = np.pad(g, (0, max(0, len(music) - len(g))), constant_values=1.0)[: len(music)]
    return music * g[:, None]
def mix_cues(cues, dur, out, music=False):
    buf = np.zeros((int(dur * SR), 2), np.float32)
    for t, name, g in cues: place(buf, load(name), t, db(g))
    if music: buf += music_track(dur, -20, 0.5, 1.5)
    write(out, buf)
