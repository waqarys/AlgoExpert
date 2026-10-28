# AlgoExpert · First Duplicate Value

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. First Duplicate Value (0:00) — `slides/01.png`

Let's solve First Duplicate Value, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Values are in 1, n ; return the value whose second occurrence comes first, else -1. Mark visited values by negating the slot at index v -1 (mutates input).

## 3. Intuition (0:25) — `slides/03.png`

Values are between one and n, so each value can mark its own index by flipping that slot negative.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Comparing every pair is quadratic. A hash set is linear but uses extra memory. Since values are between one and n, each value can mark its own slot by negating it, giving linear time and constant space.

## 5. Approach (0:46) — `slides/05.png`

Step by step. First, for each value, look at index abs value minus one. Second, if that slot is already negative, we've seen it: return it. Third, otherwise flip it negative.

## 6. Worked example (1:00) — `slides/06.png`

Value 2 marks its own slot, index 1, by flipping it negative.

## 7. Worked example (1:05) — `slides/07.png`

Value 1 marks its own slot, index 0, by flipping it negative.

## 8. Worked example (1:10) — `slides/08.png`

Value 5 marks its own slot, index 4, by flipping it negative.

## 9. Worked example (1:16) — `slides/09.png`

Value 2 points to slot 1, which is already negative, so 2 has been seen before. It's the first duplicate.

## 10. Java solution (1:24) — `slides/10.png`

For each value, we take its absolute value v and look at slot v minus one. If it's negative, v was seen before, so we return it. Otherwise we negate the slot.

## 11. Complexity (1:36) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:40) — `slides/12.png`

Always take the absolute value, because the current element may already have been negated. Return minus one if there's no duplicate, and mention that this mutates the input.

## 13. Interview tips & follow-ups (1:50) — `slides/13.png`

Ask if you're allowed to modify the input. If not, Floyd's cycle detection on the index graph also works in constant space.

## 14. Recap (1:59) — `slides/14.png`

To recap First Duplicate Value: Values are between one and n, so each value can mark its own index by flipping that slot negative. Try re-implementing it from scratch without looking.
