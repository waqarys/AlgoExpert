package graphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class RottingOrangesTest {
    RottingOranges s = new RottingOranges();
    @Test void examples() {
        assertEquals(4, s.orangesRotting(new int[][]{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}));
        assertEquals(-1, s.orangesRotting(new int[][]{{2, 1, 1}, {0, 1, 1}, {1, 0, 1}}));
        assertEquals(0, s.orangesRotting(new int[][]{{0, 2}}));
        assertEquals(0, s.orangesRotting(new int[][]{{0}}));
    }
}
