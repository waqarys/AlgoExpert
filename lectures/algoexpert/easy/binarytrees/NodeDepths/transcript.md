# AlgoExpert · Node Depths

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Node Depths (0:00) — `slides/01.png`

Let's solve Node Depths, an easy binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sum of the depths (distance from root) of every node.

## 3. Intuition (0:17) — `slides/03.png`

Each node contributes its depth, so pass the depth down while traversing and add it up.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, traverse from the root at depth zero. Second, add the current depth to the total. Third, visit children with depth plus one. Fourth, return the sum.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with node depths. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:48) — `slides/07.png`

To recap Node Depths: Each node contributes its depth, so pass the depth down while traversing and add it up. Try re-implementing it from scratch without looking.
