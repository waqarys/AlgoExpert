# AlgoExpert · Multi String Search

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Multi String Search (0:00) — `slides/01.png`

Let's solve Multi String Search, a hard tries problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. For each small string, does it occur in the big string? Trie of small strings, scanned from every start position of the big string.

## 3. Intuition (0:21) — `slides/03.png`

Put the small strings in a trie, then walk it from each position of the big string.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, build a trie. Second, start a walk at each index of the big string. Third, mark words found. Fourth, return booleans.

## 5. Java solution (0:40) — `slides/05.png`

Here's the Java solution, starting with multi string search. It follows the steps we just described.

## 6. Complexity (0:47) — `slides/06.png`

Time is O of ns plus bs where b is the big length, s the longest small. Space is O of ns.

## 7. Recap (0:55) — `slides/07.png`

To recap Multi String Search: Put the small strings in a trie, then walk it from each position of the big string. Try re-implementing it from scratch without looking.
