# AlgoExpert · Single Cycle Check

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Single Cycle Check (0:00) — `slides/01.png`

Let's solve Single Cycle Check, a medium graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Each element is a jump (wrapping). Do the jumps form one cycle visiting every index exactly once and returning to the start?

## 3. Intuition (0:22) — `slides/03.png`

Follow the jumps n times: we must visit every index exactly once and return to the start.

## 4. Approach (0:28) — `slides/04.png`

Step by step. First, jump n times with wrap-around. Second, if we return to zero early, fail. Third, after n jumps we must be at zero.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with has single cycle. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:51) — `slides/07.png`

To recap Single Cycle Check: Follow the jumps n times: we must visit every index exactly once and return to the start. Try re-implementing it from scratch without looking.
