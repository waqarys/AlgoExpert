package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MergeTripletsToFormTargetTest {
    MergeTripletsToFormTarget s = new MergeTripletsToFormTarget();
    @Test void examples() {
        assertTrue(s.mergeTriplets(new int[][]{{2, 5, 3}, {1, 8, 4}, {1, 7, 5}}, new int[]{2, 7, 5}));
        assertFalse(s.mergeTriplets(new int[][]{{3, 4, 5}, {4, 5, 6}}, new int[]{3, 2, 5}));
        assertTrue(s.mergeTriplets(new int[][]{{2, 5, 3}, {2, 3, 4}, {1, 2, 5}, {5, 2, 3}}, new int[]{5, 5, 5}));
    }
}
