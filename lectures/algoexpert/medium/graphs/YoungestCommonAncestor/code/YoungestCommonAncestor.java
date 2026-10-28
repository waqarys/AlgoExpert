public class YoungestCommonAncestor {
    public static class AncestralTree {
        public final char name;
        public AncestralTree ancestor;
        public AncestralTree(char name) { this.name = name; }
    }

    public static AncestralTree getYoungestCommonAncestor(AncestralTree top, AncestralTree a, AncestralTree b) {
        int da = depth(a, top), db = depth(b, top);
        while (da > db) { a = a.ancestor; da--; }
        while (db > da) { b = b.ancestor; db--; }
        while (a != b) { a = a.ancestor; b = b.ancestor; }
        return a;
    }

    private static int depth(AncestralTree n, AncestralTree top) {
        int d = 0;
        while (n != top) { n = n.ancestor; d++; }
        return d;
    }
}
