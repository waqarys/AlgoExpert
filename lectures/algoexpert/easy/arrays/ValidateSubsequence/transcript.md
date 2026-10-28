# AlgoExpert · Validate Subsequence

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Validate Subsequence (0:00) — `slides/01.png`

Let's solve Validate Subsequence, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Is sequence obtainable from array by deleting elements without reordering?

## 3. Intuition (0:17) — `slides/03.png`

A subsequence keeps order, so we just try to match the sequence's elements one by one while scanning the array.

## 4. Brute force vs optimal (0:24) — `slides/04.png`

A brute-force approach would try every way of choosing positions in the array, which is exponential. But matching each sequence element at its earliest opportunity is always safe, so one pass with two indices is enough.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, keep an index into the sequence. Second, scan the array. Third, advance the index on every match. Fourth, valid if the index reaches the end.

## 6. Worked example (0:51) — `slides/06.png`

The array value 1 matches the next sequence item, so j advances to 1.

## 7. Worked example (0:57) — `slides/07.png`

The array value 6 matches the next sequence item, so j advances to 2.

## 8. Worked example (1:03) — `slides/08.png`

The array value -1 matches the next sequence item, so j advances to 3.

## 9. Worked example (1:08) — `slides/09.png`

The array value 10 matches the next sequence item, so j advances to 4.

## 10. Worked example (1:14) — `slides/10.png`

We matched every element of the sequence, so it's a valid subsequence.

## 11. Java solution (1:19) — `slides/11.png`

We keep an index into the sequence. Scanning the array, whenever the current value equals the next sequence element, we advance that index. The answer is whether the index reached the sequence length.

## 12. Complexity (1:32) — `slides/12.png`

Time is O of n. Space is constant.

## 13. Edge cases & pitfalls (1:36) — `slides/13.png`

If the sequence is longer than the array it can't be a subsequence. Each array element can only be used once, which the single forward pass guarantees.

## 14. Interview tips & follow-ups (1:46) — `slides/14.png`

Clarify the difference between a subsequence and a subarray: subsequences don't have to be contiguous. A follow-up is checking many sequences quickly, where you'd preprocess positions of each value.

## 15. Recap (1:58) — `slides/15.png`

To recap Validate Subsequence: A subsequence keeps order, so we just try to match the sequence's elements one by one while scanning the array. Try re-implementing it from scratch without looking.
