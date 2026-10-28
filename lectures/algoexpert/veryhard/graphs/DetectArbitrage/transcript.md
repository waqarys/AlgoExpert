# AlgoExpert · Detect Arbitrage

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Detect Arbitrage (0:00) — `slides/01.png`

Let's solve Detect Arbitrage, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Exchange-rate matrix; is there a cycle of trades yielding profit? Take -log(rate) edge weights and look for a negative cycle with Bellman-Ford.

## 3. Intuition (0:23) — `slides/03.png`

Multiplying rates becomes adding minus logs, so profit means a negative cycle, found by Bellman-Ford.

## 4. Brute force vs optimal (0:30) — `slides/04.png`

Trying all cycles is exponential. Converting to minus log weights and detecting a negative cycle with Bellman-Ford is n cubed for a complete graph.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, weights are minus log of the rate. Second, relax all edges n minus one times. Third, if any edge still relaxes, there's arbitrage.

## 6. Worked example (0:52) — `slides/06.png`

Is there a cycle of trades that multiplies money above one?

## 7. Worked example (0:57) — `slides/07.png`

Taking minus log turns multiplication into addition, and a product above one into a negative-weight cycle.

## 8. Worked example (1:04) — `slides/08.png`

Bellman-Ford keeps improving after n minus one passes, so there's a negative cycle: arbitrage. For example, USD to CAD to GBP and back gives 1.0013.

## 9. Java solution (1:16) — `slides/09.png`

Distances start at max except zero. We relax every pair n times with minus log rates; if anything still changes on the last pass, return true.

## 10. Complexity (1:26) — `slides/10.png`

Time is O of n cubed. Space is O of n squared.

## 11. Edge cases & pitfalls (1:31) — `slides/11.png`

Use a small epsilon in comparisons.

## 12. Interview tips & follow-ups (1:35) — `slides/12.png`

The log transform is the key insight.

## 13. Recap (1:38) — `slides/13.png`

To recap Detect Arbitrage: Multiplying rates becomes adding minus logs, so profit means a negative cycle, found by Bellman-Ford. Try re-implementing it from scratch without looking.
