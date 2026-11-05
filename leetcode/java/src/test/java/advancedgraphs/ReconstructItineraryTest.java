package advancedgraphs;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class ReconstructItineraryTest {
    @Test void examples() {
        assertEquals(List.of("JFK", "MUC", "LHR", "SFO", "SJC"), new ReconstructItinerary().findItinerary(List.of(
                List.of("MUC", "LHR"), List.of("JFK", "MUC"), List.of("SFO", "SJC"), List.of("LHR", "SFO"))));
        assertEquals(List.of("JFK", "ATL", "JFK", "SFO", "ATL", "SFO"), new ReconstructItinerary().findItinerary(List.of(
                List.of("JFK", "SFO"), List.of("JFK", "ATL"), List.of("SFO", "ATL"), List.of("ATL", "JFK"), List.of("ATL", "SFO"))));
        assertEquals(List.of("JFK", "NRT", "JFK", "KUL"), new ReconstructItinerary().findItinerary(List.of(
                List.of("JFK", "KUL"), List.of("JFK", "NRT"), List.of("NRT", "JFK"))));
    }
}
