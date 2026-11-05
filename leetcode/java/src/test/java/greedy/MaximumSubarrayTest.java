package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MaximumSubarrayTest {
    MaximumSubarray s = new MaximumSubarray();
    @Test void examples() {
        assertEquals(6, s.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
        assertEquals(1, s.maxSubArray(new int[]{1}));
        assertEquals(23, s.maxSubArray(new int[]{5, 4, -1, 7, 8}));
        assertEquals(-1, s.maxSubArray(new int[]{-3, -1, -2}));
    }
}
