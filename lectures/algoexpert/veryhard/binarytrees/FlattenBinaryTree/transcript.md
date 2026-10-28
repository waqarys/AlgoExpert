# AlgoExpert · Flatten Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Flatten Binary Tree (0:00) — `slides/01.png`

Let's solve Flatten Binary Tree, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Rewire the tree in place into a doubly linked list in in-order order (left equals prev, right equals next); return the leftmost node.

## 3. Intuition (0:22) — `slides/03.png`

In-order linking: each subtree returns its leftmost and rightmost nodes so neighbours can be connected.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Collecting nodes in order and relinking uses linear space. Returning both ends of each flattened subtree lets us link in place with only the recursion stack.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, flatten left and right recursively. Second, link left's rightmost to the node. Third, link the node to right's leftmost. Fourth, return the outer ends.

## 6. Worked example (0:53) — `slides/06.png`

Flatten the tree into a doubly linked list in in-order, using left as previous and right as next.

## 7. Worked example (0:59) — `slides/07.png`

Each call returns the leftmost and rightmost of its flattened subtree, so the parent can link its left list's tail and right list's head to itself.

## 8. Worked example (1:08) — `slides/08.png`

The result is four, two, five, one, six, three, linked both ways.

## 9. Java solution (1:14) — `slides/09.png`

Flatten recurses left, links its rightmost to the node, recurses right, links its leftmost to the node, and returns the outer ends.

## 10. Complexity (1:22) — `slides/10.png`

Time is O of n. Space is O of h.

## 11. Edge cases & pitfalls (1:26) — `slides/11.png`

Return the leftmost node as the head.

## 12. Interview tips & follow-ups (1:29) — `slides/12.png`

A Morris-style approach avoids recursion.

## 13. Recap (1:33) — `slides/13.png`

To recap Flatten Binary Tree: In-order linking: each subtree returns its leftmost and rightmost nodes so neighbours can be connected. Try re-implementing it from scratch without looking.
