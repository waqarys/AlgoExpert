package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CoinChangeTest {
    CoinChange s = new CoinChange();
    @Test void examples() {
        assertEquals(3, s.coinChange(new int[]{1, 2, 5}, 11));
        assertEquals(-1, s.coinChange(new int[]{2}, 3));
        assertEquals(0, s.coinChange(new int[]{1}, 0));
        assertEquals(2, s.coinChange(new int[]{1, 3, 4}, 6));
    }
}
