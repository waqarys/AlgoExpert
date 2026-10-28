# AlgoExpert · Stable Internships

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Stable Internships (0:00) — `slides/01.png`

Let's solve Stable Internships, a medium famous algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. N interns and n teams each rank the other side; produce a stable matching (Gale-Shapley with interns proposing). Returns pairs intern, team .

## 3. Intuition (0:23) — `slides/03.png`

Gale–Shapley: interns propose in preference order; teams keep their favourite so far.

## 4. Brute force vs optimal (0:29) — `slides/04.png`

Checking all n factorial matchings is hopeless. Gale-Shapley has interns propose in preference order, and each team keeps the best proposal so far. Each intern proposes at most n times, so it's quadratic.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, queue of free interns. Second, each proposes to the next team on their list. Third, the team keeps the better intern. Fourth, rejected interns re-queue.

## 6. Worked example (0:58) — `slides/06.png`

Intern 0 proposes to team 0, their next choice. Team 0 was free → accepts intern 0.

## 7. Worked example (1:05) — `slides/07.png`

Intern 1 proposes to team 0, their next choice. Team 0 prefers 1 over 0 → 0 is freed.

## 8. Worked example (1:13) — `slides/08.png`

Intern 2 proposes to team 1, their next choice. Team 1 was free → accepts intern 2.

## 9. Worked example (1:20) — `slides/09.png`

Intern 0 proposes to team 1, their next choice. Team 1 prefers 0 over 2 → 2 is freed.

## 10. Worked example (1:28) — `slides/10.png`

Intern 2 proposes to team 2, their next choice. Team 2 was free → accepts intern 2.

## 11. Java solution (1:35) — `slides/11.png`

We build a rank table for teams, then a queue of free interns. Each free intern proposes to their next team. A free team accepts; otherwise the team keeps whichever intern it ranks higher and the other goes back in the queue. Finally we output intern-team pairs.

## 12. Complexity (1:52) — `slides/12.png`

Time is O of n squared. Space is O of n squared.

## 13. Edge cases & pitfalls (1:58) — `slides/13.png`

Precompute each team's ranking of interns so comparisons are constant time. The result is the best stable matching for the proposing side.

## 14. Interview tips & follow-ups (2:07) — `slides/14.png`

Be ready to argue stability: no intern and team both prefer each other over their matches. The proposing side gets its best stable outcome.

## 15. Recap (2:16) — `slides/15.png`

To recap Stable Internships: Gale–Shapley: interns propose in preference order; teams keep their favourite so far. Try re-implementing it from scratch without looking.
