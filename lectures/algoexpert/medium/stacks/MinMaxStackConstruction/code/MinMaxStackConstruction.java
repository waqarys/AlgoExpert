public class MinMaxStackConstruction {
    public static class MinMaxStack {
        private final List<int[]> st = new ArrayList<>();

        public int peek() { return st.get(st.size() - 1)[0]; }
        public int pop() { return st.remove(st.size() - 1)[0]; }
        public void push(int v) {
            if (st.isEmpty()) st.add(new int[]{v, v, v});
            else { int[] t = st.get(st.size() - 1); st.add(new int[]{v, Math.min(v, t[1]), Math.max(v, t[2])}); }
        }
        public int getMin() { return st.get(st.size() - 1)[1]; }
        public int getMax() { return st.get(st.size() - 1)[2]; }
    }
}
