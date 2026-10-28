# AlgoExpert · Sorted Squared Array

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Sorted Squared Array (0:00) — `slides/01.png`

Let's solve Sorted Squared Array, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Given a sorted array (may contain negatives) return the squares in sorted order. Two pointers from both ends fill the result from the back.

## 3. Intuition (0:22) — `slides/03.png`

The largest squares sit at the two ends of a sorted array, because big negatives square to big positives.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, put pointers at both ends. Second, compare absolute values. Third, write the larger square into the result from the back. Fourth, move that pointer inward.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with sorted squared array. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:55) — `slides/07.png`

To recap Sorted Squared Array: The largest squares sit at the two ends of a sorted array, because big negatives square to big positives. Try re-implementing it from scratch without looking.
