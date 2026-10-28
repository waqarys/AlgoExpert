# AlgoExpert · Evaluate Expression Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Evaluate Expression Tree (0:00) — `slides/01.png`

Let's solve Evaluate Expression Tree, an easy binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Leaves are positive ints; internal nodes encode operators -1 ' plus ', -2 '-', -3 '/' (truncating), -4 ' '. Evaluate the tree.

## 3. Intuition (0:25) — `slides/03.png`

Leaves are numbers and internal nodes are operators, so evaluate the children first and combine them.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Every node must be evaluated once, so linear time is optimal. The trick is the order: an operator can only be applied after both of its children, which is a post-order traversal.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, if the node is a leaf, return its value. Second, evaluate left and right subtrees. Third, apply the operator encoded at the node. Fourth, division truncates toward zero.

## 6. Worked example (0:59) — `slides/06.png`

Both children of this × node are evaluated: 2 and 3. Applying the operator gives 6.

## 7. Worked example (1:06) — `slides/07.png`

Both children of this − node are evaluated: 6 and 2. Applying the operator gives 4.

## 8. Worked example (1:14) — `slides/08.png`

Both children of this ÷ node are evaluated: 8 and 3. Applying the operator gives 2.

## 9. Worked example (1:22) — `slides/09.png`

Both children of this + node are evaluated: 4 and 2. Applying the operator gives 6.

## 10. Java solution (1:29) — `slides/10.png`

If the node's value is non-negative, it's a leaf, so return it. Otherwise evaluate the left and right subtrees, then switch on the operator code to add, subtract, divide or multiply.

## 11. Complexity (1:41) — `slides/11.png`

Time is O of n. Space is O of h.

## 12. Edge cases & pitfalls (1:45) — `slides/12.png`

Be careful that division truncates toward zero, which Java's integer division already does. Leaves are always non-negative numbers, and negative values encode operators.

## 13. Interview tips & follow-ups (1:56) — `slides/13.png`

Natural follow-ups are printing the expression in infix form with parentheses, or evaluating iteratively with a stack.

## 14. Recap (2:03) — `slides/14.png`

To recap Evaluate Expression Tree: Leaves are numbers and internal nodes are operators, so evaluate the children first and combine them. Try re-implementing it from scratch without looking.
