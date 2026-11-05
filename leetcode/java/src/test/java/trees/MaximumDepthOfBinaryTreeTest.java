package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MaximumDepthOfBinaryTreeTest {
    MaximumDepthOfBinaryTree s = new MaximumDepthOfBinaryTree();
    @Test void examples() {
        assertEquals(3, s.maxDepth(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(2, s.maxDepth(TreeNode.of(1, null, 2)));
        assertEquals(0, s.maxDepth(null));
    }
}
