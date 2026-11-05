package dp2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BestTimeToBuySellStockCooldownTest {
    BestTimeToBuySellStockCooldown s = new BestTimeToBuySellStockCooldown();
    @Test void examples() {
        assertEquals(3, s.maxProfit(new int[]{1, 2, 3, 0, 2}));
        assertEquals(0, s.maxProfit(new int[]{1}));
        assertEquals(0, s.maxProfit(new int[]{5, 4, 3}));
        assertEquals(6, s.maxProfit(new int[]{1, 4, 2, 1, 4}));
    }
}
