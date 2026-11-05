package heap;

import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

class TwitterTest {
    @Test void example() {
        Twitter t = new Twitter();
        t.postTweet(1, 5);
        assertEquals(List.of(5), t.getNewsFeed(1));
        t.follow(1, 2);
        t.postTweet(2, 6);
        assertEquals(List.of(6, 5), t.getNewsFeed(1));
        t.unfollow(1, 2);
        assertEquals(List.of(5), t.getNewsFeed(1));
    }
    @Test void onlyTen() {
        Twitter t = new Twitter();
        for (int i = 0; i < 12; i++) t.postTweet(1 + i % 2, i);
        t.follow(1, 2);
        assertEquals(List.of(11, 10, 9, 8, 7, 6, 5, 4, 3, 2), t.getNewsFeed(1));
        t.unfollow(1, 1);
        assertEquals(10, t.getNewsFeed(1).size());
    }
}
