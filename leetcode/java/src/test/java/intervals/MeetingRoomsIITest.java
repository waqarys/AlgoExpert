package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MeetingRoomsIITest {
    MeetingRoomsII s = new MeetingRoomsII();
    @Test void examples() {
        assertEquals(2, s.minMeetingRooms(new int[][]{{0, 30}, {5, 10}, {15, 20}}));
        assertEquals(1, s.minMeetingRooms(new int[][]{{7, 10}, {2, 4}}));
        assertEquals(3, s.minMeetingRooms(new int[][]{{1, 5}, {2, 6}, {3, 7}}));
        assertEquals(0, s.minMeetingRooms(new int[][]{}));
    }
}
