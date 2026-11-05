package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MaximumProductSubarrayTest {
    MaximumProductSubarray s = new MaximumProductSubarray();
    @Test void examples() {
        assertEquals(6, s.maxProduct(new int[]{2, 3, -2, 4}));
        assertEquals(0, s.maxProduct(new int[]{-2, 0, -1}));
        assertEquals(24, s.maxProduct(new int[]{-2, 3, -4}));
        assertEquals(-2, s.maxProduct(new int[]{-2}));
    }
}
