package advancedgraphs;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinCostToConnectAllPointsTest {
    MinCostToConnectAllPoints s = new MinCostToConnectAllPoints();
    @Test void examples() {
        assertEquals(20, s.minCostConnectPoints(new int[][]{{0, 0}, {2, 2}, {3, 10}, {5, 2}, {7, 0}}));
        assertEquals(18, s.minCostConnectPoints(new int[][]{{3, 12}, {-2, 5}, {-4, 1}}));
        assertEquals(0, s.minCostConnectPoints(new int[][]{{0, 0}}));
    }
}
