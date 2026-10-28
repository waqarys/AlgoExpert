# AlgoExpert · Colliding Asteroids

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Colliding Asteroids (0:00) — `slides/01.png`

Let's solve Colliding Asteroids, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sign is direction ( plus right, - left), magnitude is size. When they meet the smaller explodes (both if equal). Return survivors.

## 3. Intuition (0:23) — `slides/03.png`

Simulate collisions with a stack of surviving asteroids.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Re-simulating until nothing changes is quadratic. A stack of survivors handles each asteroid in amortised constant time, since each is pushed and popped at most once. Only a right-mover followed by a left-mover collides.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, right movers push. Second, a left mover destroys smaller right movers on top. Third, equal sizes destroy both. Fourth, survivors remain.

## 6. Worked example (0:57) — `slides/06.png`

Asteroid -3: nothing to collide with, push it.

## 7. Worked example (1:01) — `slides/07.png`

Asteroid 5: nothing to collide with, push it.

## 8. Worked example (1:05) — `slides/08.png`

Asteroid -8: -8 destroys 5.

## 9. Worked example (1:09) — `slides/09.png`

Asteroid 7: nothing to collide with, push it.

## 10. Worked example (1:14) — `slides/10.png`

Asteroid -4: 7 destroys -4.

## 11. Worked example (1:18) — `slides/11.png`

Asteroid -7: -7 and 7 both explode.

## 12. Java solution (1:23) — `slides/12.png`

For each asteroid we loop while it's alive, moving left, and the top moves right. A smaller top is popped; otherwise equal sizes pop the top and either way the current one dies. Survivors are pushed.

## 13. Complexity (1:36) — `slides/13.png`

Time is O of n. Space is O of n.

## 14. Edge cases & pitfalls (1:40) — `slides/14.png`

A left-mover before a right-mover never collides. Equal sizes destroy both.

## 15. Interview tips & follow-ups (1:46) — `slides/15.png`

State the collision condition first; the rest follows.

## 16. Recap (1:51) — `slides/16.png`

To recap Colliding Asteroids: Simulate collisions with a stack of surviving asteroids. Try re-implementing it from scratch without looking.
