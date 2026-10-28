# AlgoExpert · Max Path Sum In Binary Tree

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Path Sum In Binary Tree (0:00) — `slides/01.png`

Let's solve Max Path Sum In Binary Tree, a hard binary trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Maximum sum over any path (node-to-node, no repeats).

## 3. Intuition (0:19) — `slides/03.png`

At each node, the best path either bends through it or continues upward through one child.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Trying every pair of endpoints is quadratic. In one post-order pass, each node returns its best downward branch and updates a global best for paths that bend through it.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, post-order returns the best downward branch. Second, a bending path is node plus both positive branches. Third, track the global max.

## 6. Worked example (0:48) — `slides/06.png`

At 4, the best path bending through here is 4. We return 4 upward, a single branch. The best so far is 4.

## 7. Worked example (0:57) — `slides/07.png`

At 5, the best path bending through here is 5. We return 5 upward, a single branch. The best so far is 5.

## 8. Worked example (1:07) — `slides/08.png`

At 2, the best path bending through here is 11. We return 7 upward, a single branch. The best so far is 11.

## 9. Worked example (1:17) — `slides/09.png`

At 7, the best path bending through here is 7. We return 7 upward, a single branch. The best so far is 11.

## 10. Worked example (1:27) — `slides/10.png`

At 3, the best path bending through here is 16. We return 10 upward, a single branch. The best so far is 16.

## 11. Worked example (1:37) — `slides/11.png`

At 1, the best path bending through here is 18. We return 11 upward, a single branch. The best so far is 18.

## 12. Java solution (1:47) — `slides/12.png`

Branch returns zero for null, clamps both children at zero, updates best with value plus both, and returns value plus the larger.

## 13. Complexity (1:55) — `slides/13.png`

Time is O of n. Space is O of h.

## 14. Edge cases & pitfalls (1:59) — `slides/14.png`

Clamp negative branches to zero, and initialise the best with minus infinity so an all-negative tree returns its largest node.

## 15. Interview tips & follow-ups (2:07) — `slides/15.png`

Explain the difference between what you return, a branch, and what you record, a bend.

## 16. Recap (2:13) — `slides/16.png`

To recap Max Path Sum In Binary Tree: At each node, the best path either bends through it or continues upward through one child. Try re-implementing it from scratch without looking.
