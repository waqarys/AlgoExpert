"""Generate OBS scene collections for the AlgoExpert and LeetCode presets, for Windows, macOS and Linux.

  python scripts/make_obs.py            # writes obs/<preset>/<os>/BuildWithWaqar_<Preset>.json + overlays + layout PNGs
  python obs/configure_obs.py --preset leetcode --os mac --kit-dir "/Users/me/AlgoExpert/video-kit"

Paths inside the JSON use the placeholder VIDEOKIT_DIR; configure_obs.py swaps in your absolute path.
Device/window choices are intentionally EMPTY placeholders: pick your webcam, mic and IntelliJ window in OBS."""
import json, os, uuid
from PIL import Image, ImageDraw
from brand import *
import brand as B
import gfx
OBSDIR = os.path.join(KIT, "obs"); OV = os.path.join(ASSETS, "overlays")
P = lambda rel: "VIDEOKIT_DIR/" + rel
PRESETS = {k: json.load(open(os.path.join(KIT, "presets", f"{k}.json"))) for k in ("algoexpert", "leetcode")}
OS_IDS = {  # source type ids per OS (OBS 30.x). Linux window capture assumes X11; on Wayland use "pipewire-window-capture-source".
    "windows": {"camera": "dshow_input", "window": "window_capture", "display": "monitor_capture", "mic": "wasapi_input_capture",
                "window_settings": {"window": "", "method": 2, "cursor": True, "client_area": True}, "display_settings": {"monitor": 0, "capture_cursor": True}},
    "mac": {"camera": "av_capture_input_v2", "window": "screen_capture", "display": "screen_capture", "mic": "coreaudio_input_capture",
            "window_settings": {"type": 1, "window": 0, "show_cursor": True}, "display_settings": {"type": 0, "show_cursor": True}},
    "linux": {"camera": "v4l2_input", "window": "xcomposite_input", "display": "xshm_input", "mic": "pulse_input_capture",
              "window_settings": {"capture_window": "", "show_cursor": True}, "display_settings": {"screen": 0, "show_cursor": True}},
}
X0, Y0, X1, Y1 = CONTENT; CX0, CY0, CX1, CY1 = CAM; CW = CX1 - CX0

def overlays(key, pr):
    B.set_accent(pr["accent"]); shape = pr["pip_shape"]; series = pr["defaults"]["series"]
    gfx.safe_frame(os.path.join(OV, f"safe_frame_{key}.png"), shape, series)
    gfx.safe_frame(os.path.join(OV, f"safe_frame_{key}_nocam.png"), shape, series, cam=False)
    gfx.lower_third(os.path.join(OV, f"lower_third_{key}.png"), "Waqar Shaikh", series, y=905)
    m = Image.new("RGBA", (1920, 1080), (0, 0, 0, 0)); md = ImageDraw.Draw(m)
    (md.ellipse if shape == "circle" else (lambda b, **k: md.rounded_rectangle(b, 99, **k)))([420, 0, 1499, 1079], fill=(255, 255, 255, 255))
    m.save(os.path.join(OV, f"obs_mask_square_{shape}.png"))
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([16, 16, W - 16, H - 16], 30, outline=tuple(pr["accent"]) + (220,), width=5)
    im.alpha_composite(logo(110), (W - 150, 40)); im.save(os.path.join(OV, f"fullcam_frame_{key}.png"))
    return shape

def src(name, sid, settings, filters=None):
    return {"name": name, "uuid": str(uuid.uuid4()), "id": sid, "versioned_id": sid, "settings": settings, "enabled": True,
            "volume": 1.0, "muted": False, "mixers": 255, "monitoring_type": 0, "flags": 0, "sync": 0, "filters": filters or [],
            "hotkeys": {}, "private_settings": {}}

