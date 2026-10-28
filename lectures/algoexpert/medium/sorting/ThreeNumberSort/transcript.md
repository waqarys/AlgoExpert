# AlgoExpert · Three Number Sort

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Three Number Sort (0:00) — `slides/01.png`

Let's solve Three Number Sort, a medium sorting problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sort an array in place according to a 3-value order (Dutch national flag).

## 3. Intuition (0:18) — `slides/03.png`

Dutch national flag: three regions grown by three pointers in one pass.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Sorting is n log n. Counting each value and rewriting is linear but two passes. The Dutch national flag algorithm does it in one pass with three pointers.

## 5. Approach (0:33) — `slides/05.png`

Step by step. First, first, second and third pointers. Second, swap firsts to the front. Third, leave seconds. Fourth, swap thirds to the back.

## 6. Worked example (0:47) — `slides/06.png`

Mid saw 1, the second value, so we leave it.

## 7. Worked example (0:51) — `slides/07.png`

Mid saw 0, the first value, so we swap to lo.

## 8. Worked example (0:56) — `slides/08.png`

Mid saw -1, the third value, so we swap to hi.

## 9. Worked example (1:01) — `slides/09.png`

Mid saw 1, the second value, so we leave it.

## 10. Worked example (1:05) — `slides/10.png`

Mid saw 1, the second value, so we leave it.

## 11. Worked example (1:09) — `slides/11.png`

Mid saw 0, the first value, so we swap to lo.

## 12. Java solution (1:14) — `slides/12.png`

Lo, mid and hi start at the ends. While mid is at most hi, first-order values swap to lo and both advance, second-order values just advance mid, and third-order values swap with hi, which moves down.

## 13. Complexity (1:27) — `slides/13.png`

Time is O of n. Space is constant.

## 14. Edge cases & pitfalls (1:31) — `slides/14.png`

After swapping with hi, don't advance mid: the swapped-in value hasn't been examined.

## 15. Interview tips & follow-ups (1:36) — `slides/15.png`

Name the Dutch national flag problem; interviewers like hearing it.

## 16. Recap (1:41) — `slides/16.png`

To recap Three Number Sort: Dutch national flag: three regions grown by three pointers in one pass. Try re-implementing it from scratch without looking.
