#!/usr/bin/env python3
"""Make an importable OBS scene collection for YOUR machine (only rewrites a JSON file; touches nothing else).

  python obs/configure_obs.py --preset algoexpert --os windows --kit-dir "C:/Users/<you>/AlgoExpert/video-kit"
  python obs/configure_obs.py --preset leetcode   --os mac     --kit-dir "/Users/<you>/AlgoExpert/video-kit"
  python obs/configure_obs.py --preset leetcode   --os linux   --kit-dir "/home/<you>/AlgoExpert/video-kit" [--wayland]

Writes obs/<preset>/<os>/BuildWithWaqar_<Preset>.local.json -> OBS: Scene Collection > Import.
Webcam, microphone and IntelliJ window stay unselected on purpose: pick them in each source's Properties."""
import argparse, json, os
ap = argparse.ArgumentParser()
ap.add_argument("--preset", choices=["algoexpert", "leetcode"], required=True)
ap.add_argument("--os", choices=["windows", "mac", "linux"], required=True)
ap.add_argument("--kit-dir", required=True); ap.add_argument("--wayland", action="store_true")
a = ap.parse_args(); here = os.path.dirname(os.path.abspath(__file__)); d = os.path.join(here, a.preset, a.os)
src = next(f for f in os.listdir(d) if f.endswith(".json") and not f.endswith(".local.json"))
txt = open(os.path.join(d, src), encoding="utf-8").read().replace("VIDEOKIT_DIR", a.kit_dir.replace("\\", "/").rstrip("/"))
if a.wayland:
    txt = txt.replace('"xcomposite_input"', '"pipewire-window-capture-source"').replace('"xshm_input"', '"pipewire-desktop-capture-source"')
out = os.path.join(d, src.replace(".json", ".local.json")); open(out, "w", encoding="utf-8").write(txt)
json.loads(txt); print("Import in OBS (Scene Collection > Import):", out)
