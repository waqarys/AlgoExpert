# AlgoExpert · Min Number Of Jumps

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Number Of Jumps (0:00) — `slides/01.png`

Let's solve Min Number Of Jumps, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Each value is the max jump length from that index; fewest jumps to reach the end. Greedy BFS-by-ranges.

## 3. Intuition (0:22) — `slides/03.png`

Think in BFS levels: each jump extends the farthest reachable index.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, track the farthest reach and current jump end. Second, when we pass the jump end, take another jump. Third, count jumps until the end.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with min number of jumps. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Min Number Of Jumps: Think in BFS levels: each jump extends the farthest reachable index. Try re-implementing it from scratch without looking.
