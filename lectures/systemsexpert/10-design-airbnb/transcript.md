# SystemsExpert · Design Airbnb

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Airbnb (0:00) — `slides/01.png`

In this lecture we design Airbnb. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Search plus booking plus host listing management in scope? Payments? Can two guests book overlapping dates? (No). Scale of listings?

## 3. Functional requirements (0:30) — `slides/03.png`

The functional requirements. Hosts create listings with availability. Guests search by location or dates or price. Guests book; double booking impossible.

## 4. Non-functional requirements (0:42) — `slides/04.png`

The non-functional requirements. Search fast ( under 300 ms). Booking strongly consistent.

## 5. Capacity estimates (0:51) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 10M listings, about 100M searches per day (about 1.2k per s), about 1M bookings per day.

## 6. Capacity: worked out (1:03) — `slides/06.png`

Let's actually work the numbers. A hundred million searches a day is about twelve hundred a second. Around three and a half thousand at peak, served by the search index. A million bookings a day is only about twelve a second. So searches dominate load, while bookings must simply be correct.

## 7. High-level architecture (1:22) — `slides/07.png`

Here's the high-level architecture. Guest connects to API. Host connects to API. API connects to Listings DB and Search index - geo plus filters and Bookings / availability DB and Payments. Listings DB connects to Change data capture. Change data capture connects to Search index - geo plus filters.

## 8. Request flow: Book a stay (1:44) — `slides/08.png`

Let's follow a booking. The guest searches a city and dates.

## 9. Request flow: Book a stay (1:50) — `slides/09.png`

Search runs against a geo and filter index, built from the listings database through change data capture.

## 10. Request flow: Book a stay (1:57) — `slides/10.png`

The guest picks a listing and submits a booking with an idempotency key.

## 11. Request flow: Book a stay (2:01) — `slides/11.png`

The bookings service reserves the dates in a transaction, with a constraint that prevents overlapping bookings.

## 12. Request flow: Book a stay (2:08) — `slides/12.png`

Payment is authorised. If it fails, the hold on the dates is released.

## 13. Request flow: Book a stay (2:14) — `slides/13.png`

The booking is confirmed and the host is notified.

## 14. Data model (2:18) — `slides/14.png`

Here is the data model. The listings record holds id, host id, geo, price, attributes. The availability record holds listing id, date, status) PK(listing id, date. The bookings record holds id, listing id, guest id, start, end, status.

## 15. API (2:38) — `slides/15.png`

The API. The main endpoints are: GET search with lat and lng and radius and checkIn and checkOut and guests and priceMax; GET listings by id; POST listings; POST bookings. Each one is small, resource-oriented and easy to version.

## 16. No double booking (2:53) — `slides/16.png`

Deep dive: no double booking. In a single transaction, we lock the availability rows for the requested dates, with a select for update, and mark them reserved. An alternative is a unique constraint on listing and date, so a second insert for the same night simply fails. Temporary holds expire if payment doesn't go through.

## 17. Search (3:13) — `slides/17.png`

Deep dive: Search. Geo index (geohash or quadtree) in Elasticsearch with date availability filters; results may be slightly stale, so booking re-validates.

## 18. Payments (3:24) — `slides/18.png`

Deep dive: Payments. Authorise at booking, capture after check-in.

## 19. Key decisions (3:30) — `slides/19.png`

Let's pull together the key decisions. Separate search index (CDC), because fast geo and filter queries. DB constraint on date overlap, because no double booking. Search can be slightly stale, because availability rechecked at booking. Idempotent booking requests, because safe retries.

## 20. Trade-offs & alternatives (3:51) — `slides/20.png`

Finally, the key trade-offs. Search eventual consistency versus booking strong consistency. Per-date rows are simple; range types or interval trees are more compact.

## 21. Recap (4:03) — `slides/21.png`

To recap Airbnb: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Guest, API, Host, Listings DB, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
