package heap;

import java.util.*;

/**
 * LC 355 Design Twitter.
 * Approach: per-user tweet lists + k-way merge with a max-heap on timestamp for the feed.
 * Feed O(F + 10 log F).
 */
public class Twitter {
    private int clock = 0;
    private final Map<Integer, List<int[]>> tweets = new HashMap<>(); // {time, id}
    private final Map<Integer, Set<Integer>> follows = new HashMap<>();

    public void postTweet(int userId, int tweetId) {
        tweets.computeIfAbsent(userId, k -> new ArrayList<>()).add(new int[]{clock++, tweetId});
    }

    public List<Integer> getNewsFeed(int userId) {
        // heap entries: {time, tweetId, user, index}
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        Set<Integer> users = new HashSet<>(follows.getOrDefault(userId, Set.of()));
        users.add(userId);
        for (int u : users) {
            List<int[]> l = tweets.get(u);
            if (l != null && !l.isEmpty()) {
                int i = l.size() - 1;
                pq.add(new int[]{l.get(i)[0], l.get(i)[1], u, i});
            }
        }
        List<Integer> feed = new ArrayList<>();
        while (!pq.isEmpty() && feed.size() < 10) {
            int[] e = pq.poll();
            feed.add(e[1]);
            if (e[3] > 0) {
                int[] prev = tweets.get(e[2]).get(e[3] - 1);
                pq.add(new int[]{prev[0], prev[1], e[2], e[3] - 1});
            }
        }
        return feed;
    }

    public void follow(int followerId, int followeeId) {
        if (followerId != followeeId) follows.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        Set<Integer> s = follows.get(followerId);
        if (s != null) s.remove(followeeId);
    }
}
