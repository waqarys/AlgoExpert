# AlgoExpert · Radix Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Radix Sort (0:00) — `slides/01.png`

Let's solve Radix Sort, a hard sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sort non-negative ints by LSD radix sort with counting sort per decimal digit.

## 3. Intuition (0:19) — `slides/03.png`

Sort by each decimal digit from least significant, using a stable counting sort each time.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Comparison sorts can't beat n log n. Radix sort processes one digit at a time with a stable counting sort, d times n plus ten.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, find the max to know digit count. Second, for each digit, count, prefix sum, and place stably. Third, copy back.

## 6. Worked example (0:45) — `slides/06.png`

Stable counting sort on the ones digit. Earlier digit orderings are preserved within ties.

## 7. Worked example (0:52) — `slides/07.png`

Stable counting sort on the tens digit. Earlier digit orderings are preserved within ties.

## 8. Worked example (0:59) — `slides/08.png`

Stable counting sort on the hundreds digit. Earlier digit orderings are preserved within ties.

## 9. Worked example (1:07) — `slides/09.png`

Stable counting sort on the thousands digit. Earlier digit orderings are preserved within ties.

## 10. Java solution (1:14) — `slides/10.png`

For each digit place up to the max, we count digits, prefix-sum the counts, place elements from the end into out, and copy back.

## 11. Complexity (1:22) — `slides/11.png`

Time is O of d times (n plus 10). Space is O of n.

## 12. Edge cases & pitfalls (1:28) — `slides/12.png`

Each pass must be stable, which is why we fill from the end.

## 13. Interview tips & follow-ups (1:32) — `slides/13.png`

Radix wins when keys are short relative to log n.

## 14. Recap (1:37) — `slides/14.png`

To recap Radix Sort: Sort by each decimal digit from least significant, using a stable counting sort each time. Try re-implementing it from scratch without looking.
