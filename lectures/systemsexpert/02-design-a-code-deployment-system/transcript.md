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

## 6. Capacity: worked out (1:20) — `slides/06.png`

Let's actually work the numbers. A ten gigabyte artifact sent to a hundred thousand hosts is a petabyte of transfer. Even one store pushing a hundred gigabits a second would need about twenty-two hours. With regional replicas and peer-to-peer sharing, every host also uploads, so total bandwidth scales with the fleet. That's how we get the whole fleet updated in under thirty minutes.

## 7. High-level architecture (1:43) — `slides/07.png`

Here's the high-level architecture. Engineer / CI trigger connects to Deploy API. Deploy API connects to Jobs table: SQL queue and Goal state: desired build per service. Jobs table: SQL queue connects to Build workers. Build workers connects to Global blob store. Global blob store connects to Regional blob replicas. Regional blob replicas connects to Peer-to-peer distribution in each region. Hosts' agents connects to Goal state: desired build per service and Peer-to-peer distribution in each region.

## 8. Request flow: Deploy build X (2:17) — `slides/08.png`

Let's follow a deploy. An engineer asks to deploy build X of a service.

## 9. Request flow: Deploy build X (2:24) — `slides/09.png`

The deploy API checks the build exists and has been replicated to every target region, then records the deployment.

## 10. Request flow: Deploy build X (2:31) — `slides/10.png`

The key move: it simply updates the goal state, the desired build for the service, in a strongly consistent key-value store.

## 11. Request flow: Deploy build X (2:38) — `slides/11.png`

Agent processes on every host watch that key, so they notice the change within seconds.

## 12. Request flow: Deploy build X (2:44) — `slides/12.png`

Each host downloads the artifact in chunks, mostly from peers in its own region, so no single store becomes a bottleneck.

## 13. Request flow: Deploy build X (2:52) — `slides/13.png`

The agent swaps the binary, runs health checks, and reports back. Rolling back just means setting the goal state to the previous build.

## 14. Data model (3:01) — `slides/14.png`

Here is the data model. The jobs record holds id, sha, status QUEUED,RUNNING,SUCCEEDED,FAILED , worker id, heartbeat at, created at. The builds record holds sha, artifact url, size, checksum, regions replicated . The deployments record holds id, service, sha, strategy, status, started at. goal state key or value: service to sha (strongly consistent store, for example etcd or ZooKeeper).

## 15. API (3:29) — `slides/15.png`

The API. The main endpoints are: POST builds; GET builds by sha; POST deployments; GET deployments by id; POST deployments by id rollback. Each one is small, resource-oriented and easy to version.

## 16. Queue as a SQL table (3:43) — `slides/16.png`

Deep dive: the build queue is just a SQL table. A worker claims a job by updating its status to running inside a transaction, selecting the next queued row with FOR UPDATE SKIP LOCKED, so two workers can never grab the same job. Workers send heartbeats, and a reaper resets any running job whose heartbeat goes stale.

## 17. Artifact distribution (4:02) — `slides/17.png`

Deep dive: Artifact distribution. Build writes to a global store, async replicated to regional stores; deploy only proceeds once all target regions have the artifact. Within a region hosts fetch pieces from each other (BitTorrent-like) to avoid hot-spotting.

## 18. Goal state (4:19) — `slides/18.png`

Deep dive: Goal state. Deploy just flips the desired sha in a consistent KV store; host agents watch it, download, swap, and report health. Rollback equals set goal to previous sha.

## 19. Key decisions (4:31) — `slides/19.png`

Let's pull together the key decisions. SQL table as the build queue, because exactly-once claims via row locks. Goal state, not push commands, because idempotent, easy rollback. Regional replicas plus P2P, because removes the bandwidth bottleneck. Canary stages, because limits blast radius.

## 20. Trade-offs & alternatives (4:53) — `slides/20.png`

Finally, the key trade-offs. SQL queue versus Kafka: SQL gives exactly-once claim semantics with modest throughput, which is enough. P2P adds complexity but removes a bandwidth bottleneck. Canary stages slow deploys down but limit blast radius.

## 21. Recap (5:10) — `slides/21.png`

To recap a Code-Deployment System: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Engineer / CI trigger, Deploy API, Jobs table, Build workers, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
