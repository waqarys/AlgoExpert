public class CollidingAsteroids {
    public static int[] collidingAsteroids(int[] asteroids) {
        ArrayDeque<Integer> st = new ArrayDeque<>();
        for (int a : asteroids) {
            boolean alive = true;
            while (alive && a < 0 && !st.isEmpty() && st.peekLast() > 0) {
                int top = st.peekLast();
                if (top < -a) st.pollLast();
                else { if (top == -a) st.pollLast(); alive = false; }
            }
            if (alive) st.addLast(a);
        }
        return st.stream().mapToInt(Integer::intValue).toArray();
    }
}
