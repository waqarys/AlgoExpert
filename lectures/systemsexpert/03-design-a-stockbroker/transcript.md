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

## 6. High-level architecture (1:11) — `slides/06.png`

Here's the high-level architecture. App connects to API gateway. API gateway connects to Order service. Order service connects to Orders plus ledger DB, sharded by user and Outbound order queue and Push notifications / websocket. Outbound order queue connects to Exchange connector. Exchange connector connects to Exchange and Fills queue. Fills queue connects to Order service.

## 7. Data model (1:37) — `slides/07.png`

Here is the data model. orders(id, user id, idempotency key, symbol, side, type, qty, limit price, status, exchange order id). ledger entries(id, user id, amount, currency, reason, order id) - append-only, balance equals sum. positions(user id, symbol, qty) derived from fills.

## 8. API (2:00) — `slides/08.png`

The API. The main endpoints are: POST orders; DELETE orders by id; GET orders with status equals open; GET portfolio. Each one is small, resource-oriented and easy to version.

## 9. Exactly-once order placement (2:13) — `slides/09.png`

Deep dive: Exactly-once order placement. Client sends an idempotency key; order row is written (status PENDING) in the same transaction that reserves buying power. A connector picks PENDING orders, sends them with our client order id so retries are deduplicated by the exchange.

## 10. Fills (2:31) — `slides/10.png`

Deep dive: Fills. The exchange streams executions; connector writes them to a durable queue; order service applies them idempotently (keyed by execution id) updating order status, ledger and positions in one transaction.

## 11. Scaling (2:45) — `slides/11.png`

Deep dive: Scaling. Shard by user id; exchange connectors partitioned by symbol range; keep hot reads (portfolio) in a cache invalidated by fills.

## 12. Trade-offs & alternatives (2:56) — `slides/12.png`

Finally, the key trade-offs. Strong consistency on money paths over availability. Queue between us and the exchange decouples bursts but adds latency (ms). Ledger versus mutable balance: ledger is auditable; cache the sum.

## 13. Recap (3:13) — `slides/13.png`

To recap a Stockbroker: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around App, API gateway, Order service, Orders plus ledger DB, sharded by user, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
