# SystemsExpert · Design Amazon

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Amazon (0:00) — `slides/01.png`

In this lecture we design Amazon. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:12) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Catalog browsing, cart, checkout, inventory, orders? Flash sales / hot items?

## 3. Functional requirements (0:24) — `slides/03.png`

The functional requirements. Browse or search products. Cart management. Checkout with payment and inventory reservation. Order history.

## 4. Non-functional requirements (0:37) — `slides/04.png`

The non-functional requirements. Never oversell; never double charge. Browsing highly available.

## 5. Capacity estimates (0:45) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 100M DAU, about 10M orders per day (about 120 per s avg, 10x at peaks).

## 6. High-level architecture (0:57) — `slides/06.png`

Here's the high-level architecture. U connects to API. API connects to Catalog plus search and Cart store and Checkout orchestrator. Checkout orchestrator connects to Inventory and Payments and Orders. Orders connects to Fulfilment events.

## 7. Data model (1:14) — `slides/07.png`

Here is the data model. inventory(sku, warehouse, available, reserved). orders(id, user id, items, status, payment id, idempotency key).

## 8. API (1:27) — `slides/08.png`

The API. The main endpoints are: POST cart items; POST checkout; GET orders by id. Each one is small, resource-oriented and easy to version.

## 9. Saga (1:38) — `slides/09.png`

Deep dive: Saga. Reserve inventory to authorise payment to create order to capture; on failure run compensations (release reservation, void auth).

## 10. Hot items (1:48) — `slides/10.png`

Deep dive: Hot items. Shard inventory counters; for flash sales use a token queue to admit buyers.

## 11. Trade-offs & alternatives (1:56) — `slides/11.png`

Finally, the key trade-offs. Saga versus 2PC: saga is available and scalable at the cost of temporary inconsistency. Reservations with TTL avoid inventory lockup.

## 12. Recap (2:09) — `slides/12.png`

To recap Amazon: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around U, API, Catalog plus search, Cart store, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
