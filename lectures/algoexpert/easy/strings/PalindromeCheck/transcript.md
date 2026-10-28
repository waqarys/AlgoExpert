# AlgoExpert · Palindrome Check

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Palindrome Check (0:00) — `slides/01.png`

Let's solve Palindrome Check, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Does the string read the same forwards and backwards?

## 3. Intuition (0:17) — `slides/03.png`

Compare characters from both ends moving inward; any mismatch means it isn't a palindrome.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Reversing and comparing works but needs extra space, and building the reverse with repeated concatenation is quadratic. Two pointers from both ends need no extra space.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, left pointer at the start, right at the end. Second, compare and move inward. Third, stop when they meet.

## 6. Worked example (0:45) — `slides/06.png`

Left a matches right a, so both pointers move inward.

## 7. Worked example (0:49) — `slides/07.png`

Left b matches right b, so both pointers move inward.

## 8. Worked example (0:54) — `slides/08.png`

Left c matches right c, so both pointers move inward.

## 9. Worked example (0:58) — `slides/09.png`

The pointers meet in the middle with no mismatch, so it's a palindrome.

## 10. Java solution (1:03) — `slides/10.png`

Left starts at zero and right at the end. While left is less than right, mismatching characters return false; otherwise both move inward. Return true.

## 11. Complexity (1:14) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:18) — `slides/12.png`

Empty and single-character strings are palindromes. Clarify whether to ignore case and punctuation.

## 13. Interview tips & follow-ups (1:25) — `slides/13.png`

A common follow-up allows deleting one character, or asks for the longest palindromic substring.

## 14. Recap (1:32) — `slides/14.png`

To recap Palindrome Check: Compare characters from both ends moving inward; any mismatch means it isn't a palindrome. Try re-implementing it from scratch without looking.
