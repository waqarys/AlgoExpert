# AlgoExpert · Group Anagrams

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Group Anagrams (0:00) — `slides/01.png`

Let's solve Group Anagrams, a medium strings problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Group words that are anagrams of each other (key equals sorted letters).

## 3. Intuition (0:18) — `slides/03.png`

Anagrams share the same sorted letters, which makes a perfect hash key.

## 4. Brute force vs optimal (0:23) — `slides/04.png`

Comparing every pair of words is quadratic. Using the sorted letters as a hash key groups anagrams in one pass. A 26-letter count key avoids the sort.

## 5. Approach (0:35) — `slides/05.png`

Step by step. First, sort each word's letters. Second, group words by that key. Third, return the groups.

## 6. Worked example (0:45) — `slides/06.png`

Sort the letters of yo to get the key oy, and add it to that group.

## 7. Worked example (0:50) — `slides/07.png`

Sort the letters of tac to get the key act, and add it to that group.

## 8. Worked example (0:55) — `slides/08.png`

Sort the letters of cat to get the key act, and add it to that group.

## 9. Worked example (1:00) — `slides/09.png`

Sort the letters of oy to get the key oy, and add it to that group.

## 10. Worked example (1:04) — `slides/10.png`

Sort the letters of olfp to get the key flop, and add it to that group.

## 11. Java solution (1:09) — `slides/11.png`

For each word we sort its characters to form a key, and add the word to that key's list in a linked hash map, then return the lists.

## 12. Complexity (1:17) — `slides/12.png`

Time is O of w times n log n. Space is O of w times n.

## 13. Edge cases & pitfalls (1:22) — `slides/13.png`

Handle the empty list, and decide on case sensitivity.

## 14. Interview tips & follow-ups (1:27) — `slides/14.png`

Mention the count-array key as a further optimisation.

## 15. Recap (1:31) — `slides/15.png`

To recap Group Anagrams: Anagrams share the same sorted letters, which makes a perfect hash key. Try re-implementing it from scratch without looking.
