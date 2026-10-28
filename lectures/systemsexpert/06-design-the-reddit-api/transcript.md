# SystemsExpert · Design the Reddit API

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design the Reddit API (0:00) — `slides/01.png`

In this lecture we design the Reddit API. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Which entities: subreddits, posts, comments, votes, awards? Is this about API shape more than infrastructure? Pagination and sorting requirements?

## 3. Functional requirements (0:29) — `slides/03.png`

The functional requirements. Subreddits: create, get, list posts. Posts: create, edit, delete, vote. Comments: threaded create or edit or delete or vote. Sorting: hot, new, top.

## 4. Non-functional requirements (0:46) — `slides/04.png`

The non-functional requirements. Consistent, versioned, paginated REST resources. Idempotent votes.

## 5. Capacity estimates (0:55) — `slides/05.png`

Now some rough capacity estimates, which drive the design. Read-heavy (about 100:1); vote writes are the hottest write path.

## 6. Capacity: worked out (1:04) — `slides/06.png`

Let's actually work the numbers. Reddit is read-heavy, roughly a hundred reads for every write. Assume fifty million daily users casting twenty votes each: a billion votes a day. That's about twelve thousand vote writes a second. Batching deltas per post turns thousands of updates on a hot post into about one write a second.

## 7. High-level architecture (1:25) — `slides/07.png`

Here's the high-level architecture. Client connects to REST API. REST API connects to Subreddits and Posts and Comments, tree by parent id and Votes PK user,target. Votes PK user,target connects to Score aggregator. Score aggregator connects to Posts.

## 8. Request flow: Upvote a post (1:44) — `slides/08.png`

Let's follow an upvote. The client sends a PUT that sets this user's vote on the post to plus one.

## 9. Request flow: Upvote a post (1:51) — `slides/09.png`

The API authenticates the user and validates the target.

## 10. Request flow: Upvote a post (1:56) — `slides/10.png`

It upserts a row keyed by user and target, so repeating the request is harmless and a user can only vote once.

## 11. Request flow: Upvote a post (2:03) — `slides/11.png`

A score aggregator consumes vote changes and batches the deltas, so a viral post doesn't turn into a write hotspot.

## 12. Request flow: Upvote a post (2:11) — `slides/12.png`

The post's score is updated, and listings ranked by hot or top pick it up shortly after.

## 13. Data model (2:17) — `slides/13.png`

Here is the data model. The subreddit record holds id, name, description, created by. The post record holds id, subreddit id, author id, title, body, score, comment count, created at, edited at, deleted at. The comment record holds id, post id, parent id, author id, body, score, . The vote record holds user id, target id, target type, value in -1,0,1 .

## 14. API (2:45) — `slides/14.png`

The API. The main endpoints are: GET v1 subreddits by name; GET v1 subreddits by name posts with sort equals hot new top and cursor equals .. and limit equals ..; POST v1 subreddits by name posts; PATCH v1 posts by postId; DELETE v1 posts by postId; GET v1 posts by postId comments with sort equals .. and depth equals .. and cursor equals ..; POST v1 posts by postId comments; PUT v1 posts by postId vote. Each one is small, resource-oriented and easy to version.

## 15. Votes (3:17) — `slides/15.png`

Deep dive: Votes. PUT with an absolute value makes votes idempotent; the aggregator applies (new - old) deltas to cached scores asynchronously.

## 16. Comment trees (3:27) — `slides/16.png`

Deep dive: Comment trees. Fetch top-N roots by score then children to a limited depth; 'load more' via cursor on parent id.

## 17. Pagination (3:36) — `slides/17.png`

Deep dive: Pagination. Opaque cursors (score, id) rather than offsets so lists stay stable while new content arrives.

## 18. Key decisions (3:45) — `slides/18.png`

Let's pull together the key decisions. PUT vote (idempotent), because safe retries, one vote per user. Cursor pagination, because stable under inserts. Async score aggregation, because avoids hot-row contention. Comments by parent id, because simple tree loading.

## 19. Trade-offs & alternatives (4:05) — `slides/19.png`

Finally, the key trade-offs. Soft deletes keep threads intact (' deleted '). Denormalised counts are eventually consistent. PUT for votes versus POST upvote or downvote endpoints: PUT is simpler to make idempotent.

## 20. Recap (4:20) — `slides/20.png`

To recap the Reddit API: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, REST API, Subreddits, Posts, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
