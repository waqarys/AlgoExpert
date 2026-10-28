# AlgoExpert · Sweet And Savory

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sweet And Savory (0:00) — `slides/01.png`

Let's solve Sweet And Savory, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Dishes have negative (sweet) or positive (savory) flavour. Pick one sweet plus one savory whose sum is closest to target without exceeding it; return sweet, savory or 0, 0 .

## 3. Intuition (0:25) — `slides/03.png`

Sort sweet and savory dishes, then use two pointers to approach the target from below.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Trying every sweet and savory pair is quadratic. Sorting sweets from mildest to sweetest and savories from smallest to largest lets two pointers converge on the best pair in linear time after sorting.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, split by sign and sort. Second, pointer on the mildest sweet and the smallest savory. Third, if the sum fits, record it and try a bigger savory. Fourth, otherwise try a sweeter dish.

## 6. Worked example (0:59) — `slides/06.png`

The pair sums to -2. That's within the target, so we record it if it's closer, and try a bigger savory dish.

## 7. Worked example (1:08) — `slides/07.png`

The pair sums to 4. That's within the target, so we record it if it's closer, and try a bigger savory dish.

## 8. Java solution (1:16) — `slides/08.png`

We split dishes into sweet and savory lists, sort sweet descending so the mildest is first and savory ascending, then while both pointers are valid, a sum within target updates the best and advances savory; otherwise we move to a sweeter dish.

## 9. Complexity (1:29) — `slides/09.png`

Time is O of n log n. Space is O of n.

## 10. Edge cases & pitfalls (1:33) — `slides/10.png`

If no pair fits, return zero, zero. Dishes with zero flavour belong to neither group.

## 11. Interview tips & follow-ups (1:40) — `slides/11.png`

Explain why each pointer move is safe. A follow-up allows sums above the target and minimises absolute difference.

## 12. Recap (1:48) — `slides/12.png`

To recap Sweet And Savory: Sort sweet and savory dishes, then use two pointers to approach the target from below. Try re-implementing it from scratch without looking.
