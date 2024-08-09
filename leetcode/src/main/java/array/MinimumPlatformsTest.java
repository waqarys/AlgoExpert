package array;

import java.time.LocalTime;
import java.util.Arrays;

public class MinimumPlatformsTest {
    public static void main(String[] args) {
        MinimumPlatformsTest test = new MinimumPlatformsTest();
        test.testSingleTrain();
        test.testNoOverlap();
        test.testOverlap();
        test.testMultipleOverlaps();
        test.testComplexCase();
    }

    public void testSingleTrain() {
        Train[] trains = {
                new Train("", LocalTime.of(9, 0), LocalTime.of(9, 10))
        };
        int platforms = MinimumPlatforms.getPlatforms(Arrays.asList(trains));
        System.out.println(1 == platforms);
    }

    public void testNoOverlap() {
        Train[] trains = {
                new Train("", LocalTime.of(9, 0), LocalTime.of(9, 10)),
                new Train("", LocalTime.of(9, 20), LocalTime.of(9, 30)),
                new Train("", LocalTime.of(9, 40), LocalTime.of(9, 50))
        };
        int platforms = MinimumPlatforms.getPlatforms(Arrays.asList(trains));
        System.out.println(1 == platforms);
    }

    public void testOverlap() {
        Train[] trains = {
                new Train("", LocalTime.of(9, 0), LocalTime.of(9, 10)),
                new Train("", LocalTime.of(9, 5), LocalTime.of(9, 15)),
                new Train("", LocalTime.of(9, 10), LocalTime.of(9, 20))
        };
        int platforms = MinimumPlatforms.getPlatforms(Arrays.asList(trains));
        System.out.println(2 == platforms);
    }

    public void testMultipleOverlaps() {
        Train[] trains = {
                new Train("", LocalTime.of(9, 0), LocalTime.of(9, 10)),
                new Train("", LocalTime.of(9, 5), LocalTime.of(9, 15)),
                new Train("", LocalTime.of(9, 10), LocalTime.of(9, 20)),
                new Train("", LocalTime.of(9, 15), LocalTime.of(9, 25))
        };
        int platforms = MinimumPlatforms.getPlatforms(Arrays.asList(trains));
        System.out.println(2 == platforms);
    }

    public void testComplexCase() {
        Train[] trains = {
                new Train("", LocalTime.of(9, 0), LocalTime.of(9, 10)),
                new Train("", LocalTime.of(9, 40), LocalTime.of(12, 0)),
                new Train("", LocalTime.of(9, 50), LocalTime.of(11, 20)),
                new Train("", LocalTime.of(11, 0), LocalTime.of(11, 30)),
                new Train("", LocalTime.of(15, 0), LocalTime.of(19, 0)),
                new Train("", LocalTime.of(18, 0), LocalTime.of(20, 0))
        };

        int platforms = MinimumPlatforms.getPlatforms(Arrays.asList(trains));
        System.out.println(3 == platforms);
    }
}
