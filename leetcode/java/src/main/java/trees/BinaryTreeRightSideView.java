package trees;

import common.TreeNode;
import java.util.*;

/**
 * LC 199 Binary Tree Right Side View.
 * Approach: BFS by level, record the last node of each level.
 * Time O(n), Space O(n).
 */
public class BinaryTreeRightSideView {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>(List.of(root));
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode n = q.poll();
                if (i == size - 1) res.add(n.val);
                if (n.left != null) q.add(n.left);
                if (n.right != null) q.add(n.right);
            }
        }
        return res;
    }
}
