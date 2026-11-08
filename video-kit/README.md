# Build with Waqar: algorithm video kit (AlgoExpert + LeetCode)

A reusable OBS + CapCut kit for YouTube episodes built from this repo's slides and Java solutions.
The full guide is in **[VIDEO-WORKFLOW.md](VIDEO-WORKFLOW.md)**.

| | AlgoExpert | LeetCode |
|---|---|---|
| Preset | [presets/algoexpert.json](presets/algoexpert.json) | [presets/leetcode.json](presets/leetcode.json) |
| Example script | [episodes/algoexpert/two-number-sum.md](episodes/algoexpert/two-number-sum.md) | [episodes/leetcode/0001-two-sum.md](episodes/leetcode/0001-two-sum.md) |
| OBS scenes | [obs/algoexpert/](obs/algoexpert) (windows / mac / linux) | [obs/leetcode/](obs/leetcode) |
| Layouts | [docs/layouts/](docs/layouts) | [docs/layouts/](docs/layouts) |
| Demo | release `algo-video-kit-v1` | release `algo-video-kit-v1` |

```bash
python build_episode.py --preset presets/leetcode.json --slides ../leetcode/content/0001-two-sum/slides \
  --script episodes/leetcode/0001-two-sum.md --out out/two-sum.mp4 --thumb thumbnails/two-sum.png --thumb-slide 7
python obs/configure_obs.py --preset leetcode --os mac --kit-dir "$PWD"
```
The design-patterns twin of this kit lives at https://github.com/waqarys/java-design-patterns/tree/main/video-kit.
