public class DiskStacking {
    public static List<Integer[]> diskStacking(List<Integer[]> disks) {
        List<Integer[]> d = new ArrayList<>(disks);
        d.sort(Comparator.comparingInt(x -> x[2]));
        int n = d.size(), best = 0;
        int[] h = new int[n], prev = new int[n];
        for (int i = 0; i < n; i++) {
            h[i] = d.get(i)[2];
            prev[i] = -1;
            for (int j = 0; j < i; j++) {
                Integer[] a = d.get(j), b = d.get(i);
                if (a[0] < b[0] && a[1] < b[1] && a[2] < b[2] && h[j] + b[2] > h[i]) { h[i] = h[j] + b[2]; prev[i] = j; }
            }
            if (h[i] > h[best]) best = i;
        }
        LinkedList<Integer[]> out = new LinkedList<>();
        for (int i = best; i != -1; i = prev[i]) out.addFirst(d.get(i));
        return out;
    }
}
