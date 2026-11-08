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
