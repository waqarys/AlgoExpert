public class FindKthLargestValueInBst {
    private static int seen, answer;

    public static synchronized int findKthLargestValueInBst(BST tree, int k) {
        seen = 0; answer = -1;
        walk(tree, k);
        return answer;
    }

    private static void walk(BST n, int k) {
        if (n == null || seen >= k) return;
        walk(n.right, k);
        if (seen < k) { seen++; if (seen == k) { answer = n.value; return; } walk(n.left, k); }
    }
}
