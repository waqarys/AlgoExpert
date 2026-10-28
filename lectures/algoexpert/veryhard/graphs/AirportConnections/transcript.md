# AlgoExpert · Airport Connections

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Airport Connections (0:00) — `slides/01.png`

Let's solve Airport Connections, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Minimum number of new one-way routes from the starting airport so every airport is reachable. Collapse strongly connected components (Tarjan) and count SCCs with in-degree 0, excluding the one containing the start.

## 3. Intuition (0:26) — `slides/03.png`

Only unreachable airports matter; pick those that unlock the most others first.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, find unreachable airports. Second, for each, count airports reachable only through it. Third, sort by that count. Fourth, greedily connect.

## 5. Java solution (1/3) (0:46) — `slides/05.png`

Here's the Java solution, starting with airport connections. It follows the steps we just described.

## 6. Java solution (2/3) (0:53) — `slides/06.png`

Continuing with tarjan.

## 7. Java solution (3/3) (0:56) — `slides/07.png`

Continuing with strong.

## 8. Complexity (0:59) — `slides/08.png`

Time is O of a plus r. Space is O of a plus r.

## 9. Recap (1:03) — `slides/09.png`

To recap Airport Connections: Only unreachable airports matter; pick those that unlock the most others first. Try re-implementing it from scratch without looking.
