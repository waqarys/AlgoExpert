# AlgoExpert · Pattern Matcher

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Pattern Matcher (0:00) — `slides/01.png`

Let's solve Pattern Matcher, a hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Pattern of 'x'/'y'; find substrings x and y so substituting yields str. Returns x, y (empty strings if unused) or if impossible. Normalise so pattern starts with 'x', then try every length of x.

## 3. Intuition (0:27) — `slides/03.png`

Fix the length of x; the length of y follows from the counts, so test each candidate.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

Trying every pair of lengths is wasteful, since once x's length is fixed, y's length is determined. That's n times m.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, normalise so the pattern starts with x. Second, count x and y. Third, for each length of x, derive length of y. Fourth, build and compare.

## 6. Worked example (0:53) — `slides/06.png`

The pattern has four x's and two y's. The string is thirty characters.

## 7. Worked example (0:59) — `slides/07.png`

For each length of x, the length of y follows. Take x from the start and y from its first position, then rebuild and compare.

## 8. Worked example (1:08) — `slides/08.png`

With x equal to go and y equal to powerranger, the rebuilt string matches.

## 9. Java solution (1:13) — `slides/09.png`

We normalise so the pattern starts with x, count x's and y's, then for each x length compute y's length, extract both, rebuild, and compare.

## 10. Complexity (1:22) — `slides/10.png`

Time is O of n squared plus m. Space is O of n plus m.

## 11. Edge cases & pitfalls (1:27) — `slides/11.png`

If the pattern starts with y, swap the letters, then swap the answer back.

## 12. Interview tips & follow-ups (1:32) — `slides/12.png`

Explain why y's length is forced.

## 13. Recap (1:36) — `slides/13.png`

To recap Pattern Matcher: Fix the length of x; the length of y follows from the counts, so test each candidate. Try re-implementing it from scratch without looking.
