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
