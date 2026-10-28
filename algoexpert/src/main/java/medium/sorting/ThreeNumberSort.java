package medium.sorting;

/**
 * Three Number Sort: sort an array in place according to a 3-value `order` (Dutch national flag).
 * Time: O(n) | Space: O(1).
 */
public class ThreeNumberSort {
    public static int[] threeNumberSort(int[] a, int[] order) {
        int lo = 0, mid = 0, hi = a.length - 1;
        while (mid <= hi) {
            if (a[mid] == order[0]) swap(a, lo++, mid++);
            else if (a[mid] == order[1]) mid++;
            else swap(a, mid, hi--);
        }
        return a;
    }

    private static void swap(int[] a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }
}
