# AlgoExpert · Breadth First Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Breadth First Search (0:00) — `slides/01.png`

Let's solve Breadth First Search, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return node names of a tree-like graph level by level.

## 3. Intuition (0:17) — `slides/03.png`

Breadth-first search visits nodes level by level using a queue.

## 4. Brute force vs optimal (0:22) — `slides/04.png`

Breadth-first search is linear, like depth-first search; what changes is using a queue, so nodes come out level by level. That's why BFS finds shortest paths in unweighted graphs.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, enqueue the root. Second, pop, record the name, enqueue children. Third, repeat until the queue is empty.

## 6. Worked example (0:44) — `slides/06.png`

Dequeue A and record it. Its children, B, C, D, join the back of the queue.

## 7. Worked example (0:51) — `slides/07.png`

Dequeue C and record it. It has no children.

## 8. Worked example (0:56) — `slides/08.png`

Dequeue E and record it. It has no children.

## 9. Worked example (1:01) — `slides/09.png`

Dequeue G and record it. Its children, K, join the back of the queue.

## 10. Worked example (1:08) — `slides/10.png`

Dequeue I and record it. It has no children.

## 11. Worked example (1:13) — `slides/11.png`

Dequeue K and record it. It has no children.

## 12. Java solution (1:18) — `slides/12.png`

We push the start node onto an array deque. While it's non-empty, we poll a node, append its name, and add all its children to the back.

## 13. Complexity (1:27) — `slides/13.png`

Time is O of v plus e. Space is O of v.

## 14. Edge cases & pitfalls (1:31) — `slides/14.png`

Use a proper queue; removing from the front of an array list is linear. On general graphs, mark nodes visited when you enqueue them.

## 15. Interview tips & follow-ups (1:40) — `slides/15.png`

Follow-ups print each level separately or find shortest paths in a grid.

## 16. Recap (1:45) — `slides/16.png`

To recap Breadth First Search: Breadth-first search visits nodes level by level using a queue. Try re-implementing it from scratch without looking.
