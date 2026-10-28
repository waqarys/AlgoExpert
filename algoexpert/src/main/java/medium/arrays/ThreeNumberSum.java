package medium.arrays;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Three Number Sum: all triplets of distinct integers summing to target, each triplet ascending and the
 * list sorted. Sort then sweep with two pointers.
 * Time: O(n^2) | Space: O(n).
 */
public class ThreeNumberSum {
    public static List<Integer[]> threeNumberSum(int[] array, int target) {
        Arrays.sort(array);
        List<Integer[]> out = new ArrayList<>();
        for (int i = 0; i < array.length - 2; i++) {
            int l = i + 1, r = array.length - 1;
            while (l < r) {
                int s = array[i] + array[l] + array[r];
                if (s == target) { out.add(new Integer[]{array[i], array[l], array[r]}); l++; r--; }
                else if (s < target) l++; else r--;
            }
        }
        return out;
    }
}
