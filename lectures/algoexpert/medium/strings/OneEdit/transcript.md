# AlgoExpert · One Edit

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. One Edit (0:00) — `slides/01.png`

Let's solve One Edit, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Are two strings at most one insert or delete or replace apart?

## 3. Intuition (0:17) — `slides/03.png`

Walk both strings; at the first mismatch, try skipping in the longer one or replacing, once.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, if lengths differ by more than one, false. Second, find the first mismatch. Third, compare the remaining suffixes.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with one edit. It follows the steps we just described.

## 6. Complexity (0:42) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:46) — `slides/07.png`

To recap One Edit: Walk both strings; at the first mismatch, try skipping in the longer one or replacing, once. Try re-implementing it from scratch without looking.
