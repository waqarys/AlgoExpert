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

## 6. Capacity: worked out (0:57) — `slides/06.png`

Let's actually work the numbers. Ten million orders a day is about a hundred twenty a second. Big sale events push that ten times, to about twelve hundred a second. A hundred million daily users viewing twenty pages each is around twenty-three thousand reads a second. Catalogue reads are cached aggressively, while checkout writes must be exact.

## 7. High-level architecture (1:19) — `slides/07.png`

Here's the high-level architecture. U connects to API. API connects to Catalog plus search and Cart store and Checkout orchestrator. Checkout orchestrator connects to Inventory and Payments and Orders. Orders connects to Fulfilment events.

## 8. Request flow: Check out (1:36) — `slides/08.png`

Let's follow a checkout. The user clicks place order on their cart.

## 9. Request flow: Check out (1:41) — `slides/09.png`

The checkout orchestrator starts a saga, a sequence of steps each with a compensating action.

## 10. Request flow: Check out (1:48) — `slides/10.png`

First it reserves inventory for each item, with a short expiry.

## 11. Request flow: Check out (1:53) — `slides/11.png`

Next it charges the payment method with an idempotency key. If payment fails, the inventory reservation is released.

## 12. Request flow: Check out (2:01) — `slides/12.png`

Then the order is written in a confirmed state.

## 13. Request flow: Check out (2:05) — `slides/13.png`

Finally an event kicks off fulfilment, picking, packing and shipping.

## 14. Data model (2:10) — `slides/14.png`

Here is the data model. The inventory record holds sku, warehouse, available, reserved. The orders record holds id, user id, items, status, payment id, idempotency key.

## 15. API (2:24) — `slides/15.png`

The API. The main endpoints are: POST cart items; POST checkout; GET orders by id. Each one is small, resource-oriented and easy to version.

## 16. Saga (2:35) — `slides/16.png`

Deep dive: Saga. Reserve inventory to authorise payment to create order to capture; on failure run compensations (release reservation, void auth).

## 17. Hot items (2:45) — `slides/17.png`

Deep dive: Hot items. Shard inventory counters; for flash sales use a token queue to admit buyers.

## 18. Key decisions (2:53) — `slides/18.png`

Let's pull together the key decisions. Saga, not a distributed transaction, because services stay independent. Reserve inventory with expiry, because no oversell, no stuck stock. Idempotent payments, because safe retries. Event-driven fulfilment, because decoupled and scalable.

## 19. Trade-offs & alternatives (3:14) — `slides/19.png`

Finally, the key trade-offs. Saga versus 2PC: saga is available and scalable at the cost of temporary inconsistency. Reservations with TTL avoid inventory lockup.

## 20. Recap (3:27) — `slides/20.png`

To recap Amazon: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around U, API, Catalog plus search, Cart store, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
