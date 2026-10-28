# AlgoExpert · Depth First Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Depth First Search (0:00) — `slides/01.png`

Let's solve Depth First Search, an easy graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given a tree-like graph of named nodes, return names in DFS (pre-order) order.

## 3. Intuition (0:19) — `slides/03.png`

Depth-first search visits a node, then fully explores each child before moving to the next sibling.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, append the node's name. Second, recurse into each child in order. Third, return the collected list.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with node. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of v plus e. Space is O of v.

## 7. Recap (0:47) — `slides/07.png`

To recap Depth First Search: Depth-first search visits a node, then fully explores each child before moving to the next sibling. Try re-implementing it from scratch without looking.
