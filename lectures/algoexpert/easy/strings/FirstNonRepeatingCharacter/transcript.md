# AlgoExpert · First Non Repeating Character

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. First Non Repeating Character (0:00) — `slides/01.png`

Let's solve First Non Repeating Character, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Index of the first lowercase char occurring exactly once, else -1.

## 3. Intuition (0:19) — `slides/03.png`

Two passes: first count every character, then find the first with a count of one.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

The brute force checks each character against every other, which is quadratic. Counting first and scanning second is linear, and the count table is constant size because the alphabet is fixed.

## 5. Approach (0:36) — `slides/05.png`

Step by step. First, count frequencies in a map. Second, scan the string again. Third, return the first index with count one, else minus one.

## 6. Worked example (0:48) — `slides/06.png`

First pass: count each character. a and c appear twice; b, d and f once.

## 7. Worked example (0:55) — `slides/07.png`

Second pass: a at index 0 has count 2, so skip it.

## 8. Worked example (1:00) — `slides/08.png`

Second pass: b at index 1 has count 1, so the answer is 1.

## 9. Java solution (1:06) — `slides/09.png`

First we count characters in a map. Then we loop over the string again and return the first index whose count is one, or minus one.

## 10. Complexity (1:14) — `slides/10.png`

Time is O of n. Space is constant (26 counters).

## 11. Edge cases & pitfalls (1:19) — `slides/11.png`

Return minus one if every character repeats, and make sure the second pass follows the original order.

## 12. Interview tips & follow-ups (1:26) — `slides/12.png`

For a stream of characters, keep a queue of candidates or an ordered map.

## 13. Recap (1:31) — `slides/13.png`

To recap First Non Repeating Character: Two passes: first count every character, then find the first with a count of one. Try re-implementing it from scratch without looking.
