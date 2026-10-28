public class LongestPeak {
    public static int longestPeak(int[] a) {
        int best = 0, i = 1;
        while (i < a.length - 1) {
            if (a[i - 1] < a[i] && a[i] > a[i + 1]) {
                int l = i - 1, r = i + 1;
                while (l > 0 && a[l - 1] < a[l]) l--;
                while (r < a.length - 1 && a[r + 1] < a[r]) r++;
                best = Math.max(best, r - l + 1);
                i = r;
            } else i++;
        }
        return best;
    }
}
