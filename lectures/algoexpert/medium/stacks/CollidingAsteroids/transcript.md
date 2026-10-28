# AlgoExpert · Colliding Asteroids

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Colliding Asteroids (0:00) — `slides/01.png`

Let's solve Colliding Asteroids, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Sign is direction ( plus right, - left), magnitude is size. When they meet the smaller explodes (both if equal). Return survivors.

## 3. Intuition (0:23) — `slides/03.png`

Simulate collisions with a stack of surviving asteroids.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, right movers push. Second, a left mover destroys smaller right movers on top. Third, equal sizes destroy both. Fourth, survivors remain.

## 5. Java solution (0:42) — `slides/05.png`

Here's the Java solution, starting with colliding asteroids. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n. Space is O of n.

## 7. Recap (0:53) — `slides/07.png`

To recap Colliding Asteroids: Simulate collisions with a stack of surviving asteroids. Try re-implementing it from scratch without looking.
