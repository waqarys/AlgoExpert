package medium.binarysearchtrees;

import common.BST;

/**
 * Validate BST: every node must be strictly greater than all left-subtree values and <= all right-subtree values.
 * Time: O(n) | Space: O(h).
 */
public class ValidateBst {
    public static boolean validateBst(BST t) { return valid(t, Long.MIN_VALUE, Long.MAX_VALUE); }

    private static boolean valid(BST t, long min, long max) {
        if (t == null) return true;
        if (t.value < min || t.value >= max) return false;
        return valid(t.left, min, t.value) && valid(t.right, t.value, max);
    }
}
