package trees;

import common.TreeNode;
import java.util.*;

/**
 * LC 230 Kth Smallest Element in a BST.
 * Approach: iterative inorder traversal, stop at the k-th popped node.
 * Time O(h + k), Space O(h).
 */
public class KthSmallestElementInBST {
    public int kthSmallest(TreeNode root, int k) {
        Deque<TreeNode> st = new ArrayDeque<>();
        TreeNode cur = root;
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            cur = st.pop();
            if (--k == 0) return cur.val;
            cur = cur.right;
        }
        throw new IllegalArgumentException("k larger than tree size");
    }
}
