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

## 6. High-level architecture (1:04) — `slides/06.png`

Here's the high-level architecture. Client connects to REST API. REST API connects to Subreddits and Posts and Comments, tree by parent id and Votes PK user,target. Votes PK user,target connects to Score aggregator. Score aggregator connects to Posts.

## 7. Data model (1:23) — `slides/07.png`

Here is the data model. subreddit(id, name, description, created by). post(id, subreddit id, author id, title, body, score, comment count, created at, edited at, deleted at). comment(id, post id, parent id, author id, body, score, ). vote(user id, target id, target type, value in -1,0,1 ).

## 8. API (1:49) — `slides/08.png`

The API. The main endpoints are: GET v1 subreddits by name; GET v1 subreddits by name posts with sort equals hot new top and cursor equals .. and limit equals ..; POST v1 subreddits by name posts; PATCH v1 posts by postId; DELETE v1 posts by postId; GET v1 posts by postId comments with sort equals .. and depth equals .. and cursor equals ..; POST v1 posts by postId comments; PUT v1 posts by postId vote. Each one is small, resource-oriented and easy to version.

## 9. Votes (2:22) — `slides/09.png`

Deep dive: Votes. PUT with an absolute value makes votes idempotent; the aggregator applies (new - old) deltas to cached scores asynchronously.

## 10. Comment trees (2:32) — `slides/10.png`

Deep dive: Comment trees. Fetch top-N roots by score then children to a limited depth; 'load more' via cursor on parent id.

## 11. Pagination (2:41) — `slides/11.png`

Deep dive: Pagination. Opaque cursors (score, id) rather than offsets so lists stay stable while new content arrives.

## 12. Trade-offs & alternatives (2:50) — `slides/12.png`

Finally, the key trade-offs. Soft deletes keep threads intact (' deleted '). Denormalised counts are eventually consistent. PUT for votes versus POST upvote or downvote endpoints: PUT is simpler to make idempotent.

## 13. Recap (3:05) — `slides/13.png`

To recap the Reddit API: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, REST API, Subreddits, Posts, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
