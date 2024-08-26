package array;

import java.time.LocalTime;

public class Train {
    public LocalTime arrivalTime;
    public LocalTime departureTime;

    public Train(String train1, LocalTime arrivalTime, LocalTime departureTime) {
        this.arrivalTime = arrivalTime;
        this.departureTime = departureTime;
    }
}
