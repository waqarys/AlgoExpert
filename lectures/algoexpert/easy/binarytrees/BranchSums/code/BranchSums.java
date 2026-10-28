public class BranchSums {
    public static List<Integer> branchSums(BinaryTree root) {
        List<Integer> sums = new ArrayList<>();
        dfs(root, 0, sums);
        return sums;
    }

    private static void dfs(BinaryTree node, int running, List<Integer> sums) {
        if (node == null) return;
        int s = running + node.value;
        if (node.left == null && node.right == null) { sums.add(s); return; }
        dfs(node.left, s, sums);
        dfs(node.right, s, sums);
    }
}
