package tree;

import java.util.ArrayList;
import java.util.List;

class Node1 {
    public int val;
    public List<Node1> children;

    public Node1() {}

    public Node1(int _val) {
        val = _val;
    }

    public Node1(int _val, List<Node1> _children) {
        val = _val;
        children = _children;
    }
};

public class NaryTreePreOrderTraversal {
    public List<Integer> preorder(Node1 root) {
        List<Integer> output = new ArrayList<>();
        helper(root, output);
        return output;
    }

    private void helper(Node1 root, List<Integer> output) {
        if(root == null) return;

        output.add(root.val);
        for(int i = 0; i < root.children.size(); i++) {
            helper(root.children.get(i), output);
        }
    }
}
