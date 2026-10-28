# AlgoExpert · Min Max Stack Construction

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Min Max Stack Construction (0:00) — `slides/01.png`

Let's solve Min Max Stack Construction, a medium stacks problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:12) — `slides/02.png`

Here's the problem. A stack with constant push, pop, peek, getMin and getMax by storing the running min or max alongside each element.

## 3. Intuition (0:21) — `slides/03.png`

Store the current min and max alongside each pushed value so they're always available.

## 4. Approach (0:26) — `slides/04.png`

Step by step. First, push value with updated min and max. Second, pop removes both. Third, peek, getMin and getMax read the top.

## 5. Java solution (0:39) — `slides/05.png`

Here's the Java solution, starting with peek. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is constant per op. Space is O of n.

## 7. Recap (0:49) — `slides/07.png`

To recap Min Max Stack Construction: Store the current min and max alongside each pushed value so they're always available. Try re-implementing it from scratch without looking.
