# AlgoExpert · Min Height Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Height Bst (0:00) — `slides/01.png`

Let's solve Min Height Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Build a BST of minimal height from a sorted list of distinct ints (pick middle as root).

## 3. Intuition (0:20) — `slides/03.png`

Choosing the middle element as the root keeps both halves balanced.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, take the middle of the sorted range as the root. Second, recurse on the left half. Third, recurse on the right half.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with min height bst. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:47) — `slides/07.png`

To recap Min Height Bst: Choosing the middle element as the root keeps both halves balanced. Try re-implementing it from scratch without looking.
