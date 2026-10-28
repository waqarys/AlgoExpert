# AlgoExpert · Airport Connections

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Airport Connections (0:00) — `slides/01.png`

Let's solve Airport Connections, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Minimum number of new one-way routes from the starting airport so every airport is reachable. Collapse strongly connected components (Tarjan) and count SCCs with in-degree 0, excluding the one containing the start.

## 3. Intuition (0:26) — `slides/03.png`

Only unreachable airports matter; pick those that unlock the most others first.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

The greedy approach repeatedly searches. Condensing strongly connected components with Tarjan and counting sources is linear.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, find unreachable airports. Second, for each, count airports reachable only through it. Third, sort by that count. Fourth, greedily connect.

## 6. Worked example (0:55) — `slides/06.png`

We want the fewest extra one-way routes so every airport is reachable from the start.

## 7. Worked example (1:00) — `slides/07.png`

First collapse strongly connected components, since airports inside one can already reach each other.

## 8. Worked example (1:07) — `slides/08.png`

In the component DAG, every component with no incoming edge, other than the start's, needs exactly one new route.

## 9. Java solution (1/3) (1:14) — `slides/09.png`

We build the graph, label components with Tarjan, mark components with incoming cross edges, and count the rest, excluding the start's.

## 10. Java solution (2/3) (1:22) — `slides/10.png`

We build the graph, label components with Tarjan, mark components with incoming cross edges, and count the rest, excluding the start's.

## 11. Java solution (3/3) (1:31) — `slides/11.png`

We build the graph, label components with Tarjan, mark components with incoming cross edges, and count the rest, excluding the start's.

## 12. Complexity (1:39) — `slides/12.png`

Time is O of a plus r. Space is O of a plus r.

## 13. Edge cases & pitfalls (1:43) — `slides/13.png`

Don't count the start's own component.

## 14. Interview tips & follow-ups (1:47) — `slides/14.png`

Explain why each source needs exactly one edge and that's enough.

## 15. Recap (1:51) — `slides/15.png`

To recap Airport Connections: Only unreachable airports matter; pick those that unlock the most others first. Try re-implementing it from scratch without looking.
