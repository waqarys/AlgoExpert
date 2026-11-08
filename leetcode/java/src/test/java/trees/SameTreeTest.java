package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SameTreeTest {
    SameTree s = new SameTree();
    @Test void examples() {
        assertTrue(s.isSameTree(TreeNode.of(1, 2, 3), TreeNode.of(1, 2, 3)));
        assertFalse(s.isSameTree(TreeNode.of(1, 2), TreeNode.of(1, null, 2)));
        assertFalse(s.isSameTree(TreeNode.of(1, 2, 1), TreeNode.of(1, 1, 2)));
        assertTrue(s.isSameTree(null, null));
    }
}
