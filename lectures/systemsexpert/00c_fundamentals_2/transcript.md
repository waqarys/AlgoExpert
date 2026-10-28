# SystemsExpert · Fundamentals 2/4

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Fundamentals 2/4 (0:00) — `slides/01.png`

Design fundamentals, part 2 of 4. We'll cover Caching, Proxies, Load balancers, Hashing, Relational databases, and Key-value stores.

## 2. 7. Caching (0:10) — `slides/02.png`

Caching. Client, server, CDN, DB caches. Write-through versus write-back. eviction policies LRU or LFU. staleness and invalidation.

## 3. 8. Proxies (0:24) — `slides/03.png`

Proxies. Forward proxy (acts for the client) versus reverse proxy (acts for the server: LB, TLS termination, caching). Nginx.

## 4. 9. Load balancers (0:35) — `slides/04.png`

Load balancers. Round robin, weighted, least-connections, IP or consistent hashing. health checks. L4 versus L7.

## 5. 10. Hashing (0:46) — `slides/05.png`

Hashing. Consistent hashing and rendezvous hashing keep remapping small when servers join or leave.

## 6. 11. Relational databases (0:54) — `slides/06.png`

Relational databases. SQL, ACID transactions, indexes (B-trees), strong consistency, joins.

## 7. 12. Key-value stores (1:02) — `slides/07.png`

Key-value stores. Simple get or put, very fast, flexible. Redis (memory), DynamoDB, etcd or ZooKeeper (strongly consistent config).

## 8. Recap (1:14) — `slides/08.png`

To recap this part: Caching; Proxies; Load balancers; Hashing; Relational databases; Key-value stores. Each of these shows up again in the design walkthroughs.
