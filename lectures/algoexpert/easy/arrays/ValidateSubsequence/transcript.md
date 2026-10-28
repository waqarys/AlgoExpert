# AlgoExpert · Validate Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Validate Subsequence (0:00) — `slides/01.png`

Let's solve Validate Subsequence, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Is sequence obtainable from array by deleting elements without reordering?

## 3. Intuition (0:18) — `slides/03.png`

A subsequence keeps order, so we just try to match the sequence's elements one by one while scanning the array.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, keep an index into the sequence. Second, scan the array. Third, advance the index on every match. Fourth, valid if the index reaches the end.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with is valid subsequence. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Validate Subsequence: A subsequence keeps order, so we just try to match the sequence's elements one by one while scanning the array. Try re-implementing it from scratch without looking.
