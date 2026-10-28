public class MinHeightBst {
    public static BST minHeightBst(List<Integer> a) { return build(a, 0, a.size() - 1); }

    private static BST build(List<Integer> a, int lo, int hi) {
        if (lo > hi) return null;
        int mid = (lo + hi) / 2;
        BST n = new BST(a.get(mid));
        n.left = build(a, lo, mid - 1);
        n.right = build(a, mid + 1, hi);
        return n;
    }

    public static int height(BST t) { return t == null ? 0 : 1 + Math.max(height(t.left), height(t.right)); }
}
