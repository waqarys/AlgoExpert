# AlgoExpert · Two Colorable

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Two Colorable (0:00) — `slides/01.png`

Let's solve Two Colorable, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Undirected connected graph as adjacency list; can it be 2-coloured (bipartite)?

## 3. Intuition (0:19) — `slides/03.png`

A graph is two-colourable if BFS or DFS can colour neighbours alternately without conflict.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, colour the start. Second, give each neighbour the opposite colour. Third, a neighbour with the same colour means false.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with two colorable. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of v plus e. Space is O of v.

## 7. Recap (0:48) — `slides/07.png`

To recap Two Colorable: A graph is two-colourable if BFS or DFS can colour neighbours alternately without conflict. Try re-implementing it from scratch without looking.
