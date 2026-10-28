# AlgoExpert · Longest Balanced Substring

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Balanced Substring (0:00) — `slides/01.png`

Let's solve Longest Balanced Substring, a very hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Length of the longest balanced-parentheses substring. Two counting passes.

## 3. Intuition (0:20) — `slides/03.png`

Count opens and closes left to right, then right to left, resetting when the balance breaks.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Checking every substring is cubic. A stack of indices is linear; two counting scans in opposite directions are linear with constant space.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, left to right, equal counts give a candidate. Second, reset when closes exceed opens. Third, repeat right to left.

## 6. Worked example (0:47) — `slides/06.png`

Find the longest balanced substring of parentheses.

## 7. Worked example (0:52) — `slides/07.png`

Scan left to right counting opens and closes. Equal counts give a candidate; more closes means reset.

## 8. Worked example (0:59) — `slides/08.png`

A second scan from the right catches cases with surplus opens. The answer is 8.

## 9. Java solution (1:06) — `slides/09.png`

Scan counts opens and closes, records two times closes when equal, and resets when closes exceed opens; reverse mode swaps the roles.

## 10. Complexity (1:15) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:18) — `slides/11.png`

One direction alone misses cases like extra opens.

## 12. Interview tips & follow-ups (1:23) — `slides/12.png`

Mention the stack alternative.

## 13. Recap (1:26) — `slides/13.png`

To recap Longest Balanced Substring: Count opens and closes left to right, then right to left, resetting when the balance breaks. Try re-implementing it from scratch without looking.
