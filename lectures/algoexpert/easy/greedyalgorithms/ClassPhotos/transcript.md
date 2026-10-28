# AlgoExpert · Class Photos

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Class Photos (0:00) — `slides/01.png`

Let's solve Class Photos, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Equal numbers of red and blue shirted students; all of one colour in the back row, each back-row student strictly taller than the person in front. Is a photo possible?

## 3. Intuition (0:24) — `slides/03.png`

Sort both groups. The taller group must stand in the back, and then every back student must be taller than the one in front.

## 4. Approach (0:32) — `slides/04.png`

Step by step. First, sort red and blue shirts. Second, the group with the taller tallest goes in the back. Third, check every pair strictly. Fourth, any failure means false.

## 5. Java solution (0:46) — `slides/05.png`

Here's the Java solution, starting with class photos. It follows the steps we just described.

## 6. Complexity (0:53) — `slides/06.png`

Time is O of n log n. Space is constant.

## 7. Recap (0:58) — `slides/07.png`

To recap Class Photos: Sort both groups. The taller group must stand in the back, and then every back student must be taller than the one in front. Try re-implementing it from scratch without looking.
