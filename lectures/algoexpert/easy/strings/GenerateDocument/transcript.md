# AlgoExpert · Generate Document

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Generate Document (0:00) — `slides/01.png`

Let's solve Generate Document, an easy strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Can document be built from the multiset of characters in characters?

## 3. Intuition (0:18) — `slides/03.png`

We can build the document if, for every character, we have at least as many copies available as needed.

## 4. Approach (0:25) — `slides/04.png`

Step by step. First, count available characters. Second, for each document character, decrement its count. Third, if any count goes negative, return false.

## 5. Java solution (0:38) — `slides/05.png`

Here's the Java solution, starting with generate document. It follows the steps we just described.

## 6. Complexity (0:45) — `slides/06.png`

Time is O of n plus m. Space is O of c.

## 7. Recap (0:49) — `slides/07.png`

To recap Generate Document: We can build the document if, for every character, we have at least as many copies available as needed. Try re-implementing it from scratch without looking.
