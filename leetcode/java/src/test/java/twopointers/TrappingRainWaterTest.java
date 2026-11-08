package twopointers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TrappingRainWaterTest {
    TrappingRainWater s = new TrappingRainWater();
    @Test void examples() {
        assertEquals(6, s.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));
        assertEquals(9, s.trap(new int[]{4, 2, 0, 3, 2, 5}));
        assertEquals(9, s.trapArrays(new int[]{4, 2, 0, 3, 2, 5}));
    }
    @Test void edges() {
        assertEquals(0, s.trap(new int[]{}));
        assertEquals(0, s.trap(new int[]{1, 2, 3}));
        assertEquals(0, s.trapArrays(new int[]{}));
    }
}
