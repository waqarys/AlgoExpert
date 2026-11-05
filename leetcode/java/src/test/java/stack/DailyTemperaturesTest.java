package stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DailyTemperaturesTest {
    DailyTemperatures s = new DailyTemperatures();
    @Test void examples() {
        assertArrayEquals(new int[]{1, 1, 4, 2, 1, 1, 0, 0}, s.dailyTemperatures(new int[]{73, 74, 75, 71, 69, 72, 76, 73}));
        assertArrayEquals(new int[]{1, 1, 1, 0}, s.dailyTemperatures(new int[]{30, 40, 50, 60}));
        assertArrayEquals(new int[]{0, 0, 0}, s.dailyTemperatures(new int[]{50, 50, 50}));
    }
}
