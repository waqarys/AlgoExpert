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
