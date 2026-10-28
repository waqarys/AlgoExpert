# AlgoExpert · Array Of Products

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Array Of Products (0:00) — `slides/01.png`

Let's solve Array Of Products, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Out i equals product of every element except a i , without division. Prefix products then suffix products.

## 3. Intuition (0:21) — `slides/03.png`

Each output is the product of everything to the left times everything to the right, so two sweeps replace division.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

The brute force recomputes a product of n minus one numbers for every index, which is quadratic. Dividing the total product by each element is linear, but it breaks on zeros and the problem forbids it. Prefix and suffix products give linear time without division.

## 5. Approach (0:44) — `slides/05.png`

Step by step. First, fill each slot with the running product from the left. Second, sweep from the right with a second running product. Third, multiply it in. Fourth, no division needed.

## 6. Worked example (0:58) — `slides/06.png`

Left pass, index 0: everything to the left multiplies to 1, so out 0 becomes 1.

## 7. Worked example (1:05) — `slides/07.png`

Left pass, index 1: everything to the left multiplies to 5, so out 1 becomes 5.

## 8. Worked example (1:11) — `slides/08.png`

Left pass, index 2: everything to the left multiplies to 5, so out 2 becomes 5.

## 9. Worked example (1:18) — `slides/09.png`

Left pass, index 3: everything to the left multiplies to 20, so out 3 becomes 20.

## 10. Worked example (1:24) — `slides/10.png`

Right pass, index 3: everything to the right multiplies to 1, so out 3 becomes 20.

## 11. Worked example (1:31) — `slides/11.png`

Right pass, index 0: everything to the right multiplies to 8, so out 0 becomes 8.

## 12. Java solution (1:37) — `slides/12.png`

The first loop writes the running product of everything to the left into each slot, then multiplies the running value by a i. The second loop goes right to left with a fresh running product and multiplies it into each slot.

## 13. Complexity (1:49) — `slides/13.png`

Time is O of n. Space is O of n output.

## 14. Edge cases & pitfalls (1:53) — `slides/14.png`

Zeros are the classic trap: with one zero, only that position gets a non-zero product; with two, everything is zero. The prefix-suffix method handles both automatically. Watch for overflow with big inputs.

## 15. Interview tips & follow-ups (2:08) — `slides/15.png`

Bring up the division idea and explain why it fails. Our version already uses the output array for the prefix pass, so extra space is constant beyond the output.

## 16. Recap (2:18) — `slides/16.png`

To recap Array Of Products: Each output is the product of everything to the left times everything to the right, so two sweeps replace division. Try re-implementing it from scratch without looking.
