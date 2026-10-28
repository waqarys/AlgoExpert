# AlgoExpert · Zero Sum Subarray

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Zero Sum Subarray (0:00) — `slides/01.png`

Let's solve Zero Sum Subarray, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Does any non-empty contiguous subarray sum to zero? A repeated prefix sum proves it.

## 3. Intuition (0:20) — `slides/03.png`

If two prefix sums are equal, the elements between them sum to zero.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

Checking every subarray is at least quadratic. With prefix sums, if the same running total appears twice, everything between those positions sums to zero. A hash set detects that in linear time.

## 5. Approach (0:38) — `slides/05.png`

Step by step. First, keep a set of prefix sums starting with zero. Second, add each element to the running sum. Third, if the sum was seen before, return true.

## 6. Worked example (0:51) — `slides/06.png`

Adding 4, the prefix sum is 4, which we haven't seen. Add it to the set.

## 7. Worked example (0:58) — `slides/07.png`

Adding 2, the prefix sum is 6, which we haven't seen. Add it to the set.

## 8. Worked example (1:04) — `slides/08.png`

Adding -1, the prefix sum is 5, which we haven't seen. Add it to the set.

## 9. Worked example (1:11) — `slides/09.png`

The prefix sum is 4 again, so the elements in between sum to zero. Return true.

## 10. Java solution (1:18) — `slides/10.png`

We seed a set with zero, keep a running sum, and return true as soon as adding a sum to the set fails because it's already there.

## 11. Complexity (1:26) — `slides/11.png`

Time is O of n. Space is O of n.

## 12. Edge cases & pitfalls (1:30) — `slides/12.png`

Seed the set with zero so a subarray starting at index zero is detected. A single zero element counts.

## 13. Interview tips & follow-ups (1:38) — `slides/13.png`

Follow-ups count zero-sum subarrays with a map of counts, or look for a target sum k.

## 14. Recap (1:44) — `slides/14.png`

To recap Zero Sum Subarray: If two prefix sums are equal, the elements between them sum to zero. Try re-implementing it from scratch without looking.
