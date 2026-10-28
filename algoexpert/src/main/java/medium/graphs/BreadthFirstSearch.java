package medium.graphs;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

/**
 * Breadth-first Search: return node names of a tree-like graph level by level.
 * Time: O(v + e) | Space: O(v).
 */
public class BreadthFirstSearch {
    public static class Node {
        public final String name;
        public final List<Node> children = new ArrayList<>();
        public Node(String name) { this.name = name; }
        public Node addChild(String n) { children.add(new Node(n)); return this; }

        public List<String> breadthFirstSearch(List<String> out) {
            ArrayDeque<Node> q = new ArrayDeque<>();
            q.add(this);
            while (!q.isEmpty()) { Node c = q.poll(); out.add(c.name); q.addAll(c.children); }
            return out;
        }
    }
}
