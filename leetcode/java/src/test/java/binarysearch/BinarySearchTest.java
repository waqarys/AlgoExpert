package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BinarySearchTest {
    BinarySearch s = new BinarySearch();
    @Test void examples() {
        assertEquals(4, s.search(new int[]{-1, 0, 3, 5, 9, 12}, 9));
        assertEquals(-1, s.search(new int[]{-1, 0, 3, 5, 9, 12}, 2));
        assertEquals(0, s.search(new int[]{5}, 5));
        assertEquals(-1, s.search(new int[]{}, 5));
    }
}
