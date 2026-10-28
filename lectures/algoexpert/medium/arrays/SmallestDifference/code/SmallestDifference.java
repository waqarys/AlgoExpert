public class SmallestDifference {
    public static int[] smallestDifference(int[] a, int[] b) {
        Arrays.sort(a);
        Arrays.sort(b);
        int i = 0, j = 0;
        long best = Long.MAX_VALUE;
        int[] pair = new int[2];
        while (i < a.length && j < b.length) {
            long d = Math.abs((long) a[i] - b[j]);
            if (d < best) { best = d; pair = new int[]{a[i], b[j]}; }
            if (a[i] < b[j]) i++; else if (a[i] > b[j]) j++; else break;
        }
        return pair;
    }
}
