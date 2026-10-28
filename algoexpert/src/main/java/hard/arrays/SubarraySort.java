package hard.arrays;

/**
 * Subarray Sort: smallest [start, end] range which, if sorted, makes the whole array sorted; [-1, -1] if sorted.
 * Time: O(n) | Space: O(1).
 */
public class SubarraySort {
    public static int[] subarraySort(int[] a) {
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int i = 0; i < a.length; i++) {
            boolean out = (i > 0 && a[i] < a[i - 1]) || (i < a.length - 1 && a[i] > a[i + 1]);
            if (out) { min = Math.min(min, a[i]); max = Math.max(max, a[i]); }
        }
        if (min == Integer.MAX_VALUE) return new int[]{-1, -1};
        int l = 0, r = a.length - 1;
        while (a[l] <= min) l++;
        while (a[r] >= max) r--;
        return new int[]{l, r};
    }
}
