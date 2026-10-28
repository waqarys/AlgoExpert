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

## 6. High-level architecture (1:11) — `slides/06.png`

Here's the high-level architecture. Client connects to Gateway servers and REST API. REST API connects to Messages DB sharded by channel id and Pub or Sub by channel and Read state: user, channel, last read ts and Search index. Pub or Sub by channel connects to Gateway servers.

## 7. Data model (1:29) — `slides/07.png`

Here is the data model. channels(id, workspace id, name, type). memberships(channel id, user id). messages(channel id, ts, author id, body, thread ts) PK(channel id, ts). read state(user id, channel id, last read ts).

## 8. API (1:50) — `slides/08.png`

The API. The main endpoints are: POST channels by id messages; GET channels by id messages with before equals ts and limit equals 50; POST channels by id read; WS events:. Each one is small, resource-oriented and easy to version.

## 9. Real-time fan-out (2:06) — `slides/09.png`

Deep dive: Real-time fan-out. Gateways subscribe to channels their connected users belong to; a message is persisted first, then published; gateways push to sockets. Very large channels fan out through hierarchical pub or sub.

## 10. Ordering (2:21) — `slides/10.png`

Deep dive: Ordering. Server-assigned ts per channel (monotonic per shard); client dedupes with clientMsgId.

## 11. Unreads (2:30) — `slides/11.png`

Deep dive: Unreads. Compare channel latest ts with read state; computed on connect and kept live by events.

## 12. Trade-offs & alternatives (2:38) — `slides/12.png`

Finally, the key trade-offs. Sharding by channel keeps history queries local; huge workspaces need channel-level partitioning. Persist-then-publish adds a few ms but guarantees no lost messages.

## 13. Recap (2:51) — `slides/13.png`

To recap Slack: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, Gateway servers, REST API, Messages DB sharded by channel id, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
