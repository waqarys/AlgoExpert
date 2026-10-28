# AlgoExpert · Find Kth Largest Value In Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Kth Largest Value In Bst (0:00) — `slides/01.png`

Let's solve Find Kth Largest Value In Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Reverse in-order traversal, stopping after k nodes.

## 3. Intuition (0:19) — `slides/03.png`

A reverse in-order traversal visits values from largest to smallest, so stop at the kth.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

The simple approach collects all values in sorted order and indexes from the end, costing linear time and space. A reverse in-order traversal visits values from largest down and stops after k, so it costs only height plus k.

## 5. Approach (0:40) — `slides/05.png`

Step by step. First, traverse right, node, left. Second, count visited nodes. Third, stop at the kth and return its value.

## 6. Worked example (0:52) — `slides/06.png`

Reverse in-order visit number 1 is 22.

## 7. Worked example (0:56) — `slides/07.png`

Reverse in-order visit number 2 is 20.

## 8. Worked example (1:00) — `slides/08.png`

Reverse in-order visit number 3 is 17. That's the third largest, so we stop.

## 9. Java solution (1:07) — `slides/09.png`

The walk function returns early if the node is null or we've already seen k values. It recurses right first, then counts the current node, records it as the answer if it's the k-th, and only then goes left.

## 10. Complexity (1:19) — `slides/10.png`

Time is O of h plus k. Space is O of h.

## 11. Edge cases & pitfalls (1:23) — `slides/11.png`

Duplicate values count separately. Make sure recursion stops as soon as the k-th value is found.

## 12. Interview tips & follow-ups (1:31) — `slides/12.png`

For repeated queries, store subtree sizes in each node to answer in log n.

## 13. Recap (1:37) — `slides/13.png`

To recap Find Kth Largest Value In Bst: A reverse in-order traversal visits values from largest to smallest, so stop at the kth. Try re-implementing it from scratch without looking.
