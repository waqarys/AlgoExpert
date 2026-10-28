# AlgoExpert · Stable Internships

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Stable Internships (0:00) — `slides/01.png`

Let's solve Stable Internships, a medium famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. N interns and n teams each rank the other side; produce a stable matching (Gale-Shapley with interns proposing). Returns pairs intern, team .

## 3. Intuition (0:23) — `slides/03.png`

Gale–Shapley: interns propose in preference order; teams keep their favourite so far.

## 4. Approach (0:29) — `slides/04.png`

Step by step. First, queue of free interns. Second, each proposes to the next team on their list. Third, the team keeps the better intern. Fourth, rejected interns re-queue.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with stable internships. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n squared. Space is O of n squared.

## 7. Recap (0:57) — `slides/07.png`

To recap Stable Internships: Gale–Shapley: interns propose in preference order; teams keep their favourite so far. Try re-implementing it from scratch without looking.
