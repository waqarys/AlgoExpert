# 0261. Graph Valid Tree

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/graph-valid-tree/

## Problem
- n nodes and undirected edges: do they form a valid tree (connected and acyclic)?

## Intuition
- A tree with n nodes has exactly n - 1 edges. With that edge count, "no cycle" is equivalent to "connected".
- So: check edges == n - 1, then Union-Find to make sure no edge closes a cycle.

## Brute Force
- DFS checking for cycles (track parent) and then visited count == n.

## Optimal Approach
1. If edges.length != n - 1 return false.
2. Union every edge; if any union finds both ends already connected, return false.
3. Return true.

## Worked Example
- n = 5, edges [[0,1],[1,2],[2,3],[1,3],[1,4]].
```text
edges = 5 != n - 1 = 4 -> false (cycle 1-2-3)
```

## Complexity
- Time: O(n * alpha(n)). Space: O(n).

## Pitfalls
- n = 1 with no edges is a valid tree.

## Video Script
- Teach the n - 1 edges property as a shortcut, then prove it with the cycle check.

## Solution
```java file=graphs/GraphValidTree.java
package graphs;

/**
 * LC 261 Graph Valid Tree.
 * Approach: tree iff edges == n-1 and no edge closes a cycle (Union-Find).
 * Time O(n * alpha(n)), Space O(n).
 */
public class GraphValidTree {
    public boolean validTree(int n, int[][] edges) {
        if (edges.length != n - 1) return false;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] e : edges) {
            int a = find(parent, e[0]), b = find(parent, e[1]);
            if (a == b) return false;
            parent[a] = b;
        }
        return true;
    }

    private int find(int[] p, int x) {
        while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
        return x;
    }
}
```

## Tests
```java test=graphs/GraphValidTreeTest.java
package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class GraphValidTreeTest {
    GraphValidTree s = new GraphValidTree();
    @Test void examples() {
        assertTrue(s.validTree(5, new int[][]{{0, 1}, {0, 2}, {0, 3}, {1, 4}}));
        assertFalse(s.validTree(5, new int[][]{{0, 1}, {1, 2}, {2, 3}, {1, 3}, {1, 4}}));
        assertTrue(s.validTree(1, new int[][]{}));
        assertFalse(s.validTree(4, new int[][]{{0, 1}, {1, 2}, {2, 0}})); // right count, but cycle + isolated node
    }
}
```
