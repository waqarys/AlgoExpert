# AlgoExpert · Best Digits

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Best Digits (0:00) — `slides/01.png`

Let's solve Best Digits, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Remove exactly numDigits digits from a number string to make the largest possible number. Monotonic decreasing stack.

## 3. Intuition (0:21) — `slides/03.png`

Greedy with a stack: drop a previous digit whenever a larger one arrives, while deletions remain.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, push digits. Second, pop smaller tops while deletions remain. Third, trim extra from the end.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with best digits. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:50) — `slides/07.png`

To recap Best Digits: Greedy with a stack: drop a previous digit whenever a larger one arrives, while deletions remain. Try re-implementing it from scratch without looking.
