# AlgoExpert · Blackjack Probability

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Blackjack Probability (0:00) — `slides/01.png`

Let's solve Blackjack Probability, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. The dealer draws cards valued 1-10 uniformly while below target-4; busts if above target. Starting from a hand value, probability of busting (rounded to 3 decimals). Memoised recursion.

## 3. Intuition (0:27) — `slides/03.png`

The chance of busting from hand total t is the average over the ten next cards, which we memoise.

## 4. Approach (0:33) — `slides/04.png`

Step by step. First, if the total exceeds the target, it's a bust. Second, if it reaches target minus four, stop. Third, otherwise average the ten draws. Fourth, memoise by total.

## 5. Java solution (0:49) — `slides/05.png`

Here's the Java solution, starting with blackjack probability. It follows the steps we just described.

## 6. Complexity (0:56) — `slides/06.png`

Time is O of t. Space is O of t.

## 7. Recap (1:00) — `slides/07.png`

To recap Blackjack Probability: The chance of busting from hand total t is the average over the ten next cards, which we memoise. Try re-implementing it from scratch without looking.
