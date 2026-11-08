package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class KthLargestElementInArrayTest {
    KthLargestElementInArray s = new KthLargestElementInArray();
    @Test void examples() {
        assertEquals(5, s.findKthLargest(new int[]{3, 2, 1, 5, 6, 4}, 2));
        assertEquals(4, s.findKthLargest(new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4));
        assertEquals(1, s.findKthLargest(new int[]{1}, 1));
        assertEquals(4, s.findKthLargestHeap(new int[]{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4));
        assertEquals(2, s.findKthLargest(new int[]{2, 2, 2, 2}, 3));
    }
}
