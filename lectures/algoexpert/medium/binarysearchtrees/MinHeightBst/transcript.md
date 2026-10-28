# AlgoExpert · Min Height Bst

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Height Bst (0:00) — `slides/01.png`

Let's solve Min Height Bst, a medium binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Build a BST of minimal height from a sorted list of distinct ints (pick middle as root).

## 3. Intuition (0:20) — `slides/03.png`

Choosing the middle element as the root keeps both halves balanced.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Inserting sorted values one at a time creates a chain of height n. Picking the middle element as the root and recursing on each half yields minimum height, and building nodes directly takes linear time.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, take the middle of the sorted range as the root. Second, recurse on the left half. Third, recurse on the right half.

## 6. Worked example (0:47) — `slides/06.png`

In the range from 0 to 8, the middle element 10 becomes the root of this subtree.

## 7. Worked example (0:53) — `slides/07.png`

In the range from 0 to 0, the middle element 1 becomes the root of this subtree.

## 8. Worked example (0:59) — `slides/08.png`

In the range from 2 to 3, the middle element 5 becomes the root of this subtree.

## 9. Worked example (1:05) — `slides/09.png`

In the range from 5 to 8, the middle element 14 becomes the root of this subtree.

## 10. Worked example (1:11) — `slides/10.png`

In the range from 5 to 5, the middle element 13 becomes the root of this subtree.

## 11. Worked example (1:17) — `slides/11.png`

In the range from 8 to 8, the middle element 22 becomes the root of this subtree.

## 12. Java solution (1:23) — `slides/12.png`

Build takes a low and high index. If the range is empty it returns null. Otherwise it creates a node from the middle value and recursively builds its left from the lower half and its right from the upper half.

## 13. Complexity (1:36) — `slides/13.png`

Time is O of n. Space is O of n.

## 14. Edge cases & pitfalls (1:40) — `slides/14.png`

With an even range, either middle is fine. Creating nodes directly instead of calling insert keeps it linear.

## 15. Interview tips & follow-ups (1:48) — `slides/15.png`

A good follow-up converts a sorted linked list into a balanced BST in linear time by building in in-order.

## 16. Recap (1:54) — `slides/16.png`

To recap Min Height Bst: Choosing the middle element as the root keeps both halves balanced. Try re-implementing it from scratch without looking.
