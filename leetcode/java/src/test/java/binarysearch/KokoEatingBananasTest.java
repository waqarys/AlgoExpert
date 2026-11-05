package binarysearch;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class KokoEatingBananasTest {
    KokoEatingBananas s = new KokoEatingBananas();
    @Test void examples() {
        assertEquals(4, s.minEatingSpeed(new int[]{3, 6, 7, 11}, 8));
        assertEquals(30, s.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 5));
        assertEquals(23, s.minEatingSpeed(new int[]{30, 11, 23, 4, 20}, 6));
        assertEquals(3, s.minEatingSpeed(new int[]{805306368, 805306368, 805306368}, 1000000000));
    }
}
