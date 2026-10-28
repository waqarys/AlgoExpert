# AlgoExpert · Right Smaller Than

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Right Smaller Than (0:00) — `slides/01.png`

Let's solve Right Smaller Than, a very hard binary search trees problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. For each element, how many elements to its right are strictly smaller? Insert from the right into an augmented BST tracking left-subtree sizes.

## 3. Intuition (0:23) — `slides/03.png`

Insert from the right into a BST that knows its left-subtree sizes; each insert counts the smaller values already there.

## 4. Approach (0:31) — `slides/04.png`

Step by step. First, iterate from the end. Second, insert into an augmented BST. Third, add left sizes when going right. Fourth, record the count.

## 5. Java solution (1/2) (0:45) — `slides/05.png`

Here's the Java solution. It follows the steps we just described.

## 6. Java solution (2/2) (0:50) — `slides/06.png`

Continuing with right smaller than.

## 7. Complexity (0:54) — `slides/07.png`

Time is O of n log n avg, O of n squared worst. Space is O of n.

## 8. Recap (1:00) — `slides/08.png`

To recap Right Smaller Than: Insert from the right into a BST that knows its left-subtree sizes; each insert counts the smaller values already there. Try re-implementing it from scratch without looking.
