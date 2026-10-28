# AlgoExpert · Longest Palindromic Substring

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Palindromic Substring (0:00) — `slides/01.png`

Let's solve Longest Palindromic Substring, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Expand around every centre (odd and even).

## 3. Intuition (0:17) — `slides/03.png`

Every palindrome has a centre; expand around each of the 2n minus 1 centres.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Checking every substring is cubic. A DP table is quadratic in time and space. Expanding around each of the two n minus one centres is quadratic time but constant space.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, for each index, expand odd and even centres. Second, track the longest span. Third, return the substring.

## 6. Worked example (0:47) — `slides/06.png`

Expanding around the letter index 0 gives a, the longest so far.

## 7. Worked example (0:52) — `slides/07.png`

Expanding around the letter index 1 gives a b a, the longest so far.

## 8. Worked example (0:58) — `slides/08.png`

Expanding around the gap after index 5 gives x y z z y x, the longest so far.

## 9. Java solution (1:04) — `slides/09.png`

For each i we expand from i,i and i,i plus one while the ends match, then compare the length r minus l minus one with the best and update.

## 10. Complexity (1:12) — `slides/10.png`

Time is O of n squared. Space is O of n output.

## 11. Edge cases & pitfalls (1:18) — `slides/11.png`

Don't forget even-length palindromes, centred between letters.

## 12. Interview tips & follow-ups (1:22) — `slides/12.png`

Mention Manacher's algorithm for linear time.

## 13. Recap (1:27) — `slides/13.png`

To recap Longest Palindromic Substring: Every palindrome has a centre; expand around each of the 2n minus 1 centres. Try re-implementing it from scratch without looking.