def item(s, iid, x=0, y=0, sc=1.0, visible=True, crop=(0, 0, 0, 0), bounds=None, locked=False):
    it = {"name": s["name"], "source_uuid": s["uuid"], "visible": visible, "locked": locked, "rot": 0.0, "pos": {"x": x, "y": y},
          "scale": {"x": sc, "y": sc}, "align": 5, "bounds_type": 0, "bounds_align": 0, "bounds": {"x": 0.0, "y": 0.0},
          "crop_left": crop[0], "crop_top": crop[1], "crop_right": crop[2], "crop_bottom": crop[3], "id": iid,
          "group_item_backup": False, "scale_filter": "lanczos", "blend_method": "default", "blend_type": "normal", "private_settings": {}}
    if bounds: it.update({"bounds_type": 2, "bounds": {"x": bounds[0], "y": bounds[1]}})
    return it

def scene(name, items):
    s = src(name, "scene", {"id_counter": len(items), "custom_size": False, "items": items}); return s

def collection(key, pr, osname, shape):
    o = OS_IDS[osname]; label = pr["name"]
    mask = {"name": "Camera shape mask", "id": "mask_filter_v2", "versioned_id": "mask_filter_v2", "enabled": True,
            "settings": {"type": "mask_alpha_filter.effect", "image_path": P(f"assets/overlays/obs_mask_square_{shape}.png")}}
    cam_settings = {}  # placeholder: choose your webcam in the source properties
    cam_col = src("Camera · side column (pick your webcam)", o["camera"], dict(cam_settings), [mask])
    cam_full = src("Camera · full (pick your webcam)", o["camera"], dict(cam_settings))
    ij = src("IntelliJ window (select your IntelliJ IDEA window)", o["window"], dict(o["window_settings"]))
    ij_full = src("IntelliJ window · full screen (select your IntelliJ IDEA window)", o["window"], dict(o["window_settings"]))
    slides = src("Slides (display capture, or swap to window capture of your PDF viewer)", o["display"], dict(o["display_settings"]))
    editor = src("Code editor window (any editor / slide code)", o["window"], dict(o["window_settings"]))
    board = src("Whiteboard window (Excalidraw / tablet app / IntelliJ debugger)", o["window"], dict(o["window_settings"]))
    img = lambda n, rel: src(n, "image_source", {"file": P(rel), "unload": False})
    frame = img("Safe layout frame", f"assets/overlays/safe_frame_{key}.png")
    full_frame = img("Full facecam frame", f"assets/overlays/fullcam_frame_{key}.png")
    lower = img("Lower third", f"assets/overlays/lower_third_{key}.png")
    media = lambda n, rel, loop: src(n, "ffmpeg_source", {"local_file": P(rel), "is_local_file": True, "looping": loop, "restart_on_activate": True, "close_when_inactive": True})
    intro = media("Intro video", f"assets/intro/intro_{key}.mp4", True); outro = media("Outro video", f"assets/outro/outro_{key}.mp4", False)
    bed = media("Music bed (low)", "assets/audio/music_bed_loop.wav", True); bed["volume"] = 0.1
    sc = CW / 1080; cam_item = lambda iid: item(cam_col, iid, CX0, CY0, sc, crop=(420, 0, 420, 0))
    content = lambda s, iid: item(s, iid, X0, Y0, bounds=(X1 - X0, Y1 - Y0))
    scenes = [
        scene(f"1 · Intro ({label})", [item(intro, 1), item(bed, 2)]),
        scene("2 · Full Facecam Hook", [item(cam_full, 1, bounds=(1920, 1080)), item(full_frame, 2, locked=True), item(lower, 3)]),
        scene("3 · Slides + PiP", [content(slides, 1), item(frame, 2, locked=True), cam_item(3), item(lower, 4, visible=False)]),
        scene("4 · Code + PiP", [content(editor, 1), item(frame, 2, locked=True), cam_item(3), item(lower, 4, visible=False)]),
        scene("5 · IntelliJ — Code + Run Console", [content(ij, 1), item(frame, 2, locked=True), cam_item(3), item(lower, 4, visible=False)]),
        scene("6 · IntelliJ — Full Screen", [item(ij_full, 1, bounds=(1920, 1080))]),
        scene("7 · Dry Run / Whiteboard", [content(board, 1), item(frame, 2, locked=True), cam_item(3)]),
        scene(f"8 · Outro ({label})", [item(outro, 1)]),
    ]
    mic_filters = [
        {"name": "1 Noise Suppression (RNNoise)", "id": "noise_suppress_filter_v2", "versioned_id": "noise_suppress_filter_v2", "enabled": True, "settings": {"method": "rnnoise"}},
        {"name": "2 Noise Gate", "id": "noise_gate_filter", "versioned_id": "noise_gate_filter", "enabled": True, "settings": {"open_threshold": -36.0, "close_threshold": -46.0}},
        {"name": "3 Compressor", "id": "compressor_filter", "versioned_id": "compressor_filter", "enabled": True, "settings": {"ratio": 4.0, "threshold": -20.0, "attack_time": 6, "release_time": 60, "output_gain": 4.0}},
        {"name": "4 Limiter", "id": "limiter_filter", "versioned_id": "limiter_filter", "enabled": True, "settings": {"threshold": -2.0, "release_time": 60}},
    ]
    mic = src("Mic/Aux (pick your microphone)", o["mic"], {}, mic_filters)
    inputs = [cam_col, cam_full, ij, ij_full, slides, editor, board, frame, full_frame, lower, intro, outro, bed]
    return {"name": f"Build with Waqar — {label} ({osname})", "current_scene": scenes[2]["name"], "current_program_scene": scenes[2]["name"],
            "scene_order": [{"name": s["name"]} for s in scenes], "sources": scenes + inputs, "groups": [], "AuxAudioDevice1": mic,
            "transitions": [], "current_transition": "Fade", "transition_duration": 300, "quick_transitions": [], "preview_locked": False,
            "scaling_enabled": False, "modules": {}}

