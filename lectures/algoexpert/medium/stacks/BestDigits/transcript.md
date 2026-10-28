# AlgoExpert · Best Digits

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Best Digits (0:00) — `slides/01.png`

Let's solve Best Digits, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Remove exactly numDigits digits from a number string to make the largest possible number. Monotonic decreasing stack.

## 3. Intuition (0:21) — `slides/03.png`

Greedy with a stack: drop a previous digit whenever a larger one arrives, while deletions remain.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Trying every set of removals is exponential. A greedy monotonic stack pops smaller digits whenever a bigger one arrives, because a bigger digit earlier always makes a bigger number.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, push digits. Second, pop smaller tops while deletions remain. Third, trim extra from the end.

## 6. Worked example (0:50) — `slides/06.png`

Read 4. Keep it.

## 7. Worked example (0:54) — `slides/07.png`

Read 6. It's bigger than 4 on the stack, so removing those makes the number larger.

## 8. Worked example (1:01) — `slides/08.png`

Read 2. Keep it.

## 9. Worked example (1:05) — `slides/09.png`

Read 8. It's bigger than 2 on the stack, so removing those makes the number larger.

## 10. Worked example (1:12) — `slides/10.png`

Read 3. Keep it.

## 11. Worked example (1:16) — `slides/11.png`

Read 9. Keep it.

## 12. Java solution (1:19) — `slides/12.png`

For each digit, while removals remain and the top is smaller, pop and decrement. Push the digit. Then pop from the end any remaining removals and join.

## 13. Complexity (1:30) — `slides/13.png`

Time is O of n. Space is O of n.

## 14. Edge cases & pitfalls (1:34) — `slides/14.png`

If removals remain after the scan, drop digits from the end.

## 15. Interview tips & follow-ups (1:39) — `slides/15.png`

The mirror problem, remove k digits for the smallest number, flips the comparison.

## 16. Recap (1:45) — `slides/16.png`

To recap Best Digits: Greedy with a stack: drop a previous digit whenever a larger one arrives, while deletions remain. Try re-implementing it from scratch without looking.
