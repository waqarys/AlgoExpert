# SystemsExpert · Fundamentals 4/4

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Fundamentals 4/4 (0:00) — `slides/01.png`

Design fundamentals, part 4 of 4. We'll cover Rate limiting, Logging and monitoring, Publish or subscribe pattern, MapReduce, Security and HTTPS, and API design.

## 2. 19. Rate limiting (0:11) — `slides/02.png`

Rate limiting. Token bucket, leaky bucket, fixed or sliding window. per user or IP or region. a shared store such as Redis. DoS protection.

## 3. 20. Logging and monitoring (0:25) — `slides/03.png`

Logging and monitoring. Structured logs, metrics (time-series), dashboards, alerts on SLOs, tracing.

## 4. 21. Publish/subscribe pattern (0:33) — `slides/04.png`

Publish or subscribe pattern. Topics, publishers, subscribers. at-least-once delivery means idempotent consumers. ordering per partition. Kafka, Pub or Sub.

## 5. 22. MapReduce (0:47) — `slides/05.png`

MapReduce. Map to shuffle to reduce over a distributed file system. idempotent tasks. data stays where it is and the code moves to it.

## 6. 23. Security and HTTPS (0:59) — `slides/06.png`

Security and HTTPS. Symmetric or asymmetric encryption, TLS handshake, certificates and CAs, MITM.

## 7. 24. API design (1:09) — `slides/07.png`

API design. Resource-oriented REST or RPC or GraphQL. pagination, versioning, idempotency keys, rate limits, clear errors.

## 8. Recap (1:20) — `slides/08.png`

To recap this part: Rate limiting; Logging and monitoring; Publish or subscribe pattern; MapReduce; Security and HTTPS; API design. Each of these shows up again in the design walkthroughs.
