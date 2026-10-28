# AlgoExpert · Longest Increasing Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Increasing Subsequence (0:00) — `slides/01.png`

Let's solve Longest Increasing Subsequence, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. One strictly increasing subsequence of maximum length (patience sorting with predecessor links).

## 3. Intuition (0:21) — `slides/03.png`

Patience sorting: keep the smallest possible tail for each length and binary search where each number goes.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

The classic DP is quadratic. Keeping the smallest possible tail for each length, and binary-searching where each value goes, is n log n.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, tails array of indices. Second, binary search the position. Third, record predecessors. Fourth, rebuild from the last tail.

## 6. Worked example (0:51) — `slides/06.png`

Binary search where 5 fits among the tails: position 0. It extends the longest so far.

## 7. Worked example (0:58) — `slides/07.png`

Binary search where -24 fits among the tails: position 0. It replaces a larger tail, keeping that length's tail as small as possible.

## 8. Worked example (1:08) — `slides/08.png`

Binary search where 12 fits among the tails: position 2. It extends the longest so far.

## 9. Worked example (1:16) — `slides/09.png`

Binary search where 2 fits among the tails: position 1. It replaces a larger tail, keeping that length's tail as small as possible.

## 10. Worked example (1:25) — `slides/10.png`

Binary search where 12 fits among the tails: position 3. It extends the longest so far.

## 11. Worked example (1:32) — `slides/11.png`

Binary search where 6 fits among the tails: position 4. It extends the longest so far.

## 12. Worked example (1:40) — `slides/12.png`

Binary search where 35 fits among the tails: position 5. It extends the longest so far.

## 13. Java solution (1:47) — `slides/13.png`

For each i, binary search tails for the first value not less than a i, set prev to the index before, store i, and grow length if at the end. Then follow prev from the last tail.

## 14. Complexity (1:59) — `slides/14.png`

Time is O of n log n. Space is O of n.

## 15. Edge cases & pitfalls (2:03) — `slides/15.png`

The tails array isn't the sequence; keep prev pointers to rebuild it.

## 16. Interview tips & follow-ups (2:08) — `slides/16.png`

Explain why smaller tails leave room to extend.

## 17. Recap (2:12) — `slides/17.png`

To recap Longest Increasing Subsequence: Patience sorting: keep the smallest possible tail for each length and binary search where each number goes. Try re-implementing it from scratch without looking.
