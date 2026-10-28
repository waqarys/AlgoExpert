# AlgoExpert · Find Closest Value In Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Closest Value In Bst (0:00) — `slides/01.png`

Let's solve Find Closest Value In Bst, an easy binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Return the value in the BST closest to the target (assume one answer). Iteratively walk down, pruning half the tree each step.

## 3. Intuition (0:23) — `slides/03.png`

The BST ordering lets us discard half the tree at every step, just like binary search.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, start at the root, tracking the closest value. Second, update closest if this node is nearer. Third, go left if the target is smaller, right if larger. Fourth, stop on an exact match or a null child.

## 5. Java solution (0:47) — `slides/05.png`

Here's the Java solution, starting with find closest value in bst. It follows the steps we just described.

## 6. Complexity (0:55) — `slides/06.png`

Time is O of log n avg, O of n worst. Space is constant.

## 7. Recap (1:01) — `slides/07.png`

To recap Find Closest Value In Bst: The BST ordering lets us discard half the tree at every step, just like binary search. Try re-implementing it from scratch without looking.
