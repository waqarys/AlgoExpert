# AlgoExpert · First Non Repeating Character

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. First Non Repeating Character (0:00) — `slides/01.png`

Let's solve First Non Repeating Character, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Index of the first lowercase char occurring exactly once, else -1.

## 3. Intuition (0:19) — `slides/03.png`

Two passes: first count every character, then find the first with a count of one.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, count frequencies in a map. Second, scan the string again. Third, return the first index with count one, else minus one.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with first non repeating character. It follows the steps we just described.

## 6. Complexity (0:44) — `slides/06.png`

Time is O of n. Space is constant (26 counters).

## 7. Recap (0:49) — `slides/07.png`

To recap First Non Repeating Character: Two passes: first count every character, then find the first with a count of one. Try re-implementing it from scratch without looking.
