# AlgoExpert · Remove Islands

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Remove Islands (0:00) — `slides/01.png`

Let's solve Remove Islands, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Set to 0 every group of 1s not connected (4-directionally) to the matrix border. Flood-fill from border 1s marking them, then clear the rest.

## 3. Intuition (0:23) — `slides/03.png`

Ones connected to the border survive; everything else is an island to remove.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, flood-fill from every border one, marking them safe. Second, turn the remaining ones into zeros. Third, restore the safe marks.

## 5. Java solution (0:41) — `slides/05.png`

Here's the Java solution, starting with remove islands. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of w times h. Space is O of w times h.

## 7. Recap (0:53) — `slides/07.png`

To recap Remove Islands: Ones connected to the border survive; everything else is an island to remove. Try re-implementing it from scratch without looking.
