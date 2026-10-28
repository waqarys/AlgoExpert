# AlgoExpert · Search For Range

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Search For Range (0:00) — `slides/01.png`

Let's solve Search For Range, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. First and last index of target in a sorted array, -1, -1 if absent. Two modified binary searches.

## 3. Intuition (0:21) — `slides/03.png`

Two binary searches: one biased left for the first occurrence, one biased right for the last.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, search keeping left on matches. Second, search keeping right on matches. Third, return both indices or minus ones.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with search for range. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of log n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Search For Range: Two binary searches: one biased left for the first occurrence, one biased right for the last. Try re-implementing it from scratch without looking.
