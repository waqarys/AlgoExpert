# AlgoExpert · Largest Rectangle Under Skyline

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Largest Rectangle Under Skyline (0:00) — `slides/01.png`

Let's solve Largest Rectangle Under Skyline, a hard stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Largest rectangle area within adjacent buildings of width 1. Monotonic increasing stack of indices.

## 3. Intuition (0:21) — `slides/03.png`

A monotonic stack finds, for each building, how far it extends left and right before a shorter one.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, push indices with increasing heights. Second, when a shorter building arrives, pop and compute area. Third, width spans to the new top. Fourth, flush at the end.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with largest rectangle under skyline. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:55) — `slides/07.png`

To recap Largest Rectangle Under Skyline: A monotonic stack finds, for each building, how far it extends left and right before a shorter one. Try re-implementing it from scratch without looking.
