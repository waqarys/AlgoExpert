# AlgoExpert · Move Element To End

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Move Element To End (0:00) — `slides/01.png`

Let's solve Move Element To End, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In place, move every occurrence of toMove to the end (other order irrelevant).

## 3. Intuition (0:18) — `slides/03.png`

Two pointers: move the target from the left end out of the way by swapping with non-targets from the right.

## 4. Brute force vs optimal (0:25) — `slides/04.png`

You could build a new list, or bubble each two to the end one step at a time, which is quadratic. Two pointers swap targets from the left with non-targets from the right in a single pass, in place.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, left and right pointers. Second, skip targets already at the right. Third, swap a target on the left with a non-target on the right. Fourth, meet in the middle.

## 6. Worked example (0:52) — `slides/06.png`

The right pointer skips trailing twos and stops at index 6. The left value was a two, so we swap it to the right.

## 7. Worked example (1:00) — `slides/07.png`

The value at index 1 isn't a two, so it stays.

## 8. Worked example (1:04) — `slides/08.png`

The right pointer skips trailing twos and stops at index 5. The left value was a two, so we swap it to the right.

## 9. Worked example (1:13) — `slides/09.png`

The right pointer skips trailing twos and stops at index 3. The left value was a two, so we swap it to the right.

## 10. Java solution (1:21) — `slides/10.png`

While l is less than r, we move r left past targets, swap if the left element is the target, then advance l.

## 11. Complexity (1:28) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:32) — `slides/12.png`

The problem doesn't require preserving order of the other elements. Guard the inner loop with l less than r so it never crosses.

## 13. Interview tips & follow-ups (1:40) — `slides/13.png`

If order must be preserved, use a write pointer that copies non-targets forward, then fill the tail with targets.

## 14. Recap (1:48) — `slides/14.png`

To recap Move Element To End: Two pointers: move the target from the left end out of the way by swapping with non-targets from the right. Try re-implementing it from scratch without looking.
