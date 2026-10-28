# AlgoExpert · Palindrome Check

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Palindrome Check (0:00) — `slides/01.png`

Let's solve Palindrome Check, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Does the string read the same forwards and backwards?

## 3. Intuition (0:17) — `slides/03.png`

Compare characters from both ends moving inward; any mismatch means it isn't a palindrome.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, left pointer at the start, right at the end. Second, compare and move inward. Third, stop when they meet.

## 5. Java solution (0:34) — `slides/05.png`

Here's the Java solution, starting with is palindrome. It follows the steps we just described.

## 6. Complexity (0:41) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:45) — `slides/07.png`

To recap Palindrome Check: Compare characters from both ends moving inward; any mismatch means it isn't a palindrome. Try re-implementing it from scratch without looking.
