# AlgoExpert · Compare Leaf Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Compare Leaf Traversal (0:00) — `slides/01.png`

Let's solve Compare Leaf Traversal, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Do two trees have the same sequence of leaves left-to-right? Lazy iterators.

## 3. Intuition (0:20) — `slides/03.png`

Walk both trees' leaves lazily in parallel so we can stop at the first difference.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Collecting both leaf lists works but uses linear space. Lazy generation with stacks uses only height space and can stop early.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, iterator per tree with a stack. Second, advance to the next leaf. Third, compare values. Fourth, both must end together.

## 6. Worked example (0:48) — `slides/06.png`

Two trees match if their leaves, read left to right, are the same sequence.

## 7. Worked example (0:53) — `slides/07.png`

Use one stack per tree to produce the next leaf on demand, and compare leaf by leaf, stopping at the first mismatch.

## 8. Worked example (1:01) — `slides/08.png`

All four leaves match, and both run out together, so it's true.

## 9. Java solution (1:05) — `slides/09.png`

Next leaf pops nodes, pushing right then left children, until it pops a leaf. The main loop compares leaves until either runs out, returning true only if both run out together.

## 10. Complexity (1:17) — `slides/10.png`

Time is O of n plus m. Space is O of h1 plus h2.

## 11. Edge cases & pitfalls (1:21) — `slides/11.png`

Push right before left so leaves come out left to right.

## 12. Interview tips & follow-ups (1:25) — `slides/12.png`

Point out the early exit on mismatch.

## 13. Recap (1:29) — `slides/13.png`

To recap Compare Leaf Traversal: Walk both trees' leaves lazily in parallel so we can stop at the first difference. Try re-implementing it from scratch without looking.
