package easy.sorting;

/**
 * Insertion Sort: grow a sorted prefix by sinking each new element into place.
 * Time: O(n^2) worst, O(n) best | Space: O(1).
 */
public class InsertionSort {
    public static int[] insertionSort(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int x = a[i], j = i - 1;
            while (j >= 0 && a[j] > x) { a[j + 1] = a[j]; j--; }
            a[j + 1] = x;
        }
        return a;
    }
}
