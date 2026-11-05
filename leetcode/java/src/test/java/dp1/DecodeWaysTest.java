package dp1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DecodeWaysTest {
    DecodeWays s = new DecodeWays();
    @Test void examples() {
        assertEquals(2, s.numDecodings("12"));
        assertEquals(3, s.numDecodings("226"));
        assertEquals(0, s.numDecodings("06"));
        assertEquals(1, s.numDecodings("10"));
        assertEquals(0, s.numDecodings("30"));
        assertEquals(1, s.numDecodings("2101"));
    }
}
