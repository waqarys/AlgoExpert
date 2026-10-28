# AlgoExpert · Longest Subarray With Sum

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Subarray With Sum (0:00) — `slides/01.png`

Let's solve Longest Subarray With Sum, a hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Non-negative ints; start, end of the longest subarray summing to target, or if none. Sliding window.

## 3. Intuition (0:21) — `slides/03.png`

Values are non-negative, so a sliding window grows to add and shrinks to subtract.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, expand the right edge adding values. Second, shrink from the left while the sum is too big. Third, record the longest window equal to target.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with longest subarray with sum. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Longest Subarray With Sum: Values are non-negative, so a sliding window grows to add and shrinks to subtract. Try re-implementing it from scratch without looking.
