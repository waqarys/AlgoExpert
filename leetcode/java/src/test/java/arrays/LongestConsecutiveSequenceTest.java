package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LongestConsecutiveSequenceTest {
    LongestConsecutiveSequence s = new LongestConsecutiveSequence();
    @Test void examples() {
        assertEquals(4, s.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));
        assertEquals(9, s.longestConsecutive(new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}));
    }
    @Test void edges() {
        assertEquals(0, s.longestConsecutive(new int[]{}));
        assertEquals(3, s.longestConsecutive(new int[]{1, 2, 0, 1}));
        assertEquals(2, s.longestConsecutive(new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE - 1}));
    }
}
