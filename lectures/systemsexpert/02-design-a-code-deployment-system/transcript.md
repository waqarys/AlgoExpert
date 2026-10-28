# SystemsExpert · Design a Code-Deployment System

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design a Code-Deployment System (0:00) — `slides/01.png`

In this lecture we design a Code-Deployment System. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Build plus deploy, or deploy only? How many machines or regions; how big are binaries? How fast must a deploy reach every machine? Do we need rollbacks and canary or gradual rollouts?

## 3. Functional requirements (0:32) — `slides/03.png`

The functional requirements. Trigger a build for a commit SHA. Store build artifacts. Deploy a chosen build to all hosts (global) with progress. Roll back to a previous build.

## 4. Non-functional requirements (0:46) — `slides/04.png`

The non-functional requirements. Builds take minutes but must never be lost or run twice. Deploy to hundreds of thousands of hosts in under about 30 min. Highly available control plane.

## 5. Capacity estimates (0:59) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about thousands of builds per day; artifacts up to about 10 GB. about 100k-1M hosts across about 10 regions. Fan-out: 10 GB x 1M hosts is impossible from one store to regional replication plus peer-to-peer distribution.

## 6. High-level architecture (1:20) — `slides/06.png`

Here's the high-level architecture. Engineer / CI trigger connects to Deploy API. Deploy API connects to Jobs table: SQL queue and Goal state: desired build per service. Jobs table: SQL queue connects to Build workers. Build workers connects to Global blob store. Global blob store connects to Regional blob replicas. Regional blob replicas connects to Peer-to-peer distribution in each region. Hosts' agents connects to Goal state: desired build per service and Peer-to-peer distribution in each region.

## 7. Data model (1:54) — `slides/07.png`

Here is the data model. jobs(id, sha, status QUEUED,RUNNING,SUCCEEDED,FAILED , worker id, heartbeat at, created at). builds(sha, artifact url, size, checksum, regions replicated ). deployments(id, service, sha, strategy, status, started at). goal state key or value: service to sha (strongly consistent store, for example etcd or ZooKeeper).

## 8. API (2:20) — `slides/08.png`

The API. The main endpoints are: POST builds; GET builds by sha; POST deployments; GET deployments by id; POST deployments by id rollback. Each one is small, resource-oriented and easy to version.

## 9. Queue as a SQL table (2:34) — `slides/09.png`

Deep dive: Queue as a SQL table. Workers dequeue with UPDATE SET status equals 'RUNNING', worker id equals ? WHERE id equals (SELECT FOR UPDATE SKIP LOCKED). ACID guarantees each job runs once. Workers heartbeat; a reaper resets stale RUNNING jobs.

## 10. Artifact distribution (2:53) — `slides/10.png`

Deep dive: Artifact distribution. Build writes to a global store, async replicated to regional stores; deploy only proceeds once all target regions have the artifact. Within a region hosts fetch pieces from each other (BitTorrent-like) to avoid hot-spotting.

## 11. Goal state (3:09) — `slides/11.png`

Deep dive: Goal state. Deploy just flips the desired sha in a consistent KV store; host agents watch it, download, swap, and report health. Rollback equals set goal to previous sha.

## 12. Trade-offs & alternatives (3:22) — `slides/12.png`

Finally, the key trade-offs. SQL queue versus Kafka: SQL gives exactly-once claim semantics with modest throughput, which is enough. P2P adds complexity but removes a bandwidth bottleneck. Canary stages slow deploys down but limit blast radius.

## 13. Recap (3:40) — `slides/13.png`

To recap a Code-Deployment System: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Engineer / CI trigger, Deploy API, Jobs table, Build workers, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
