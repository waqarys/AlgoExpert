package twopointers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ContainerWithMostWaterTest {
    ContainerWithMostWater s = new ContainerWithMostWater();
    @Test void examples() {
        assertEquals(49, s.maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}));
        assertEquals(1, s.maxArea(new int[]{1, 1}));
        assertEquals(16, s.maxArea(new int[]{4, 3, 2, 1, 4}));
    }
}
