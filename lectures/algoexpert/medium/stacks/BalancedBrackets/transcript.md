# AlgoExpert · Balanced Brackets

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Balanced Brackets (0:00) — `slides/01.png`

Let's solve Balanced Brackets, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Are (), , properly balanced and nested? Non-bracket chars are ignored.

## 3. Intuition (0:19) — `slides/03.png`

A stack matches each closing bracket with the most recent opening one.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, push openers. Second, on a closer, pop and compare. Third, ignore other characters. Fourth, valid if the stack ends empty.

## 5. Java solution (0:37) — `slides/05.png`

Here's the Java solution, starting with balanced brackets. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:48) — `slides/07.png`

To recap Balanced Brackets: A stack matches each closing bracket with the most recent opening one. Try re-implementing it from scratch without looking.
