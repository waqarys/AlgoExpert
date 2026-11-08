package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class InvertBinaryTreeTest {
    InvertBinaryTree s = new InvertBinaryTree();
    @Test void examples() {
        assertEquals(Arrays.asList(4, 7, 2, 9, 6, 3, 1), TreeNode.toList(s.invertTree(TreeNode.of(4, 2, 7, 1, 3, 6, 9))));
        assertEquals(Arrays.asList(2, 3, 1), TreeNode.toList(s.invertTree(TreeNode.of(2, 1, 3))));
        assertNull(s.invertTree(null));
    }
}
