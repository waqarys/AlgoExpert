# AlgoExpert · Move Element To End

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Move Element To End (0:00) — `slides/01.png`

Let's solve Move Element To End, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. In place, move every occurrence of toMove to the end (other order irrelevant).

## 3. Intuition (0:18) — `slides/03.png`

Two pointers: move the target from the left end out of the way by swapping with non-targets from the right.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, left and right pointers. Second, skip targets already at the right. Third, swap a target on the left with a non-target on the right. Fourth, meet in the middle.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with move element to end. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Move Element To End: Two pointers: move the target from the left end out of the way by swapping with non-targets from the right. Try re-implementing it from scratch without looking.
