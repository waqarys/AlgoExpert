package advancedgraphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CheapestFlightsWithinKStopsTest {
    CheapestFlightsWithinKStops s = new CheapestFlightsWithinKStops();
    @Test void examples() {
        int[][] f = {{0, 1, 100}, {1, 2, 100}, {2, 0, 100}, {1, 3, 600}, {2, 3, 200}};
        assertEquals(700, s.findCheapestPrice(4, f, 0, 3, 1));
        int[][] g = {{0, 1, 100}, {1, 2, 100}, {0, 2, 500}};
        assertEquals(200, s.findCheapestPrice(3, g, 0, 2, 1));
        assertEquals(500, s.findCheapestPrice(3, g, 0, 2, 0));
        assertEquals(-1, s.findCheapestPrice(3, new int[][]{{0, 1, 1}}, 0, 2, 5));
    }
}
