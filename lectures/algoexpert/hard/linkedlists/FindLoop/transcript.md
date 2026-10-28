# AlgoExpert · Find Loop

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Find Loop (0:00) — `slides/01.png`

Let's solve Find Loop, a hard linked lists problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. The list contains a cycle; return the node where the loop begins (Floyd's algorithm).

## 3. Intuition (0:18) — `slides/03.png`

Floyd's cycle detection: after slow and fast meet, a pointer from the head and one from the meeting point meet at the loop start.

## 4. Brute force vs optimal (0:26) — `slides/04.png`

Storing visited nodes finds the loop start but uses memory. Floyd's algorithm uses two speeds to meet inside the loop, then a reset finds the start with constant space.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, slow moves one, fast two. Second, they meet inside the loop. Third, reset one to the head. Fourth, move both by one until they meet.

## 6. Worked example (0:51) — `slides/06.png`

The tail points back to node four. Slow moves one step, fast two.

## 7. Worked example (0:57) — `slides/07.png`

They meet inside the loop, at node 6.

## 8. Worked example (1:00) — `slides/08.png`

Reset slow to the head; now both move one step at a time.

## 9. Worked example (1:05) — `slides/09.png`

After 4 steps they meet at node 4, the start of the loop. The distance from head to loop start equals the distance from the meeting point to loop start.

## 10. Java solution (1:14) — `slides/10.png`

Slow and fast start one and two steps in and move until equal. Then slow restarts at the head and both move one step until they meet at the loop start.

## 11. Complexity (1:24) — `slides/11.png`

Time is O of n. Space is constant.

## 12. Edge cases & pitfalls (1:28) — `slides/12.png`

Initialise the pointers carefully and compare nodes by identity.

## 13. Interview tips & follow-ups (1:32) — `slides/13.png`

Be ready to prove why the reset works.

## 14. Recap (1:36) — `slides/14.png`

To recap Find Loop: Floyd's cycle detection: after slow and fast meet, a pointer from the head and one from the meeting point meet at the loop start. Try re-implementing it from scratch without looking.
