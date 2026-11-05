package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MedianFinderTest {
    @Test void example() {
        MedianFinder m = new MedianFinder();
        m.addNum(1); m.addNum(2);
        assertEquals(1.5, m.findMedian());
        m.addNum(3);
        assertEquals(2.0, m.findMedian());
    }
    @Test void largeAndNegative() {
        MedianFinder m = new MedianFinder();
        m.addNum(Integer.MAX_VALUE); m.addNum(Integer.MAX_VALUE);
        assertEquals((double) Integer.MAX_VALUE, m.findMedian());
        m.addNum(-5);
        assertEquals((double) Integer.MAX_VALUE, m.findMedian());
    }
}
