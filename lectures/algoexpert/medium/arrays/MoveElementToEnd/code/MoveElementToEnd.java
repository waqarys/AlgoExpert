public class MoveElementToEnd {
    public static List<Integer> moveElementToEnd(List<Integer> array, int toMove) {
        int l = 0, r = array.size() - 1;
        while (l < r) {
            while (l < r && array.get(r) == toMove) r--;
            if (array.get(l) == toMove) Collections.swap(array, l, r);
            l++;
        }
        return array;
    }
}
