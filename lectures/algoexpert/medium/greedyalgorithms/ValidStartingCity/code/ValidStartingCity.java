public class ValidStartingCity {
    public static int validStartingCity(int[] distances, int[] fuel, int mpg) {
        int miles = 0, minMiles = 0, start = 0;
        for (int i = 1; i < distances.length; i++) {
            miles += fuel[i - 1] * mpg - distances[i - 1];
            if (miles < minMiles) { minMiles = miles; start = i; }
        }
        return start;
    }
}
