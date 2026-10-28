package medium.arrays;

/**
 * First Duplicate Value: values are in [1, n]; return the value whose second occurrence comes first, else -1.
 * Mark visited values by negating the slot at index |v|-1 (mutates input).
 * Time: O(n) | Space: O(1).
 */
public class FirstDuplicateValue {
    public static int firstDuplicateValue(int[] a) {
        for (int x : a) {
            int v = Math.abs(x);
            if (a[v - 1] < 0) return v;
            a[v - 1] = -a[v - 1];
        }
        return -1;
    }
}
