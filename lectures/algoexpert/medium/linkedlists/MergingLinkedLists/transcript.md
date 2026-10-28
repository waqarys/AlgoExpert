# AlgoExpert · Merging Linked Lists

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Merging Linked Lists (0:00) — `slides/01.png`

Let's solve Merging Linked Lists, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Two lists may converge into a shared tail; return the first shared node or null. Two pointers that switch lists meet at the junction after at most n plus m steps.

## 3. Intuition (0:24) — `slides/03.png`

Two pointers that switch to the other list after finishing travel the same distance and meet at the junction.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, advance both pointers. Second, when one ends, jump to the other list's head. Third, they meet at the shared node or both null.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with merging linked lists. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n plus m. Space is constant.

## 7. Recap (0:54) — `slides/07.png`

To recap Merging Linked Lists: Two pointers that switch to the other list after finishing travel the same distance and meet at the junction. Try re-implementing it from scratch without looking.
