package heap;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TaskSchedulerTest {
    TaskScheduler s = new TaskScheduler();
    @Test void examples() {
        char[] t = "AAABBB".toCharArray();
        assertEquals(8, s.leastInterval(t, 2));
        assertEquals(6, s.leastInterval(t, 0));
        assertEquals(16, s.leastInterval("AAAAAABCDEFG".toCharArray(), 2));
        assertEquals(8, s.leastIntervalSim(t, 2));
        assertEquals(16, s.leastIntervalSim("AAAAAABCDEFG".toCharArray(), 2));
        assertEquals(6, s.leastIntervalSim(t, 0));
    }
}
