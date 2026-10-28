# AlgoExpert · Continuous Median

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Continuous Median (0:00) — `slides/01.png`

Let's solve Continuous Median, a hard heaps problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Insert numbers one at a time and query the running median, using a max-heap for the lower half and a min-heap for the upper half.

## 3. Intuition (0:20) — `slides/03.png`

Keep the smaller half in a max-heap and the larger half in a min-heap, balanced in size.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, insert into the right heap. Second, rebalance so sizes differ by at most one. Third, median is the top of the bigger heap or the average of tops.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with insert. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of log n insert, constant median. Space is O of n.

## 7. Recap (0:53) — `slides/07.png`

To recap Continuous Median: Keep the smaller half in a max-heap and the larger half in a min-heap, balanced in size. Try re-implementing it from scratch without looking.
