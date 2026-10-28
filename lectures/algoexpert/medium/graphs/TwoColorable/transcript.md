# AlgoExpert · Two Colorable

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Two Colorable (0:00) — `slides/01.png`

Let's solve Two Colorable, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Undirected connected graph as adjacency list; can it be 2-coloured (bipartite)?

## 3. Intuition (0:19) — `slides/03.png`

A graph is two-colourable if BFS or DFS can colour neighbours alternately without conflict.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Trying every colouring is exponential. Instead, colour a node, give each neighbour the opposite colour, and look for a conflict, in linear time. A graph is two-colourable exactly when it has no odd cycle.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, colour the start. Second, give each neighbour the opposite colour. Third, a neighbour with the same colour means false.

## 6. Worked example (0:50) — `slides/06.png`

Start by colouring node zero blue.

## 7. Worked example (0:54) — `slides/07.png`

Its neighbours, one and two, must get the opposite colour, pink.

## 8. Worked example (0:59) — `slides/08.png`

But one and two are connected, and both are pink. A triangle is an odd cycle, so it can't be two-coloured.

## 9. Java solution (1:06) — `slides/09.png`

We keep a colour per node. For each uncoloured start, colour it one and push it. Popping a node, uncoloured neighbours get the opposite colour; a neighbour with the same colour returns false.

## 10. Complexity (1:19) — `slides/10.png`

Time is O of v plus e. Space is O of v.

## 11. Edge cases & pitfalls (1:23) — `slides/11.png`

Start a search from every uncoloured node for disconnected graphs. A self-loop makes it impossible.

## 12. Interview tips & follow-ups (1:30) — `slides/12.png`

Mention the odd-cycle characterisation and practical uses like splitting into two conflict-free groups.

## 13. Recap (1:37) — `slides/13.png`

To recap Two Colorable: A graph is two-colourable if BFS or DFS can colour neighbours alternately without conflict. Try re-implementing it from scratch without looking.
