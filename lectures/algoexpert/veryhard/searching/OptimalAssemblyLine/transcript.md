# AlgoExpert · Optimal Assembly Line

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Optimal Assembly Line (0:00) — `slides/01.png`

Let's solve Optimal Assembly Line, a very hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Split step durations (in order) into k contiguous stations minimising the longest station time. Binary search on the answer with a greedy feasibility check.

## 3. Intuition (0:24) — `slides/03.png`

Binary search the maximum station time; greedily check whether k stations suffice.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Trying every split is exponential and the DP is k n squared. Binary search on the answer with a greedy feasibility check is n log of the sum.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, bounds are the largest step and the total. Second, greedily fill stations. Third, shrink the range when feasible.

## 6. Worked example (0:51) — `slides/06.png`

With a max of 90 per station, we'd need 2 stations, which fits, so try smaller.

## 7. Worked example (0:57) — `slides/07.png`

With a max of 67 per station, we'd need 3 stations, which fits, so try smaller.

## 8. Worked example (1:04) — `slides/08.png`

With a max of 62 per station, we'd need 3 stations, which fits, so try smaller.

## 9. Worked example (1:10) — `slides/09.png`

With a max of 59 per station, we'd need 4 stations, too many, so go larger.

## 10. Worked example (1:16) — `slides/10.png`

With a max of 60 per station, we'd need 3 stations, which fits, so try smaller.

## 11. Worked example (1:22) — `slides/11.png`

The smallest feasible maximum is 60.

## 12. Java solution (1:26) — `slides/12.png`

We binary search between the max and the sum; the greedy count of stations decides which half to keep.

## 13. Complexity (1:32) — `slides/13.png`

Time is O of n log S. Space is constant.

## 14. Edge cases & pitfalls (1:36) — `slides/14.png`

The lower bound is the largest single step.

## 15. Interview tips & follow-ups (1:40) — `slides/15.png`

This is split array largest sum.

## 16. Recap (1:44) — `slides/16.png`

To recap Optimal Assembly Line: Binary search the maximum station time; greedily check whether k stations suffice. Try re-implementing it from scratch without looking.
