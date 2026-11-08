package arrays;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ProductOfArrayExceptSelfTest {
    ProductOfArrayExceptSelf s = new ProductOfArrayExceptSelf();
    @Test void examples() {
        assertArrayEquals(new int[]{24, 12, 8, 6}, s.productExceptSelf(new int[]{1, 2, 3, 4}));
        assertArrayEquals(new int[]{0, 0, 9, 0, 0}, s.productExceptSelf(new int[]{-1, 1, 0, -3, 3}));
    }
    @Test void twoZeros() {
        assertArrayEquals(new int[]{0, 0, 0}, s.productExceptSelf(new int[]{0, 2, 0}));
        assertArrayEquals(new int[]{3, 2}, s.productExceptSelf(new int[]{2, 3}));
    }
}
