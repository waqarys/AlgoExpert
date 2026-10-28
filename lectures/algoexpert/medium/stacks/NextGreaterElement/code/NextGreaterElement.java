public class NextGreaterElement {
    public static int[] nextGreaterElement(int[] a) {
        int n = a.length;
        int[] out = new int[n];
        Arrays.fill(out, -1);
        ArrayDeque<Integer> st = new ArrayDeque<>();
        for (int i = 0; i < 2 * n; i++) {
            int j = i % n;
            while (!st.isEmpty() && a[st.peek()] < a[j]) out[st.pop()] = a[j];
            if (i < n) st.push(j);
        }
        return out;
    }
}
