package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LastStoneWeightTest {
    LastStoneWeight s = new LastStoneWeight();
    @Test void examples() {
        assertEquals(1, s.lastStoneWeight(new int[]{2, 7, 4, 1, 8, 1}));
        assertEquals(1, s.lastStoneWeight(new int[]{1}));
        assertEquals(0, s.lastStoneWeight(new int[]{3, 3}));
    }
}
