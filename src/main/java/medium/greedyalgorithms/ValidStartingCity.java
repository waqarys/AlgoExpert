package medium.greedyalgorithms;

/**
 * <div class="html">
 * <p>
 *   Imagine you have a set of cities that are laid out in a circle, connected by a
 *   circular road that runs clockwise. Each city has a gas station that provides
 *   gallons of fuel, and each city is some distance away from the next city.
 * </p>
 * <p>
 *   You have a car that can drive some number of miles per gallon of fuel, and
 *   your goal is to pick a starting city such that you can fill up your car with
 *   that city's fuel, drive to the next city, refill up your car with that city's
 *   fuel, drive to the next city, and so on and so forth until you return back to
 *   the starting city with 0 or more gallons of fuel left.
 * </p>
 * <p>
 *   This city is called a valid starting city, and it's guaranteed that there will
 *   always be exactly one valid starting city.
 * </p>
 * <p>
 *   For the actual problem, you'll be given an array of distances such that city
 *   <span>i</span> is <span>distances[i]</span> away from city <span>i + 1</span>.
 *   Since the cities are connected via a circular road, the last city is connected
 *   to the first city. In other words, the last distance in the
 *   <span>distances</span> array is equal to the distance from the last city to
 *   the first city. You'll also be given an array of fuel available at each city,
 *   where <span>fuel[i]</span> is equal to the fuel available at city
 *   <span>i</span>. The total amount of fuel available (from all cities combined)
 *   is exactly enough to travel to all cities. Your fuel tank always starts out
 *   empty, and you're given a positive integer value for the number of miles that
 *   your car can travel per gallon of fuel (miles per gallon, or MPG). You can
 *   assume that you will always be given at least two cities.
 * </p>
 * <p>Write a function that returns the index of the valid starting city.</p>
 * <h3>Sample Input</h3>
 * <pre><span class="CodeEditor-promptParameter">distances</span> = [5, 25, 15, 10, 15]
 * <span class="CodeEditor-promptParameter">fuel</span> = [1, 2, 1, 0, 3]
 * <span class="CodeEditor-promptParameter">mpg</span> = 10
 * </pre>
 * <h3>Sample Output</h3>
 * <pre>4
 * </pre>
 * </div>
 */
public class ValidStartingCity {
    public static void main(String[] args) {
        int[] distances = new int[] {5, 25, 15, 10, 15};
        int[] fuel = new int[] {1, 2, 1, 0, 3};
        int mpg = 10;
        int expected = 4;
        var actual = new ValidStartingCity().validStartingCity(distances, fuel, mpg);
        System.out.println(expected == actual);
    }

    public int validStartingCity(int[] distances, int[] fuel, int mpg) {
        int numberOfCities = distances.length;
        int milesRemaining = 0;

        int indexOfStartingCityCandidate = 0;
        int milesRemainingAtStartingCityCandiate = 0;

        for (int cityIdx = 1; cityIdx < numberOfCities; cityIdx++) {
            int distanceFromPreviousCity  = distances[cityIdx - 1];
            int fuelFromPreviousCit = fuel[cityIdx - 1];
            milesRemaining += fuelFromPreviousCit * mpg - distanceFromPreviousCity;

            if (milesRemaining < milesRemainingAtStartingCityCandiate) {
                milesRemainingAtStartingCityCandiate = milesRemaining;
                indexOfStartingCityCandidate = cityIdx;
            }
        }
        return indexOfStartingCityCandidate;
    }
}
