package hard.sorting;

/**
 * Heap Sort: build a max-heap in place then repeatedly move the max to the end.
 * Time: O(n log n) | Space: O(1).
 */
public class HeapSort {
    public static int[] heapSort(int[] a) {
        for (int i = a.length / 2 - 1; i >= 0; i--) sift(a, i, a.length);
        for (int end = a.length - 1; end > 0; end--) { int t = a[0]; a[0] = a[end]; a[end] = t; sift(a, 0, end); }
        return a;
    }

    private static void sift(int[] a, int i, int n) {
        while (2 * i + 1 < n) {
            int c = 2 * i + 1;
            if (c + 1 < n && a[c + 1] > a[c]) c++;
            if (a[i] >= a[c]) return;
            int t = a[i]; a[i] = a[c]; a[c] = t;
            i = c;
        }
    }
}
