# AlgoExpert · Staircase Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Staircase Traversal (0:00) — `slides/01.png`

Let's solve Staircase Traversal, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Ways to climb height steps taking 1..maxSteps at a time. Sliding-window sum DP.

## 3. Intuition (0:20) — `slides/03.png`

Ways to reach step n is the sum of ways for the last maxSteps steps, a sliding window.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Plain recursion branches k ways per step. A DP summing the previous k entries is n times k, and keeping a running window sum makes it linear.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, ways of zero is one. Second, keep a running window sum. Third, add the new value and drop the oldest.

## 6. Worked example (0:48) — `slides/06.png`

To reach step 1, the last move came from one of the previous 2 steps, so we sum them: 1.

## 7. Worked example (0:54) — `slides/07.png`

To reach step 2, the last move came from one of the previous 2 steps, so we sum them: 2.

## 8. Worked example (1:00) — `slides/08.png`

To reach step 3, the last move came from one of the previous 2 steps, so we sum them: 3.

## 9. Worked example (1:06) — `slides/09.png`

To reach step 4, the last move came from one of the previous 2 steps, so we sum them: 5.

## 10. Java solution (1:13) — `slides/10.png`

Ways of zero is one. For each height, add ways of h minus one to the window, subtract the value that left the window, and store the window as ways of h.

## 11. Complexity (1:23) — `slides/11.png`

Time is O of n. Space is O of n.

## 12. Edge cases & pitfalls (1:26) — `slides/12.png`

Ways of zero is one. When the window slides, subtract the value falling out of it.

## 13. Interview tips & follow-ups (1:33) — `slides/13.png`

With k equal to two, it's Fibonacci. Forbidden steps are a nice follow-up.

## 14. Recap (1:40) — `slides/14.png`

To recap Staircase Traversal: Ways to reach step n is the sum of ways for the last maxSteps steps, a sliding window. Try re-implementing it from scratch without looking.
