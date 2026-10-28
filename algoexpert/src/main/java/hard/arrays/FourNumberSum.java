package hard.arrays;

import java.util.*;

/**
 * Four Number Sum: all quadruplets of distinct integers summing to target (any order). Store pair sums
 * seen before index i, combine with pairs after i, so each quadruplet is reported once.
 * Time: O(n^2) avg | Space: O(n^2).
 */
public class FourNumberSum {
    public static List<Integer[]> fourNumberSum(int[] a, int target) {
        Map<Integer, List<int[]>> pairs = new HashMap<>();
        List<Integer[]> out = new ArrayList<>();
        for (int i = 1; i < a.length - 1; i++) {
            for (int j = i + 1; j < a.length; j++) {
                List<int[]> ps = pairs.get(target - a[i] - a[j]);
                if (ps != null) for (int[] p : ps) out.add(new Integer[]{p[0], p[1], a[i], a[j]});
            }
            for (int k = 0; k < i; k++) pairs.computeIfAbsent(a[i] + a[k], x -> new ArrayList<>()).add(new int[]{a[k], a[i]});
        }
        return out;
    }
}
