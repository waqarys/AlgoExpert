package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class KthSmallestElementInBSTTest {
    KthSmallestElementInBST s = new KthSmallestElementInBST();
    @Test void examples() {
        assertEquals(1, s.kthSmallest(TreeNode.of(3, 1, 4, null, 2), 1));
        assertEquals(3, s.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 3));
        assertEquals(6, s.kthSmallest(TreeNode.of(5, 3, 6, 2, 4, null, null, 1), 6));
    }
}
