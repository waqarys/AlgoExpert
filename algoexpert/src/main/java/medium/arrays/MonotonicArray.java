package medium.arrays;

/**
 * Monotonic Array: is the array entirely non-increasing or entirely non-decreasing?
 * Time: O(n) | Space: O(1).
 */
public class MonotonicArray {
    public static boolean isMonotonic(int[] a) {
        boolean inc = true, dec = true;
        for (int i = 1; i < a.length; i++) {
            if (a[i] < a[i - 1]) inc = false;
            if (a[i] > a[i - 1]) dec = false;
        }
        return inc || dec;
    }
}
