"""Procedurally synthesise every SFX and the music bed with numpy (no samples, no copyright).
Outputs 48 kHz stereo 16-bit WAVs into assets/audio/."""
import os, wave
import numpy as np
from brand import ASSETS
SR = 48000
OUT = os.path.join(ASSETS, "audio"); os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

def t_(d): return np.arange(int(SR * d)) / SR
def onepole_lp(x, fc):
    fc = np.broadcast_to(np.asarray(fc, float), x.shape)
    a = np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); s = 0.0
    for i in range(len(x)): s = (1 - a[i]) * x[i] + a[i] * s; y[i] = s
    return y
def bandpass(x, fc, q=1.0):  # crude: lp(fc*1.4) - lp(fc/1.4)
    return onepole_lp(x, np.asarray(fc) * (1 + 0.5 / q)) - onepole_lp(x, np.asarray(fc) / (1 + 0.5 / q))
def reverb(x, secs=1.2, mix=0.25, seed=1):
    r = np.random.default_rng(seed); n = int(SR * secs)
    ir = r.standard_normal(n) * np.exp(-np.linspace(0, 6, n)); ir = onepole_lp(ir, 5000); ir /= np.abs(ir).sum() / 8
    L = len(x) + n; F = np.fft.rfft(x, L) * np.fft.rfft(ir, L)
    wet = np.fft.irfft(F, L); dry = np.pad(x, (0, n))
    return (1 - mix) * dry + mix * wet
def fade(x, a=0.005, b=0.02):
    na, nb = int(SR * a), int(SR * b); x = x.copy()
    if na: x[:na] *= np.linspace(0, 1, na)
    if nb: x[-nb:] *= np.linspace(1, 0, nb)
    return x
def norm(x, peak_db=-1.0):
    return x / (np.abs(x).max() + 1e-9) * 10 ** (peak_db / 20)
def stereo(x, width=0.0, pan_sweep=None):
    if pan_sweep is not None:
        p = np.linspace(pan_sweep[0], pan_sweep[1], len(x)); l = x * np.cos((p + 1) * np.pi / 4); r = x * np.sin((p + 1) * np.pi / 4)
        return np.stack([l, r], 1) * 1.41
    d = int(SR * 0.012 * width); r = np.concatenate([np.zeros(d), x[:len(x) - d]]) if d else x
    return np.stack([x, r * (1 - 0.1 * width)], 1)
