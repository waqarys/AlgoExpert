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

## 6. High-level architecture (1:11) — `slides/06.png`

Here's the high-level architecture. Client connects to API. API connects to Post service and Feed service. Post service connects to Posts DB sharded by post id and Post-created stream. Post-created stream connects to Fan-out workers. Fan-out workers connects to Feed cache: user to post ids. Feed service connects to Feed cache: user to post ids and Ranking service and Posts DB sharded by post id. Social graph connects to Fan-out workers.

## 7. Data model (1:43) — `slides/07.png`

Here is the data model. posts(id, author id, body, media urls, created at). edges(user id, friend id). feed cache: user id to list of (post id, score) capped about 500.

## 8. API (1:59) — `slides/08.png`

The API. The main endpoints are: POST posts; GET feed with cursor equals and limit equals 20. Each one is small, resource-oriented and easy to version.

## 9. Fan-out on write vs read (2:10) — `slides/09.png`

Deep dive: Fan-out on write versus read. Push post ids into followers' precomputed feeds for normal users (fast reads). For celebrities ( over about 10k followers) skip fan-out and merge their recent posts at read time - hybrid model.

## 10. Ranking (2:26) — `slides/10.png`

Deep dive: Ranking. Feed service fetches candidate ids, hydrates posts in batch, scores with a model (affinity, recency, engagement) and paginates with a stable cursor.

## 11. Storage (2:38) — `slides/11.png`

Deep dive: Storage. Posts in a sharded KV or SQL store; media in blob store plus CDN; feed cache in Redis or Memcache clusters sharded by user id, rebuildable from source.

## 12. Trade-offs & alternatives (2:50) — `slides/12.png`

Finally, the key trade-offs. Precomputed feeds use a lot of memory but give low latency. Hybrid fan-out adds read-time merge complexity. Eventual consistency means your own post may appear slightly late - write-through to your own feed fixes it.

## 13. Recap (3:07) — `slides/13.png`

To recap Facebook News Feed: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, API, Post service, Posts DB sharded by post id, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
