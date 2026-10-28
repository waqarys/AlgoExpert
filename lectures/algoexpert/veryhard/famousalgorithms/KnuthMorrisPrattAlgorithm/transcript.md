# AlgoExpert · Knuth Morris Pratt Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Knuth Morris Pratt Algorithm (0:00) — `slides/01.png`

Let's solve Knuth Morris Pratt Algorithm, a very hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Does sub occur in str? Prefix-function (failure table) matching.

## 3. Intuition (0:21) — `slides/03.png`

A failure table tells us how far to fall back on a mismatch, so we never rescan the text.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Naive matching can rescan the same text many times. KMP's failure table lets the text pointer only move forward, linear overall.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, build the prefix function of the pattern. Second, walk the text. Third, on mismatch, fall back via the table. Fourth, match when the pattern is complete.

## 6. Worked example (0:51) — `slides/06.png`

The failure table stores, for each prefix, the longest proper prefix that's also a suffix.

## 7. Worked example (0:57) — `slides/07.png`

Scanning the text, a mismatch doesn't restart from scratch; we fall back to the failure value and keep going.

## 8. Worked example (1:04) — `slides/08.png`

When the matched length reaches the pattern's length, we've found it.

## 9. Java solution (1:09) — `slides/09.png`

We build fail with a k pointer that falls back on mismatches. Then we scan the text with the same logic, returning true when k equals the pattern length.

## 10. Complexity (1:19) — `slides/10.png`

Time is O of n plus m. Space is O of m.

## 11. Edge cases & pitfalls (1:23) — `slides/11.png`

Building the table uses the same fallback loop as matching.

## 12. Interview tips & follow-ups (1:27) — `slides/12.png`

Mention Rabin-Karp and the Z algorithm as alternatives.

## 13. Recap (1:32) — `slides/13.png`

To recap Knuth Morris Pratt Algorithm: A failure table tells us how far to fall back on a mismatch, so we never rescan the text. Try re-implementing it from scratch without looking.
