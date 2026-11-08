"""Render the shared brand pack + per-preset (AlgoExpert / LeetCode) intro, outro and section cards into assets/."""
import os, json
from brand import ASSETS, KIT
import brand as B
import gfx
from mixer import mix_cues
A = lambda *p: os.path.join(ASSETS, *p)
def slug(c): return c.lower().replace(" & ", "-").replace(" / ", "-").replace(" ", "-")
def main():
    for s in ["swipe", "glitch", "lightleak"]:
        mov = A("stingers", f"stinger_{s}.mov"); cues = gfx.stinger(mov, s)
        gfx.flatten_stinger(mov, A("stingers", f"stinger_{s}_green.mp4"), cues=cues); mix_cues(cues, 0.9, A("stingers", f"stinger_{s}_sfx.wav"))
    gfx.facecam_frame(A("overlays", "facecam_frame_rounded.png"), "rounded"); gfx.facecam_frame(A("overlays", "facecam_frame_circle.png"), "circle")
    for key in ("algoexpert", "leetcode"):
        pr = json.load(open(os.path.join(KIT, "presets", f"{key}.json"))); B.set_accent(pr["accent"]); series = pr["defaults"]["series"]
        v = A("intro", "_i.mp4"); cues = gfx.intro(v, series=series, dur=6.5); gfx.mux(v, cues, A("intro", f"intro_{key}.mp4"), 6.5, music=True); os.remove(v)
        v = A("outro", "_o.mp4"); cues = gfx.outro(v, "Next up · your next problem", pr["defaults"]["repo"]); gfx.mux(v, cues, A("outro", f"outro_{key}.mp4"), 9.5, music=True); os.remove(v)
        os.makedirs(A("cards", key), exist_ok=True)
        for i, c in enumerate(pr["sections"], 1):
            v = A("cards", "_c.mp4"); cues = gfx.section_card(v, c, i, pr["name"]); gfx.mux(v, cues, A("cards", key, f"card_{i:02d}_{slug(c)}.mp4"), 2.2); os.remove(v)
    print("assets done")
if __name__ == "__main__": main()
