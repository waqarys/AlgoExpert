package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BestTimeToBuyAndSellStockTest {
    BestTimeToBuyAndSellStock s = new BestTimeToBuyAndSellStock();
    @Test void examples() {
        assertEquals(5, s.maxProfit(new int[]{7, 1, 5, 3, 6, 4}));
        assertEquals(0, s.maxProfit(new int[]{7, 6, 4, 3, 1}));
        assertEquals(0, s.maxProfit(new int[]{5}));
        assertEquals(4, s.maxProfit(new int[]{2, 4, 1, 5}));
    }
}
