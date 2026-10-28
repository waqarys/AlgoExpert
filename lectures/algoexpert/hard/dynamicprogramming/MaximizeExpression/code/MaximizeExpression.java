public class MaximizeExpression {
    public static int maximizeExpression(int[] a) {
        if (a.length < 4) return 0;
        long s1 = Long.MIN_VALUE / 4, s2 = Long.MIN_VALUE / 4, s3 = Long.MIN_VALUE / 4, s4 = Long.MIN_VALUE / 4;
        for (int i = 0; i < a.length; i++) {
            if (i >= 3) s4 = Math.max(s4, s3 - a[i]);
            if (i >= 2) s3 = Math.max(s3, s2 + a[i]);
            if (i >= 1) s2 = Math.max(s2, s1 - a[i]);
            s1 = Math.max(s1, a[i]);
        }
        return (int) s4;
    }
}
