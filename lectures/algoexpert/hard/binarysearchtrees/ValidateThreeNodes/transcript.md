# AlgoExpert · Validate Three Nodes

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Validate Three Nodes (0:00) — `slides/01.png`

Let's solve Validate Three Nodes, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Is nodeTwo a descendant of one of nodeOne or nodeThree and an ancestor of the other?

## 3. Intuition (0:19) — `slides/03.png`

Node two must sit on the path between the other two, so search down from node one and node three.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, check if node two descends from node one or node three. Second, then check that the other one descends from node two. Third, use BST search for each step.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with validate three nodes. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of h. Space is constant.

## 7. Recap (0:50) — `slides/07.png`

To recap Validate Three Nodes: Node two must sit on the path between the other two, so search down from node one and node three. Try re-implementing it from scratch without looking.
