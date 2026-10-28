public class TwoColorable {
    public static boolean twoColorable(int[][] edges) {
        int[] color = new int[edges.length];
        java.util.ArrayDeque<Integer> st = new java.util.ArrayDeque<>();
        for (int s = 0; s < edges.length; s++) {
            if (color[s] != 0) continue;
            color[s] = 1;
            st.push(s);
            while (!st.isEmpty()) {
                int v = st.pop();
                for (int w : edges[v]) {
                    if (color[w] == 0) { color[w] = -color[v]; st.push(w); }
                    else if (color[w] == color[v]) return false;
                }
            }
        }
        return true;
    }
}
