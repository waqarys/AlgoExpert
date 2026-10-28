# SystemsExpert · Design Slack

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Slack (0:00) — `slides/01.png`

In this lecture we design Slack. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:12) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Channels and DMs? Threads, reactions, file uploads? Max workspace size? Must messages sync across devices with unread counts?

## 3. Functional requirements (0:29) — `slides/03.png`

The functional requirements. Send or receive messages in channels and DMs in real time. Load message history with pagination. Unread indicators and mentions. Workspaces or organisations.

## 4. Non-functional requirements (0:44) — `slides/04.png`

The non-functional requirements. Messages delivered in under about 500 ms. No message loss; ordering per channel. Large orgs (100k members) supported.

## 5. Capacity estimates (0:56) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 10M DAU, about 100 messages per user per day to about 1B messages per day about 12k per s avg. Messages about 1 KB to about 1 TB per day.

## 6. Capacity: worked out (1:11) — `slides/06.png`

Let's actually work the numbers. Ten million daily users sending a hundred messages each is a billion messages a day. That's about twelve thousand messages a second, maybe thirty-five thousand at peak. At a kilobyte each that's a terabyte a day, over three hundred terabytes a year. If each message reaches about ten online members, gateways push around three hundred fifty thousand messages a second.

## 7. High-level architecture (1:35) — `slides/07.png`

Here's the high-level architecture. Client connects to Gateway servers and REST API. REST API connects to Messages DB sharded by channel id and Pub or Sub by channel and Read state: user, channel, last read ts and Search index. Pub or Sub by channel connects to Gateway servers.

## 8. Request flow: Send a message (1:54) — `slides/08.png`

Let's follow a message. The client sends it with a client message ID, so retries can be de-duplicated.

## 9. Request flow: Send a message (2:01) — `slides/09.png`

The API checks channel membership and writes the message.

## 10. Request flow: Send a message (2:06) — `slides/10.png`

It's stored in the shard for that channel, with a server timestamp that orders messages in the channel.

## 11. Request flow: Send a message (2:12) — `slides/11.png`

The API publishes the message to the channel's pub-sub topic.

## 12. Request flow: Send a message (2:17) — `slides/12.png`

Gateway servers holding websocket connections for channel members receive it and push it instantly.

## 13. Request flow: Send a message (2:23) — `slides/13.png`

Each member's read state determines unread badges, updated when they view the channel.

## 14. Data model (2:29) — `slides/14.png`

Here is the data model. The channels record holds id, workspace id, name, type. The memberships record holds channel id, user id. The messages record holds channel id, ts, author id, body, thread ts) PK(channel id, ts. The read state record holds user id, channel id, last read ts.

## 15. API (2:52) — `slides/15.png`

The API. The main endpoints are: POST channels by id messages; GET channels by id messages with before equals ts and limit equals 50; POST channels by id read; WS events:. Each one is small, resource-oriented and easy to version.

## 16. Real-time fan-out (3:08) — `slides/16.png`

Deep dive: Real-time fan-out. Gateways subscribe to channels their connected users belong to; a message is persisted first, then published; gateways push to sockets. Very large channels fan out through hierarchical pub or sub.

## 17. Ordering (3:23) — `slides/17.png`

Deep dive: Ordering. Server-assigned ts per channel (monotonic per shard); client dedupes with clientMsgId.

## 18. Unreads (3:31) — `slides/18.png`

Deep dive: Unreads. Compare channel latest ts with read state; computed on connect and kept live by events.

## 19. Key decisions (3:39) — `slides/19.png`

Let's pull together the key decisions. Shard messages by channel, because channel reads stay on one shard. WebSocket gateways plus pub or sub, because real-time delivery. Server timestamps per channel, because consistent ordering. Client message IDs, because dedupe on retry.

## 20. Trade-offs & alternatives (3:59) — `slides/20.png`

Finally, the key trade-offs. Sharding by channel keeps history queries local; huge workspaces need channel-level partitioning. Persist-then-publish adds a few ms but guarantees no lost messages.

## 21. Recap (4:13) — `slides/21.png`

To recap Slack: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, Gateway servers, REST API, Messages DB sharded by channel id, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
