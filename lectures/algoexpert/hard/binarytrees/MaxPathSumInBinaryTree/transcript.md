# AlgoExpert · Max Path Sum In Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Path Sum In Binary Tree (0:00) — `slides/01.png`

Let's solve Max Path Sum In Binary Tree, a hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Maximum sum over any path (node-to-node, no repeats).

## 3. Intuition (0:19) — `slides/03.png`

At each node, the best path either bends through it or continues upward through one child.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, post-order returns the best downward branch. Second, a bending path is node plus both positive branches. Third, track the global max.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with max path sum. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is O of h.

## 7. Recap (0:48) — `slides/07.png`

To recap Max Path Sum In Binary Tree: At each node, the best path either bends through it or continues upward through one child. Try re-implementing it from scratch without looking.
