package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class BinaryTreeRightSideViewTest {
    BinaryTreeRightSideView s = new BinaryTreeRightSideView();
    @Test void examples() {
        assertEquals(List.of(1, 3, 4), s.rightSideView(TreeNode.of(1, 2, 3, null, 5, null, 4)));
        assertEquals(List.of(1, 3), s.rightSideView(TreeNode.of(1, null, 3)));
        assertEquals(List.of(1, 3, 4), s.rightSideView(TreeNode.of(1, 2, 3, 4)));
        assertEquals(List.of(), s.rightSideView(null));
    }
}
