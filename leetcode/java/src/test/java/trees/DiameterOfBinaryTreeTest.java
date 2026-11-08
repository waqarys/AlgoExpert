package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DiameterOfBinaryTreeTest {
    DiameterOfBinaryTree s = new DiameterOfBinaryTree();
    @Test void examples() {
        assertEquals(3, s.diameterOfBinaryTree(TreeNode.of(1, 2, 3, 4, 5)));
        assertEquals(1, s.diameterOfBinaryTree(TreeNode.of(1, 2)));
        // longest path entirely inside the left subtree
        assertEquals(4, s.diameterOfBinaryTree(TreeNode.of(1, 2, null, 3, 4, 5, null, null, 6)));
    }
}
