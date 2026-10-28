# AlgoExpert · Reverse Polish Notation

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Reverse Polish Notation (0:00) — `slides/01.png`

Let's solve Reverse Polish Notation, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Evaluate postfix tokens with plus - / (integer division truncating toward zero).

## 3. Intuition (0:20) — `slides/03.png`

Operands go on a stack; each operator pops two and pushes the result.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

You could build an expression tree, but a single stack is enough: numbers are pushed, operators pop two and push the result.

## 5. Approach (0:32) — `slides/05.png`

Step by step. First, push numbers. Second, on an operator, pop right then left. Third, apply and push. Fourth, return the last value.

## 6. Worked example (0:46) — `slides/06.png`

Number: push 50.

## 7. Worked example (0:49) — `slides/07.png`

Number: push 3.

## 8. Worked example (0:51) — `slides/08.png`

Number: push 17.

## 9. Worked example (0:55) — `slides/09.png`

Operator +: pop 17 and 3, compute 3 + 17 = 20, push it.

## 10. Worked example (1:01) — `slides/10.png`

Number: push 2.

## 11. Worked example (1:04) — `slides/11.png`

Operator -: pop 2 and 20, compute 20 - 2 = 18, push it.

## 12. Worked example (1:11) — `slides/12.png`

Operator /: pop 18 and 50, compute 50 / 18 = 2, push it.

## 13. Java solution (1:18) — `slides/13.png`

For each token: plus and times push the result of two pops; minus and divide pop b first then compute a op b; anything else is parsed and pushed. Return the final pop.

## 14. Complexity (1:29) — `slides/14.png`

Time is O of n. Space is O of n.

## 15. Edge cases & pitfalls (1:32) — `slides/15.png`

For minus and divide, the first pop is the right operand. Division truncates toward zero.

## 16. Interview tips & follow-ups (1:39) — `slides/16.png`

A follow-up converts infix to RPN with the shunting-yard algorithm.

## 17. Recap (1:45) — `slides/17.png`

To recap Reverse Polish Notation: Operands go on a stack; each operator pops two and pushes the result. Try re-implementing it from scratch without looking.
