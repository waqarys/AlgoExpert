# SystemsExpert · Design a Stockbroker

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design a Stockbroker (0:00) — `slides/01.png`

In this lecture we design a Stockbroker. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Do we run the exchange or route orders to one? Order types (market, limit), and is trading only during market hours? How many users and orders per day? Need real-time price feeds in the app?

## 3. Functional requirements (0:31) — `slides/03.png`

The functional requirements. Place, cancel and view orders. See balances and positions. Order status updates when filled.

## 4. Non-functional requirements (0:42) — `slides/04.png`

The non-functional requirements. Never lose or duplicate an order; balances must be correct. Low latency to the exchange. Highly available during market hours.

## 5. Capacity estimates (0:55) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 10M users, about 20M orders per day, peaks at open or close about 2k orders per s. Each order about 1 KB to tiny storage; correctness dominates design.

## 6. Capacity: worked out (1:11) — `slides/06.png`

Let's actually work the numbers. Twenty million orders a day divided by eighty-six thousand seconds is about two hundred thirty orders a second. Activity spikes about ten times at the open and close, so design for two thousand orders a second. At a kilobyte each that's only about twenty gigabytes a day. Storage is trivial; the real challenge is correctness and never double-spending.

## 7. High-level architecture (1:35) — `slides/07.png`

Here's the high-level architecture. App connects to API gateway. API gateway connects to Order service. Order service connects to Orders plus ledger DB, sharded by user and Outbound order queue and Push notifications / websocket. Outbound order queue connects to Exchange connector. Exchange connector connects to Exchange and Fills queue. Fills queue connects to Order service.

## 8. Request flow: Place a buy order (2:01) — `slides/08.png`

Let's follow a buy order. The user taps buy for ten shares, and the app sends the order with an idempotency key.

## 9. Request flow: Place a buy order (2:10) — `slides/09.png`

The gateway authenticates the user and routes the request to the order service.

## 10. Request flow: Place a buy order (2:15) — `slides/10.png`

The order service checks buying power and, in one transaction, writes the order and reserves the cash in the ledger.

## 11. Request flow: Place a buy order (2:22) — `slides/11.png`

The order goes onto a durable outbound queue, so nothing is lost if the connector restarts.

## 12. Request flow: Place a buy order (2:28) — `slides/12.png`

The exchange connector sends it to the exchange and receives acknowledgements and fills.

## 13. Request flow: Place a buy order (2:34) — `slides/13.png`

Fills flow back through a queue to the order service, which updates the position and ledger, and the user gets a push notification.

## 14. Data model (2:41) — `slides/14.png`

Here is the data model. The orders record holds id, user id, idempotency key, symbol, side, type, qty, limit price, status, exchange order id. The ledger entries record holds id, user id, amount, currency, reason, order id. - append-only, balance equals sum. The positions record holds user id, symbol, qty. derived from fills.

## 15. API (3:07) — `slides/15.png`

The API. The main endpoints are: POST orders; DELETE orders by id; GET orders with status equals open; GET portfolio. Each one is small, resource-oriented and easy to version.

## 16. Exactly-once order placement (3:20) — `slides/16.png`

Deep dive: Exactly-once order placement. Client sends an idempotency key; order row is written (status PENDING) in the same transaction that reserves buying power. A connector picks PENDING orders, sends them with our client order id so retries are deduplicated by the exchange.

## 17. Fills (3:38) — `slides/17.png`

Deep dive: Fills. The exchange streams executions; connector writes them to a durable queue; order service applies them idempotently (keyed by execution id) updating order status, ledger and positions in one transaction.

## 18. Scaling (3:52) — `slides/18.png`

Deep dive: Scaling. Shard by user id; exchange connectors partitioned by symbol range; keep hot reads (portfolio) in a cache invalidated by fills.

## 19. Key decisions (4:03) — `slides/19.png`

Let's pull together the key decisions. Ledger with double-entry, because auditable, never lose money. Idempotency keys, because safe client retries. Queues around the exchange, because decouple from exchange outages. Shard by user, because keeps a user's orders in one place.

## 20. Trade-offs & alternatives (4:23) — `slides/20.png`

Finally, the key trade-offs. Strong consistency on money paths over availability. Queue between us and the exchange decouples bursts but adds latency (ms). Ledger versus mutable balance: ledger is auditable; cache the sum.

## 21. Recap (4:39) — `slides/21.png`

To recap a Stockbroker: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around App, API gateway, Order service, Orders plus ledger DB, sharded by user, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
