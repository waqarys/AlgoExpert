# AlgoExpert · Balanced Brackets

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Balanced Brackets (0:00) — `slides/01.png`

Let's solve Balanced Brackets, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Are (), , properly balanced and nested? Non-bracket chars are ignored.

## 3. Intuition (0:19) — `slides/03.png`

A stack matches each closing bracket with the most recent opening one.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

Repeatedly deleting matched pairs is quadratic. A stack of opening brackets checks each closer against the most recent opener in linear time.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, push openers. Second, on a closer, pop and compare. Third, ignore other characters. Fourth, valid if the stack ends empty.

## 6. Worked example (0:47) — `slides/06.png`

An opening bracket: push it.

## 7. Worked example (0:50) — `slides/07.png`

A closing bracket: it must match the top, so we pop.

## 8. Worked example (0:54) — `slides/08.png`

A closing bracket: it must match the top, so we pop.

## 9. Worked example (0:59) — `slides/09.png`

An opening bracket: push it.

## 10. Worked example (1:02) — `slides/10.png`

A closing bracket: it must match the top, so we pop.

## 11. Java solution (1:07) — `slides/11.png`

We push openers. For closers, we fail if the stack is empty or the popped opener doesn't correspond. At the end the stack must be empty.

## 12. Complexity (1:17) — `slides/12.png`

Time is O of n. Space is O of n.

## 13. Edge cases & pitfalls (1:21) — `slides/13.png`

A closer with an empty stack fails, and leftover openers at the end fail too.

## 14. Interview tips & follow-ups (1:26) — `slides/14.png`

A follow-up asks for the minimum insertions to balance a string.

## 15. Recap (1:31) — `slides/15.png`

To recap Balanced Brackets: A stack matches each closing bracket with the most recent opening one. Try re-implementing it from scratch without looking.
