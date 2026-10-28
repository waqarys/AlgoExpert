# AlgoExpert · Boggle Board

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Boggle Board (0:00) — `slides/01.png`

Let's solve Boggle Board, a hard graphs problem. We'll restate the problem, build the intuition, walk through the approach, read the Java solution, and finish with its complexity.

## 2. The problem (0:11) — `slides/02.png`

Here's the problem. Which words can be formed by chaining 8-directionally adjacent letters without reusing a cell? Trie of words plus DFS from every cell.

## 3. Intuition (0:22) — `slides/03.png`

A trie of the words lets the board DFS prune paths that can't spell any word.

## 4. Approach (0:27) — `slides/04.png`

Step by step. First, insert words into a trie. Second, dFS from every cell along trie edges. Third, mark visited cells. Fourth, record words at word-end markers.

## 5. Java solution (1/2) (0:42) — `slides/05.png`

Here's the Java solution, starting with boggle board. It follows the steps we just described.

## 6. Java solution (2/2) (0:49) — `slides/06.png`

Continuing with dfs.

## 7. Complexity (0:52) — `slides/07.png`

Time is O of ws plus w times h times 8 to the s. Space is O of ws plus w times h.

## 8. Recap (1:00) — `slides/08.png`

To recap Boggle Board: A trie of the words lets the board DFS prune paths that can't spell any word. Try re-implementing it from scratch without looking.
