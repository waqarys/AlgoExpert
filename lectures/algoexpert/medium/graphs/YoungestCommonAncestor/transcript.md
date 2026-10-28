# AlgoExpert · Youngest Common Ancestor

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Youngest Common Ancestor (0:00) — `slides/01.png`

Let's solve Youngest Common Ancestor, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Nodes have only an ancestor pointer; find the deepest common ancestor of two descendants. Equalise depths, then walk up together.

## 3. Intuition (0:22) — `slides/03.png`

Bring both descendants to the same depth, then climb together until they meet.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, compute both depths. Second, lift the deeper one. Third, move both up until equal.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with ancestral tree. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of d. Space is constant.

## 7. Recap (0:49) — `slides/07.png`

To recap Youngest Common Ancestor: Bring both descendants to the same depth, then climb together until they meet. Try re-implementing it from scratch without looking.
