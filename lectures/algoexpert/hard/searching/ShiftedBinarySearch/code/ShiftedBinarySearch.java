public class ShiftedBinarySearch {
    public static int shiftedBinarySearch(int[] a, int t) {
        int lo = 0, hi = a.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] == t) return mid;
            if (a[lo] <= a[mid]) { if (t >= a[lo] && t < a[mid]) hi = mid - 1; else lo = mid + 1; }
            else { if (t > a[mid] && t <= a[hi]) lo = mid + 1; else hi = mid - 1; }
        }
        return -1;
    }
}
