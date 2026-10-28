# Systems Design Fundamentals - study notes

## Interview framework (45-60 min)
1. **Clarify** scope, users, scale, what's out of scope (5 min).
2. **Requirements**: functional + non-functional (latency, availability, consistency, durability).
3. **Estimate**: QPS (avg/peak), storage/year, bandwidth, memory for caches.
4. **High-level design**: clients, LB, stateless services, data stores, async pipelines.
5. **Deep dives** on the 2-3 hardest parts; **trade-offs**; failure modes; evolution.

## Building blocks
| Topic | Key points |
|---|---|
| Client-server, HTTP | Request/response, statelessness, idempotent verbs (GET/PUT/DELETE), status codes |
| Latency numbers | memory ~100 ns, SSD read ~100 µs, same-DC RTT ~0.5 ms, cross-continent ~150 ms |
| Availability | 99.9% ≈ 8.8 h/yr, 99.99% ≈ 53 min/yr; redundancy, no SPOFs, health checks, failover |
| Caching | Cache-aside, write-through, write-back; eviction LRU/LFU; TTLs; stampede protection |
| Proxies & LB | Forward vs reverse proxy; L4 vs L7; round-robin, least-conn, consistent hashing |
| Hashing | Consistent / rendezvous hashing to minimise remapping when nodes change |
| Relational DBs | ACID, indexes (B-tree), isolation levels, read replicas, transactions |
| NoSQL | Key-value, wide-column, document, graph; choose by access pattern |
| Replication & sharding | Leader-follower, multi-leader, leaderless quorum (R+W>N); shard keys, hot spots, resharding |
| Consistency | Strong vs eventual; CAP / PACELC; read-your-writes; leader election (Raft/ZooKeeper/etcd) |
| Messaging | Queues vs pub/sub; Kafka partitions & consumer groups; at-least-once + idempotent consumers |
| Polling vs streaming | Long polling, SSE, WebSockets |
| Rate limiting | Token/leaky bucket, sliding window; per-user/IP; distributed counters in Redis |
| Blob storage & CDN | Object stores for large immutable data; CDN for static/edge caching |
| Logging & monitoring | Structured logs, metrics, traces, SLOs/alerts |
| MapReduce / batch | Offline processing of large datasets; stream processing for near-real-time |
| Security | AuthN/AuthZ, TLS, encryption at rest, least privilege |

## Back-of-envelope cheatsheet
- 1 day ≈ 86,400 s ≈ 10^5 s. 1M req/day ≈ 12 req/s.
- Peak ≈ 2-10x average.
- 1 KB x 1B = 1 TB.
