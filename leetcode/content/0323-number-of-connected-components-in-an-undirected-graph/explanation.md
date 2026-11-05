# 0323. Number of Connected Components in an Undirected Graph

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

## Problem
- n nodes and a list of undirected edges. Return the number of connected components.

## Intuition
- Start with n components; every successful union of two different components reduces the count by one.

## Brute Force
- DFS/BFS from each unvisited node, counting starts: O(V + E), also fine.

## Optimal Approach
1. components = n.
2. For each edge, if union(u, v) merges two roots, components--.

## Worked Example
- n = 5, edges [[0,1],[1,2],[3,4]].
```text
start 5
[0,1] merge -> 4
[1,2] merge -> 3
[3,4] merge -> 2
answer 2
```

## Complexity
- Time: O(E * alpha(n)). Space: O(n).

## Pitfalls
- Duplicate or already-connected edges must not decrement the count.

## Video Script
- Show both DFS and Union-Find and when each is preferable (static vs incremental edges).

## Solution
```java file=graphs/NumberOfConnectedComponents.java
package graphs;

/**
 * LC 323 Number of Connected Components in an Undirected Graph.
 * Approach: Union-Find; each successful union reduces the component count.
 * Time O(E * alpha(n)), Space O(n).
 */
public class NumberOfConnectedComponents {
    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int comps = n;
        for (int[] e : edges) {
            int a = find(parent, e[0]), b = find(parent, e[1]);
            if (a != b) { parent[a] = b; comps--; }
        }
        return comps;
    }

    private int find(int[] p, int x) {
        while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
        return x;
    }
}
```

## Tests
```java test=graphs/NumberOfConnectedComponentsTest.java
package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NumberOfConnectedComponentsTest {
    NumberOfConnectedComponents s = new NumberOfConnectedComponents();
    @Test void examples() {
        assertEquals(2, s.countComponents(5, new int[][]{{0, 1}, {1, 2}, {3, 4}}));
        assertEquals(1, s.countComponents(5, new int[][]{{0, 1}, {1, 2}, {2, 3}, {3, 4}}));
        assertEquals(3, s.countComponents(3, new int[][]{}));
        assertEquals(1, s.countComponents(3, new int[][]{{0, 1}, {1, 2}, {2, 0}}));
    }
}
```
