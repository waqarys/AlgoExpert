# AlgoExpert · Remove Kth Node From End

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Remove Kth Node From End (0:00) — `slides/01.png`

Let's solve Remove Kth Node From End, a medium linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Remove in place (list length over equals 2, k valid). If the head is removed, the head node takes its successor's value so the reference stays valid.

## 3. Intuition (0:24) — `slides/03.png`

Keep a gap of k between two pointers so the leading one hits the end when the trailing one is just before the target.

## 4. Brute force vs optimal (0:31) — `slides/04.png`

Two passes, one to count and one to walk, works fine. The single-pass trick keeps two pointers exactly k apart, so when the leading one reaches the end, the trailing one is right before the target.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, advance the lead k steps. Second, move both until the lead ends. Third, unlink the target, handling the head.

## 6. Worked example (0:55) — `slides/06.png`

Move fast 4 nodes ahead, so the gap between fast and slow is exactly k.

## 7. Worked example (1:00) — `slides/07.png`

Move both together. Slow is at 2, fast at 6.

## 8. Worked example (1:06) — `slides/08.png`

Move both together. Slow is at 5, fast at 9.

## 9. Worked example (1:11) — `slides/09.png`

Fast is at the last node, so slow is just before the k-th from the end. Skip over 6 to remove it.

## 10. Java solution (1:19) — `slides/10.png`

Fast moves k steps. If it's null, the head is the target, so we overwrite the head with its next. Otherwise we advance both until fast is the last node and skip slow's next.

## 11. Complexity (1:31) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:35) — `slides/12.png`

Removing the head is the special case: fast becomes null, so we copy the second node into the head and skip it.

## 13. Interview tips & follow-ups (1:42) — `slides/13.png`

Using a dummy node avoids the head special case. Mention it.

## 14. Recap (1:48) — `slides/14.png`

To recap Remove Kth Node From End: Keep a gap of k between two pointers so the leading one hits the end when the trailing one is just before the target. Try re-implementing it from scratch without looking.
