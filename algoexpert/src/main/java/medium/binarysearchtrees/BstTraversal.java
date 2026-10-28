package medium.binarysearchtrees;

import common.BST;
import java.util.List;

/**
 * BST Traversal: in-order, pre-order and post-order traversals appending into a list.
 * Time: O(n) | Space: O(n).
 */
public class BstTraversal {
    public static List<Integer> inOrderTraverse(BST t, List<Integer> out) {
        if (t != null) { inOrderTraverse(t.left, out); out.add(t.value); inOrderTraverse(t.right, out); }
        return out;
    }

    public static List<Integer> preOrderTraverse(BST t, List<Integer> out) {
        if (t != null) { out.add(t.value); preOrderTraverse(t.left, out); preOrderTraverse(t.right, out); }
        return out;
    }

    public static List<Integer> postOrderTraverse(BST t, List<Integer> out) {
        if (t != null) { postOrderTraverse(t.left, out); postOrderTraverse(t.right, out); out.add(t.value); }
        return out;
    }
}
