# AlgoExpert · Linked List Palindrome

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Linked List Palindrome (0:00) — `slides/01.png`

Let's solve Linked List Palindrome, a very hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Do the values read the same both ways? Reverse the second half, compare, restore.

## 3. Intuition (0:21) — `slides/03.png`

Reverse the second half, then compare it with the first half.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Copying values uses linear space. Finding the middle, reversing the second half and comparing uses constant space.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, find the middle. Second, reverse the second half. Third, compare node by node. Fourth, restore the list.

## 6. Worked example (0:47) — `slides/06.png`

Slow and fast pointers find the middle.

## 7. Worked example (0:50) — `slides/07.png`

Reverse the second half in place.

## 8. Worked example (0:54) — `slides/08.png`

Compare the halves node by node. All match, so it's a palindrome. Then reverse back to restore the list.

## 9. Java solution (1:02) — `slides/09.png`

Slow and fast find the middle, we reverse from slow, compare against the head, reverse back, and return the result.

## 10. Complexity (1:09) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:13) — `slides/11.png`

Restore the list afterwards; mutating input is rude.

## 12. Interview tips & follow-ups (1:18) — `slides/12.png`

Mention the recursive outer-pointer approach.

## 13. Recap (1:21) — `slides/13.png`

To recap Linked List Palindrome: Reverse the second half, then compare it with the first half. Try re-implementing it from scratch without looking.
