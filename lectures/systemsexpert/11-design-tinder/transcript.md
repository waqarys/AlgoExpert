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

## 6. Capacity: worked out (0:58) — `slides/06.png`

Let's actually work the numbers. Fifty million daily users swiping a hundred times each is five billion swipes a day. That's about fifty-eight thousand swipes a second on average. At around twenty bytes per row that's a hundred gigabytes a day. Partition by swiper, and the reverse lookup is a direct key read.

## 7. High-level architecture (1:19) — `slides/07.png`

Here's the high-level architecture. App connects to API. API connects to Profiles and Deck service - geo plus prefs plus ranking and Swipes PK swiper, swipee and Messaging service. Swipes PK swiper, swipee connects to Match detector. Match detector connects to Matches.

## 8. Request flow: Swipe right (1:38) — `slides/08.png`

Let's follow a right swipe. The app sends the swipe for the profile shown.

## 9. Request flow: Swipe right (1:44) — `slides/09.png`

The API records the swipe.

## 10. Request flow: Swipe right (1:48) — `slides/10.png`

It writes a row keyed by swiper and swipee, which makes the write idempotent.

## 11. Request flow: Swipe right (1:53) — `slides/11.png`

The match detector looks up the reverse row: did the other person already swipe right on this user?

## 12. Request flow: Swipe right (1:59) — `slides/12.png`

If so, it creates a match record exactly once.

## 13. Request flow: Swipe right (2:03) — `slides/13.png`

Both users are notified, and the messaging service opens a conversation.

## 14. Data model (2:09) — `slides/14.png`

Here is the data model. The profile record holds user id, name, photos, bio, geo, prefs. The swipe record holds swiper id, swipee id, decision, ts. The match record holds id, user a, user b, created at) unique(min,max.

## 15. API (2:27) — `slides/15.png`

The API. The main endpoints are: GET v1 profile,; GET v1 deck with limit equals 50; POST v1 swipes; GET v1 matches with cursor; POST v1 matches by id messages; GET v1 matches by id messages with cursor. Each one is small, resource-oriented and easy to version.

## 16. Match detection (2:46) — `slides/16.png`

Deep dive: Match detection. On LIKE, check whether the reverse LIKE exists; insert the match with a unique constraint on the ordered pair so concurrent likes create one match.

## 17. Deck (2:57) — `slides/17.png`

Deep dive: Deck. Precompute decks in the background per user; exclude already-swiped profiles with a bloom filter.

## 18. Key decisions (3:05) — `slides/18.png`

Let's pull together the key decisions. Precompute decks, because instant swiping. Swipe key (swiper, swipee), because O(1) match check. Geo plus preference filters first, because small candidate sets. Separate messaging service, because scales on its own.

## 19. Trade-offs & alternatives (3:24) — `slides/19.png`

Finally, the key trade-offs. Synchronous match check gives instant 'It's a match!' at slightly higher write latency. Precomputed decks may be slightly stale.

## 20. Recap (3:35) — `slides/20.png`

To recap Tinder: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around App, API, Profiles, Deck service - geo plus prefs plus ranking, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
