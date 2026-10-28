# AlgoExpert · Same Bsts

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Same Bsts (0:00) — `slides/01.png`

Let's solve Same Bsts, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Would inserting the two arrays (left to right) produce identical BSTs, without building them? Recurse on first-smaller / first-greater-or-equal descendants within value bounds, using indices only.

## 3. Intuition (0:26) — `slides/03.png`

Two arrays give the same BST if they share the root and their smaller and larger elements build the same subtrees.

## 4. Approach (0:33) — `slides/04.png`

Step by step. First, compare first elements and lengths. Second, split each into smaller and bigger-or-equal lists keeping order. Third, recurse on both halves.

## 5. Java solution (1/2) (0:46) — `slides/05.png`

Here's the Java solution, starting with same bsts. It follows the steps we just described.

## 6. Java solution (2/2) (0:53) — `slides/06.png`

Continuing with bigger.

## 7. Complexity (0:56) — `slides/07.png`

Time is O of n squared. Space is O of d.

## 8. Recap (1:01) — `slides/08.png`

To recap Same Bsts: Two arrays give the same BST if they share the root and their smaller and larger elements build the same subtrees. Try re-implementing it from scratch without looking.
