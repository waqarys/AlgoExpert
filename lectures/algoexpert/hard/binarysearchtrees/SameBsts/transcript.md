# AlgoExpert · Same Bsts

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Same Bsts (0:00) — `slides/01.png`

Let's solve Same Bsts, a hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Would inserting the two arrays (left to right) produce identical BSTs, without building them? Recurse on first-smaller / first-greater-or-equal descendants within value bounds, using indices only.

## 3. Intuition (0:26) — `slides/03.png`

Two arrays give the same BST if they share the root and their smaller and larger elements build the same subtrees.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

Building both trees and comparing is straightforward. Without building, we can recursively compare roots and split each array into smaller and larger values. Passing indices and bounds avoids copying.

## 5. Approach (0:46) — `slides/05.png`

Step by step. First, compare first elements and lengths. Second, split each into smaller and bigger-or-equal lists keeping order. Third, recurse on both halves.

## 6. Worked example (0:59) — `slides/06.png`

Both arrays start with ten, so the roots match.

## 7. Worked example (1:03) — `slides/07.png`

Values smaller than ten, in order, form the left subtree. Both start with eight; recurse.

## 8. Worked example (1:10) — `slides/08.png`

Values at least ten form the right subtree. Both begin with fifteen. Recursing all the way, everything matches.

## 9. Worked example (1:20) — `slides/09.png`

So both arrays build exactly this BST, without us ever building it.

## 10. Java solution (1/2) (1:25) — `slides/10.png`

Same compares the current roots, then recurses on the first smaller element in range and the first bigger element in range, for both arrays, narrowing the min and max bounds.

## 11. Java solution (2/2) (1:35) — `slides/11.png`

Same compares the current roots, then recurses on the first smaller element in range and the first bigger element in range, for both arrays, narrowing the min and max bounds.

## 12. Complexity (1:45) — `slides/12.png`

Time is O of n squared. Space is O of d.

## 13. Edge cases & pitfalls (1:50) — `slides/13.png`

Duplicates go to the right subtree. Different lengths mean different trees.

## 14. Interview tips & follow-ups (1:57) — `slides/14.png`

Explain that only relative order within each subtree matters.

## 15. Recap (2:01) — `slides/15.png`

To recap Same Bsts: Two arrays give the same BST if they share the root and their smaller and larger elements build the same subtrees. Try re-implementing it from scratch without looking.
