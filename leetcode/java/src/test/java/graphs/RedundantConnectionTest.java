package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class RedundantConnectionTest {
    RedundantConnection s = new RedundantConnection();
    @Test void examples() {
        assertArrayEquals(new int[]{2, 3}, s.findRedundantConnection(new int[][]{{1, 2}, {1, 3}, {2, 3}}));
        assertArrayEquals(new int[]{1, 4}, s.findRedundantConnection(new int[][]{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}}));
    }
}
