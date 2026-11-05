package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HouseRobberIITest {
    HouseRobberII s = new HouseRobberII();
    @Test void examples() {
        assertEquals(3, s.rob(new int[]{2, 3, 2}));
        assertEquals(4, s.rob(new int[]{1, 2, 3, 1}));
        assertEquals(3, s.rob(new int[]{1, 2, 3}));
        assertEquals(7, s.rob(new int[]{7}));
    }
}
