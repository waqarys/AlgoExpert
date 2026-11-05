package trees;

import common.TreeNode;
import java.util.*;

/**
 * LC 102 Binary Tree Level Order Traversal.
 * Approach: BFS, processing queue.size() nodes per level.
 * Time O(n), Space O(n).
 */
public class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>(List.of(root));
        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            for (int i = q.size(); i > 0; i--) {
                TreeNode n = q.poll();
                level.add(n.val);
                if (n.left != null) q.add(n.left);
                if (n.right != null) q.add(n.right);
            }
            res.add(level);
        }
        return res;
    }
}
