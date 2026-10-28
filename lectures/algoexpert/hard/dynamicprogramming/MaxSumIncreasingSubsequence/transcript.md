# AlgoExpert · Max Sum Increasing Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Sum Increasing Subsequence (0:00) — `slides/01.png`

Let's solve Max Sum Increasing Subsequence, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Returns maxSum , subsequence for the strictly increasing subsequence with the greatest sum.

## 3. Intuition (0:20) — `slides/03.png`

For each index, the best sum ending there extends the best smaller earlier element.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Enumerating subsequences is exponential. A longest-increasing-subsequence style DP on sums is quadratic.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, for each i, scan earlier j with smaller value. Second, keep best sums and predecessors. Third, rebuild the sequence from the best end.

## 6. Worked example (0:48) — `slides/06.png`

For 10, extend the best earlier smaller value; there's none, so it's just 10.

## 7. Worked example (0:53) — `slides/07.png`

For 70, extend the best earlier smaller value, 10, giving 80.

## 8. Worked example (0:59) — `slides/08.png`

For 30, extend the best earlier smaller value, 20, giving 60.

## 9. Worked example (1:05) — `slides/09.png`

For 50, extend the best earlier smaller value, 30, giving 110.

## 10. Worked example (1:11) — `slides/10.png`

For 30, extend the best earlier smaller value, 20, giving 60.

## 11. Worked example (1:17) — `slides/11.png`

The best is 110: [10, 20, 30, 50].

## 12. Java solution (1:22) — `slides/12.png`

Sums starts as a copy. For each i and each earlier smaller j, extend if better and record prev. Rebuild from the best index.

## 13. Complexity (1:31) — `slides/13.png`

Time is O of n squared. Space is O of n.

## 14. Edge cases & pitfalls (1:36) — `slides/14.png`

Keep it strictly increasing; with negatives, a single element may be best.

## 15. Interview tips & follow-ups (1:41) — `slides/15.png`

A Fenwick tree keyed by value gets it to n log n.

## 16. Recap (1:46) — `slides/16.png`

To recap Max Sum Increasing Subsequence: For each index, the best sum ending there extends the best smaller earlier element. Try re-implementing it from scratch without looking.
