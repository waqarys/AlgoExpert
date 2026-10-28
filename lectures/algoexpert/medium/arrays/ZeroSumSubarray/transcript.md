# AlgoExpert · Zero Sum Subarray

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Zero Sum Subarray (0:00) — `slides/01.png`

Let's solve Zero Sum Subarray, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Does any non-empty contiguous subarray sum to zero? A repeated prefix sum proves it.

## 3. Intuition (0:20) — `slides/03.png`

If two prefix sums are equal, the elements between them sum to zero.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, keep a set of prefix sums starting with zero. Second, add each element to the running sum. Third, if the sum was seen before, return true.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with zero sum subarray. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:49) — `slides/07.png`

To recap Zero Sum Subarray: If two prefix sums are equal, the elements between them sum to zero. Try re-implementing it from scratch without looking.
