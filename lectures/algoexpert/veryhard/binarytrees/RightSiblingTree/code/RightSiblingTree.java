public class RightSiblingTree {
    public static BinaryTree rightSiblingTree(BinaryTree root) {
        java.util.List<BinaryTree> level = java.util.List.of(root);
        while (!level.isEmpty()) {
            java.util.List<BinaryTree> next = new java.util.ArrayList<>();
            for (BinaryTree n : level) { if (n.left != null) next.add(n.left); if (n.right != null) next.add(n.right); }
            for (int i = 0; i < level.size(); i++) level.get(i).right = i + 1 < level.size() ? level.get(i + 1) : null;
            level = next;
        }
        return root;
    }
}
