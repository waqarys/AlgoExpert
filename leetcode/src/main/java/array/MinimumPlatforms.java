package array;

import java.time.LocalTime;
import java.util.Arrays;
import java.util.List;

public class MinimumPlatforms {
    public static void main(String[] args) {
        Train train1 = new Train("train1", LocalTime.of(8, 00), LocalTime.of(11, 00));
        Train train2 = new Train("train2", LocalTime.of(8, 15), LocalTime.of(9, 00));
        Train train3 = new Train("train3", LocalTime.of(8, 20), LocalTime.of(8, 30));
        Train train4 = new Train("train4", LocalTime.of(8, 25), LocalTime.of(9, 10));
        Train train5 = new Train("train5", LocalTime.of(8, 45), LocalTime.of(8, 55));
        Train train6 = new Train("train6", LocalTime.of(9, 15), LocalTime.of(10, 00));
        Train train7 = new Train("train7", LocalTime.of(9, 30), LocalTime.of(9, 45));

        List<Train> trains = Arrays.asList(train1, train2, train3, train4, train5, train6, train7);
        System.out.println(getPlatforms(trains));
    }
    public static int getPlatforms(List<Train> trains) {
        int n = trains.size();
        LocalTime[] arrivals = new LocalTime[n];
        LocalTime[] departures = new LocalTime[n];

        for (int i = 0; i < n; i++) {
            arrivals[i] = trains.get(i).arrivalTime;
            departures[i] = trains.get(i).departureTime;
        }
        Arrays.sort(departures);

        int platNeeded = 1;
        int output = 1;
        int arrivalIndex = 1;
        int departureIndex = 0;

        while (arrivalIndex < n && departureIndex < n) {

            if(arrivals[arrivalIndex].isBefore(departures[departureIndex])) {
                platNeeded ++;
                arrivalIndex++;
            } else {
                platNeeded--;
                departureIndex++;
            }

            if(platNeeded > output) {
                output = platNeeded;
            }
        }

        return output;
    }

//    private static LocalTime findLatestDeparture(LocalTime[] departures) {
//        Arrays.sort(departures);
//        LocalTime latestDeparture = departures[0];
//        departures = Arrays.copyOfRange(departures, 1, departures.length);
//        return latestDeparture;
//    }
}
