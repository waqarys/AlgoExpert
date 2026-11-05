# 0133. Clone Graph

**Difficulty:** Medium | **Category:** Graphs | **LeetCode:** https://leetcode.com/problems/clone-graph/

## Problem
- Deep-copy a connected undirected graph given one node (each node has val and a neighbors list).

## Intuition
- DFS through the graph, keeping a map original -> clone.
- The map doubles as the visited set and handles cycles: if a node is already cloned, reuse the clone.

## Brute Force
- No meaningfully slower approach; BFS with the same map is an equal alternative.

## Optimal Approach
1. clone(node): if null return null; if in map return map.get(node).
2. copy = new Node(val); map.put(node, copy) before visiting neighbours (breaks cycles).
3. For each neighbour: copy.neighbors.add(clone(nb)).

## Worked Example
- adjacency [[2,4],[1,3],[2,4],[1,3]] (a square).
```text
clone 1 -> clone 2 -> clone 3 -> clone 4 -> neighbour 1 already in map (reuse)
back in 3: neighbour 4 done ; back in 2: neighbour 3 done
... all 4 nodes copied, edges point to copies
```

## Complexity
- Time: O(V + E). Space: O(V).

## Pitfalls
- Insert into the map before recursing, or a cycle recurses forever.

## Video Script
- Same "old -> new map" idea as Copy List with Random Pointer.

## Solution
```java file=graphs/CloneGraph.java
package graphs;

import java.util.*;

/**
 * LC 133 Clone Graph.
 * Approach: DFS with an original -> clone map that also acts as the visited set.
 * Time O(V+E), Space O(V).
 */
public class CloneGraph {
    public static class Node {
        public int val;
        public List<Node> neighbors = new ArrayList<>();
        public Node(int val) { this.val = val; }
    }

    private final Map<Node, Node> map = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        Node existing = map.get(node);
        if (existing != null) return existing;
        Node copy = new Node(node.val);
        map.put(node, copy);
        for (Node nb : node.neighbors) copy.neighbors.add(cloneGraph(nb));
        return copy;
    }
}
```

## Tests
```java test=graphs/CloneGraphTest.java
package graphs;

import graphs.CloneGraph.Node;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class CloneGraphTest {
    static Node[] build(int[][] adj) {
        Node[] ns = new Node[adj.length];
        for (int i = 0; i < adj.length; i++) ns[i] = new Node(i + 1);
        for (int i = 0; i < adj.length; i++) for (int j : adj[i]) ns[i].neighbors.add(ns[j - 1]);
        return ns;
    }
    @Test void square() {
        Node[] ns = build(new int[][]{{2, 4}, {1, 3}, {2, 4}, {1, 3}});
        Node c = new CloneGraph().cloneGraph(ns[0]);
        assertNotSame(ns[0], c);
        assertEquals(1, c.val);
        assertEquals(List.of(2, 4), c.neighbors.stream().map(n -> n.val).toList());
        Node c3 = c.neighbors.get(0).neighbors.get(1);
        assertEquals(3, c3.val);
        assertNotSame(ns[2], c3);
        assertSame(c, c.neighbors.get(1).neighbors.get(0));
    }
    @Test void empty() { assertNull(new CloneGraph().cloneGraph(null)); }
}
```
