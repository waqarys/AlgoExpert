# AlgoExpert · Remove Kth Node From End

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Remove Kth Node From End (0:00) — `slides/01.png`

Let's solve Remove Kth Node From End, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Remove in place (list length over equals 2, k valid). If the head is removed, the head node takes its successor's value so the reference stays valid.

## 3. Intuition (0:24) — `slides/03.png`

Keep a gap of k between two pointers so the leading one hits the end when the trailing one is just before the target.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, advance the lead k steps. Second, move both until the lead ends. Third, unlink the target, handling the head.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with remove kth node from end. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:54) — `slides/07.png`

To recap Remove Kth Node From End: Keep a gap of k between two pointers so the leading one hits the end when the trailing one is just before the target. Try re-implementing it from scratch without looking.
