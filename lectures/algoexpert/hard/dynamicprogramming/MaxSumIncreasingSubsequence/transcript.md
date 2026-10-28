# AlgoExpert · Max Sum Increasing Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Max Sum Increasing Subsequence (0:00) — `slides/01.png`

Let's solve Max Sum Increasing Subsequence, a hard dynamic programming problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Returns maxSum , subsequence for the strictly increasing subsequence with the greatest sum.

## 3. Intuition (0:20) — `slides/03.png`

For each index, the best sum ending there extends the best smaller earlier element.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, for each i, scan earlier j with smaller value. Second, keep best sums and predecessors. Third, rebuild the sequence from the best end.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with max sum increasing subsequence. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n squared. Space is O of n.

## 7. Recap (0:52) — `slides/07.png`

To recap Max Sum Increasing Subsequence: For each index, the best sum ending there extends the best smaller earlier element. Try re-implementing it from scratch without looking.
