# SystemsExpert · Design Netflix

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Netflix (0:00) — `slides/01.png`

In this lecture we design Netflix. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:12) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Focus on streaming or video delivery, recommendations, or both? How many titles and subscribers? Need to support many device types and bitrates?

## 3. Functional requirements (0:28) — `slides/03.png`

The functional requirements. Browse catalogue, personalised home page. Stream a title with adaptive bitrate. Resume playback across devices.

## 4. Non-functional requirements (0:40) — `slides/04.png`

The non-functional requirements. Very high availability, global low latency. Startup under 2 s, minimal rebuffering.

## 5. Capacity estimates (0:50) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 200M subscribers, about 10k titles; each title encoded in about dozens of bitrate or resolution variants to PB scale. Peak egress tens of Tbps to must be served from edge caches (Open Connect style) close to ISPs.

## 6. High-level architecture (1:10) — `slides/06.png`

Here's the high-level architecture. Device connects to Control plane APIs - cloud and Edge caches inside ISPs and Event stream. Control plane APIs - cloud connects to Catalogue plus user DB and Recommendation service and Device. Studio upload connects to Transcoding pipeline. Transcoding pipeline connects to Origin blob store. Origin blob store connects to Edge caches inside ISPs. Event stream connects to Batch or stream analytics. Batch or stream analytics connects to Recommendation service.

## 7. Data model (1:43) — `slides/07.png`

Here is the data model. titles(id, metadata, encodes ). viewing history(user id, title id, position, updated at) - write-heavy, wide-column store. manifest: per title, list of segment URLs per bitrate.

## 8. API (2:00) — `slides/08.png`

The API. The main endpoints are: GET home; GET titles by id; POST playback by titleId start; POST playback by titleId heartbeat. Each one is small, resource-oriented and easy to version.

## 9. Encoding (2:14) — `slides/09.png`

Deep dive: Encoding. Split source into chunks, transcode in parallel into many codecs or bitrates; segment into about 2-4 s pieces for ABR (DASH or HLS).

## 10. Delivery (2:25) — `slides/10.png`

Deep dive: Delivery. Popular content is pre-positioned at edges during off-peak; clients measure throughput and switch bitrate per segment.

## 11. Recommendations (2:35) — `slides/11.png`

Deep dive: Recommendations. Offline batch training on viewing logs produces candidate lists; online service re-ranks per request.

## 12. Trade-offs & alternatives (2:44) — `slides/12.png`

Finally, the key trade-offs. Own CDN gives control and cost savings but large capex. Pre-positioning wastes some storage on titles that won't be watched. Resume position is eventually consistent (heartbeat every about 10-30 s).

## 13. Recap (3:01) — `slides/13.png`

To recap Netflix: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Device, Control plane APIs - cloud, Catalogue plus user DB, Recommendation service, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
