package twopointers;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class ThreeSumTest {
    ThreeSum s = new ThreeSum();
    @Test void examples() {
        assertEquals(List.of(List.of(-1, -1, 2), List.of(-1, 0, 1)), s.threeSum(new int[]{-1, 0, 1, 2, -1, -4}));
        assertEquals(List.of(), s.threeSum(new int[]{0, 1, 1}));
        assertEquals(List.of(List.of(0, 0, 0)), s.threeSum(new int[]{0, 0, 0, 0}));
    }
    @Test void manyDuplicates() {
        assertEquals(List.of(List.of(-2, 0, 2), List.of(-2, 1, 1)), s.threeSum(new int[]{-2, 0, 0, 2, 2, 1, 1}));
    }
}
