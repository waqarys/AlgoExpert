package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PartitionEqualSubsetSumTest {
    PartitionEqualSubsetSum s = new PartitionEqualSubsetSum();
    @Test void examples() {
        assertTrue(s.canPartition(new int[]{1, 5, 11, 5}));
        assertFalse(s.canPartition(new int[]{1, 2, 3, 5}));
        assertFalse(s.canPartition(new int[]{2}));
        assertTrue(s.canPartition(new int[]{3, 3}));
    }
}
