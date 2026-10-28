# AlgoExpert · Group Anagrams

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Group Anagrams (0:00) — `slides/01.png`

Let's solve Group Anagrams, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Group words that are anagrams of each other (key equals sorted letters).

## 3. Intuition (0:18) — `slides/03.png`

Anagrams share the same sorted letters, which makes a perfect hash key.

## 4. Approach (0:23) — `slides/04.png`

Step by step. First, sort each word's letters. Second, group words by that key. Third, return the groups.

## 5. Java solution (0:33) — `slides/05.png`

Here's the Java solution, starting with group anagrams. It follows the steps we just described.

## 6. Complexity (0:41) — `slides/06.png`

Time is O of w times n log n. Space is O of w times n.

## 7. Recap (0:46) — `slides/07.png`

To recap Group Anagrams: Anagrams share the same sorted letters, which makes a perfect hash key. Try re-implementing it from scratch without looking.
