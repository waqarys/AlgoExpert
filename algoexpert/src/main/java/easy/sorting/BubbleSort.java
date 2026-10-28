package easy.sorting;

/**
 * Bubble Sort: repeatedly swap adjacent out-of-order pairs; stop early when a pass makes no swaps.
 * Time: O(n^2) worst, O(n) best | Space: O(1).
 */
public class BubbleSort {
    public static int[] bubbleSort(int[] a) {
        boolean swapped = true;
        for (int end = a.length - 1; swapped && end > 0; end--) {
            swapped = false;
            for (int i = 0; i < end; i++)
                if (a[i] > a[i + 1]) { int t = a[i]; a[i] = a[i + 1]; a[i + 1] = t; swapped = true; }
        }
        return a;
    }
}
