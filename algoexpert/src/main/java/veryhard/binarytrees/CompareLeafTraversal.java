package veryhard.binarytrees;

import common.BinaryTree;
import java.util.ArrayDeque;

/**
 * Compare Leaf Traversal: do two trees have the same sequence of leaves left-to-right? Lazy iterators.
 * Time: O(n + m) | Space: O(h1 + h2).
 */
public class CompareLeafTraversal {
    public static boolean compareLeafTraversal(BinaryTree a, BinaryTree b) {
        ArrayDeque<BinaryTree> sa = new ArrayDeque<>(), sb = new ArrayDeque<>();
        sa.push(a); sb.push(b);
        while (true) {
            BinaryTree la = nextLeaf(sa), lb = nextLeaf(sb);
            if (la == null || lb == null) return la == lb;
            if (la.value != lb.value) return false;
        }
    }

    private static BinaryTree nextLeaf(ArrayDeque<BinaryTree> st) {
        while (!st.isEmpty()) {
            BinaryTree n = st.pop();
            if (n.left == null && n.right == null) return n;
            if (n.right != null) st.push(n.right);
            if (n.left != null) st.push(n.left);
        }
        return null;
    }
}
