# AlgoExpert · Underscorify Substring

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Underscorify Substring (0:00) — `slides/01.png`

Let's solve Underscorify Substring, a hard strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Wrap every occurrence of sub in str with underscores, merging overlapping or adjacent occurrences into one wrapped block.

## 3. Intuition (0:21) — `slides/03.png`

Find all occurrences, merge overlapping or touching ones, then insert underscores.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, collect occurrence intervals. Second, merge overlaps and adjacency. Third, insert underscores at boundaries.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with underscorify substring. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n times m. Space is O of n.

## 7. Recap (0:50) — `slides/07.png`

To recap Underscorify Substring: Find all occurrences, merge overlapping or touching ones, then insert underscores. Try re-implementing it from scratch without looking.
