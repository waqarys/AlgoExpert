# AlgoExpert · Boggle Board

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Boggle Board (0:00) — `slides/01.png`

Let's solve Boggle Board, a hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Which words can be formed by chaining 8-directionally adjacent letters without reusing a cell? Trie of words plus DFS from every cell.

## 3. Intuition (0:22) — `slides/03.png`

A trie of the words lets the board DFS prune paths that can't spell any word.

## 4. Brute force vs optimal (0:27) — `slides/04.png`

Searching for each word separately repeats work for shared prefixes. A trie of all words lets one DFS from each cell explore them together and prune early.

## 5. Approach (0:37) — `slides/05.png`

Step by step. First, insert words into a trie. Second, dFS from every cell along trie edges. Third, mark visited cells. Fourth, record words at word-end markers.

## 6. Worked example (0:52) — `slides/06.png`

Put every word in a trie, then search the board from each cell.

## 7. Worked example (0:57) — `slides/07.png`

From the t in the corner, the trie has a branch for t, so continue.

## 8. Worked example (1:02) — `slides/08.png`

Moving to neighbours h, i, s, we reach a trie node marking the word this.

## 9. Worked example (1:08) — `slides/09.png`

Any time the trie has no branch for the next letter, we stop exploring that path. That pruning is what makes it fast.

## 10. Java solution (1/2) (1:16) — `slides/10.png`

We build a trie with words at terminal nodes. DFS from every cell follows the trie child for the cell's letter, records any word, marks the cell, recurses in eight directions, then unmarks it.

## 11. Java solution (2/2) (1:28) — `slides/11.png`

We build a trie with words at terminal nodes. DFS from every cell follows the trie child for the cell's letter, records any word, marks the cell, recurses in eight directions, then unmarks it.

## 12. Complexity (1:40) — `slides/12.png`

Time is O of ws plus w times h times 8 to the s. Space is O of ws plus w times h.

## 13. Edge cases & pitfalls (1:48) — `slides/13.png`

Moves include diagonals, a cell can't be reused in one word, and the same word may be found twice.

## 14. Interview tips & follow-ups (1:54) — `slides/14.png`

Explain the pruning. Removing found words from the trie speeds things up further.

## 15. Recap (2:00) — `slides/15.png`

To recap Boggle Board: A trie of the words lets the board DFS prune paths that can't spell any word. Try re-implementing it from scratch without looking.
