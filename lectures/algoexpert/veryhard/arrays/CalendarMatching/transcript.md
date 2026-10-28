# AlgoExpert · Calendar Matching

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Calendar Matching (0:00) — `slides/01.png`

Let's solve Calendar Matching, a very hard arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Two people's meetings ("HH:MM" pairs) and daily bounds; return all free slots of at least duration minutes available to both. Convert to minutes, merge busy intervals, invert.

## 3. Intuition (0:25) — `slides/03.png`

Merge both calendars, including bounds as meetings, then gaps of the right length are free slots.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

You could check every minute, but merging busy intervals is cleaner: add bounds as busy, sort, merge, and read off gaps.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, convert times to minutes. Second, add each person's bounds as blocked time. Third, sort and merge meetings. Fourth, return gaps at least duration long.

## 6. Worked example (0:53) — `slides/06.png`

Each person has meetings and daily bounds. Treat time outside the bounds as busy.

## 7. Worked example (1:00) — `slides/07.png`

Convert to minutes, add the out-of-bounds time as busy, sort, and merge overlapping intervals.

## 8. Worked example (1:06) — `slides/08.png`

The gaps between merged busy blocks that are at least the meeting length are the answer.

## 9. Java solution (1/2) (1:12) — `slides/09.png`

We add each calendar's meetings plus before-start and after-end blocks, sort, merge overlapping intervals, and output gaps at least the duration long.

## 10. Java solution (2/2) (1:20) — `slides/10.png`

We add each calendar's meetings plus before-start and after-end blocks, sort, merge overlapping intervals, and output gaps at least the duration long.

## 11. Complexity (1:29) — `slides/11.png`

Time is O of c1 plus c2. Space is O of c1 plus c2.

## 12. Edge cases & pitfalls (1:35) — `slides/12.png`

Work in minutes and format back at the end.

## 13. Interview tips & follow-ups (1:39) — `slides/13.png`

This generalises to any number of calendars.

## 14. Recap (1:43) — `slides/14.png`

To recap Calendar Matching: Merge both calendars, including bounds as meetings, then gaps of the right length are free slots. Try re-implementing it from scratch without looking.
