# AlgoExpert · First Duplicate Value

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. First Duplicate Value (0:00) — `slides/01.png`

Let's solve First Duplicate Value, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Values are in 1, n ; return the value whose second occurrence comes first, else -1. Mark visited values by negating the slot at index v -1 (mutates input).

## 3. Intuition (0:25) — `slides/03.png`

Values are between one and n, so each value can mark its own index by flipping that slot negative.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, for each value, look at index abs value minus one. Second, if that slot is already negative, we've seen it: return it. Third, otherwise flip it negative.

## 5. Java solution (0:45) — `slides/05.png`

Here's the Java solution, starting with first duplicate value. It follows the steps we just described.

## 6. Complexity (0:53) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:57) — `slides/07.png`

To recap First Duplicate Value: Values are between one and n, so each value can mark its own index by flipping that slot negative. Try re-implementing it from scratch without looking.
