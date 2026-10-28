# AlgoExpert · Breadth First Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Breadth First Search (0:00) — `slides/01.png`

Let's solve Breadth First Search, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return node names of a tree-like graph level by level.

## 3. Intuition (0:17) — `slides/03.png`

Breadth-first search visits nodes level by level using a queue.

## 4. Approach (0:22) — `slides/04.png`

Step by step. First, enqueue the root. Second, pop, record the name, enqueue children. Third, repeat until the queue is empty.

## 5. Java solution (0:33) — `slides/05.png`

Here's the Java solution, starting with node. It follows the steps we just described.

## 6. Complexity (0:40) — `slides/06.png`

Time is O of v plus e. Space is O of v.

## 7. Recap (0:44) — `slides/07.png`

To recap Breadth First Search: Breadth-first search visits nodes level by level using a queue. Try re-implementing it from scratch without looking.
