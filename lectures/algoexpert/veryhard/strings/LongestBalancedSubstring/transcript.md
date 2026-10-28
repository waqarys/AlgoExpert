# AlgoExpert · Longest Balanced Substring

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest Balanced Substring (0:00) — `slides/01.png`

Let's solve Longest Balanced Substring, a very hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Length of the longest balanced-parentheses substring. Two counting passes.

## 3. Intuition (0:20) — `slides/03.png`

Count opens and closes left to right, then right to left, resetting when the balance breaks.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, left to right, equal counts give a candidate. Second, reset when closes exceed opens. Third, repeat right to left.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with longest balanced substring. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:49) — `slides/07.png`

To recap Longest Balanced Substring: Count opens and closes left to right, then right to left, resetting when the balance breaks. Try re-implementing it from scratch without looking.
