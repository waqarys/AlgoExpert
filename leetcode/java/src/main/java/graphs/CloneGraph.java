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
