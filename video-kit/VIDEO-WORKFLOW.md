# Build with Waqar: algorithm video workflow (AlgoExpert + LeetCode)

This is the same brand kit as the design-patterns series (`waqarys/java-design-patterns/video-kit`), retuned for
algorithm episodes. There are two presets that share the logo, dark 1920×1080 look, sound effects and music. Each has its own accent colour:

| Preset | Accent | Camera shape | Slides | Java |
|---|---|---|---|---|
| **AlgoExpert** (`presets/algoexpert.json`) | sky blue #38BDF8 | rounded square | `lectures/algoexpert/<difficulty>/<category>/<Problem>/slides/` | `algoexpert/src/main/java/<difficulty>/<category>/<Problem>.java` |
| **LeetCode** (`presets/leetcode.json`) | orange #FB923C | circle | `leetcode/content/<NNNN-slug>/slides/` | `leetcode/java/src/main/java/<category>/<Problem>.java` |

Both demos are in the GitHub release **`algo-video-kit-v1`** on this repo. They're built from real
material: AlgoExpert *Two Number Sum* and LeetCode *#1 Two Sum*.

> Audio: every SFX and the music bed are synthesised in `scripts/make_audio.py` with numpy, from no third-party samples.
> That avoids the usual stock-music licensing problems. It is **not** a legal guarantee against automated claims, so keep the
> generator script as your proof of origin. The narration in the demos is text-to-speech (edge-tts `en-US-GuyNeural`) and
> is a **placeholder for your own voice**. The face-cam boxes labelled "YOUR FACE CAM" are **placeholders for your camera**.

## 1. Episode structure (algorithm sections)
```
Hook (Full Facecam, ≤15 s) → Intro 6.5 s →
 01 Problem → 02 Examples & Constraints → 03 Brute Force → 04 Optimized Approach →
 05 Dry Run → 06 Java Walkthrough → 07 Complexity → 08 Edge Cases & Recap → Outro 9.5 s
```
Each section opens with an animated card (`assets/cards/<preset>/card_0N_*.mp4`, glitch stinger + swoosh/pop).
Every slide change gets a swipe stinger + whoosh. Each KEY POINT callout gets a ding. The music sits about 20 dB under the voice.

## 2. One command per episode
```bash
# once: python3 -m venv .venv && .venv/bin/pip install pillow numpy edge-tts   (+ ffmpeg on PATH)
cd video-kit
python scripts/make_audio.py && python scripts/make_assets.py && python scripts/make_obs.py   # optional: regenerate the pack

# AlgoExpert demo (real paths on the leetcode branch)
python build_episode.py --preset presets/algoexpert.json \
  --slides ../lectures/algoexpert/easy/arrays/TwoNumberSum/slides \
  --script episodes/algoexpert/two-number-sum.md \
  --out out/algoexpert-two-number-sum.mp4 --thumb thumbnails/algoexpert-two-number-sum.png --thumb-slide 12

# LeetCode demo
python build_episode.py --preset presets/leetcode.json \
  --slides ../leetcode/content/0001-two-sum/slides \
  --script episodes/leetcode/0001-two-sum.md \
  --out out/leetcode-0001-two-sum.mp4 --thumb thumbnails/leetcode-0001-two-sum.png --thumb-slide 7
```
To make a new episode, copy one of the `episodes/*/*.md` scripts, keep the 8 `# Section` headings, and point each `[NN]` at a slide number.
Use `[face-pip NN]` on code slides: the slide shrinks into the safe content box and the camera placeholder goes in the right
column, so it never covers code. Use `{key: …}` for one callout per section, and keep callouts **off** dry-run slides, because their own
captions sit at the bottom.
Outputs: MP4 (1080p30 H.264, AAC, two-pass loudnorm to −14 LUFS), `.srt`, `.timeline.json` (use it for YouTube chapters),
and the thumbnail. Add `--voice-db -60` to get a sound-effects-and-music-only timing guide to record your own voice against.

## 3. OBS: scene collections for each preset and OS
`obs/<preset>/<windows|mac|linux>/BuildWithWaqar_<Preset>.json`. Generate a copy with your paths:
```bash
python obs/configure_obs.py --preset algoexpert --os windows --kit-dir "C:/Users/<you>/AlgoExpert/video-kit"
python obs/configure_obs.py --preset leetcode   --os mac     --kit-dir "/Users/<you>/AlgoExpert/video-kit"
python obs/configure_obs.py --preset leetcode   --os linux   --kit-dir "/home/<you>/AlgoExpert/video-kit"  # add --wayland on Wayland
```
Then OBS: **Scene Collection → Import** the `.local.json`. These files were generated to OBS 30's collection format
but **haven't been test-imported in a real OBS install**. If a source shows as missing or empty, re-add it with the same name and position.
Missing media can be repointed with OBS's *Missing Files* dialog.

