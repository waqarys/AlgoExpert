public class FindClosestValueInBst {
    public static int findClosestValueInBst(BST tree, int target) {
        int closest = tree.value;
        BST cur = tree;
        while (cur != null) {
            if (Math.abs(target - cur.value) < Math.abs(target - closest)) closest = cur.value;
            if (target < cur.value) cur = cur.left;
            else if (target > cur.value) cur = cur.right;
            else break;
        }
        return closest;
    }
}
