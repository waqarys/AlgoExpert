# AlgoExpert · Disk Stacking

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Disk Stacking (0:00) — `slides/01.png`

Let's solve Disk Stacking, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Disks width, depth, height ; stack them so each disk is strictly smaller in all three dimensions than the one below, maximising total height. Returns the chosen disks ordered from top (smallest) to bottom (largest).

## 3. Intuition (0:27) — `slides/03.png`

Sort disks by height; each disk's best stack is itself on top of the best compatible stack below.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

Trying every order is exponential. Sorting by height and running a longest-increasing-subsequence style DP over strictly smaller disks is quadratic.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, sort by height. Second, for each disk, check smaller earlier disks. Third, keep the best height and a predecessor link. Fourth, rebuild the stack.

## 6. Worked example (0:58) — `slides/06.png`

Disk [1, 3, 1]: the tallest stack with it on the bottom is 1, alone.

## 7. Worked example (1:04) — `slides/07.png`

Disk [2, 1, 2]: the tallest stack with it on the bottom is 2, alone.

## 8. Worked example (1:10) — `slides/08.png`

Disk [3, 2, 3]: the tallest stack with it on the bottom is 5, placing it under [2, 1, 2].

## 9. Worked example (1:17) — `slides/09.png`

Disk [4, 4, 5]: the tallest stack with it on the bottom is 10, placing it under [3, 2, 3].

## 10. Worked example (1:25) — `slides/10.png`

Disk [2, 2, 8]: the tallest stack with it on the bottom is 8, alone.

## 11. Worked example (1:31) — `slides/11.png`

Following the back-pointers gives [[2, 1, 2], [3, 2, 3], [4, 4, 5]], height 10.

## 12. Java solution (1:39) — `slides/12.png`

We sort by height. For each disk, start with its own height, and for each earlier strictly smaller disk extend if taller. Track the best index, then follow prev to build the answer.

## 13. Complexity (1:52) — `slides/13.png`

Time is O of n squared. Space is O of n.

## 14. Edge cases & pitfalls (1:57) — `slides/14.png`

All three dimensions must be strictly smaller.

## 15. Interview tips & follow-ups (2:01) — `slides/15.png`

Relate it to longest increasing subsequence.

## 16. Recap (2:05) — `slides/16.png`

To recap Disk Stacking: Sort disks by height; each disk's best stack is itself on top of the best compatible stack below. Try re-implementing it from scratch without looking.