**Placeholders you must pick yourself (in each source's Properties):** camera device (`Camera · side column`,
`Camera · full`), microphone (`Mic/Aux`), the **IntelliJ IDEA window** (both IntelliJ sources), the slides display/window, the
code-editor window, and the whiteboard window. Nothing machine-specific is hard-coded.

| # | Scene | Layout |
|---|---|---|
| 1 | Intro (preset) | `assets/intro/intro_<preset>.mp4` + low music bed |
| 2 | Full Facecam Hook | Camera full frame, accent border, lower third |
| 3 | Slides + PiP | Slides in the 1520×855 content box (24,24). Camera 328×328 in the right column (1568,24). Branding below it. |
| 4 | Code + PiP | Any editor window in the content box, camera in the column |
| 5 | **IntelliJ — Code + Run Console** | IntelliJ window in the content box (editor on top, Run/Debug console docked at the bottom), camera in the column |
| 6 | **IntelliJ — Full Screen** | IntelliJ at 1920×1080, **no camera, no overlays** |
| 7 | Dry Run / Whiteboard | Whiteboard app or the IntelliJ debugger in the content box, camera in the column |
| 8 | Outro (preset) | `assets/outro/outro_<preset>.mp4` |

The annotated layouts are in `docs/layouts/<preset>-{3-slides-pip,5-intellij-code-run,6-intellij-full,7-dry-run}.png`.
The camera only ever sits in the right column (x ≥ 1568), and captured content stays inside x ≤ 1544, y ≤ 879, so **the camera can't cover code
or the console**. The lower third sits at y ≥ 905, below the content box.

### IntelliJ screen share
1. **Selecting the window:** open the `IntelliJ window …` source in scenes 5 and 6. On Windows choose `[idea64.exe]: <project>` with
   the Windows 10/11 capture method. On macOS (OBS 30, ScreenCaptureKit) choose the IntelliJ IDEA window and grant Screen Recording
   permission. On Linux/X11 pick it in Window Capture (Xcomposite); on Wayland the PipeWire portal asks you each time.
2. **Window size:** maximise IntelliJ on a 1920×1080 display (or set it to 1920×1080). Scene 5 scales it into the 1520×855 box, which is 79%.
   That's why the fonts below are larger than usual.
3. **Fonts:** Editor 18–20 pt (Settings → Editor → Font), Console 16–18 pt (Editor → Color Scheme → Console Font), and IDE zoom
   about 110–125%. IntelliJ's **Presentation Mode** or **Zen Mode** hides chrome. Leave the Run tool window docked at the **bottom**, at about 35% of the height.
