# 0200. Number of Islands

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/number-of-islands/

## Problem
- In a grid of '1' (land) and '0' (water), count the islands (groups of land connected up/down/left/right).

## Intuition
- Each unvisited land cell starts a new island. Flood-fill (DFS/BFS) from it to mark the whole island as visited.

## Brute Force
- Union-Find over land cells also works in near-linear time; flood fill is simpler.

## Optimal Approach
1. For every cell: if '1', count++ and sink(r, c).
2. sink: if out of bounds or not '1' return; set '0'; recurse 4 directions.

## Worked Example
```text
11000
11000      island 1: top-left 2x2 block
00100      island 2: the single centre cell
00011      island 3: bottom-right pair
answer 3
```

## Complexity
- Time: O(m * n). Space: O(m * n) recursion in the worst case.

## Pitfalls
- This version mutates the input; copy the grid if the caller needs it.
- Diagonal cells are not connected.

## Video Script
- The gateway graph problem: a grid is an implicit graph.

## Solution
```java file=graphs/NumberOfIslands.java
package graphs;

/**
 * LC 200 Number of Islands.
 * Approach: scan cells; each unvisited land starts a DFS flood fill that sinks the island.
 * Time O(mn), Space O(mn) recursion worst case.
 */
public class NumberOfIslands {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int r = 0; r < grid.length; r++)
            for (int c = 0; c < grid[0].length; c++)
                if (grid[r][c] == '1') { count++; sink(grid, r, c); }
        return count;
    }

    private void sink(char[][] g, int r, int c) {
        if (r < 0 || c < 0 || r >= g.length || c >= g[0].length || g[r][c] != '1') return;
        g[r][c] = '0';
        sink(g, r + 1, c); sink(g, r - 1, c); sink(g, r, c + 1); sink(g, r, c - 1);
    }
}
```

## Tests
```java test=graphs/NumberOfIslandsTest.java
package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NumberOfIslandsTest {
    static char[][] g(String... rows) {
        char[][] b = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) b[i] = rows[i].toCharArray();
        return b;
    }
    NumberOfIslands s = new NumberOfIslands();
    @Test void examples() {
        assertEquals(1, s.numIslands(g("11110", "11010", "11000", "00000")));
        assertEquals(3, s.numIslands(g("11000", "11000", "00100", "00011")));
        assertEquals(0, s.numIslands(g("0")));
        assertEquals(2, s.numIslands(g("10", "01")));
    }
}
```
