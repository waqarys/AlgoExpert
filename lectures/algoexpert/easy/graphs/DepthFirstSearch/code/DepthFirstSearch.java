public class DepthFirstSearch {
    public static class Node {
        public final String name;
        public final List<Node> children = new ArrayList<>();
        public Node(String name) { this.name = name; }
        public Node addChild(String name) { children.add(new Node(name)); return this; }
        public List<String> depthFirstSearch(List<String> out) {
            out.add(name);
            for (Node c : children) c.depthFirstSearch(out);
            return out;
        }
    }
}
