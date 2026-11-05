package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class FindMinimumInRotatedSortedArrayTest {
    FindMinimumInRotatedSortedArray s = new FindMinimumInRotatedSortedArray();
    @Test void examples() {
        assertEquals(1, s.findMin(new int[]{3, 4, 5, 1, 2}));
        assertEquals(0, s.findMin(new int[]{4, 5, 6, 7, 0, 1, 2}));
        assertEquals(11, s.findMin(new int[]{11, 13, 15, 17}));
        assertEquals(1, s.findMin(new int[]{2, 1}));
        assertEquals(5, s.findMin(new int[]{5}));
    }
}
