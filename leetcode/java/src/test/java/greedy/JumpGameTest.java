package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class JumpGameTest {
    JumpGame s = new JumpGame();
    @Test void examples() {
        assertTrue(s.canJump(new int[]{2, 3, 1, 1, 4}));
        assertFalse(s.canJump(new int[]{3, 2, 1, 0, 4}));
        assertTrue(s.canJump(new int[]{0}));
        assertFalse(s.canJump(new int[]{0, 1}));
    }
}
