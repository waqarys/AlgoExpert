# SystemsExpert · Design Tinder

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Tinder (0:00) — `slides/01.png`

In this lecture we design Tinder. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:12) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Profiles, swiping, matches, chat - which are in scope? How are recommendations generated?

## 3. Functional requirements (0:24) — `slides/03.png`

The functional requirements. Create or update profile and preferences. Get a deck of candidate profiles. Swipe left or right; mutual right swipe creates a match. List matches; message matches.

## 4. Non-functional requirements (0:40) — `slides/04.png`

The non-functional requirements. Deck loads quickly; swipes never lost. Match created exactly once.

## 5. Capacity estimates (0:48) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 50M DAU x about 100 swipes per day about 60k swipes per s peak.

## 6. High-level architecture (0:58) — `slides/06.png`

Here's the high-level architecture. App connects to API. API connects to Profiles and Deck service - geo plus prefs plus ranking and Swipes PK swiper, swipee and Messaging service. Swipes PK swiper, swipee connects to Match detector. Match detector connects to Matches.

## 7. Data model (1:18) — `slides/07.png`

Here is the data model. profile(user id, name, photos, bio, geo, prefs). swipe(swiper id, swipee id, decision, ts). match(id, user a, user b, created at) unique(min,max).

## 8. API (1:35) — `slides/08.png`

The API. The main endpoints are: GET v1 profile,; GET v1 deck with limit equals 50; POST v1 swipes; GET v1 matches with cursor; POST v1 matches by id messages; GET v1 matches by id messages with cursor. Each one is small, resource-oriented and easy to version.

## 9. Match detection (1:54) — `slides/09.png`

Deep dive: Match detection. On LIKE, check whether the reverse LIKE exists; insert the match with a unique constraint on the ordered pair so concurrent likes create one match.

## 10. Deck (2:05) — `slides/10.png`

Deep dive: Deck. Precompute decks in the background per user; exclude already-swiped profiles with a bloom filter.

## 11. Trade-offs & alternatives (2:13) — `slides/11.png`

Finally, the key trade-offs. Synchronous match check gives instant 'It's a match!' at slightly higher write latency. Precomputed decks may be slightly stale.

## 12. Recap (2:24) — `slides/12.png`

To recap Tinder: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around App, API, Profiles, Deck service - geo plus prefs plus ranking, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
