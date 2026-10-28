public class TaskAssignment {
    public static List<List<Integer>> taskAssignment(int k, List<Integer> tasks) {
        List<Integer> idx = new ArrayList<>();
        for (int i = 0; i < tasks.size(); i++) idx.add(i);
        idx.sort(Comparator.comparingInt(tasks::get));
        List<List<Integer>> out = new ArrayList<>();
        for (int i = 0; i < k; i++) out.add(List.of(idx.get(i), idx.get(idx.size() - 1 - i)));
        return out;
    }
}
