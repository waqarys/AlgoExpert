package easy.sorting;

/**
 * Selection Sort: repeatedly select the minimum of the unsorted suffix and swap it to the front.
 * Time: O(n^2) | Space: O(1).
 */
public class SelectionSort {
    public static int[] selectionSort(int[] a) {
        for (int i = 0; i < a.length - 1; i++) {
            int min = i;
            for (int j = i + 1; j < a.length; j++) if (a[j] < a[min]) min = j;
            int t = a[i]; a[i] = a[min]; a[min] = t;
        }
        return a;
    }
}
