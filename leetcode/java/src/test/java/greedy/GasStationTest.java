package greedy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class GasStationTest {
    GasStation s = new GasStation();
    @Test void examples() {
        assertEquals(3, s.canCompleteCircuit(new int[]{1, 2, 3, 4, 5}, new int[]{3, 4, 5, 1, 2}));
        assertEquals(-1, s.canCompleteCircuit(new int[]{2, 3, 4}, new int[]{3, 4, 3}));
        assertEquals(0, s.canCompleteCircuit(new int[]{5}, new int[]{4}));
    }
}
