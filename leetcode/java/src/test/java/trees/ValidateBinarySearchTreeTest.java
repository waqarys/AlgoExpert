package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ValidateBinarySearchTreeTest {
    ValidateBinarySearchTree s = new ValidateBinarySearchTree();
    @Test void examples() {
        assertTrue(s.isValidBST(TreeNode.of(2, 1, 3)));
        assertFalse(s.isValidBST(TreeNode.of(5, 1, 4, null, null, 3, 6)));
        assertFalse(s.isValidBST(TreeNode.of(5, 4, 6, null, null, 3, 7)));
        assertFalse(s.isValidBST(TreeNode.of(2, 2, 2)));
        assertTrue(s.isValidBST(TreeNode.of(Integer.MAX_VALUE)));
    }
}
