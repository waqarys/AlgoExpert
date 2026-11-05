package trees;

import common.TreeNode;

/**
 * LC 297 Serialize and Deserialize Binary Tree.
 * Approach: preorder DFS with "N" null markers; deserialize with a token pointer.
 * Time O(n), Space O(n).
 */
public class SerializeDeserializeBinaryTree {
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        write(root, sb);
        return sb.substring(0, sb.length() - 1);
    }

    private void write(TreeNode n, StringBuilder sb) {
        if (n == null) { sb.append("N,"); return; }
        sb.append(n.val).append(',');
        write(n.left, sb);
        write(n.right, sb);
    }

    private String[] tokens;
    private int pos;

    public TreeNode deserialize(String data) {
        tokens = data.split(",");
        pos = 0;
        return read();
    }

    private TreeNode read() {
        String t = tokens[pos++];
        if (t.equals("N")) return null;
        TreeNode n = new TreeNode(Integer.parseInt(t));
        n.left = read();
        n.right = read();
        return n;
    }
}
