# AlgoExpert · Dijkstras Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Dijkstras Algorithm (0:00) — `slides/01.png`

Let's solve Dijkstras Algorithm, a hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Edges v lists destination, weight (non-negative). Shortest distance from start to every vertex, -1 if unreachable.

## 3. Intuition (0:23) — `slides/03.png`

Always expand the closest unvisited vertex; with non-negative weights its distance is final.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, distances start at infinity. Second, use a min-heap of distance and vertex. Third, relax outgoing edges. Fourth, unreached vertices are minus one.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with dijkstras algorithm. It follows the steps we just described.

## 6. Complexity (0:52) — `slides/06.png`

Time is O of (v plus e) log v. Space is O of v.

## 7. Recap (0:56) — `slides/07.png`

To recap Dijkstras Algorithm: Always expand the closest unvisited vertex; with non-negative weights its distance is final. Try re-implementing it from scratch without looking.
