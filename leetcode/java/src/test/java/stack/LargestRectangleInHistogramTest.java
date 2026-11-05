package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LargestRectangleInHistogramTest {
    LargestRectangleInHistogram s = new LargestRectangleInHistogram();
    @Test void examples() {
        assertEquals(10, s.largestRectangleArea(new int[]{2, 1, 5, 6, 2, 3}));
        assertEquals(4, s.largestRectangleArea(new int[]{2, 4}));
        assertEquals(6, s.largestRectangleArea(new int[]{2, 2, 2}));
        assertEquals(9, s.largestRectangleArea(new int[]{1, 2, 3, 4, 5}));
    }
}
