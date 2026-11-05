package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TargetSumTest {
    TargetSum s = new TargetSum();
    @Test void examples() {
        assertEquals(5, s.findTargetSumWays(new int[]{1, 1, 1, 1, 1}, 3));
        assertEquals(1, s.findTargetSumWays(new int[]{1}, 1));
        assertEquals(2, s.findTargetSumWays(new int[]{0, 1}, 1));
        assertEquals(0, s.findTargetSumWays(new int[]{1, 2}, 4));
        assertEquals(1, s.findTargetSumWays(new int[]{1, 2}, -3));
    }
}
