package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class BinaryTreeLevelOrderTraversalTest {
    BinaryTreeLevelOrderTraversal s = new BinaryTreeLevelOrderTraversal();
    @Test void examples() {
        assertEquals(List.of(List.of(3), List.of(9, 20), List.of(15, 7)), s.levelOrder(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(List.of(List.of(1)), s.levelOrder(TreeNode.of(1)));
        assertEquals(List.of(), s.levelOrder(null));
    }
}
