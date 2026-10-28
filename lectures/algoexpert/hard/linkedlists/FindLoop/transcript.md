# AlgoExpert · Find Loop

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Loop (0:00) — `slides/01.png`

Let's solve Find Loop, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. The list contains a cycle; return the node where the loop begins (Floyd's algorithm).

## 3. Intuition (0:18) — `slides/03.png`

Floyd's cycle detection: after slow and fast meet, a pointer from the head and one from the meeting point meet at the loop start.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, slow moves one, fast two. Second, they meet inside the loop. Third, reset one to the head. Fourth, move both by one until they meet.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with find loop. It follows the steps we just described.

## 6. Complexity (0:46) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:50) — `slides/07.png`

To recap Find Loop: Floyd's cycle detection: after slow and fast meet, a pointer from the head and one from the meeting point meet at the loop start. Try re-implementing it from scratch without looking.
