# AlgoExpert · Max Subset Sum No Adjacent

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Subset Sum No Adjacent (0:00) — `slides/01.png`

Let's solve Max Subset Sum No Adjacent, a medium dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Max sum of positive ints with no two chosen elements adjacent.

## 3. Intuition (0:19) — `slides/03.png`

At each index, either take it plus the best up to two back, or skip it.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Trying every non-adjacent subset is exponential. A DP where best i is the max of best i minus one and best i minus two plus the value is linear, and only the last two values are ever needed.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, keep the best up to i minus one and i minus two. Second, choose the max of skip or take. Third, slide forward.

## 6. Worked example (0:48) — `slides/06.png`

At 75: skipping keeps 0; taking adds 75 to the best two back. Taking wins, so the best is 75.

## 7. Worked example (0:57) — `slides/07.png`

At 105: skipping keeps 75; taking adds 105 to the best two back. Taking wins, so the best is 105.

## 8. Worked example (1:08) — `slides/08.png`

At 120: skipping keeps 105; taking adds 120 to the best two back. Taking wins, so the best is 195.

## 9. Worked example (1:18) — `slides/09.png`

At 75: skipping keeps 195; taking adds 75 to the best two back. Skipping wins, so the best stays 195.

## 10. Worked example (1:28) — `slides/10.png`

At 90: skipping keeps 195; taking adds 90 to the best two back. Taking wins, so the best is 285.

## 11. Worked example (1:38) — `slides/11.png`

At 135: skipping keeps 285; taking adds 135 to the best two back. Taking wins, so the best is 330.

## 12. Java solution (1:49) — `slides/12.png`

We keep prev and cur, both starting at zero. For each value, next is the max of cur and prev plus the value; then we slide: prev becomes cur and cur becomes next.

## 13. Complexity (2:00) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (2:04) — `slides/14.png`

An empty array gives zero. With negatives, choosing nothing is allowed, which the zero initial values handle.

## 15. Interview tips & follow-ups (2:12) — `slides/15.png`

This is the classic house robber problem. The circular version runs the algorithm twice, excluding the first or last house.

## 16. Recap (2:21) — `slides/16.png`

To recap Max Subset Sum No Adjacent: At each index, either take it plus the best up to two back, or skip it. Try re-implementing it from scratch without looking.
