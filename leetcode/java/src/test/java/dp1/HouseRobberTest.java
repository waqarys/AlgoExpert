package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HouseRobberTest {
    HouseRobber s = new HouseRobber();
    @Test void examples() {
        assertEquals(4, s.rob(new int[]{1, 2, 3, 1}));
        assertEquals(12, s.rob(new int[]{2, 7, 9, 3, 1}));
        assertEquals(4, s.rob(new int[]{2, 1, 1, 2}));
        assertEquals(0, s.rob(new int[]{}));
    }
}
