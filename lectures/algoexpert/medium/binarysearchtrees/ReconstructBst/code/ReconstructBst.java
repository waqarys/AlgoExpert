public class ReconstructBst {
    private static int idx;

    public static synchronized BST reconstructBst(List<Integer> pre) {
        idx = 0;
        return build(pre, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private static BST build(List<Integer> pre, long lo, long hi) {
        if (idx == pre.size()) return null;
        int v = pre.get(idx);
        if (v < lo || v >= hi) return null;
        idx++;
        BST n = new BST(v);
        n.left = build(pre, lo, v);
        n.right = build(pre, v, hi);
        return n;
    }
}
