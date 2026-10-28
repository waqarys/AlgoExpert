# AlgoExpert · Minimum Waiting Time

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Minimum Waiting Time (0:00) — `slides/01.png`

Let's solve Minimum Waiting Time, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Minimum Waiting

## 3. Intuition (0:16) — `slides/03.png`

Short queries should run first, because each query's duration is waited on by everyone after it.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, sort durations ascending. Second, each duration is waited on by the queries remaining after it. Third, add duration times queries left. Fourth, return the total.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with minimum waiting time. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is queries with durations run one at a time; choose an order minimising the total time all queries spend waiting. Shortest-first is optimal. Time is O of n log n. Space is constant.

## 7. Recap (0:59) — `slides/07.png`

To recap Minimum Waiting Time: Short queries should run first, because each query's duration is waited on by everyone after it. Try re-implementing it from scratch without looking.
