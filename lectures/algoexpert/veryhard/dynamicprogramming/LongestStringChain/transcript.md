# AlgoExpert · Longest String Chain

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Longest String Chain (0:00) — `slides/01.png`

Let's solve Longest String Chain, a very hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. A chain is built by removing one character at a time where every intermediate string is in the input. Return the longest chain (length over equals 2) from longest to shortest, or .

## 3. Intuition (0:25) — `slides/03.png`

Process strings by length; each string's chain extends the best chain of any one-character-shorter string.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, sort by length. Second, for each string, try removing each character. Third, look up the result. Fourth, keep best lengths and next links.

## 5. Java solution (0:46) — `slides/05.png`

Here's the Java solution, starting with longest string chain. It follows the steps we just described.

## 6. Complexity (0:53) — `slides/06.png`

Time is O of n times m squared plus n log n. Space is O of n times m.

## 7. Recap (0:59) — `slides/07.png`

To recap Longest String Chain: Process strings by length; each string's chain extends the best chain of any one-character-shorter string. Try re-implementing it from scratch without looking.
