package tree;

import java.util.ArrayList;
import java.util.List;

class Node {
    public int val;
    public List<Node1> children;

    public Node() {
    }

    public Node(int val, List<Node1> children) {
        this.val = val;
        this.children = children;
    }
}

public class NaryTreePostOrderTraversal {
    public List<Integer> postOrder(Node1 root) {
        List<Integer> output = new ArrayList<>();

        helper(root, output);
        return output;
    }

    private void helper(Node1 root, List<Integer> output) {
        if(root == null) return;
        for(int i = 0; i < root.children.size(); i++){
            helper(root.children.get(i), output);
        }
        output.add(root.val);
    }
}
