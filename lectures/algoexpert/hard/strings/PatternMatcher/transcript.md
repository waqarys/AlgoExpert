# AlgoExpert · Pattern Matcher

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Pattern Matcher (0:00) — `slides/01.png`

Let's solve Pattern Matcher, a hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Pattern of 'x'/'y'; find substrings x and y so substituting yields str. Returns x, y (empty strings if unused) or if impossible. Normalise so pattern starts with 'x', then try every length of x.

## 3. Intuition (0:27) — `slides/03.png`

Fix the length of x; the length of y follows from the counts, so test each candidate.

## 4. Approach (0:33) — `slides/04.png`

Step by step. First, normalise so the pattern starts with x. Second, count x and y. Third, for each length of x, derive length of y. Fourth, build and compare.

## 5. Java solution (0:45) — `slides/05.png`

Here's the Java solution, starting with pattern matcher. It follows the steps we just described.

## 6. Complexity (0:52) — `slides/06.png`

Time is O of n squared plus m. Space is O of n plus m.

## 7. Recap (0:57) — `slides/07.png`

To recap Pattern Matcher: Fix the length of x; the length of y follows from the counts, so test each candidate. Try re-implementing it from scratch without looking.
