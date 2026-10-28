# SystemsExpert · Fundamentals 3/4

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Fundamentals 3/4 (0:00) — `slides/01.png`

Design fundamentals, part 3 of 4. We'll cover Specialized storage paradigms, Replication and sharding, Leader election, Peer-to-peer networks, Polling and streaming, and Configuration.

## 2. 13. Specialized storage paradigms (0:12) — `slides/02.png`

Specialized storage paradigms. Blob storage (S3 or GCS), time-series DBs (InfluxDB, Prometheus), graph DBs (Neo4j), spatial indexes (quadtrees, geohash).

## 3. 14. Replication and sharding (0:25) — `slides/03.png`

Replication and sharding. Sync versus async replicas. sharding by range, hash or region. hot spots. resharding with consistent hashing.

## 4. 15. Leader election (0:38) — `slides/04.png`

Leader election. One leader handles writes or jobs. consensus via Paxos or Raft. in practice use ZooKeeper or etcd leases.

## 5. 16. Peer-to-peer networks (0:50) — `slides/05.png`

Peer-to-peer networks. Split a large file into chunks shared between peers (BitTorrent). gossip protocols. DHT for peer discovery.

## 6. 17. Polling and streaming (1:01) — `slides/06.png`

Polling and streaming. Polling at intervals versus a long-lived connection (WebSockets or SSE). streaming suits chat and live data.

## 7. 18. Configuration (1:12) — `slides/07.png`

Configuration. Static (deployed with the code, reviewed) versus dynamic (a config service, instant but riskier).

## 8. Recap (1:21) — `slides/08.png`

To recap this part: Specialized storage paradigms; Replication and sharding; Leader election; Peer-to-peer networks; Polling and streaming; Configuration. Each of these shows up again in the design walkthroughs.
