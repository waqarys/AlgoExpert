package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BinaryTreeMaximumPathSumTest {
    BinaryTreeMaximumPathSum s = new BinaryTreeMaximumPathSum();
    @Test void examples() {
        assertEquals(6, s.maxPathSum(TreeNode.of(1, 2, 3)));
        assertEquals(42, s.maxPathSum(TreeNode.of(-10, 9, 20, null, null, 15, 7)));
        assertEquals(-3, s.maxPathSum(TreeNode.of(-3)));
        assertEquals(-1, s.maxPathSum(TreeNode.of(-2, -1)));
    }
}
