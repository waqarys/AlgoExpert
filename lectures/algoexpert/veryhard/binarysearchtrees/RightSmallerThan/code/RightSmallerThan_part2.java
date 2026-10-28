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
