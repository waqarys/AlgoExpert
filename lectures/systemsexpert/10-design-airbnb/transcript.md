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

## 6. High-level architecture (1:03) — `slides/06.png`

Here's the high-level architecture. Guest connects to API. Host connects to API. API connects to Listings DB and Search index - geo plus filters and Bookings / availability DB and Payments. Listings DB connects to Change data capture. Change data capture connects to Search index - geo plus filters.

## 7. Data model (1:25) — `slides/07.png`

Here is the data model. listings(id, host id, geo, price, attributes). availability(listing id, date, status) PK(listing id, date). bookings(id, listing id, guest id, start, end, status).

## 8. API (1:43) — `slides/08.png`

The API. The main endpoints are: GET search with lat and lng and radius and checkIn and checkOut and guests and priceMax; GET listings by id; POST listings; POST bookings. Each one is small, resource-oriented and easy to version.

## 9. No double booking (1:58) — `slides/09.png`

Deep dive: No double booking. In one transaction, lock the availability rows for the date range (SELECT FOR UPDATE) and mark them reserved; or insert into a table with a unique (listing id, date) constraint. Temporary holds expire if payment fails.

## 10. Search (2:15) — `slides/10.png`

Deep dive: Search. Geo index (geohash or quadtree) in Elasticsearch with date availability filters; results may be slightly stale, so booking re-validates.

## 11. Payments (2:26) — `slides/11.png`

Deep dive: Payments. Authorise at booking, capture after check-in.

## 12. Trade-offs & alternatives (2:32) — `slides/12.png`

Finally, the key trade-offs. Search eventual consistency versus booking strong consistency. Per-date rows are simple; range types or interval trees are more compact.

## 13. Recap (2:44) — `slides/13.png`

To recap Airbnb: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Guest, API, Host, Listings DB, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
