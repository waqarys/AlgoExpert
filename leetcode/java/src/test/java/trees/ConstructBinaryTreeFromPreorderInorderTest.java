package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class ConstructBinaryTreeFromPreorderInorderTest {
    ConstructBinaryTreeFromPreorderInorder s = new ConstructBinaryTreeFromPreorderInorder();
    @Test void examples() {
        assertEquals(Arrays.asList(3, 9, 20, null, null, 15, 7),
                TreeNode.toList(s.buildTree(new int[]{3, 9, 20, 15, 7}, new int[]{9, 3, 15, 20, 7})));
        assertEquals(List.of(-1), TreeNode.toList(s.buildTree(new int[]{-1}, new int[]{-1})));
        assertEquals(Arrays.asList(1, null, 2, null, 3),
                TreeNode.toList(s.buildTree(new int[]{1, 2, 3}, new int[]{1, 2, 3})));
    }
}
