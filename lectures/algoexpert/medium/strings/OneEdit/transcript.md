# AlgoExpert · One Edit

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. One Edit (0:00) — `slides/01.png`

Let's solve One Edit, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Are two strings at most one insert or delete or replace apart?

## 3. Intuition (0:17) — `slides/03.png`

Walk both strings; at the first mismatch, try skipping in the longer one or replacing, once.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Computing the full Levenshtein distance is overkill. A single scan allowing one mismatch, skipping in the longer string when lengths differ, is linear.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, if lengths differ by more than one, false. Second, find the first mismatch. Third, compare the remaining suffixes.

## 6. Worked example (0:45) — `slides/06.png`

hello versus hollo: the first difference is at index 1. One replace → true.

## 7. Worked example (0:51) — `slides/07.png`

hello versus helo: the first difference is at index 3. One delete → true.

## 8. Worked example (0:58) — `slides/08.png`

hello versus hlelo: the first difference is at index 1. Two mismatches → false.

## 9. Java solution (1:05) — `slides/09.png`

We bail if lengths differ by more than one. Scanning, the first mismatch sets edited and skips in the longer string, or both if equal; a second mismatch returns false.

## 10. Complexity (1:15) — `slides/10.png`

Time is O of n. Space is constant.

## 11. Edge cases & pitfalls (1:19) — `slides/11.png`

If lengths differ by more than one, return false immediately.

## 12. Interview tips & follow-ups (1:24) — `slides/12.png`

Relate it to Levenshtein distance, then explain why one pass is enough.

## 13. Recap (1:29) — `slides/13.png`

To recap One Edit: Walk both strings; at the first mismatch, try skipping in the longer one or replacing, once. Try re-implementing it from scratch without looking.
