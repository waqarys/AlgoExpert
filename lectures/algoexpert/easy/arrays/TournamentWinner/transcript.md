# AlgoExpert · Tournament Winner

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Tournament Winner (0:00) — `slides/01.png`

Let's solve Tournament Winner, an easy arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Competitions are home, away pairs, results i equals equals 1 means home won. A win is worth 3 points; return the team with most points (guaranteed unique).

## 3. Intuition (0:23) — `slides/03.png`

Every match has exactly one winner worth three points, so a running score table is all we need.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

There isn't a slow brute force here so much as a clumsy one: tally everything, then scan the table for the max. We can do it in a single pass by updating the leader whenever a team's score passes it.

## 5. Approach (0:41) — `slides/05.png`

Step by step. First, keep a hash map of team to points. Second, for each match, credit the winner. Third, track the leader as scores change. Fourth, return the best team.

## 6. Worked example (0:56) — `slides/06.png`

HTML plays C#, and the result is 0, so C# wins and gets three points. The current leader is C#.

## 7. Worked example (1:05) — `slides/07.png`

C# plays Python, and the result is 0, so Python wins and gets three points. The current leader is C#.

## 8. Worked example (1:13) — `slides/08.png`

Python plays HTML, and the result is 1, so Python wins and gets three points. The current leader is Python.

## 9. Java solution (1:22) — `slides/09.png`

We loop over competitions and results together, pick the winner, add three points in the map, and update the leader if this team now has more points than the current leader.

## 10. Complexity (1:31) — `slides/10.png`

Time is O of n. Space is O of k teams.

## 11. Edge cases & pitfalls (1:35) — `slides/11.png`

The main pitfall is reading the result backwards: one means the home team won. Initialise the leader as an empty name with zero points so the first winner takes over.

## 12. Interview tips & follow-ups (1:46) — `slides/12.png`

Clarify the result encoding before you start. A natural follow-up is how you'd break ties, for example alphabetically.

## 13. Recap (1:54) — `slides/13.png`

To recap Tournament Winner: Every match has exactly one winner worth three points, so a running score table is all we need. Try re-implementing it from scratch without looking.