def save(name, x, peak_db=-1.0):
    if x.ndim == 1: x = stereo(x)
    x = norm(x, peak_db); pcm = (x * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

def whoosh(d=0.75, f0=300, f1=3500, seed=0, peak=-3):
    t = t_(d); n = np.random.default_rng(seed).standard_normal(len(t))
    sweep = f0 * (f1 / f0) ** (np.sin(np.pi * t / d) ** 1.0)
    env = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2.2
    return fade(bandpass(n, sweep, 0.8) * env), peak

def main():
    x, p = whoosh(0.8, 250, 3200, 1); save("whoosh.wav", stereo(x, pan_sweep=(-0.8, 0.8)), -3)
    x, p = whoosh(0.42, 600, 6000, 2); save("swoosh.wav", stereo(x, pan_sweep=(0.6, -0.6)), -4)
    # pop / click
    t = t_(0.12); f = 900 * np.exp(-t * 30) + 250
    pop = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 45)
    pop[:96] += rng.standard_normal(96) * np.linspace(0.6, 0, 96)
    save("pop.wav", fade(pop, 0.0005, 0.01), -4)
    t = t_(0.05); click = np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 160); save("click.wav", fade(click, 0.0003, 0.005), -8)
    # ding (bell partials)
    t = t_(1.6); ding = sum(a * np.sin(2 * np.pi * 1318.5 * r * t) * np.exp(-t * dcy)
                           for r, a, dcy in [(1, 1, 3), (2.0, .35, 5), (2.76, .25, 7), (5.4, .1, 11)])
    save("ding.wav", stereo(fade(reverb(ding, 1.0, 0.2), 0.001, 0.1), 0.6), -5)
    # riser: noise + rising tone, crescendo
    d = 1.6; t = t_(d); n = rng.standard_normal(len(t))
    f = 180 * (8 ** (t / d)); tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.35
    env = (t / d) ** 2.5
    riser = (bandpass(n, 400 + 5000 * (t / d) ** 2, 1.0) + tone) * env
    save("riser.wav", stereo(fade(riser, 0.01, 0.01), 0.8), -3)
    # impact: sub boom + noise crack + tail
    t = t_(1.8); f = 110 * np.exp(-t * 6) + 38
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 3.2)
    crack = onepole_lp(rng.standard_normal(len(t)), 3000) * np.exp(-t * 28) * 2.2
    imp = reverb(boom + crack, 1.4, 0.3)[:len(t) + SR // 2]
    save("impact.wav", stereo(fade(imp, 0.0005, 0.3), 0.5), -1)
    # glitch: stuttered digital noise bursts
    d = 0.55; t = t_(d); g = np.zeros(len(t)); r2 = np.random.default_rng(5)
    for s in np.sort(r2.uniform(0, d - 0.06, 9)):
        i = int(s * SR); L = int(r2.uniform(0.015, 0.05) * SR); fq = r2.choice([220, 440, 880, 1760, 3520])
        g[i:i + L] += np.sign(np.sin(2 * np.pi * fq * np.arange(L) / SR)) * 0.4 + r2.standard_normal(L) * 0.3
    save("glitch.wav", stereo(fade(onepole_lp(g, 7000), 0.001, 0.02), 0.4), -6)
    # shimmer (light-leak) : airy noise + high chord
    d = 0.9; t = t_(d); env = np.sin(np.pi * t / d) ** 2
    sh = (bandpass(rng.standard_normal(len(t)), 7000, 1) * 0.6 +
          sum(np.sin(2 * np.pi * f * t) for f in [1760, 2217, 2637]) * 0.12) * env
    save("shimmer.wav", stereo(reverb(sh, 0.8, 0.3), 0.9), -6)
    music_bed()

def music_bed(bpm=84, bars=16):
    """Loopable lo-fi pad + pluck arpeggio. Am - F - C - G. Tails wrapped so the loop is seamless."""
    beat = 60 / bpm; bar = 4 * beat; L = int(SR * bar * bars); mix = np.zeros((L + SR * 4, 2))
    chords = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    for b in range(bars):
        ch = chords[b % 4]; s0 = int(b * bar * SR); t = t_(bar + 1.5)
        env = np.minimum(1, t / 0.8) * np.exp(-np.maximum(0, t - bar) * 3)
        pad = sum(np.sin(2 * np.pi * hz(m) * t + 0.3 * np.sin(2 * np.pi * 0.2 * t)) +
                  0.3 * np.sin(2 * np.pi * hz(m) * 2.003 * t) for m in ch) * env * 0.12
        bass = np.sin(2 * np.pi * hz(ch[0] - 12) * t) * env * 0.18
        mix[s0:s0 + len(t), 0] += pad + bass; mix[s0:s0 + len(t), 1] += pad * 0.95 + bass
        arp = ch + [ch[0] + 12, ch[1] + 12, ch[0] + 12, ch[2], ch[1]]
        for k in range(8):
            if b % 2 == 0 and k in (6,): continue
            st = s0 + int(k * beat / 2 * SR); tt = t_(1.2)
            pl = np.sin(2 * np.pi * hz(arp[k] + 12) * tt) * np.exp(-tt * 5) * 0.09
            pan = 0.3 * np.sin(k); mix[st:st + len(tt), 0] += pl * (1 - pan); mix[st:st + len(tt), 1] += pl * (1 + pan)
        for k in range(4):  # soft brushed hat on off-beats
            st = s0 + int((k + 0.5) * beat * SR); tt = t_(0.08)
            h = rng.standard_normal(len(tt)) * np.exp(-tt * 60) * 0.025; mix[st:st + len(tt)] += h[:, None]
    tail = mix[L:]; mix = mix[:L]; mix[:len(tail)] += tail  # wrap for seamless loop
    mono_rev = reverb(mix.mean(1), 2.0, 1.0, 3)[: L + SR * 2]
    wet = mono_rev[:L].copy(); wet[: SR * 2] += mono_rev[L:L + SR * 2]
    mix = mix * 0.8 + wet[:, None] * 0.25
    mix[:, 0] = onepole_lp(mix[:, 0], 3500); mix[:, 1] = onepole_lp(mix[:, 1], 3500)
    save("music_bed_loop.wav", mix, -6)

if __name__ == "__main__":
    main(); print("audio ->", OUT)
