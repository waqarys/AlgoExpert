package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class JumpGameIITest {
    JumpGameII s = new JumpGameII();
    @Test void examples() {
        assertEquals(2, s.jump(new int[]{2, 3, 1, 1, 4}));
        assertEquals(2, s.jump(new int[]{2, 3, 0, 1, 4}));
        assertEquals(0, s.jump(new int[]{0}));
        assertEquals(1, s.jump(new int[]{5, 1, 1}));
    }
}
