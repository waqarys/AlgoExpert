package twopointers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TwoSumIITest {
    TwoSumII s = new TwoSumII();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 2}, s.twoSum(new int[]{2, 7, 11, 15}, 9));
        assertArrayEquals(new int[]{1, 3}, s.twoSum(new int[]{2, 3, 4}, 6));
        assertArrayEquals(new int[]{1, 2}, s.twoSum(new int[]{-1, 0}, -1));
        assertArrayEquals(new int[]{3, 4}, s.twoSum(new int[]{1, 3, 4, 5, 7, 11}, 9));
    }
}
