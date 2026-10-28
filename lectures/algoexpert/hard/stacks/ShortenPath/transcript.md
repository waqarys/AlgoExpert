# AlgoExpert · Shorten Path

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Shorten Path (0:00) — `slides/01.png`

Let's solve Shorten Path, a hard stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Simplify a Unix path (absolute or relative), resolving "." and ".." and duplicate slashes. Leading ".." are kept for relative paths and dropped at the root of absolute paths.

## 3. Intuition (0:24) — `slides/03.png`

Process path tokens with a stack: dots are ignored, double dots pop, names push.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, split on slashes. Second, skip empty tokens and single dots. Third, double dot pops, or is kept for relative paths. Fourth, join back.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with shorten path. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:55) — `slides/07.png`

To recap Shorten Path: Process path tokens with a stack: dots are ignored, double dots pop, names push. Try re-implementing it from scratch without looking.
