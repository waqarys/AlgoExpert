package hard.binarysearchtrees;

import common.BST;
import java.util.ArrayDeque;

/**
 * Repair BST: exactly two nodes' values were swapped; swap them back in place. Iterative in-order finds
 * the two out-of-order nodes.
 * Time: O(n) | Space: O(h).
 */
public class RepairBst {
    public static BST repairBst(BST tree) {
        BST first = null, second = null, prev = null, cur = tree;
        ArrayDeque<BST> st = new ArrayDeque<>();
        while (cur != null || !st.isEmpty()) {
            while (cur != null) { st.push(cur); cur = cur.left; }
            cur = st.pop();
            if (prev != null && prev.value > cur.value) { if (first == null) first = prev; second = cur; }
            prev = cur;
            cur = cur.right;
        }
        int t = first.value; first.value = second.value; second.value = t;
        return tree;
    }
}
