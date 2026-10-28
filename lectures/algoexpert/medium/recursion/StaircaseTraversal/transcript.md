# AlgoExpert · Staircase Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Staircase Traversal (0:00) — `slides/01.png`

Let's solve Staircase Traversal, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Ways to climb height steps taking 1..maxSteps at a time. Sliding-window sum DP.

## 3. Intuition (0:20) — `slides/03.png`

Ways to reach step n is the sum of ways for the last maxSteps steps, a sliding window.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, ways of zero is one. Second, keep a running window sum. Third, add the new value and drop the oldest.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with staircase traversal. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:49) — `slides/07.png`

To recap Staircase Traversal: Ways to reach step n is the sum of ways for the last maxSteps steps, a sliding window. Try re-implementing it from scratch without looking.
