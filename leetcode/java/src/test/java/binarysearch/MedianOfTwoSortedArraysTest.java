package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MedianOfTwoSortedArraysTest {
    MedianOfTwoSortedArrays s = new MedianOfTwoSortedArrays();
    @Test void examples() {
        assertEquals(2.0, s.findMedianSortedArrays(new int[]{1, 3}, new int[]{2}));
        assertEquals(2.5, s.findMedianSortedArrays(new int[]{1, 2}, new int[]{3, 4}));
        assertEquals(1.0, s.findMedianSortedArrays(new int[]{}, new int[]{1}));
        assertEquals(3.0, s.findMedianSortedArrays(new int[]{1, 2, 3, 4, 5}, new int[]{}));
        assertEquals(4.0, s.findMedianSortedArrays(new int[]{1, 5, 9}, new int[]{2, 3, 4, 6}));
    }
}
