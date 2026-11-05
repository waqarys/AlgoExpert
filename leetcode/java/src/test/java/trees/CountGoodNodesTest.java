package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CountGoodNodesTest {
    CountGoodNodes s = new CountGoodNodes();
    @Test void examples() {
        assertEquals(4, s.goodNodes(TreeNode.of(3, 1, 4, 3, null, 1, 5)));
        assertEquals(3, s.goodNodes(TreeNode.of(3, 3, null, 4, 2)));
        assertEquals(1, s.goodNodes(TreeNode.of(1)));
    }
}
