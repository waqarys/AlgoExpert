# SystemsExpert · Design the Twitch API

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design the Twitch API (0:00) — `slides/01.png`

In this lecture we design the Twitch API. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Which parts of the page are in scope: video player, chat, viewer count, follow or subscribe buttons? Logged-in and anonymous viewers? Are there chat moderation features (bans, slow mode, emote-only)? Does the API serve the video itself, or only metadata plus a playback URL?

## 3. Functional requirements (0:37) — `slides/03.png`

The functional requirements. Get stream info for a channel: title, game, live or offline, viewer count, playback URL. Real-time chat: send and receive messages, with moderation. Follow and unfollow a channel; subscribe (paid tiers). Notify followers when a channel goes live.

## 4. Non-functional requirements (0:57) — `slides/04.png`

The non-functional requirements. Chat fan-out to 100k plus viewers in one channel, delivered in under a second. Viewer counts can be approximate and a few seconds stale. Subscriptions and payments must be strongly consistent and idempotent.

## 5. Entities (1:14) — `slides/05.png`

Here are the core entities. The main records are Channel, User, Follow, Subscription, ChatMessage, Ban. Each one maps to a table or a key-value record, keyed so that the hot queries are single lookups.

## 6. API (1:28) — `slides/06.png`

The API. The main endpoints are: GET channels by channelId; GET channels by channelId viewers count; POST channels by channelId follow; DELETE channels by channelId follow; POST channels by channelId subscriptions; DELETE subscriptions by subscriptionId; WS channels by channelId chat; POST channels by channelId bans. Each one is small, resource-oriented and easy to version.

## 7. API (1:51) — `slides/07.png`

Pagination with cursors on list endpoints. Auth with OAuth bearer tokens, scoped per action.

## 8. High-level architecture (1:58) — `slides/08.png`

Here's the high-level architecture. Clients connects to API Gateway / LB. API Gateway / LB connects to Channel and Follow API and Chat WebSocket servers. Chat WebSocket servers connects to Pub or Sub per channel and Chat moderation service. Channel and Follow API connects to SQL: channels, follows, subs and Redis: live state, viewer counts. Stream ingest connects to Event queue. Event queue connects to Notification service.

## 9. Deep dives (2:26) — `slides/09.png`

Let's go deeper on one of the hard parts: Chat fan-out: clients hash to WebSocket servers; each server subscribes to the channel topic it has viewers for. A message is published once and each server pushes to its local sockets. For huge channels, batch messages every about 100 ms and sample or rate-limit sending. Moderation: check bans and slow mode before publishing (cache them in Redis). Deletions are published as moderation events so clients remove messages. Viewer count: each WS or edge server reports per-channel counts every few seconds; an aggregator sums them into Redis. Show approximate values. Go-live notifications: an ingest event goes onto a queue; workers page through followers and send push or email in batches. Large channels take minutes, which is acceptable. Subscriptions: require an idempotency key, call the payment provider, write the subscription in a transaction, then emit an event (badge in chat, emote unlock). Video: the API returns only a signed CDN playlist URL (HLS); the video bytes never go through this API.

## 10. Trade-offs (3:31) — `slides/10.png`

Finally, the key trade-offs. WebSockets versus long polling for chat: WS gives lower latency and less overhead. Chat is persisted asynchronously (log or queue to storage). The live path doesn't wait on the database. Viewer counts are eventually consistent; payments are strongly consistent.

## 11. Recap (3:52) — `slides/11.png`

To recap the Twitch API: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Clients, API Gateway / LB, Channel and Follow API, Chat WebSocket servers, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
