public class FirstDuplicateValue {
    public static int firstDuplicateValue(int[] a) {
        for (int x : a) {
            int v = Math.abs(x);
            if (a[v - 1] < 0) return v;
            a[v - 1] = -a[v - 1];
        }
        return -1;
    }
}
