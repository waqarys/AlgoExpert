# AlgoExpert · Remove Islands

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Remove Islands (0:00) — `slides/01.png`

Let's solve Remove Islands, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Set to 0 every group of 1s not connected (4-directionally) to the matrix border. Flood-fill from border 1s marking them, then clear the rest.

## 3. Intuition (0:23) — `slides/03.png`

Ones connected to the border survive; everything else is an island to remove.

## 4. Brute force vs optimal (0:28) — `slides/04.png`

Checking each interior one separately for a path to the border repeats work. Flipping the question, flood-filling from the border to mark safe cells, solves it in one linear pass.

## 5. Approach (0:39) — `slides/05.png`

Step by step. First, flood-fill from every border one, marking them safe. Second, turn the remaining ones into zeros. Third, restore the safe marks.

## 6. Worked example (0:52) — `slides/06.png`

Any one on the border, and anything connected to it, isn't an island. Start a flood fill from every border one.

## 7. Worked example (1:00) — `slides/07.png`

After the flood fill, the green ones are connected to the border. The red ones are islands.

## 8. Worked example (1:07) — `slides/08.png`

Turn the islands into zeros. Everything connected to the border stays.

## 9. Java solution (1:13) — `slides/09.png`

We push every border one onto a stack and mark it two. Popping cells, we mark and push neighbouring ones. Finally, cells marked two become one and everything else becomes zero.

## 10. Complexity (1:25) — `slides/10.png`

Time is O of w times h. Space is O of w times h.

## 11. Edge cases & pitfalls (1:30) — `slides/11.png`

Only four directions count. Use an explicit stack to avoid recursion depth problems, and convert the temporary marks back at the end.

## 12. Interview tips & follow-ups (1:39) — `slides/12.png`

This is the surrounded regions pattern; counting islands is the River Sizes problem.

## 13. Recap (1:45) — `slides/13.png`

To recap Remove Islands: Ones connected to the border survive; everything else is an island to remove. Try re-implementing it from scratch without looking.
