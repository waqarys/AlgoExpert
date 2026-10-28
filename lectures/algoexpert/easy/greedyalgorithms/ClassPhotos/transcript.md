# AlgoExpert · Class Photos

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Class Photos (0:00) — `slides/01.png`

Let's solve Class Photos, an easy greedy algorithms problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Equal numbers of red and blue shirted students; all of one colour in the back row, each back-row student strictly taller than the person in front. Is a photo possible?

## 3. Intuition (0:24) — `slides/03.png`

Sort both groups. The taller group must stand in the back, and then every back student must be taller than the one in front.

## 4. Brute force vs optimal (0:32) — `slides/04.png`

Trying every arrangement would be factorial. If any arrangement works, pairing the sorted groups position by position works too, so we sort and compare, in n log n.

## 5. Approach (0:43) — `slides/05.png`

Step by step. First, sort red and blue shirts. Second, the group with the taller tallest goes in the back. Third, check every pair strictly. Fourth, any failure means false.

## 6. Worked example (0:57) — `slides/06.png`

Sort both groups by height. The tallest blue student, nine, beats the tallest red, eight, so blue must be the back row.

## 7. Worked example (1:06) — `slides/07.png`

Position 0: back 9 versus front 8. The back student is strictly taller, so this pair works.

## 8. Worked example (1:14) — `slides/08.png`

Position 2: back 5 versus front 4. The back student is strictly taller, so this pair works.

## 9. Worked example (1:22) — `slides/09.png`

Position 4: back 2 versus front 1. The back student is strictly taller, so this pair works.

## 10. Java solution (1:29) — `slides/10.png`

We sort both lists in descending order, choose the back row by comparing the first elements, then check every position strictly. Any failure returns false.

## 11. Complexity (1:40) — `slides/11.png`

Time is O of n log n. Space is constant.

## 12. Edge cases & pitfalls (1:44) — `slides/12.png`

Heights must be strictly greater, so equal heights fail. Decide which colour goes in the back from the tallest students, then never switch.

## 13. Interview tips & follow-ups (1:53) — `slides/13.png`

Justify the greedy with an exchange argument: swapping any pair out of sorted order can't help.

## 14. Recap (1:59) — `slides/14.png`

To recap Class Photos: Sort both groups. The taller group must stand in the back, and then every back student must be taller than the one in front. Try re-implementing it from scratch without looking.
