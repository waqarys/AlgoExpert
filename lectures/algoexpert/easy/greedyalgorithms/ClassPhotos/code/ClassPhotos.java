public class ClassPhotos {
    public static boolean classPhotos(List<Integer> red, List<Integer> blue) {
        Collections.sort(red, Collections.reverseOrder());
        Collections.sort(blue, Collections.reverseOrder());
        boolean redBack = red.get(0) > blue.get(0);
        for (int i = 0; i < red.size(); i++) {
            int back = redBack ? red.get(i) : blue.get(i), front = redBack ? blue.get(i) : red.get(i);
            if (back <= front) return false;
        }
        return true;
    }
}
