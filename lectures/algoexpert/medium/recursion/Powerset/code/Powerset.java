public class Powerset {
    public static List<List<Integer>> powerset(List<Integer> array) {
        List<List<Integer>> subsets = new ArrayList<>();
        subsets.add(new ArrayList<>());
        for (int x : array) {
            int size = subsets.size();
            for (int i = 0; i < size; i++) { List<Integer> s = new ArrayList<>(subsets.get(i)); s.add(x); subsets.add(s); }
        }
        return subsets;
    }
}
