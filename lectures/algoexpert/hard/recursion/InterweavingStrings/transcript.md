# AlgoExpert · Interweaving Strings

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Interweaving Strings (0:00) — `slides/01.png`

Let's solve Interweaving Strings, a hard recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Can three be formed by interleaving one and two keeping each one's order?

## 3. Intuition (0:18) — `slides/03.png`

Each prefix pair of the two strings either explains the next character of three or not, so memoise by indices.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, recursive i and j into one and two. Second, next character of three must come from one or the other. Third, memoise failed states. Fourth, succeed when all are used.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with interweaving strings. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n times m. Space is O of m.

## 7. Recap (0:52) — `slides/07.png`

To recap Interweaving Strings: Each prefix pair of the two strings either explains the next character of three or not, so memoise by indices. Try re-implementing it from scratch without looking.
