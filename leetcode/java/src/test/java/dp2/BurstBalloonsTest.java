package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BurstBalloonsTest {
    BurstBalloons s = new BurstBalloons();
    @Test void examples() {
        assertEquals(167, s.maxCoins(new int[]{3, 1, 5, 8}));
        assertEquals(10, s.maxCoins(new int[]{1, 5}));
        assertEquals(7, s.maxCoins(new int[]{7}));
    }
}
