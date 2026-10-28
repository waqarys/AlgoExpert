# AlgoExpert · Smallest Substring Containing

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Smallest Substring Containing (0:00) — `slides/01.png`

Let's solve Smallest Substring Containing, a very hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Shortest substring of big containing every character of small (with multiplicity), or "". Sliding window.

## 3. Intuition (0:22) — `slides/03.png`

A sliding window expands until it covers all needed characters, then shrinks to the minimum.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, count needed characters. Second, expand right updating coverage. Third, shrink left while still covering. Fourth, track the smallest window.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with smallest substring containing. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of b plus s. Space is O of s.

## 7. Recap (0:54) — `slides/07.png`

To recap Smallest Substring Containing: A sliding window expands until it covers all needed characters, then shrinks to the minimum. Try re-implementing it from scratch without looking.
