package trees;

import common.TreeNode;

/**
 * LC 1448 Count Good Nodes in Binary Tree.
 * Approach: DFS carrying the max value on the root path.
 * Time O(n), Space O(h).
 */
public class CountGoodNodes {
    public int goodNodes(TreeNode root) { return dfs(root, Integer.MIN_VALUE); }

    private int dfs(TreeNode n, int max) {
        if (n == null) return 0;
        int good = n.val >= max ? 1 : 0;
        max = Math.max(max, n.val);
        return good + dfs(n.left, max) + dfs(n.right, max);
    }
}
