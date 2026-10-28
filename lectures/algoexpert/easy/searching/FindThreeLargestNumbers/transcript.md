# AlgoExpert · Find Three Largest Numbers

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Three Largest Numbers (0:00) — `slides/01.png`

Let's solve Find Three Largest Numbers, an easy searching problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Return the three largest values (sorted ascending) without sorting the input.

## 3. Intuition (0:19) — `slides/03.png`

Keep a tiny sorted window of the three largest seen so far, and shift values into place as larger ones arrive.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Sorting and taking the last three costs n log n. A single pass that maintains three slots does it in linear time with constant space.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, start with three empty slots. Second, compare each number with the largest slot first. Third, shift smaller values down to make room. Fourth, return the three values ascending.

## 6. Worked example (0:51) — `slides/06.png`

141 beats slot 2, so it goes there, and smaller values shift down.

## 7. Worked example (0:57) — `slides/07.png`

1 beats slot 1, so it goes there, and smaller values shift down.

## 8. Worked example (1:02) — `slides/08.png`

17 beats slot 1, so it goes there, and smaller values shift down.

## 9. Worked example (1:08) — `slides/09.png`

18 beats slot 1, so it goes there, and smaller values shift down.

## 10. Worked example (1:13) — `slides/10.png`

541 beats slot 2, so it goes there, and smaller values shift down.

## 11. Java solution (1:19) — `slides/11.png`

For each number we compare against the largest slot first, then the middle, then the smallest, and a small shift-and-insert helper moves the smaller values down.

## 12. Complexity (1:28) — `slides/12.png`

Time is O of n. Space is constant.

## 13. Edge cases & pitfalls (1:32) — `slides/13.png`

Initialise slots as empty rather than zero, or negatives break. Duplicates may occupy multiple slots, and shifting must happen before you overwrite.

## 14. Interview tips & follow-ups (1:42) — `slides/14.png`

For k largest, use a min-heap of size k, or quickselect.

## 15. Recap (1:47) — `slides/15.png`

To recap Find Three Largest Numbers: Keep a tiny sorted window of the three largest seen so far, and shift values into place as larger ones arrive. Try re-implementing it from scratch without looking.
