# Systems Design Fundamentals - study notes

My own notes following the 25-lesson SystemsExpert fundamentals syllabus (topic list checked against the public course outline).

## Interview framework (45-60 min)
1. Clarify the scope and the users. 2. Functional and non-functional requirements. 3. Rough estimates.
4. Entities and API. 5. High-level diagram. 6. Deep dives on bottlenecks. 7. Trade-offs and failure modes.

## Topics (course order)
| # | Topic | Key points |
|---|---|---|
| 1 | What are design fundamentals? | Four pillars: the basis (networking, storage), the key characteristics (availability, latency, throughput, redundancy, consistency), the components (LBs, caches, proxies, DBs), the tech (Kafka, Redis, S3...). |
| 2 | Client–server model | DNS resolves to an IP; the client opens a connection to the server's port; the server listens. HTTP runs on 80, HTTPS on 443. |
| 3 | Network protocols | IP packets, TCP (ordered, reliable, handshake), UDP (fast, lossy), HTTP request/response on top of TCP. |
| 4 | Storage | Memory versus disk; persistence; databases are just servers that write to disk. |
| 5 | Latency and throughput | Latency = time per operation (memory ~µs, SSD ~100 µs, cross-continent ~150 ms). Throughput = operations per second. Improve them separately. |
| 6 | Availability | Nines (99.99% ≈ 52 min a year). SLA vs SLO. Redundancy, no single point of failure, passive/active failover. |
| 7 | Caching | Client, server, CDN, DB caches. Write-through vs write-back; eviction policies LRU/LFU; staleness and invalidation. |
| 8 | Proxies | Forward proxy (acts for the client) vs reverse proxy (acts for the server: LB, TLS termination, caching). Nginx. |
| 9 | Load balancers | Round robin, weighted, least-connections, IP/consistent hashing; health checks; L4 vs L7. |
| 10 | Hashing | Consistent hashing and rendezvous hashing keep remapping small when servers join or leave. |
| 11 | Relational databases | SQL, ACID transactions, indexes (B-trees), strong consistency, joins. |
| 12 | Key-value stores | Simple get/put, very fast, flexible; Redis (memory), DynamoDB, etcd/ZooKeeper (strongly consistent config). |
| 13 | Specialized storage paradigms | Blob storage (S3/GCS), time-series DBs (InfluxDB, Prometheus), graph DBs (Neo4j), spatial indexes (quadtrees, geohash). |
| 14 | Replication and sharding | Sync vs async replicas; sharding by range, hash or region; hot spots; resharding with consistent hashing. |
| 15 | Leader election | One leader handles writes/jobs; consensus via Paxos/Raft; in practice use ZooKeeper/etcd leases. |
| 16 | Peer-to-peer networks | Split a large file into chunks shared between peers (BitTorrent); gossip protocols; DHT for peer discovery. |
| 17 | Polling and streaming | Polling at intervals vs a long-lived connection (WebSockets/SSE); streaming suits chat and live data. |
| 18 | Configuration | Static (deployed with the code, reviewed) vs dynamic (a config service, instant but riskier). |
| 19 | Rate limiting | Token bucket, leaky bucket, fixed/sliding window; per user/IP/region; a shared store such as Redis; DoS protection. |
| 20 | Logging and monitoring | Structured logs, metrics (time-series), dashboards, alerts on SLOs, tracing. |
| 21 | Publish/subscribe pattern | Topics, publishers, subscribers; at-least-once delivery means idempotent consumers; ordering per partition; Kafka, Pub/Sub. |
| 22 | MapReduce | Map → shuffle → reduce over a distributed file system; idempotent tasks; data stays where it is and the code moves to it. |
| 23 | Security and HTTPS | Symmetric/asymmetric encryption, TLS handshake, certificates and CAs, MITM. |
| 24 | API design | Resource-oriented REST or RPC/GraphQL; pagination, versioning, idempotency keys, rate limits, clear errors. |

## Back-of-envelope cheatsheet
- 1 day ≈ 86,400 s ≈ 10^5 s; 1M requests/day ≈ 12 QPS; peak ≈ 2–3× the average.
- Character 1 B; tweet-size text ~300 B; photo ~200 KB–2 MB; 1 min of HD video ~50–100 MB.
- One server handles ~10k concurrent connections and ~1k–10k simple QPS; Redis does ~100k ops/s.
- A disk sequential read is ~100× faster than random; reading 1 MB from memory takes ~250 µs, from SSD ~1 ms.
