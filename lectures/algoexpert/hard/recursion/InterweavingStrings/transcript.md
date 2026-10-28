# AlgoExpert · Interweaving Strings

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Interweaving Strings (0:00) — `slides/01.png`

Let's solve Interweaving Strings, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Can three be formed by interleaving one and two keeping each one's order?

## 3. Intuition (0:18) — `slides/03.png`

Each prefix pair of the two strings either explains the next character of three or not, so memoise by indices.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Recursing on which string supplies the next letter is exponential. The state is just i and j, so memoising makes it n times m.

## 5. Approach (0:34) — `slides/05.png`

Step by step. First, recursive i and j into one and two. Second, next character of three must come from one or the other. Third, memoise failed states. Fourth, succeed when all are used.

## 6. Worked example (0:49) — `slides/06.png`

Can we build fralgogo by interleaving algo and frog, keeping each in order?

## 7. Worked example (0:55) — `slides/07.png`

Dp i, j says whether the first i letters of one and j letters of two make the first i plus j letters of three. A cell is reachable from above if one's letter matches, or from the left if two's does.

## 8. Worked example (1:07) — `slides/08.png`

The bottom-right cell is true, so the answer is yes.

## 9. Java solution (1:11) — `slides/09.png`

We check lengths, then recurse on i and j with a memo: if one's letter matches the next of three try advancing i, and if two's matches try advancing j.

## 10. Complexity (1:20) — `slides/10.png`

Time is O of n times m. Space is O of m.

## 11. Edge cases & pitfalls (1:24) — `slides/11.png`

If lengths don't add up, return false immediately.

## 12. Interview tips & follow-ups (1:28) — `slides/12.png`

A one-dimensional DP row is enough.

## 13. Recap (1:32) — `slides/13.png`

To recap Interweaving Strings: Each prefix pair of the two strings either explains the next character of three or not, so memoise by indices. Try re-implementing it from scratch without looking.
