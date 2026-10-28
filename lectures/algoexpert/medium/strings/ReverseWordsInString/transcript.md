# AlgoExpert · Reverse Words In String

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reverse Words In String (0:00) — `slides/01.png`

Let's solve Reverse Words In String, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Reverse the order of space-separated words, preserving all whitespace runs.

## 3. Intuition (0:19) — `slides/03.png`

Reverse the order of words while keeping whitespace runs intact.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

The library approach is fine but may lose spacing. Scanning from the end, collecting words and space runs, is linear. In place, reverse the whole string then each word.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, tokenise into words and spaces. Second, reverse the token list. Third, join back.

## 6. Worked example (0:46) — `slides/06.png`

Reverse the words, keeping the spaces exactly as they are.

## 7. Worked example (0:50) — `slides/07.png`

Split into words and runs of spaces.

## 8. Worked example (0:54) — `slides/08.png`

Reverse the tokens and join: best, is, the... reversed with spacing preserved.

## 9. Java solution (1:00) — `slides/09.png`

We scan from the end, and whenever we switch between space and non-space we append the token from i plus one to end, then move end.

## 10. Complexity (1:07) — `slides/10.png`

Time is O of n. Space is O of n.

## 11. Edge cases & pitfalls (1:11) — `slides/11.png`

Preserve runs of spaces and leading or trailing spaces.

## 12. Interview tips & follow-ups (1:15) — `slides/12.png`

Mention the in-place two-reversal trick.

## 13. Recap (1:19) — `slides/13.png`

To recap Reverse Words In String: Reverse the order of words while keeping whitespace runs intact. Try re-implementing it from scratch without looking.
