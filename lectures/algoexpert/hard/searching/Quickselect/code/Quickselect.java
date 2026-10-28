public class Quickselect {
    public static int quickselect(int[] a, int k) {
        int lo = 0, hi = a.length - 1, target = k - 1;
        while (true) {
            int p = lo, l = lo + 1, r = hi;
            while (l <= r) {
                if (a[l] > a[p] && a[r] < a[p]) swap(a, l, r);
                if (a[l] <= a[p]) l++;
                if (a[r] >= a[p]) r--;
            }
            swap(a, p, r);
            if (r == target) return a[r];
            if (r < target) lo = r + 1; else hi = r - 1;
        }
    }

    static void swap(int[] a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }
}
