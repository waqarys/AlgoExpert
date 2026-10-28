# AlgoExpert · Find Kth Largest Value In Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Kth Largest Value In Bst (0:00) — `slides/01.png`

Let's solve Find Kth Largest Value In Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Reverse in-order traversal, stopping after k nodes.

## 3. Intuition (0:19) — `slides/03.png`

A reverse in-order traversal visits values from largest to smallest, so stop at the kth.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, traverse right, node, left. Second, count visited nodes. Third, stop at the kth and return its value.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with find kth largest value in bst. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of h plus k. Space is O of h.

## 7. Recap (0:50) — `slides/07.png`

To recap Find Kth Largest Value In Bst: A reverse in-order traversal visits values from largest to smallest, so stop at the kth. Try re-implementing it from scratch without looking.
