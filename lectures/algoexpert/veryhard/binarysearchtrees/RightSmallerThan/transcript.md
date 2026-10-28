# AlgoExpert · Right Smaller Than

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Right Smaller Than (0:00) — `slides/01.png`

Let's solve Right Smaller Than, a very hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. For each element, how many elements to its right are strictly smaller? Insert from the right into an augmented BST tracking left-subtree sizes.

## 3. Intuition (0:23) — `slides/03.png`

Insert from the right into a BST that knows its left-subtree sizes; each insert counts the smaller values already there.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Scanning right from every element is quadratic. Inserting right to left into a BST that tracks left-subtree sizes counts smaller values during insertion.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, iterate from the end. Second, insert into an augmented BST. Third, add left sizes when going right. Fourth, record the count.

## 6. Worked example (0:55) — `slides/06.png`

Moving right to left, insert 2 into a BST of everything to its right. Every time we go right, we add the left-subtree size plus one: 0 smaller values.

## 7. Worked example (1:05) — `slides/07.png`

Moving right to left, insert 3 into a BST of everything to its right. Every time we go right, we add the left-subtree size plus one: 1 smaller values.

## 8. Worked example (1:16) — `slides/08.png`

Moving right to left, insert 11 into a BST of everything to its right. Every time we go right, we add the left-subtree size plus one: 4 smaller values.

## 9. Worked example (1:26) — `slides/09.png`

Moving right to left, insert 8 into a BST of everything to its right. Every time we go right, we add the left-subtree size plus one: 5 smaller values.

## 10. Java solution (1/2) (1:37) — `slides/10.png`

We insert from the end. Going left increments that node's left size; going right adds left size plus one, unless equal. The accumulated count is the answer for that index.

## 11. Java solution (2/2) (1:49) — `slides/11.png`

We insert from the end. Going left increments that node's left size; going right adds left size plus one, unless equal. The accumulated count is the answer for that index.

## 12. Complexity (2:01) — `slides/12.png`

Time is O of n log n avg, O of n squared worst. Space is O of n.

## 13. Edge cases & pitfalls (2:08) — `slides/13.png`

A sorted input makes the BST degenerate; a Fenwick tree avoids that.

## 14. Interview tips & follow-ups (2:13) — `slides/14.png`

Mention the Fenwick-tree and merge-sort alternatives.

## 15. Recap (2:17) — `slides/15.png`

To recap Right Smaller Than: Insert from the right into a BST that knows its left-subtree sizes; each insert counts the smaller values already there. Try re-implementing it from scratch without looking.
