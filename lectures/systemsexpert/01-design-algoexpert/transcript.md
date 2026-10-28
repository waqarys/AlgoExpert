# SystemsExpert · Design AlgoExpert

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design AlgoExpert (0:00) — `slides/01.png`

In this lecture we design AlgoExpert. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Which parts are in scope: browsing questions, the code editor, running code, user progress, payments? How many languages must code execution support? Global audience or one region? Latency targets for 'Run Code'? Is static content (prompts, video) mostly read-only and edited by a small team?

## 3. Functional requirements (0:38) — `slides/03.png`

The functional requirements. List questions with per-user completion status. View a question (prompt, hints, video walkthrough). Write code in the browser, autosave it per language. Run code against test cases and see results. Track progress across devices.

## 4. Non-functional requirements (0:58) — `slides/04.png`

The non-functional requirements. about 99.9 percent availability for browsing; code execution can degrade gracefully. Run-code p95 under about 3 s. No loss of saved user code. Strong isolation of untrusted code.

## 5. Capacity estimates (1:16) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 1M users, about 10k concurrent at peak; about 200 questions. Static content about few hundred MB excl. video to CDN. Autosave every few seconds while typing: about 10k writes per s peak to debounce client-side to about 1 or 10s to about 1k writes per s. Code runs: about 1-2k per min peak; each needs about 1-2 s of sandbox CPU to about 50 concurrent sandboxes, provision headroom x3.

## 6. Capacity: worked out (1:46) — `slides/06.png`

Let's actually work the numbers. Ten thousand concurrent users saving every second would be ten thousand writes a second. Debouncing on the client to one save every ten seconds cuts that to about a thousand writes a second, easy for one Postgres primary. Code runs peak around two thousand a minute, about thirty-three a second. Each takes about one and a half seconds, so roughly fifty sandboxes are busy at once. With three times headroom for spikes, we provision about one hundred and fifty sandbox slots.

## 7. High-level architecture (2:17) — `slides/07.png`

Here's the high-level architecture. Browser connects to CDN: static site, prompts, video and Load balancer. Load balancer connects to API servers - stateless. API servers - stateless connects to Postgres: users, progress, saved code and Redis: question list, sessions and Run queue and Payments provider. Run queue connects to Sandbox workers per language. Sandbox workers per language connects to API servers - stateless.

## 8. Request flow: Run Code (2:45) — `slides/08.png`

Let's follow one Run Code click. The browser sends the user's code and the question ID in a single POST.

## 9. Request flow: Run Code (2:53) — `slides/09.png`

The load balancer forwards it to any healthy API server. Because API servers are stateless, any one will do.

## 10. Request flow: Run Code (3:01) — `slides/10.png`

The API server checks the session, rate-limits the user, and puts a run job on the queue instead of executing anything itself.

## 11. Request flow: Run Code (3:09) — `slides/11.png`

The job waits in the queue for that language. The queue absorbs bursts, so a spike in runs never overloads the API tier.

## 12. Request flow: Run Code (3:17) — `slides/12.png`

A sandbox worker picks up the job, compiles the code in an isolated container with CPU and memory limits, and runs the test cases.

## 13. Request flow: Run Code (3:26) — `slides/13.png`

Results flow back to the API server, which returns them to the browser, typically within two or three seconds.

## 14. Data model (3:33) — `slides/14.png`

Here is the data model. The questions record holds id, name, difficulty, category, prompt md, tests json, version. The users record holds id, email, plan, created at. The user code record holds user id, question id, language, code, updated at) PK(user id, question id, language. The completions record holds user id, question id, completed at.

## 15. API (4:00) — `slides/15.png`

The API. The main endpoints are: GET questions; GET questions by id; PUT questions by id code by language; POST questions by id run; GET runs by runId. Each one is small, resource-oriented and easy to version.

## 16. Code execution (4:15) — `slides/16.png`

Deep dive: Code execution. Untrusted code runs in per-language container pools (gVisor or Firecracker style isolation), no network, CPU or memory or time limits. Keep warm containers to avoid cold starts; route by language via the queue. Results are pushed back (websocket) or polled.

## 17. Autosave (4:35) — `slides/17.png`

Deep dive: Autosave. Client debounces and sends deltas; server does last-write-wins keyed by (user, question, language) with updated at. Local storage keeps a copy for offline edits.

## 18. Global latency (4:49) — `slides/18.png`

Deep dive: Global latency. Static assets on a CDN; API in 2-3 regions with a primary DB and read replicas; sandbox fleets in each region so run latency stays low.

## 19. Key decisions (5:01) — `slides/19.png`

Let's pull together the key decisions. CDN for prompts and videos, because content is read-only and global. Queue in front of sandboxes, because absorbs bursts, isolates failures. Containers per run with hard limits, because untrusted code must never touch the host. Client-side debounce, because 10× fewer writes, no lost work.

## 20. Trade-offs & alternatives (5:23) — `slides/20.png`

Finally, the key trade-offs. Polling versus websockets for run results: polling is simpler and fine at this scale. Single relational DB is enough at this size; shard by user id later if needed. Pre-warmed sandboxes cost money but are what keeps p95 low.

## 21. Recap (5:42) — `slides/21.png`

To recap AlgoExpert: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Browser, CDN, Load balancer, API servers - stateless, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
