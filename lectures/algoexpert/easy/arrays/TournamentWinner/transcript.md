# AlgoExpert · Tournament Winner

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Tournament Winner (0:00) — `slides/01.png`

Let's solve Tournament Winner, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Competitions are home, away pairs, results i equals equals 1 means home won. A win is worth 3 points; return the team with most points (guaranteed unique).

## 3. Intuition (0:23) — `slides/03.png`

Every match has exactly one winner worth three points, so a running score table is all we need.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, keep a hash map of team to points. Second, for each match, credit the winner. Third, track the leader as scores change. Fourth, return the best team.

## 5. Java solution (0:44) — `slides/05.png`

Here's the Java solution, starting with tournament winner. It follows the steps we just described.

## 6. Complexity (0:51) — `slides/06.png`

Time is O of n. Space is O of k teams.

## 7. Recap (0:55) — `slides/07.png`

To recap Tournament Winner: Every match has exactly one winner worth three points, so a running score table is all we need. Try re-implementing it from scratch without looking.
