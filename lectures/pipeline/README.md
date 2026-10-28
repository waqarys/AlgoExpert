# Lecture pipeline

Turns a slide spec into a narrated 1280x720 MP4 plus `transcript.md`.

- Slides: matplotlib (mathtext for equations, real plots for visuals) + Pygments (monokai code images). Dark theme, Inter font.
- Voice: Microsoft Edge neural TTS via `edge-tts` (free, default `en-US-GuyNeural`). Truncated clips are detected and retried.
- Assembly: ffmpeg, each slide held for its clip + 0.6 s, H.264 CRF 28 (stillimage, 15 fps), AAC 96k mono, concat, faststart.

## Usage
```bash
pip install edge-tts matplotlib pillow pygments numpy   # plus ffmpeg on PATH
python lectures/pipeline/make_lecture.py lectures/pipeline/specs/mlexpert/linear_regression.py [--voice en-IN-PrabhatNeural]
```

## Spec format
A Python module with `TITLE`, `OUT` (path under `lectures/`, e.g. `algoexpert/easy/arrays/TwoNumberSum`) and `SLIDES`, a list of dicts:

| kind | fields |
|---|---|
| `title` | `heading`, `subtitle` |
| `bullets` | `heading`, `bullets`, optional `size` |
| `equations` | `heading`, `equations` (mathtext `$...$`), `bullets` |
| `code` | `heading`, `code`, `lang` (`python`/`java`), `font_size` |
| `plot` | `heading`, `draw(ax)` callable, `bullets` (mathtext allowed) |

Every slide needs `narration`; it is spoken and written to the transcript with timestamps.
