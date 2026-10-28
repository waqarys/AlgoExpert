# AlgoExpert · Detect Arbitrage

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Detect Arbitrage (0:00) — `slides/01.png`

Let's solve Detect Arbitrage, a very hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Exchange-rate matrix; is there a cycle of trades yielding profit? Take -log(rate) edge weights and look for a negative cycle with Bellman-Ford.

## 3. Intuition (0:23) — `slides/03.png`

Multiplying rates becomes adding minus logs, so profit means a negative cycle, found by Bellman-Ford.

## 4. Approach (0:30) — `slides/04.png`

Step by step. First, weights are minus log of the rate. Second, relax all edges n minus one times. Third, if any edge still relaxes, there's arbitrage.

## 5. Java solution (0:43) — `slides/05.png`

Here's the Java solution, starting with detect arbitrage. It follows the steps we just described.

## 6. Complexity (0:50) — `slides/06.png`

Time is O of n cubed. Space is O of n squared.

## 7. Recap (0:55) — `slides/07.png`

To recap Detect Arbitrage: Multiplying rates becomes adding minus logs, so profit means a negative cycle, found by Bellman-Ford. Try re-implementing it from scratch without looking.
