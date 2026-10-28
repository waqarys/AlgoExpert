package hard.sorting;

import java.util.ArrayList;

/**
 * Radix Sort: sort non-negative ints by LSD radix sort with counting sort per decimal digit.
 * Time: O(d * (n + 10)) | Space: O(n).
 */
public class RadixSort {
    public static ArrayList<Integer> radixSort(ArrayList<Integer> a) {
        if (a.isEmpty()) return a;
        int max = a.stream().max(Integer::compare).get();
        int[] out = new int[a.size()];
        for (long exp = 1; max / exp > 0; exp *= 10) {
            int[] count = new int[10];
            for (int x : a) count[(int) (x / exp % 10)]++;
            for (int i = 1; i < 10; i++) count[i] += count[i - 1];
            for (int i = a.size() - 1; i >= 0; i--) out[--count[(int) (a.get(i) / exp % 10)]] = a.get(i);
            for (int i = 0; i < out.length; i++) a.set(i, out[i]);
        }
        return a;
    }
}
