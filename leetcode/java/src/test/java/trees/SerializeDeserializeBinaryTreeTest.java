package trees;

import common.TreeNode;
import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class SerializeDeserializeBinaryTreeTest {
    SerializeDeserializeBinaryTree c = new SerializeDeserializeBinaryTree();
    @Test void roundTrip() {
        TreeNode t = TreeNode.of(1, 2, 3, null, null, 4, 5);
        assertEquals("1,2,N,N,3,4,N,N,5,N,N", c.serialize(t));
        assertEquals(Arrays.asList(1, 2, 3, null, null, 4, 5), TreeNode.toList(c.deserialize(c.serialize(t))));
        assertNull(c.deserialize(c.serialize(null)));
        assertEquals(Arrays.asList(-10, null, 200), TreeNode.toList(c.deserialize(c.serialize(TreeNode.of(-10, null, 200)))));
    }
}
