package easy.recursion;

import java.util.List;

/**
 * Product Sum: a "special" array holds ints or nested special arrays; each nested array's sum is
 * multiplied by its depth (outermost = 1).
 * Time: O(n) total elements | Space: O(d) depth.
 */
public class ProductSum {
    public static int productSum(List<Object> array) { return productSum(array, 1); }

    @SuppressWarnings("unchecked")
    private static int productSum(List<Object> array, int depth) {
        int sum = 0;
        for (Object o : array) sum += (o instanceof List) ? productSum((List<Object>) o, depth + 1) : (Integer) o;
        return sum * depth;
    }
}
