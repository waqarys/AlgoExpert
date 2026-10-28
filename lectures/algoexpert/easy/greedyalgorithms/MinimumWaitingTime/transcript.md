# AlgoExpert · Minimum Waiting Time

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Waiting Time (0:00) — `slides/01.png`

Let's solve Minimum Waiting Time, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Minimum Waiting

## 3. Intuition (0:16) — `slides/03.png`

Short queries should run first, because each query's duration is waited on by everyone after it.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Trying every execution order is factorial. Exchange argument: if a longer query runs before a shorter one, swapping them reduces total waiting. So shortest first is optimal, and sorting costs n log n.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, sort durations ascending. Second, each duration is waited on by the queries remaining after it. Third, add duration times queries left. Fourth, return the total.

## 6. Worked example (0:52) — `slides/06.png`

Take the queries three, two, one, two, six. Sorted, they become one, two, two, three, six.

## 7. Worked example (1:01) — `slides/07.png`

Query 0 takes 1 seconds, and the 4 queries after it all wait for it, adding 4. The total is now 4.

## 8. Worked example (1:09) — `slides/08.png`

Query 1 takes 2 seconds, and the 3 queries after it all wait for it, adding 6. The total is now 10.

## 9. Worked example (1:17) — `slides/09.png`

Query 3 takes 3 seconds, and the 1 queries after it all wait for it, adding 3. The total is now 17.

## 10. Worked example (1:26) — `slides/10.png`

Query 4 takes 6 seconds, and the 0 queries after it all wait for it, adding 0. The total is now 17.

## 11. Java solution (1:34) — `slides/11.png`

We sort the array, then for each index multiply the duration by the number of queries left after it and add it to the total.

## 12. Complexity (1:42) — `slides/12.png`

Time is queries with durations run one at a time; choose an order minimising the total time all queries spend waiting. Shortest-first is optimal. Time is O of n log n. Space is constant.

## 13. Edge cases & pitfalls (1:55) — `slides/13.png`

The last query contributes nothing. Sorting in place mutates the input, which you should mention. Use a long if totals can be large.

## 14. Interview tips & follow-ups (2:05) — `slides/14.png`

Prove the greedy with an exchange argument. A follow-up adds weights, where you sort by duration divided by weight.

## 15. Recap (2:13) — `slides/15.png`

To recap Minimum Waiting Time: Short queries should run first, because each query's duration is waited on by everyone after it. Try re-implementing it from scratch without looking.