def layouts(key, pr, shape):
    B.set_accent(pr["accent"]); s = pr["defaults"]["series"]; out = os.path.join(KIT, "docs", "layouts"); os.makedirs(out, exist_ok=True)
    A = tuple(pr["accent"]); G = (74, 222, 128); Y = GOLD; R = (248, 113, 113)
    cam = (CAM, "Facecam\n(optional)", PINK)
    gfx.annotate_layout(os.path.join(out, f"{key}-5-intellij-code-run.png"), f"{pr['name']} · 5 · IntelliJ — Code + Run Console",
        [((X0, Y0, X1, 600), "IntelliJ editor  (font 18–20 pt, Presentation/Zen mode)", G), ((X0, 606, X1, Y1), "Run / Debug console — keep it docked & visible (font 16–18)", Y), cam,
         ((X0, Y1 + 8, CX1, 934), "Bottom strip: captions / lower third only", MUTED)], shape, s,
        note="IntelliJ window is scaled into the 1520×855 box; the camera lives in the right column, never over code or the console.")
    gfx.annotate_layout(os.path.join(out, f"{key}-6-intellij-full.png"), f"{pr['name']} · 6 · IntelliJ — Full Screen (no PiP)",
        [((0, 0, 1920, 640), "IntelliJ full screen: editor", G), ((0, 646, 1920, 930), "Run / Debug console", Y)], shape, s, cam=False,
        note="Use for dense code, stack traces and debugger variables. No camera, no overlays.")
    gfx.annotate_layout(os.path.join(out, f"{key}-3-slides-pip.png"), f"{pr['name']} · 3 · Slides + PiP",
        [((X0, Y0, X1, Y1), "Slides (PDF viewer / slides.pdf, full-screen mode)", A), cam], shape, s, note="Same safe layout as Code + PiP: slide text is never under the camera.")
    gfx.annotate_layout(os.path.join(out, f"{key}-7-dry-run.png"), f"{pr['name']} · 7 · Dry Run / Whiteboard",
        [((X0, Y0, X1, Y1), "Whiteboard / tablet app / IntelliJ debugger stepping", R), cam], shape, s, note="Trace the array by hand or step with the debugger; camera stays in the column.")

def main():
    for key, pr in PRESETS.items():
        shape = overlays(key, pr); layouts(key, pr, shape)
        for osname in OS_IDS:
            d = os.path.join(OBSDIR, key, osname); os.makedirs(d, exist_ok=True)
            json.dump(collection(key, pr, osname, shape), open(os.path.join(d, f"BuildWithWaqar_{pr['name']}.json"), "w"), indent=2)
    print("obs collections + layouts written")
if __name__ == "__main__": main()
