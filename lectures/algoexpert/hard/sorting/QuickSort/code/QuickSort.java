public class QuickSort {
    public static int[] quickSort(int[] a) { sort(a, 0, a.length - 1); return a; }

    private static void sort(int[] a, int lo, int hi) {
        while (lo < hi) {
            int p = lo, l = lo + 1, r = hi;
            while (l <= r) {
                if (a[l] > a[p] && a[r] < a[p]) swap(a, l, r);
                if (a[l] <= a[p]) l++;
                if (a[r] >= a[p]) r--;
            }
            swap(a, p, r);
            if (r - lo < hi - r) { sort(a, lo, r - 1); lo = r + 1; } else { sort(a, r + 1, hi); hi = r - 1; }
        }
    }

    private static void swap(int[] a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }
}
