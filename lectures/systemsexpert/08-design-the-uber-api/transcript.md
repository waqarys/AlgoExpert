# SystemsExpert · Design the Uber API

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design the Uber API (0:00) — `slides/01.png`

In this lecture we design the Uber API. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Rider and driver APIs both? Payments in scope? Real-time location updates required?

## 3. Functional requirements (0:26) — `slides/03.png`

The functional requirements. Rider: request ride, see ETA or driver location, cancel, rate. Driver: go online or offline, accept ride, update location, complete trip.

## 4. Non-functional requirements (0:39) — `slides/04.png`

The non-functional requirements. Real-time updates (about seconds). Idempotent state transitions.

## 5. Capacity estimates (0:47) — `slides/05.png`

Now some rough capacity estimates, which drive the design. Drivers send location every about 4 s; about 1M active drivers to about 250k writes per s to the location service.

## 6. Capacity: worked out (0:59) — `slides/06.png`

Let's actually work the numbers. A million active drivers each send their location every four seconds. That's two hundred fifty thousand location writes a second. We keep only the latest position per driver in memory, about a hundred bytes each. That's only a hundred megabytes total, but the write rate means we shard by geographic cell.

## 7. High-level architecture (1:21) — `slides/07.png`

Here's the high-level architecture. Rider connects to API. Driver connects to API. API connects to Trips: state machine and Location service - geo index and Matching service and Push / websocket gateway. Matching service connects to Location service - geo index.

## 8. Request flow: Request a ride (1:40) — `slides/08.png`

Let's follow a ride request. The rider sends pickup and destination, and gets back a trip in the requested state.

## 9. Request flow: Request a ride (1:48) — `slides/09.png`

The API creates the trip record, which is a state machine starting at requested.

## 10. Request flow: Request a ride (1:54) — `slides/10.png`

The matching service asks the location service for available drivers near the pickup point.

## 11. Request flow: Request a ride (2:00) — `slides/11.png`

The location service, a geo index over recent driver positions, returns the closest candidates.

## 12. Request flow: Request a ride (2:06) — `slides/12.png`

The best driver gets an offer over a websocket, with a timeout.

## 13. Request flow: Request a ride (2:11) — `slides/13.png`

When the driver accepts, the trip moves to accepted atomically, and the rider is notified.

## 14. Data model (2:17) — `slides/14.png`

Here is the data model. Trip tripId, riderId, driverId?, status: REQUESTED ACCEPTED ARRIVED IN PROGRESS COMPLETED CANCELLED, pickup, dropoff, fare. DriverStatus driverId, online, location, tripId?

## 15. API (2:33) — `slides/15.png`

The API. The main endpoints are: POST trips; GET trips by tripId; POST trips by tripId cancel; POST trips by tripId rating; PUT drivers me status; PUT drivers me location; POST trips by tripId accept; POST trips by tripId arrive. Each one is small, resource-oriented and easy to version.

## 16. State machine (2:53) — `slides/16.png`

Deep dive: State machine. Every transition is validated server-side (for example accept only from REQUESTED) with optimistic concurrency, so double taps or two drivers accepting resolve deterministically.

## 17. Location (3:06) — `slides/17.png`

Deep dive: Location. Updates go to an in-memory geo index (geohash or S2 cells) sharded by region; matching queries nearby cells.

## 18. Push vs poll (3:16) — `slides/18.png`

Deep dive: Push versus poll. Websocket for live location; polling fallback.

## 19. Key decisions (3:23) — `slides/19.png`

Let's pull together the key decisions. In-memory geo index, because write rate too high for a DB. Trip as a state machine, because no double assignment. WebSockets for drivers, because low-latency offers. Shard by city / geo cell, because locality of matching.

## 20. Trade-offs & alternatives (3:42) — `slides/20.png`

Finally, the key trade-offs. Separate endpoints per transition are explicit and auditable versus a generic PATCH status. In-memory geo index trades durability for speed (locations are ephemeral anyway).

## 21. Recap (3:56) — `slides/21.png`

To recap the Uber API: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Rider, API, Driver, Trips, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
