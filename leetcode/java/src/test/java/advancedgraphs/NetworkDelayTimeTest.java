package advancedgraphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class NetworkDelayTimeTest {
    NetworkDelayTime s = new NetworkDelayTime();
    @Test void examples() {
        assertEquals(2, s.networkDelayTime(new int[][]{{2, 1, 1}, {2, 3, 1}, {3, 4, 1}}, 4, 2));
        assertEquals(1, s.networkDelayTime(new int[][]{{1, 2, 1}}, 2, 1));
        assertEquals(-1, s.networkDelayTime(new int[][]{{1, 2, 1}}, 2, 2));
        assertEquals(3, s.networkDelayTime(new int[][]{{1, 2, 5}, {1, 3, 1}, {3, 2, 2}}, 3, 1));
    }
}
