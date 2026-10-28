package veryhard.binarysearchtrees;

import java.util.ArrayList;
import java.util.List;

/**
 * Right Smaller Than: for each element, how many elements to its right are strictly smaller?
 * Insert from the right into an augmented BST tracking left-subtree sizes.
 * Time: O(n log n) avg, O(n^2) worst | Space: O(n).
 */
public class RightSmallerThan {
    private static class Node {
        int value, leftSize;
        Node left, right;
        Node(int v) { value = v; }
    }

    public static List<Integer> rightSmallerThan(List<Integer> array) {
        int n = array.size();
        Integer[] out = new Integer[n];
        if (n == 0) return new ArrayList<>();
        Node root = new Node(array.get(n - 1));
        out[n - 1] = 0;
        for (int i = n - 2; i >= 0; i--) {
            int v = array.get(i), smaller = 0;
            Node cur = root;
            while (true) {
                if (v < cur.value) {
                    cur.leftSize++;
                    if (cur.left == null) { cur.left = new Node(v); break; }
                    cur = cur.left;
                } else {
                    smaller += cur.leftSize + (v > cur.value ? 1 : 0);
                    if (cur.right == null) { cur.right = new Node(v); break; }
                    cur = cur.right;
                }
            }
            out[i] = smaller;
        }
        return new ArrayList<>(List.of(out));
    }
}
