package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestIncreasingSubsequenceTest {
    LongestIncreasingSubsequence s = new LongestIncreasingSubsequence();
    @Test void examples() {
        assertEquals(4, s.lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18}));
        assertEquals(4, s.lengthOfLIS(new int[]{0, 1, 0, 3, 2, 3}));
        assertEquals(1, s.lengthOfLIS(new int[]{7, 7, 7, 7}));
        assertEquals(4, s.lengthOfLISQuadratic(new int[]{10, 9, 2, 5, 3, 7, 101, 18}));
    }
}
