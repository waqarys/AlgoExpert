package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LowestCommonAncestorBSTTest {
    @Test void examples() {
        TreeNode r = TreeNode.of(6, 2, 8, 0, 4, 7, 9, null, null, 3, 5);
        var s = new LowestCommonAncestorBST();
        assertEquals(6, s.lowestCommonAncestor(r, r.find(2), r.find(8)).val);
        assertEquals(2, s.lowestCommonAncestor(r, r.find(2), r.find(4)).val);
        assertEquals(4, s.lowestCommonAncestor(r, r.find(3), r.find(5)).val);
    }
}
