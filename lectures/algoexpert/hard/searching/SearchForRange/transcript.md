# AlgoExpert · Search For Range

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Search For Range (0:00) — `slides/01.png`

Let's solve Search For Range, a hard searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. First and last index of target in a sorted array, -1, -1 if absent. Two modified binary searches.

## 3. Intuition (0:21) — `slides/03.png`

Two binary searches: one biased left for the first occurrence, one biased right for the last.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Scanning, or finding one match and expanding, can be linear with many duplicates. Two lower-bound searches give both ends in log n.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, search keeping left on matches. Second, search keeping right on matches. Third, return both indices or minus ones.

## 6. Worked example (0:48) — `slides/06.png`

Binary search for the first index whose value is at least 45: index 4.

## 7. Worked example (0:54) — `slides/07.png`

Search again for 46: index 10. One before it, 9, is the last 45.

## 8. Worked example (1:02) — `slides/08.png`

So 45 occupies indices 4 to 9.

## 9. Java solution (1:06) — `slides/09.png`

Bound returns the first index whose value is at least t. The range is bound of t through bound of t plus one minus one, if the value at the lower bound equals t.

## 10. Complexity (1:16) — `slides/10.png`

Time is O of log n. Space is constant.

## 11. Edge cases & pitfalls (1:20) — `slides/11.png`

Check the target actually exists at the lower bound.

## 12. Interview tips & follow-ups (1:25) — `slides/12.png`

Use the lower-bound and upper-bound vocabulary.

## 13. Recap (1:29) — `slides/13.png`

To recap Search For Range: Two binary searches: one biased left for the first occurrence, one biased right for the last. Try re-implementing it from scratch without looking.
