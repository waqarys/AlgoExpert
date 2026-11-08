package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DetectSquaresTest {
    @Test void example() {
        DetectSquares d = new DetectSquares();
        d.add(new int[]{3, 10}); d.add(new int[]{11, 2}); d.add(new int[]{3, 2});
        assertEquals(1, d.count(new int[]{11, 10}));
        assertEquals(0, d.count(new int[]{14, 8}));
        d.add(new int[]{11, 2});
        assertEquals(2, d.count(new int[]{11, 10}));
    }
}
