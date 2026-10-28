# AlgoExpert · Find Closest Value In Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Closest Value In Bst (0:00) — `slides/01.png`

Let's solve Find Closest Value In Bst, an easy binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Return the value in the BST closest to the target (assume one answer). Iteratively walk down, pruning half the tree each step.

## 3. Intuition (0:23) — `slides/03.png`

The BST ordering lets us discard half the tree at every step, just like binary search.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Brute force visits every node and tracks the closest, which is linear. Using the BST property, each comparison discards an entire subtree, so on a balanced tree we only walk one root-to-leaf path, log n on average.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, start at the root, tracking the closest value. Second, update closest if this node is nearer. Third, go left if the target is smaller, right if larger. Fourth, stop on an exact match or a null child.

## 6. Worked example (1:00) — `slides/06.png`

At node 10, the closest value so far is 10. The target 12 is larger, so we go right and ignore the other subtree.

## 7. Worked example (1:09) — `slides/07.png`

At node 15, the closest value so far is 10. The target 12 is smaller, so we go left and ignore the other subtree.

## 8. Worked example (1:18) — `slides/08.png`

At node 13, the closest value so far is 13. The target 12 is smaller, so we go left and ignore the other subtree.

## 9. Java solution (1:28) — `slides/09.png`

We start at the root with the closest set to its value. In the loop we update closest if this node is nearer, then move left if the target is smaller, right if it's larger, and return immediately on an exact match.

## 10. Complexity (1:40) — `slides/10.png`

Time is O of log n avg, O of n worst. Space is constant.

## 11. Edge cases & pitfalls (1:47) — `slides/11.png`

Stop early on an exact match. On a skewed tree the path can be n long. And compute differences carefully if values are near the integer limits.

## 12. Interview tips & follow-ups (1:57) — `slides/12.png`

Mention that the iterative version uses constant space while recursion uses the call stack. A follow-up is finding the k closest values.

## 13. Recap (2:07) — `slides/13.png`

To recap Find Closest Value In Bst: The BST ordering lets us discard half the tree at every step, just like binary search. Try re-implementing it from scratch without looking.
