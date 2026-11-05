package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ClimbingStairsTest {
    ClimbingStairs s = new ClimbingStairs();
    @Test void examples() {
        assertEquals(1, s.climbStairs(1));
        assertEquals(2, s.climbStairs(2));
        assertEquals(3, s.climbStairs(3));
        assertEquals(8, s.climbStairs(5));
        assertEquals(1836311903, s.climbStairs(45));
    }
}
