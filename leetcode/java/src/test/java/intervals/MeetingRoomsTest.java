package intervals;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MeetingRoomsTest {
    MeetingRooms s = new MeetingRooms();
    @Test void examples() {
        assertFalse(s.canAttendMeetings(new int[][]{{0, 30}, {5, 10}, {15, 20}}));
        assertTrue(s.canAttendMeetings(new int[][]{{7, 10}, {2, 4}}));
        assertTrue(s.canAttendMeetings(new int[][]{{5, 10}, {10, 15}}));
        assertTrue(s.canAttendMeetings(new int[][]{}));
    }
}
