# AlgoExpert · Majority Element

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Majority Element (0:00) — `slides/01.png`

Let's solve Majority Element, a medium arrays problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. An element occurs in more than half the array; find it (Boyer-Moore voting).

## 3. Intuition (0:18) — `slides/03.png`

Boyer-Moore voting: pair off different values; the majority survives the cancellation.

## 4. Approach (0:24) — `slides/04.png`

Step by step. First, keep a candidate and a count. Second, same value increments, different decrements. Third, when the count hits zero, adopt the current value. Fourth, the final candidate is the answer.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with majority element. It follows the steps we just described.

## 6. Complexity (0:48) — `slides/06.png`

Time is O of n. Space is constant.

## 7. Recap (0:52) — `slides/07.png`

To recap Majority Element: Boyer-Moore voting: pair off different values; the majority survives the cancellation. Try re-implementing it from scratch without looking.
