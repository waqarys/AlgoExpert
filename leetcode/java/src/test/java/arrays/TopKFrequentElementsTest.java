package arrays;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class TopKFrequentElementsTest {
    TopKFrequentElements s = new TopKFrequentElements();
    static int[] sorted(int[] a) { a = a.clone(); Arrays.sort(a); return a; }
    @Test void examples() {
        assertArrayEquals(new int[]{1, 2}, sorted(s.topKFrequent(new int[]{1, 1, 1, 2, 2, 3}, 2)));
        assertArrayEquals(new int[]{1}, s.topKFrequent(new int[]{1}, 1));
    }
    @Test void negatives() {
        assertArrayEquals(new int[]{-1, 2}, sorted(s.topKFrequent(new int[]{4, -1, -1, 2, 2, 2, -1, 3}, 2)));
    }
}
