package slidingwindow;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SlidingWindowMaximumTest {
    SlidingWindowMaximum s = new SlidingWindowMaximum();
    @Test void examples() {
        assertArrayEquals(new int[]{3, 3, 5, 5, 6, 7}, s.maxSlidingWindow(new int[]{1, 3, -1, -3, 5, 3, 6, 7}, 3));
        assertArrayEquals(new int[]{1}, s.maxSlidingWindow(new int[]{1}, 1));
        assertArrayEquals(new int[]{11}, s.maxSlidingWindow(new int[]{9, 11}, 2));
        assertArrayEquals(new int[]{7, 4}, s.maxSlidingWindow(new int[]{7, 2, 4}, 2));
    }
}
