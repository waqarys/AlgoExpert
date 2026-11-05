package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinCostClimbingStairsTest {
    MinCostClimbingStairs s = new MinCostClimbingStairs();
    @Test void examples() {
        assertEquals(15, s.minCostClimbingStairs(new int[]{10, 15, 20}));
        assertEquals(6, s.minCostClimbingStairs(new int[]{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}));
        assertEquals(0, s.minCostClimbingStairs(new int[]{5, 0}));
    }
}
