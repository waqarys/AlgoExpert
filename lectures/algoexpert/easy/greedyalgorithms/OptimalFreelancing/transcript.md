# AlgoExpert · Optimal Freelancing

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Optimal Freelancing (0:00) — `slides/01.png`

Let's solve Optimal Freelancing, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. Each job takes one day and has a deadline (days left) and a payment. Working at most 7 days, one job per day, maximise profit. Greedy: take jobs by payment descending and place each in the latest free day on or before its deadline.

## 3. Intuition (0:29) — `slides/03.png`

Greedy by payment: take the most valuable jobs first and schedule each as late as its deadline allows.

## 4. Approach (0:35) — `slides/04.png`

Step by step. First, sort jobs by payment, highest first. Second, keep seven day slots. Third, place each job in the latest free day before its deadline. Fourth, sum the payments of placed jobs.

## 5. Java solution (0:51) — `slides/05.png`

Here's the Java solution, starting with optimal freelancing. It follows the steps we just described.

## 6. Complexity (0:58) — `slides/06.png`

Time is O of n log n. Space is constant (7 slots).

## 7. Recap (1:03) — `slides/07.png`

To recap Optimal Freelancing: Greedy by payment: take the most valuable jobs first and schedule each as late as its deadline allows. Try re-implementing it from scratch without looking.
