# AlgoExpert · Kadanes Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Kadanes Algorithm (0:00) — `slides/01.png`

Let's solve Kadanes Algorithm, a medium famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Maximum sum of a non-empty contiguous subarray.

## 3. Intuition (0:18) — `slides/03.png`

The best subarray ending here is either this element alone or it extends the best ending at the previous index.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, running best ending here. Second, max of element or element plus running. Third, track the global max.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with kadanes algorithm. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:47) — `slides/07.png`

To recap Kadanes Algorithm: The best subarray ending here is either this element alone or it extends the best ending at the previous index. Try re-implementing it from scratch without looking.
