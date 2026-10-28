package medium.graphs;

import java.util.ArrayList;
import java.util.List;

/**
 * <div class="html">
 * <p>
 *   You're given a <span>Node</span> class that has a <span>name</span> and an
 *   array of optional <span>children</span> nodes. When put together, nodes form
 *   an acyclic tree-like structure.
 * </p>
 * <p>
 *   Implement the <span>depthFirstSearch</span> method on the
 *   <span>Node</span> class, which takes in an empty array, traverses the tree
 *   using the Depth-first Search approach (specifically navigating the tree from
 *   left to right), stores all of the nodes' names in the input array, and returns
 *   it.
 * </p>
 * <p>
 *   If you're unfamiliar with Depth-first Search, we recommend watching the
 *   Conceptual Overview section of this question's video explanation before
 *   starting to code.
 * </p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">graph</span> = A
 *      /  |  \
 *     B   C   D
 *    / \     / \
 *   E   F   G   H
 *      / \   \
 *     I   J   K
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
 * </pre>
 * </div>
 */
public class DepthFirstSearch {
    public static void main(String[] args) {
        Node graph = new Node("A");
        graph.addChild("B").addChild("C").addChild("D");
        graph.children.get(0).addChild("E").addChild("F");
        graph.children.get(2).addChild("G").addChild("H");
        graph.children.get(0).children.get(1).addChild("I").addChild("J");
        graph.children.get(2).children.get(0).addChild("K");
        String[] expected = {"A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"};
        List<String> inputArray = new ArrayList<String>();
        System.out.println(compare(graph.depthFirstSearch(inputArray), expected));
    }

    public static boolean compare(List<String> arr1, String[] arr2) {
        if (arr1.size() != arr2.length) {
            return false;
        }
        for (int i = 0; i < arr1.size(); i++) {
            if (!arr1.get(i).equals(arr2[i])) {
                return false;
            }
        }
        return true;
    }

    static class Node {
        String name;
        List<Node> children = new ArrayList<Node>();

        public Node(String name) {
            this.name = name;
        }

        public List<String> depthFirstSearch(List<String> array) {
            // Write your code here.
            array.add(this.name);
            for(int i = 0; i < children.size(); i++) {
                children.get(i).depthFirstSearch(array);
            }
            return array;
        }

        public Node addChild(String name) {
            Node child = new Node(name);
            children.add(child);
            return this;
        }
    }
}
