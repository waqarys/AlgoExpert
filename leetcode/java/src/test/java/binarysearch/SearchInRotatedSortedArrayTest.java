package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SearchInRotatedSortedArrayTest {
    SearchInRotatedSortedArray s = new SearchInRotatedSortedArray();
    @Test void examples() {
        assertEquals(4, s.search(new int[]{4, 5, 6, 7, 0, 1, 2}, 0));
        assertEquals(-1, s.search(new int[]{4, 5, 6, 7, 0, 1, 2}, 3));
        assertEquals(-1, s.search(new int[]{1}, 0));
        assertEquals(1, s.search(new int[]{3, 1}, 1));
        assertEquals(0, s.search(new int[]{5, 1, 3}, 5));
    }
}
