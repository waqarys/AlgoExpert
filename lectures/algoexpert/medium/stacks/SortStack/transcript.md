# AlgoExpert · Sort Stack

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sort Stack (0:00) — `slides/01.png`

Let's solve Sort Stack, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sort a stack (list, top equals end) ascending using only push or pop or peek and recursion.

## 3. Intuition (0:19) — `slides/03.png`

Recursively pop to empty, then insert each value back in sorted position.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, pop the top and sort the rest. Second, insert it back. Third, insertion pops larger tops temporarily.

## 5. Java solution (0:36) — `slides/05.png`

Here's the Java solution, starting with sort stack. It follows the steps we just described.

## 6. Complexity (0:43) — `slides/06.png`

Time is O of n squared. Space is O of n recursion.

## 7. Recap (0:49) — `slides/07.png`

To recap Sort Stack: Recursively pop to empty, then insert each value back in sorted position. Try re-implementing it from scratch without looking.
