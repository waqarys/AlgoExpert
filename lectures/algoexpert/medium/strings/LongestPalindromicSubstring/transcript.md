# AlgoExpert · Longest Palindromic Substring

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Palindromic Substring (0:00) — `slides/01.png`

Let's solve Longest Palindromic Substring, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Expand around every centre (odd and even).

## 3. Intuition (0:17) — `slides/03.png`

Every palindrome has a centre; expand around each of the 2n minus 1 centres.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, for each index, expand odd and even centres. Second, track the longest span. Third, return the substring.

## 5. Java solution (0:35) — `slides/05.png`

Here's the Java solution, starting with longest palindromic substring. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n squared. Space is O of n output.

## 7. Recap (0:48) — `slides/07.png`

To recap Longest Palindromic Substring: Every palindrome has a centre; expand around each of the 2n minus 1 centres. Try re-implementing it from scratch without looking.
