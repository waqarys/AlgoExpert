# AlgoExpert · Optimal Freelancing

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Optimal Freelancing (0:00) — `slides/01.png`

Let's solve Optimal Freelancing, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Each job takes one day and has a deadline (days left) and a payment. Working at most 7 days, one job per day, maximise profit. Greedy: take jobs by payment descending and place each in the latest free day on or before its deadline.

## 3. Intuition (0:29) — `slides/03.png`

Greedy by payment: take the most valuable jobs first and schedule each as late as its deadline allows.

## 4. Brute force vs optimal (0:35) — `slides/04.png`

Brute force would try every subset and ordering. Instead, take jobs from highest pay to lowest and place each on the latest free day before its deadline. Placing late keeps early days open for jobs with tight deadlines.

## 5. Approach (0:48) — `slides/05.png`

Step by step. First, sort jobs by payment, highest first. Second, keep seven day slots. Third, place each job in the latest free day before its deadline. Fourth, sum the payments of placed jobs.

## 6. Worked example (1:04) — `slides/06.png`

Job C pays 2 with deadline 3. The latest free day on or before the deadline is day 3, so we book it. Earnings so far: 2.

## 7. Worked example (1:14) — `slides/07.png`

Job D pays 2 with deadline 2. The latest free day on or before the deadline is day 2, so we book it. Earnings so far: 4.

## 8. Worked example (1:24) — `slides/08.png`

Job A pays 1 with deadline 1. The latest free day on or before the deadline is day 1, so we book it. Earnings so far: 5.

## 9. Worked example (1:34) — `slides/09.png`

Job B pays 1 with deadline 2. Every day up to its deadline is taken, so we skip it. Earnings so far: 5.

## 10. Java solution (1:44) — `slides/10.png`

We sort jobs by payment descending and keep a seven-slot boolean array. For each job, we scan backwards from its capped deadline for a free day, mark it, and add the payment.

## 11. Complexity (1:55) — `slides/11.png`

Time is O of n log n. Space is constant (7 slots).

## 12. Edge cases & pitfalls (1:59) — `slides/12.png`

Cap deadlines at seven since the week only has seven days. With no jobs, the answer is zero.

## 13. Interview tips & follow-ups (2:07) — `slides/13.png`

Explain why scheduling late matters. With many days instead of seven, a union-find of free slots makes the search fast.

## 14. Recap (2:15) — `slides/14.png`

To recap Optimal Freelancing: Greedy by payment: take the most valuable jobs first and schedule each as late as its deadline allows. Try re-implementing it from scratch without looking.
