public class ValidateThreeNodes {
    public static boolean validateThreeNodes(BST one, BST two, BST three) {
        if (descends(two, one)) return descends(three, two);
        if (descends(two, three)) return descends(one, two);
        return false;
    }

    /** true if `target` is reachable going down from `from`. */
    private static boolean descends(BST from, BST target) {
        BST c = from;
        while (c != null && c != target) c = target.value < c.value ? c.left : c.right;
        return c == target;
    }
}
