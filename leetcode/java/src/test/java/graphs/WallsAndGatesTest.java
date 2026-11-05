package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class WallsAndGatesTest {
    static final int I = Integer.MAX_VALUE;
    @Test void example() {
        int[][] g = {{I, -1, 0, I}, {I, I, I, -1}, {I, -1, I, -1}, {0, -1, I, I}};
        new WallsAndGates().wallsAndGates(g);
        assertArrayEquals(new int[][]{{3, -1, 0, 1}, {2, 2, 1, -1}, {1, -1, 2, -1}, {0, -1, 3, 4}}, g);
        int[][] g2 = {{I, -1}, {-1, 0}};
        new WallsAndGates().wallsAndGates(g2);
        assertArrayEquals(new int[][]{{I, -1}, {-1, 0}}, g2);
    }
}
