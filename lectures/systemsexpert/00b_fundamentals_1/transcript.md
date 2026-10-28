# SystemsExpert · Fundamentals 1/4

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Fundamentals 1/4 (0:00) — `slides/01.png`

Design fundamentals, part 1 of 4. We'll cover What are design fundamentals?, Client–server model, Network protocols, Storage, Latency and throughput, and Availability.

## 2. 1. What are design fundamentals? (0:11) — `slides/02.png`

What are design fundamentals?. Four pillars: the basis (networking, storage), the key characteristics (availability, latency, throughput, redundancy, consistency), the components (LBs, caches, proxies, DBs), the tech (Kafka, Redis, S3 ).

## 3. 2. Client–server model (0:29) — `slides/03.png`

Client–server model. DNS resolves to an IP. the client opens a connection to the server's port. the server listens. HTTP runs on 80, HTTPS on 443.

## 4. 3. Network protocols (0:44) — `slides/04.png`

Network protocols. IP packets, TCP (ordered, reliable, handshake), UDP (fast, lossy), HTTP request or response on top of TCP.

## 5. 4. Storage (0:56) — `slides/05.png`

Storage. Memory versus disk. persistence. databases are just servers that write to disk.

## 6. 5. Latency and throughput (1:05) — `slides/06.png`

Latency and throughput. Latency equals time per operation (memory about µs, SSD about 100 µs, cross-continent about 150 ms). Throughput equals operations per second. Improve them separately.

## 7. 6. Availability (1:21) — `slides/07.png`

Availability. Nines (99.99 percent about 52 min a year). SLA versus SLO. Redundancy, no single point of failure, passive or active failover.

## 8. Recap (1:35) — `slides/08.png`

To recap this part: What are design fundamentals?; Client–server model; Network protocols; Storage; Latency and throughput; Availability. Each of these shows up again in the design walkthroughs.
