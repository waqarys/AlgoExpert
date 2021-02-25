package easy.quesstion3;

public class ClosestValueInBst2 {
    public static void main(String[] args) {
        var root = new ClosestValueInBst2.BST(10);
        root.left = new ClosestValueInBst2.BST(5);
        root.left.left = new ClosestValueInBst2.BST(2);
        root.left.left.left = new ClosestValueInBst2.BST(1);
        root.left.right = new ClosestValueInBst2.BST(5);
        root.right = new ClosestValueInBst2.BST(15);
        root.right.left = new ClosestValueInBst2.BST(13);
        root.right.left.right = new ClosestValueInBst2.BST(14);
        root.right.right = new ClosestValueInBst2.BST(22);

        var expected = 13;
        var actual = ClosestValueInBst2.findClosestValueInBst(root, 12);
        System.out.println(expected == actual);
    }

    public static int findClosestValueInBst(ClosestValueInBst2.BST tree, int target) {
        return findClosestValueInBst(tree, target, tree.value);
    }

    public static int findClosestValueInBst(BST tree, int target, int closest) {
        BST currentNode = tree;
        while(currentNode != null){
            if(Math.abs(target - closest) > Math.abs(target - currentNode.value)){
                closest = currentNode.value;
            }
            if(target < currentNode.value){
                currentNode = currentNode.left;
            } else if(target > currentNode.value){
                currentNode = currentNode.right;
            } else {
                break;
            }
        }
        return closest;
    }

    static class BST {
        public int value;
        public ClosestValueInBst2.BST left;
        public ClosestValueInBst2.BST right;

        public BST(int value) {
            this.value = value;
        }
    }
}
