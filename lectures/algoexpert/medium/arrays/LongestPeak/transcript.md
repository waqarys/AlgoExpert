# AlgoExpert · Longest Peak

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Peak (0:00) — `slides/01.png`

Let's solve Longest Peak, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Length of the longest strictly-increasing-then-strictly-decreasing run (needs over equals 3 items).

## 3. Intuition (0:19) — `slides/03.png`

A peak is a strict rise then a strict fall, so find each tip and expand both ways.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, find indices higher than both neighbours. Second, expand left while values keep decreasing outward. Third, expand right likewise. Fourth, track the longest span.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with longest peak. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Longest Peak: A peak is a strict rise then a strict fall, so find each tip and expand both ways. Try re-implementing it from scratch without looking.
