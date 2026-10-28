# AlgoExpert · Knuth Morris Pratt Algorithm

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Knuth Morris Pratt Algorithm (0:00) — `slides/01.png`

Let's solve Knuth Morris Pratt Algorithm, a very hard famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:13) — `slides/02.png`

Here's the problem. Does sub occur in str? Prefix-function (failure table) matching.

## 3. Intuition (0:21) — `slides/03.png`

A failure table tells us how far to fall back on a mismatch, so we never rescan the text.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, build the prefix function of the pattern. Second, walk the text. Third, on mismatch, fall back via the table. Fourth, match when the pattern is complete.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with knuth morris pratt algorithm. It follows the steps we just described.

## 6. Complexity (0:49) — `slides/06.png`

Time is O of n plus m. Space is O of m.

## 7. Recap (0:53) — `slides/07.png`

To recap Knuth Morris Pratt Algorithm: A failure table tells us how far to fall back on a mismatch, so we never rescan the text. Try re-implementing it from scratch without looking.
