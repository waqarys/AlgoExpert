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

## 6. Capacity: worked out (1:10) — `slides/06.png`

Let's actually work the numbers. Suppose ten million concurrent streams at five megabits a second. That's fifty terabits per second of egress. If one edge appliance serves around a hundred gigabits, we need at least five hundred of them, spread across ISPs. Ten thousand titles with dozens of encodes each puts storage in the petabytes.

## 7. High-level architecture (1:31) — `slides/07.png`

Here's the high-level architecture. Device connects to Control plane APIs - cloud and Edge caches inside ISPs and Event stream. Control plane APIs - cloud connects to Catalogue plus user DB and Recommendation service and Device. Studio upload connects to Transcoding pipeline. Transcoding pipeline connects to Origin blob store. Origin blob store connects to Edge caches inside ISPs. Event stream connects to Batch or stream analytics. Batch or stream analytics connects to Recommendation service.

## 8. Request flow: Press Play (2:05) — `slides/08.png`

Let's follow a play request. The device calls the control plane to start playback for a title.

## 9. Request flow: Press Play (2:12) — `slides/09.png`

The control plane checks the subscription and picks the best edge cache for this user's network, then returns a manifest.

## 10. Request flow: Press Play (2:19) — `slides/10.png`

The device streams video segments directly from an edge cache inside the user's ISP, switching bitrate as bandwidth changes.

## 11. Request flow: Press Play (2:27) — `slides/11.png`

Every few seconds, playback heartbeats go to the event stream, recording position for resume.

## 12. Request flow: Press Play (2:33) — `slides/12.png`

Those events feed analytics and the recommendation models that shape the next home page.

## 13. Data model (2:39) — `slides/13.png`

Here is the data model. The titles record holds id, metadata, encodes . The viewing history record holds user id, title id, position, updated at. - write-heavy, wide-column store. manifest: per title, list of segment URLs per bitrate.

## 14. API (2:58) — `slides/14.png`

The API. The main endpoints are: GET home; GET titles by id; POST playback by titleId start; POST playback by titleId heartbeat. Each one is small, resource-oriented and easy to version.

## 15. Encoding (3:12) — `slides/15.png`

Deep dive: Encoding. Split source into chunks, transcode in parallel into many codecs or bitrates; segment into about 2-4 s pieces for ABR (DASH or HLS).

## 16. Delivery (3:23) — `slides/16.png`

Deep dive: Delivery. Popular content is pre-positioned at edges during off-peak; clients measure throughput and switch bitrate per segment.

## 17. Recommendations (3:33) — `slides/17.png`

Deep dive: Recommendations. Offline batch training on viewing logs produces candidate lists; online service re-ranks per request.

## 18. Key decisions (3:42) — `slides/18.png`

Let's pull together the key decisions. Own CDN inside ISPs, because cost and quality at this egress. Pre-position popular titles off-peak, because cache hits at prime time. Adaptive bitrate segments, because smooth playback on any network. Control plane in cloud, data plane at edge, because each scales independently.

## 19. Trade-offs & alternatives (4:04) — `slides/19.png`

Finally, the key trade-offs. Own CDN gives control and cost savings but large capex. Pre-positioning wastes some storage on titles that won't be watched. Resume position is eventually consistent (heartbeat every about 10-30 s).

## 20. Recap (4:21) — `slides/20.png`

To recap Netflix: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Device, Control plane APIs - cloud, Catalogue plus user DB, Recommendation service, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
