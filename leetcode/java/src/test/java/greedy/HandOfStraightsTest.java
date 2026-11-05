package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class HandOfStraightsTest {
    HandOfStraights s = new HandOfStraights();
    @Test void examples() {
        assertTrue(s.isNStraightHand(new int[]{1, 2, 3, 6, 2, 3, 4, 7, 8}, 3));
        assertFalse(s.isNStraightHand(new int[]{1, 2, 3, 4, 5}, 4));
        assertTrue(s.isNStraightHand(new int[]{8, 10, 12}, 1));
        assertFalse(s.isNStraightHand(new int[]{1, 1, 2, 3}, 2));
    }
}
