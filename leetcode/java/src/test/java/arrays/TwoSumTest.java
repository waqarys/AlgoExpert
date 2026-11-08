package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TwoSumTest {
    TwoSum s = new TwoSum();
    @Test void examples() {
        assertArrayEquals(new int[]{0, 1}, s.twoSum(new int[]{2, 7, 11, 15}, 9));
        assertArrayEquals(new int[]{1, 2}, s.twoSum(new int[]{3, 2, 4}, 6));
        assertArrayEquals(new int[]{0, 1}, s.twoSum(new int[]{3, 3}, 6));
    }
    @Test void negativesAndBrute() {
        assertArrayEquals(new int[]{0, 2}, s.twoSum(new int[]{-3, 4, 3, 90}, 0));
        assertArrayEquals(new int[]{1, 2}, s.twoSumBrute(new int[]{3, 2, 4}, 6));
    }
}
