package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SubtreeOfAnotherTreeTest {
    SubtreeOfAnotherTree s = new SubtreeOfAnotherTree();
    @Test void examples() {
        assertTrue(s.isSubtree(TreeNode.of(3, 4, 5, 1, 2), TreeNode.of(4, 1, 2)));
        assertFalse(s.isSubtree(TreeNode.of(3, 4, 5, 1, 2, null, null, null, null, 0), TreeNode.of(4, 1, 2)));
        assertTrue(s.isSubtree(TreeNode.of(1, 1), TreeNode.of(1)));
    }
}
