# AlgoExpert · Reverse Polish Notation

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reverse Polish Notation (0:00) — `slides/01.png`

Let's solve Reverse Polish Notation, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Evaluate postfix tokens with plus - / (integer division truncating toward zero).

## 3. Intuition (0:20) — `slides/03.png`

Operands go on a stack; each operator pops two and pushes the result.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, push numbers. Second, on an operator, pop right then left. Third, apply and push. Fourth, return the last value.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with reverse polish notation. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:49) — `slides/07.png`

To recap Reverse Polish Notation: Operands go on a stack; each operator pops two and pushes the result. Try re-implementing it from scratch without looking.
