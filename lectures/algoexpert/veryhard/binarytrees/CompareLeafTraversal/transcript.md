# AlgoExpert · Compare Leaf Traversal

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Compare Leaf Traversal (0:00) — `slides/01.png`

Let's solve Compare Leaf Traversal, a very hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Do two trees have the same sequence of leaves left-to-right? Lazy iterators.

## 3. Intuition (0:20) — `slides/03.png`

Walk both trees' leaves lazily in parallel so we can stop at the first difference.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, iterator per tree with a stack. Second, advance to the next leaf. Third, compare values. Fourth, both must end together.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with compare leaf traversal. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n plus m. Space is O of h1 plus h2.

## 7. Recap (0:52) — `slides/07.png`

To recap Compare Leaf Traversal: Walk both trees' leaves lazily in parallel so we can stop at the first difference. Try re-implementing it from scratch without looking.
