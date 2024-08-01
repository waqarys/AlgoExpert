package easy.quesstion3;

public class ClosestValueInBst1 {
    public static void main(String[] args) {
        var root = new ClosestValueInBst1.BST(10);
        root.left = new ClosestValueInBst1.BST(5);
        root.left.left = new ClosestValueInBst1.BST(2);
        root.left.left.left = new ClosestValueInBst1.BST(1);
        root.left.right = new ClosestValueInBst1.BST(5);
        root.right = new ClosestValueInBst1.BST(15);
        root.right.left = new ClosestValueInBst1.BST(13);
        root.right.left.right = new ClosestValueInBst1.BST(14);
        root.right.right = new ClosestValueInBst1.BST(22);

        var expected = 13;
        var actual = ClosestValueInBst1.findClosestValueInBst(root, 12);
        System.out.println(expected == actual);
    }

    public static int findClosestValueInBst(BST tree, int target) {
        return findClosestValueInBst(tree, target, tree.value);
    }

    public static int findClosestValueInBst(BST tree, int target, int closest) {
        if(Math.abs(target - closest) > Math.abs(target - tree.value)){
            closest = tree.value;
        }
        if(target < tree.value && tree.left != null){
            return findClosestValueInBst(tree.left, target, closest);
        } else if(target > tree.value && tree.right != null){
            return findClosestValueInBst(tree.right, target, closest);
        } else {
            return closest;
        }
    }

    static class BST {
        public int value;
        public BST left;
        public BST right;

        public BST(int value) {
            this.value = value;
        }
    }
}
