# AlgoExpert · Longest Substring Without Duplication

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Substring Without Duplication (0:00) — `slides/01.png`

Let's solve Longest Substring Without Duplication, a hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Sliding window with last-seen index per character.

## 3. Intuition (0:18) — `slides/03.png`

Slide a window; when a character repeats, jump the start past its last occurrence.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, map characters to last index. Second, move start past a repeat. Third, track the longest window.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with longest substring without duplication. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n. Space is O of min(n, a).

## 7. Recap (0:48) — `slides/07.png`

To recap Longest Substring Without Duplication: Slide a window; when a character repeats, jump the start past its last occurrence. Try re-implementing it from scratch without looking.
