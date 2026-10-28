# Lecture pipeline

Turns a slide spec into a narrated lecture plus reusable slide assets:

```
lectures/<section>/<topic>/
  lecture.mp4      720p H.264 CRF 28 + AAC 96k mono
  transcript.md    narration per slide with timestamps (use as your recording script)
  slides/NN.png    1920x1080, palette-optimised PNGs (use in OBS / CapCut)
  slides.pdf       all slides in order (lossless, embeds the PNGs)
  code/            every code slide as a plain source file
```

- Slides: matplotlib (mathtext equations, real plots, auto-layout box diagrams) + Pygments (monokai). Dark theme, Inter font.
- Voice: Microsoft Edge neural TTS via `edge-tts` (free), default `en-US-GuyNeural`. Clips shorter than ~words/4.5 s are treated as truncated and re-synthesised.
- Assembly: ffmpeg, each slide held for its clip + 0.6 s with a short fade-in, concatenated with faststart.

## Usage
```bash
pip install edge-tts matplotlib pillow pygments numpy img2pdf   # plus ffmpeg on PATH
cd lectures/pipeline
python make_lecture.py specs/mlexpert/02_linear_regression.py          # one lecture
python make_lecture.py --skip-existing specs/algoexpert/easy/*.json    # resume a batch
python gen_systems_specs.py && python gen_algo_specs.py                # regenerate generated specs
python build_index.py                                                   # refresh lectures/README.md
```

## Spec format
Python module (`TITLE`, `OUT`, `SLIDES`; helpers in `speclib.py`) or JSON (`{"title", "out", "slides"}`).
`OUT` is the folder under `lectures/`. Slide kinds:

| kind | fields |
|---|---|
| `title` | `heading`, `subtitle` |
| `bullets` | `heading`, `bullets`, optional `size` |
| `equations` | `heading`, `equations` (mathtext `$...$`), `bullets` |
| `code` | `heading`, `code`, `lang` (`python`/`java`), optional `filename`, `font_size` |
| `plot` | `heading`, `draw(ax)` callable (Python specs only), `bullets` |
| `diagram` | `heading`, `edges` (list of `[src, dst]`), drawn as a left-to-right box diagram |

Every slide needs `narration`. Keep bullets under ~60 characters so nothing overflows.

MLExpert specs are hand-written. SystemsExpert and AlgoExpert specs are generated from the repo's design docs and Java sources by `gen_systems_specs.py` and `gen_algo_specs.py`.
