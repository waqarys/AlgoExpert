package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BalancedBinaryTreeTest {
    BalancedBinaryTree s = new BalancedBinaryTree();
    @Test void examples() {
        assertTrue(s.isBalanced(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertFalse(s.isBalanced(TreeNode.of(1, 2, 2, 3, 3, null, null, 4, 4)));
        assertTrue(s.isBalanced(null));
        assertFalse(s.isBalanced(TreeNode.of(1, null, 2, null, 3)));
    }
}
