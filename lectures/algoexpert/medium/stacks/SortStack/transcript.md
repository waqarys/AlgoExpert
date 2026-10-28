# AlgoExpert · Sort Stack

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sort Stack (0:00) — `slides/01.png`

Let's solve Sort Stack, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sort a stack (list, top equals end) ascending using only push or pop or peek and recursion.

## 3. Intuition (0:19) — `slides/03.png`

Recursively pop to empty, then insert each value back in sorted position.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

With only stack operations, this is insertion sort: sort the rest recursively, then insert the top into place. That's quadratic time and linear recursion depth.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, pop the top and sort the rest. Second, insert it back. Third, insertion pops larger tops temporarily.

## 6. Worked example (0:47) — `slides/06.png`

Sort stack pops the top and recursively sorts the rest, until the stack is empty.

## 7. Worked example (0:53) — `slides/07.png`

Unwinding, insert -5: pop larger tops, place it, and push them back.

## 8. Worked example (0:59) — `slides/08.png`

Unwinding, insert 2: pop larger tops, place it, and push them back.

## 9. Worked example (1:04) — `slides/09.png`

Unwinding, insert 4: pop larger tops, place it, and push them back.

## 10. Worked example (1:10) — `slides/10.png`

Unwinding, insert 3: pop larger tops, place it, and push them back.

## 11. Worked example (1:16) — `slides/11.png`

Unwinding, insert 1: pop larger tops, place it, and push them back.

## 12. Java solution (1:21) — `slides/12.png`

Sort stack removes the top, sorts the rest, and inserts the top. Insert adds the value if the stack is empty or the top is smaller or equal; otherwise it removes the top, inserts recursively and pushes the top back.

## 13. Complexity (1:35) — `slides/13.png`

Time is O of n squared. Space is O of n recursion.

## 14. Edge cases & pitfalls (1:40) — `slides/14.png`

Insert pops while the top is bigger than the value, places it, and pushes the popped values back.

## 15. Interview tips & follow-ups (1:47) — `slides/15.png`

Mention the iterative two-stack version as well.

## 16. Recap (1:51) — `slides/16.png`

To recap Sort Stack: Recursively pop to empty, then insert each value back in sorted position. Try re-implementing it from scratch without looking.
