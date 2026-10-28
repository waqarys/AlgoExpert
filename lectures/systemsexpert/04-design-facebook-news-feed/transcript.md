# SystemsExpert · Design Facebook News Feed

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Facebook News Feed (0:00) — `slides/01.png`

In this lecture we design Facebook News Feed. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Ranked or chronological? Text only or media too? Friends only, or pages or groups? How fresh must the feed be?

## 3. Functional requirements (0:28) — `slides/03.png`

The functional requirements. Create posts. See a feed of friends' posts. Like or comment counts on posts.

## 4. Non-functional requirements (0:38) — `slides/04.png`

The non-functional requirements. Feed load p95 under 500 ms. Eventual consistency acceptable (seconds). Billions of users, highly available.

## 5. Capacity estimates (0:50) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 2B users, about 1B DAU, each opens feed about 10x per day to about 100k feed reads per s avg, about 300k peak. about 500M posts per day to about 6k writes per s. Average about 500 friends; celebrities millions of followers.

## 6. Capacity: worked out (1:11) — `slides/06.png`

Let's actually work the numbers. A billion daily users each opening the feed ten times is ten billion reads a day. That's about a hundred fifteen thousand reads a second, and around three hundred fifty thousand at peak. Five hundred million posts a day is about six thousand writes a second. Fanning each out to five hundred friends means about three million cache writes a second, which is why celebrities are handled differently.

## 7. High-level architecture (1:36) — `slides/07.png`

Here's the high-level architecture. Client connects to API. API connects to Post service and Feed service. Post service connects to Posts DB sharded by post id and Post-created stream. Post-created stream connects to Fan-out workers. Fan-out workers connects to Feed cache: user to post ids. Feed service connects to Feed cache: user to post ids and Ranking service and Posts DB sharded by post id. Social graph connects to Fan-out workers.

## 8. Request flow: Open the feed (2:07) — `slides/08.png`

Let's follow a feed load. The user opens the app and requests the first page of the feed.

## 9. Request flow: Open the feed (2:14) — `slides/09.png`

The API authenticates and calls the feed service.

## 10. Request flow: Open the feed (2:18) — `slides/10.png`

The feed service reads the user's precomputed list of post IDs from the feed cache, built earlier by fan-out workers.

## 11. Request flow: Open the feed (2:26) — `slides/11.png`

The cache returns a few hundred candidate post IDs. Posts from celebrities are pulled at read time instead and merged in.

## 12. Request flow: Open the feed (2:34) — `slides/12.png`

The ranking service scores the candidates for this user, using engagement predictions and freshness.

## 13. Request flow: Open the feed (2:41) — `slides/13.png`

Finally we hydrate the top posts with their content from the posts store and return the page.

## 14. Data model (2:47) — `slides/14.png`

Here is the data model. The posts record holds id, author id, body, media urls, created at. The edges record holds user id, friend id. feed cache: user id to list of (post id, score) capped about 500.

## 15. API (3:04) — `slides/15.png`

The API. The main endpoints are: POST posts; GET feed with cursor equals and limit equals 20. Each one is small, resource-oriented and easy to version.

## 16. Fan-out on write vs read (3:16) — `slides/16.png`

Deep dive: Fan-out on write versus read. Push post ids into followers' precomputed feeds for normal users (fast reads). For celebrities ( over about 10k followers) skip fan-out and merge their recent posts at read time - hybrid model.

## 17. Ranking (3:31) — `slides/17.png`

Deep dive: Ranking. Feed service fetches candidate ids, hydrates posts in batch, scores with a model (affinity, recency, engagement) and paginates with a stable cursor.

## 18. Storage (3:43) — `slides/18.png`

Deep dive: Storage. Posts in a sharded KV or SQL store; media in blob store plus CDN; feed cache in Redis or Memcache clusters sharded by user id, rebuildable from source.

## 19. Key decisions (3:55) — `slides/19.png`

Let's pull together the key decisions. Fan-out on write for most users, because fast reads. Fan-out on read for celebrities, because avoids millions of writes per post. Feed cache stores IDs only, because small, cheap to update. Separate ranking service, because iterate on models independently.

## 20. Trade-offs & alternatives (4:16) — `slides/20.png`

Finally, the key trade-offs. Precomputed feeds use a lot of memory but give low latency. Hybrid fan-out adds read-time merge complexity. Eventual consistency means your own post may appear slightly late - write-through to your own feed fixes it.

## 21. Recap (4:32) — `slides/21.png`

To recap Facebook News Feed: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, API, Post service, Posts DB sharded by post id, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
