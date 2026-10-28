# AlgoExpert · Blackjack Probability

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Blackjack Probability (0:00) — `slides/01.png`

Let's solve Blackjack Probability, a medium recursion problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. The dealer draws cards valued 1-10 uniformly while below target-4; busts if above target. Starting from a hand value, probability of busting (rounded to 3 decimals). Memoised recursion.

## 3. Intuition (0:27) — `slides/03.png`

The chance of busting from hand total t is the average over the ten next cards, which we memoise.

## 4. Brute force vs optimal (0:33) — `slides/04.png`

Plain recursion explores the same hand totals repeatedly. Memoising by hand value makes it linear in the target, times ten cards.

## 5. Approach (0:42) — `slides/05.png`

Step by step. First, if the total exceeds the target, it's a bust. Second, if it reaches target minus four, stop. Third, otherwise average the ten draws. Fourth, memoise by total.

## 6. Worked example (0:58) — `slides/06.png`

With a hand of 16, average over the ten possible cards. Hands of seventeen to twenty-one stand, and anything over twenty-one busts. That gives 0.500.

## 7. Worked example (1:10) — `slides/07.png`

With a hand of 15, average over the ten possible cards. Hands of seventeen to twenty-one stand, and anything over twenty-one busts. That gives 0.450.

## 8. Java solution (1:23) — `slides/08.png`

Bust returns one above the target, zero when the dealer would stand, otherwise the memoised average of bust over the ten next cards. The answer is rounded to three decimals.

## 9. Complexity (1:34) — `slides/09.png`

Time is O of t. Space is O of t.

## 10. Edge cases & pitfalls (1:37) — `slides/10.png`

The dealer stands at target minus four or more. Round only the final answer, not intermediate values.

## 11. Interview tips & follow-ups (1:45) — `slides/11.png`

The state is only the hand total because cards are drawn with replacement. A real deck adds card counts to the state.

## 12. Recap (1:53) — `slides/12.png`

To recap Blackjack Probability: The chance of busting from hand total t is the average over the ten next cards, which we memoise. Try re-implementing it from scratch without looking.