4. **Keep the Run console visible:** pin the Run tool window, turn on "Soft-wrap" in the console, and clear it before each run.
5. **Privacy:** hide notifications (Do Not Disturb, and IntelliJ's balloon notifications), close private tabs, `.env` files, terminals with tokens,
   and Git tool windows that show emails. Use a dedicated "recording" IDE profile or project if you can. Check the first frame before every take.
6. **What to record:**
   - *Problem demo:* run `main` or a scratch test with the slide's example input.
   - *Run tests:* `cd algoexpert && mvn test -Dtest=…` or the gutter ▶ on the JUnit class. Show the green bar.
   - *Debugger dry run:* put a breakpoint on the `seen.contains` / `index.get` line, then Step Over with the Variables pane visible. Use scene 7 or 6.
7. **Hotkeys** (OBS Settings → Hotkeys; suggestions): F1 Intro, F2 Hook, F3 Slides+PiP, F4 Code+PiP, **F5 IntelliJ Code+Run**,
   **F6 IntelliJ Full**, F7 Dry Run, F8 Outro, F9 start/stop recording, F10 pause, Ctrl+M mute mic. Avoid IntelliJ's own
   F-key shortcuts (F8 Step Over, F7 Step Into, F9 Resume) clashing with OBS while the IDE has focus. Either use **Ctrl+Alt+1…8** for scenes or
   a stream deck or phone remote.

### Recording settings
1080p **60 fps** for IDE scrolling (30 for slides only). **MKV** then *Remux Recordings*. Hardware encoder with **CQP 18–20** (x264 CRF 18).
48 kHz audio, with the mic on its own track. Mic filters are pre-wired in this order: RNNoise noise suppression → noise gate (−36/−46 dB) → compressor (4:1,
−20 dB) → limiter (−2 dB). Camera tips: lens at eye height, eyes on the top third line in the hook, soft key light at 45°, purple/pink
rim light to match the brand, and lock exposure and white balance.

## 4. CapCut (desktop) assembly
CapCut renames menus often, so the steps below name **features**, not menu paths.

**Track order (top → bottom):** V5 text and KEY POINT callouts, lower third · V4 stingers (green MP4, Chroma key) · V3 camera
overlay + frame PNG (only if not baked in by OBS) · V2 section cards · V1 main (hook → intro → OBS recording → outro) ·
A1 your voice · A2 SFX · A3 music bed.

1. **Template once:** build `BWW-AlgoExpert` and `BWW-LeetCode` drafts with the matching intro, outro, 8 cards, a stinger and
   the music bed. For each episode, **duplicate the draft** from the project list (a reliable way to reuse a layout).
2. **Replace the placeholders:** drop your OBS recording on V1 and delete the demo's TTS. If you used `build_episode.py` as a guide, mute it or
   use `--voice-db -60`. Your real camera replaces every "YOUR FACE CAM" box. In OBS scenes 3–5 and 7 it's already in the column.
3. **Cut:** use CapCut's silence or filler-word removal if your version has it, then trim by hand. Keep the hook under 15 s.
4. **Intro and outro:** the intro goes right after the hook. Add the title text at 3.6 s in the empty slot (Montserrat ExtraBold). The outro goes last. Leave
   the two right-hand boxes empty for YouTube's end-screen elements (they must sit in the last 5–20 s).
5. **Transitions and SFX levels:** centre each stinger's middle (0.35 s) on the cut. Use swipe for slide→slide, glitch into section cards, and light-leak
   for big moments. Suggested levels relative to the voice: whoosh/glitch −10 dB, pop −14 dB, ding −12 dB, music −20 dB under speech
   (use auto-ducking if your version has it, otherwise keyframe the volume).
6. **Zoom emphasis:** add keyframes at 100% → 120–130% on the line you're explaining (6–8 frames in, hold, about 10 frames out) with a soft
   whoosh. Use it at most every 20–30 s, and never zoom so the camera column covers code. In IntelliJ Full Screen there's no camera, so zoom freely.
7. **Captions:** run auto captions (speech-to-text) on A1, fix the jargon (HashSet, HashMap, O(n), indices), style them white on a dark box, and
   keep them in the bottom strip (y > 880). Or upload the `.srt` to YouTube as closed captions.
8. **Background tools:** CapCut's background removal works for a cut-out thumbnail face. Auto-reframe helps when you turn an episode
   into a 9:16 Short.
9. **Export:** 1080p (or 4K upscale), 30 fps for slide-only episodes or 60 if you recorded the IDE at 60, H.264, high bitrate, AAC.
   Aim for about −14 LUFS: use loudness normalisation if your version offers it, otherwise keep voice peaks around −6 dBFS.

## 5. Quick batch-recording checklist (3–4 episodes in one session)
- [ ] Scripts ready in `episodes/<preset>/*.md`. Slides PDF open, and IntelliJ project open on the right branch.
- [ ] OBS: right collection (AlgoExpert vs LeetCode), mic filters on, MKV, 60 fps, a 10 s test take played back.
- [ ] IntelliJ: fonts 18–20 / 16–18, notifications off, private tabs closed, Run console docked and cleared.
- [ ] Camera: framing, light, exposure locked. Water nearby. Phone on silent.
- [ ] For each episode: Hook (F2) → Slides (F3) → IntelliJ run + tests (F5) → debugger dry run (F7/F6) → recap on slides → clap to mark the end.
- [ ] Remux all MKVs at the end. Name them `<preset>-<problem>-take1.mp4`.
- [ ] In CapCut: duplicate the template, then do the per-episode edit (about 60–90 min each).

## 6. Thumbnails and hooks
The `thumbnails/` samples follow the recipe: 2–3 huge words, a gold promise pill (`O(n²) → O(n)`), a series tag
(ALGOEXPERT / LEETCODE #1), a tilted code screenshot and the WS logo. Add a cut-out of your face for real uploads.
Hook checklist: state the stake in the first sentence, show something visual within 5 s, open a loop ("the twist that trips people
up…"), and don't make claims you can't back up.
