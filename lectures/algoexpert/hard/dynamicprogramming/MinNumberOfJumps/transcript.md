# AlgoExpert · Min Number Of Jumps

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Number Of Jumps (0:00) — `slides/01.png`

Let's solve Min Number Of Jumps, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Each value is the max jump length from that index; fewest jumps to reach the end. Greedy BFS-by-ranges.

## 3. Intuition (0:22) — `slides/03.png`

Think in BFS levels: each jump extends the farthest reachable index.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

A DP checking every earlier index is quadratic. Greedily, think of ranges like BFS levels: within each jump's range, track the farthest reach, and jump when you exhaust the range.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, track the farthest reach and current jump end. Second, when we pass the jump end, take another jump. Third, count jumps until the end.

## 6. Worked example (0:52) — `slides/06.png`

At index 0, we've used up the range of the current jump. Take jump number 1, extending the reach to index 3.

## 7. Worked example (1:00) — `slides/07.png`

At index 3, we've used up the range of the current jump. Take jump number 2, extending the reach to index 5.

## 8. Worked example (1:09) — `slides/08.png`

At index 5, we've used up the range of the current jump. Take jump number 3, extending the reach to index 8.

## 9. Worked example (1:17) — `slides/09.png`

At index 8, we've used up the range of the current jump. Take jump number 4, extending the reach to index 13.

## 10. Java solution (1:26) — `slides/10.png`

We track jumps, current end and farthest. For each index before the last, extend farthest; when i reaches end, count a jump and move end to farthest.

## 11. Complexity (1:36) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:40) — `slides/12.png`

Stop before the last index, or you'll count an extra jump.

## 13. Interview tips & follow-ups (1:44) — `slides/13.png`

Explain it as BFS levels over ranges.

## 14. Recap (1:48) — `slides/14.png`

To recap Min Number Of Jumps: Think in BFS levels: each jump extends the farthest reachable index. Try re-implementing it from scratch without looking.
