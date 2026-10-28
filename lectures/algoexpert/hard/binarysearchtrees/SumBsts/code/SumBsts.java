public class SumBsts {
    public static int sumBsts(BinaryTree t) { long[] total = {0}; info(t, total); return (int) total[0]; }

    /** returns {isBst, size, min, max, sum} */
    private static long[] info(BinaryTree t, long[] total) {
        if (t == null) return new long[]{1, 0, Long.MAX_VALUE, Long.MIN_VALUE, 0};
        long[] l = info(t.left, total), r = info(t.right, total);
        boolean bst = l[0] == 1 && r[0] == 1 && l[3] < t.value && t.value <= r[2];
        long size = l[1] + r[1] + 1, sum = l[4] + r[4] + t.value;
        if (bst && size >= 3) {
            total[0] += sum;
            // children already counted? subtract their counted contributions to avoid double counting
            if (l[1] >= 3) total[0] -= l[4];
            if (r[1] >= 3) total[0] -= r[4];
        }
        return new long[]{bst ? 1 : 0, size, Math.min(l[2], t.value), Math.max(r[3], t.value), sum};
    }
}
