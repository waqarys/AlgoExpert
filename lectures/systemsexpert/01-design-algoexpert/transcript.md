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

## 6. High-level architecture (1:46) — `slides/06.png`

Here's the high-level architecture. Browser connects to CDN: static site, prompts, video and Load balancer. Load balancer connects to API servers - stateless. API servers - stateless connects to Postgres: users, progress, saved code and Redis: question list, sessions and Run queue and Payments provider. Run queue connects to Sandbox workers per language. Sandbox workers per language connects to API servers - stateless.

## 7. Data model (2:15) — `slides/07.png`

Here is the data model. questions(id, name, difficulty, category, prompt md, tests json, version). users(id, email, plan, created at). user code(user id, question id, language, code, updated at) PK(user id, question id, language). completions(user id, question id, completed at).

## 8. API (2:40) — `slides/08.png`

The API. The main endpoints are: GET questions; GET questions by id; PUT questions by id code by language; POST questions by id run; GET runs by runId. Each one is small, resource-oriented and easy to version.

## 9. Code execution (2:55) — `slides/09.png`

Deep dive: Code execution. Untrusted code runs in per-language container pools (gVisor or Firecracker style isolation), no network, CPU or memory or time limits. Keep warm containers to avoid cold starts; route by language via the queue. Results are pushed back (websocket) or polled.

## 10. Autosave (3:15) — `slides/10.png`

Deep dive: Autosave. Client debounces and sends deltas; server does last-write-wins keyed by (user, question, language) with updated at. Local storage keeps a copy for offline edits.

## 11. Global latency (3:29) — `slides/11.png`

Deep dive: Global latency. Static assets on a CDN; API in 2-3 regions with a primary DB and read replicas; sandbox fleets in each region so run latency stays low.

## 12. Trade-offs & alternatives (3:41) — `slides/12.png`

Finally, the key trade-offs. Polling versus websockets for run results: polling is simpler and fine at this scale. Single relational DB is enough at this size; shard by user id later if needed. Pre-warmed sandboxes cost money but are what keeps p95 low.

## 13. Recap (3:59) — `slides/13.png`

To recap AlgoExpert: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Browser, CDN, Load balancer, API servers - stateless, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
