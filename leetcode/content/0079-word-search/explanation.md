# 0079. Word Search

**Difficulty:** Medium | **Category:** Backtracking | **LeetCode:** https://leetcode.com/problems/word-search/

## Problem
- Does word exist in the grid as a path of horizontally/vertically adjacent cells, each used at most once?

## Intuition
- Try every cell as a start; DFS matching one character at a time.
- Temporarily mark the cell as visited (overwrite with '#') and restore it when backtracking.

## Brute Force
- The backtracking search is the brute force; the optimisation is pruning (stop at the first mismatch, optional character-count precheck).

## Optimal Approach
1. For each (r, c): if dfs(r, c, 0) return true.
2. dfs: if i == len return true; out of bounds or board[r][c] != word[i] return false.
3. Mark, recurse in 4 directions, restore.

## Worked Example
- board ABCE / SFCS / ADEE, word "ABCCED".
```text
(0,0)A -> (0,1)B -> (0,2)C -> (1,2)C -> (2,2)E -> (2,1)D  -> found
```

## Complexity
- Time: O(m * n * 3^L). Space: O(L) recursion.

## Pitfalls
- Forgetting to restore the cell breaks later searches.

## Video Script
- Grid backtracking template; preview of Word Search II (trie version).

## Solution
```java file=backtracking/WordSearch.java
package backtracking;

/**
 * LC 79 Word Search.
 * Approach: DFS from every cell with in-place visited marking and restore.
 * Time O(mn * 3^L), Space O(L).
 */
public class WordSearch {
    public boolean exist(char[][] board, String word) {
        for (int r = 0; r < board.length; r++)
            for (int c = 0; c < board[0].length; c++)
                if (dfs(board, word, r, c, 0)) return true;
        return false;
    }

    private boolean dfs(char[][] b, String w, int r, int c, int i) {
        if (i == w.length()) return true;
        if (r < 0 || c < 0 || r >= b.length || c >= b[0].length || b[r][c] != w.charAt(i)) return false;
        char saved = b[r][c];
        b[r][c] = '#';
        boolean found = dfs(b, w, r + 1, c, i + 1) || dfs(b, w, r - 1, c, i + 1)
                || dfs(b, w, r, c + 1, i + 1) || dfs(b, w, r, c - 1, i + 1);
        b[r][c] = saved;
        return found;
    }
}
```

## Tests
```java test=backtracking/WordSearchTest.java
package backtracking;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WordSearchTest {
    static char[][] g() { return new char[][]{"ABCE".toCharArray(), "SFCS".toCharArray(), "ADEE".toCharArray()}; }
    WordSearch s = new WordSearch();
    @Test void examples() {
        assertTrue(s.exist(g(), "ABCCED"));
        assertTrue(s.exist(g(), "SEE"));
        assertFalse(s.exist(g(), "ABCB"));
        assertTrue(s.exist(new char[][]{{'a'}}, "a"));
    }
}
```
