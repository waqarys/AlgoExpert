"""Per-design enrichment: a request-flow walkthrough, worked capacity maths, and key decisions.
flow: (request name, [(node label on the diagram, caption, narration)])
capacity: [(slide line, spoken sentence)]
decisions: [(decision, reason)]
"""
D = {}
D["01-design-algoexpert"] = dict(
 flow=("Run Code", [
  ("Browser", "1. User clicks Run Code", "Let's follow one Run Code click. The browser sends the user's code and the question ID in a single POST."),
  ("Load balancer", "2. LB picks a healthy API server", "The load balancer forwards it to any healthy API server. Because API servers are stateless, any one will do."),
  ("API servers - stateless", "3. API validates and enqueues", "The API server checks the session, rate-limits the user, and puts a run job on the queue instead of executing anything itself."),
  ("Run queue", "4. Job waits in the per-language queue", "The job waits in the queue for that language. The queue absorbs bursts, so a spike in runs never overloads the API tier."),
  ("Sandbox workers per language", "5. Sandbox compiles and runs tests", "A sandbox worker picks up the job, compiles the code in an isolated container with CPU and memory limits, and runs the test cases."),
  ("API servers - stateless", "6. Results return to the browser", "Results flow back to the API server, which returns them to the browser, typically within two or three seconds.")]),
 capacity=[("Autosave: 10k users typing, 1 save/s → 10k writes/s", "Ten thousand concurrent users saving every second would be ten thousand writes a second."),
           ("Debounce to 1 save / 10 s → ~1k writes/s", "Debouncing on the client to one save every ten seconds cuts that to about a thousand writes a second, easy for one Postgres primary."),
           ("Runs: 2k/min ≈ 33/s × 1.5 s CPU ≈ 50 busy sandboxes", "Code runs peak around two thousand a minute, about thirty-three a second. Each takes about one and a half seconds, so roughly fifty sandboxes are busy at once."),
           ("Provision ×3 headroom → ~150 sandboxes", "With three times headroom for spikes, we provision about one hundred and fifty sandbox slots.")],
 decisions=[("CDN for prompts and videos", "content is read-only and global"), ("Queue in front of sandboxes", "absorbs bursts, isolates failures"),
            ("Containers per run with hard limits", "untrusted code must never touch the host"), ("Client-side debounce", "10× fewer writes, no lost work")])
D["02-design-a-code-deployment-system"] = dict(
 flow=("Deploy build X", [
  ("Engineer / CI trigger", "1. Engineer requests a deploy", "Let's follow a deploy. An engineer asks to deploy build X of a service."),
  ("Deploy API", "2. Deploy API records the request", "The deploy API checks the build exists and has been replicated to every target region, then records the deployment."),
  ("Goal state: desired build per service", "3. Goal state flips to build X", "The key move: it simply updates the goal state, the desired build for the service, in a strongly consistent key-value store."),
  ("Hosts' agents", "4. Agents notice the new goal", "Agent processes on every host watch that key, so they notice the change within seconds."),
  ("Peer-to-peer distribution in each region", "5. Hosts fetch chunks from peers", "Each host downloads the artifact in chunks, mostly from peers in its own region, so no single store becomes a bottleneck."),
  ("Hosts' agents", "6. Swap, health-check, report", "The agent swaps the binary, runs health checks, and reports back. Rolling back just means setting the goal state to the previous build.")]),
 capacity=[("Artifact 10 GB × 100k hosts = 1 PB of transfer", "A ten gigabyte artifact sent to a hundred thousand hosts is a petabyte of transfer."),
           ("One store at 100 Gbps ≈ 12.5 GB/s → ~22 hours", "Even one store pushing a hundred gigabits a second would need about twenty-two hours."),
           ("10 regions + P2P: bandwidth grows with hosts", "With regional replicas and peer-to-peer sharing, every host also uploads, so total bandwidth scales with the fleet."),
           ("Goal: whole fleet in < 30 min", "That's how we get the whole fleet updated in under thirty minutes.")],
 decisions=[("SQL table as the build queue", "exactly-once claims via row locks"), ("Goal state, not push commands", "idempotent, easy rollback"),
            ("Regional replicas + P2P", "removes the bandwidth bottleneck"), ("Canary stages", "limits blast radius")],
 speech={"Queue as a SQL table": "Deep dive: the build queue is just a SQL table. A worker claims a job by updating its status to running inside a transaction, selecting the next queued row with FOR UPDATE SKIP LOCKED, so two workers can never grab the same job. Workers send heartbeats, and a reaper resets any running job whose heartbeat goes stale."})
D["03-design-a-stockbroker"] = dict(
 flow=("Place a buy order", [
  ("App", "1. User taps Buy", "Let's follow a buy order. The user taps buy for ten shares, and the app sends the order with an idempotency key."),
  ("API gateway", "2. Gateway authenticates", "The gateway authenticates the user and routes the request to the order service."),
  ("Order service", "3. Check and reserve funds", "The order service checks buying power and, in one transaction, writes the order and reserves the cash in the ledger."),
  ("Outbound order queue", "4. Order queued for the exchange", "The order goes onto a durable outbound queue, so nothing is lost if the connector restarts."),
  ("Exchange connector", "5. Connector sends to the exchange", "The exchange connector sends it to the exchange and receives acknowledgements and fills."),
  ("Fills queue", "6. Fills update the ledger", "Fills flow back through a queue to the order service, which updates the position and ledger, and the user gets a push notification.")]),
 capacity=[("20M orders/day ÷ 86,400 s ≈ 230 orders/s", "Twenty million orders a day divided by eighty-six thousand seconds is about two hundred thirty orders a second."),
           ("Market open/close spikes ~10× → ~2k orders/s", "Activity spikes about ten times at the open and close, so design for two thousand orders a second."),
           ("1 KB/order × 20M ≈ 20 GB/day", "At a kilobyte each that's only about twenty gigabytes a day."),
           ("Storage is small; correctness dominates", "Storage is trivial; the real challenge is correctness and never double-spending.")],
 decisions=[("Ledger with double-entry", "auditable, never lose money"), ("Idempotency keys", "safe client retries"),
            ("Queues around the exchange", "decouple from exchange outages"), ("Shard by user", "keeps a user's orders in one place")])
D["04-design-facebook-news-feed"] = dict(
 flow=("Open the feed", [
  ("Client", "1. User opens the app", "Let's follow a feed load. The user opens the app and requests the first page of the feed."),
  ("API", "2. API routes to feed service", "The API authenticates and calls the feed service."),
  ("Feed service", "3. Read precomputed post IDs", "The feed service reads the user's precomputed list of post IDs from the feed cache, built earlier by fan-out workers."),
  ("Feed cache: user -> post ids", "4. Cache returns candidates", "The cache returns a few hundred candidate post IDs. Posts from celebrities are pulled at read time instead and merged in."),
  ("Ranking service", "5. Rank candidates", "The ranking service scores the candidates for this user, using engagement predictions and freshness."),
  ("Posts DB sharded by post_id", "6. Hydrate the top posts", "Finally we hydrate the top posts with their content from the posts store and return the page.")]),
 capacity=[("1B DAU × 10 opens/day = 10B reads/day", "A billion daily users each opening the feed ten times is ten billion reads a day."),
           ("10B ÷ 86,400 ≈ 115k reads/s; peak ~3× ≈ 350k/s", "That's about a hundred fifteen thousand reads a second, and around three hundred fifty thousand at peak."),
           ("500M posts/day ≈ 6k writes/s", "Five hundred million posts a day is about six thousand writes a second."),
           ("Fan-out: 6k/s × 500 friends ≈ 3M cache writes/s", "Fanning each out to five hundred friends means about three million cache writes a second, which is why celebrities are handled differently.")],
 decisions=[("Fan-out on write for most users", "fast reads"), ("Fan-out on read for celebrities", "avoids millions of writes per post"),
            ("Feed cache stores IDs only", "small, cheap to update"), ("Separate ranking service", "iterate on models independently")])
D["05-design-google-drive"] = dict(
 flow=("Upload a file", [
  ("Client", "1. Client chunks the file", "Let's follow an upload. The client splits the file into chunks of a few megabytes and hashes each one."),
  ("Metadata service", "2. Ask which chunks are new", "It asks the metadata service which chunk hashes the server doesn't already have, enabling dedup and resumable uploads."),
  ("Upload service", "3. Upload only missing chunks", "The client uploads just the missing chunks to the upload service."),
  ("Blob store, replicated, content-addressed chunks", "4. Chunks stored by hash", "Chunks land in the blob store, addressed by their hash and replicated across zones."),
  ("Metadata DB sharded by owner/folder", "5. Commit the new file version", "Then the metadata service commits the new file version, the ordered list of chunk hashes, in one transaction."),
  ("Change notifications", "6. Other devices sync", "A change notification goes out, and the user's other devices pull the new metadata and fetch only changed chunks.")]),
 capacity=[("1B users × 15 GB ≈ 15 EB of blobs", "A billion users at fifteen gigabytes each is fifteen exabytes of data."),
           ("× 3 replicas ≈ 45 EB raw (dedup helps)", "With three replicas that's about forty-five exabytes raw, before deduplication saves a chunk."),
           ("100 files/user → 100B metadata rows", "A hundred files per user means a hundred billion metadata rows."),
           ("~1 KB/row → ~100 TB metadata → shard by owner", "At about a kilobyte per row that's a hundred terabytes, so the metadata store must be sharded, by owner.")],
 decisions=[("Separate metadata from blobs", "different scale and consistency needs"), ("Content-addressed chunks", "dedup and resumable uploads"),
            ("Strongly consistent metadata", "no lost edits"), ("Push change notifications", "fast sync without polling")])
D["06-design-the-reddit-api"] = dict(
 flow=("Upvote a post", [
  ("Client", "1. User taps upvote", "Let's follow an upvote. The client sends a PUT that sets this user's vote on the post to plus one."),
  ("REST API", "2. API validates", "The API authenticates the user and validates the target."),
  ("Votes PK user,target", "3. Upsert the vote row", "It upserts a row keyed by user and target, so repeating the request is harmless and a user can only vote once."),
  ("Score aggregator", "4. Aggregate score changes", "A score aggregator consumes vote changes and batches the deltas, so a viral post doesn't turn into a write hotspot."),
  ("Posts", "5. Post score updated", "The post's score is updated, and listings ranked by hot or top pick it up shortly after.")]),
 capacity=[("Read:write ≈ 100:1", "Reddit is read-heavy, roughly a hundred reads for every write."),
           ("Say 50M DAU × 20 votes = 1B votes/day", "Assume fifty million daily users casting twenty votes each: a billion votes a day."),
           ("1B ÷ 86,400 ≈ 12k votes/s", "That's about twelve thousand vote writes a second."),
           ("Batching per post turns hot rows into 1 write/s", "Batching deltas per post turns thousands of updates on a hot post into about one write a second.")],
 decisions=[("PUT vote (idempotent)", "safe retries, one vote per user"), ("Cursor pagination", "stable under inserts"),
            ("Async score aggregation", "avoids hot-row contention"), ("Comments by parent_id", "simple tree loading")])
D["07-design-netflix"] = dict(
 flow=("Press Play", [
  ("Device", "1. User presses Play", "Let's follow a play request. The device calls the control plane to start playback for a title."),
  ("Control plane APIs - cloud", "2. Control plane picks a CDN", "The control plane checks the subscription and picks the best edge cache for this user's network, then returns a manifest."),
  ("Edge caches inside ISPs", "3. Stream segments from the edge", "The device streams video segments directly from an edge cache inside the user's ISP, switching bitrate as bandwidth changes."),
  ("Event stream", "4. Heartbeats record progress", "Every few seconds, playback heartbeats go to the event stream, recording position for resume."),
  ("Batch/stream analytics", "5. Analytics feed recommendations", "Those events feed analytics and the recommendation models that shape the next home page.")]),
 capacity=[("Peak 10M concurrent streams × 5 Mbps", "Suppose ten million concurrent streams at five megabits a second."),
           ("= 50 Tbps of egress", "That's fifty terabits per second of egress."),
           ("Edge box ~100 Gbps → ~500+ boxes at peak", "If one edge appliance serves around a hundred gigabits, we need at least five hundred of them, spread across ISPs."),
           ("Catalogue 10k titles × 50 encodes × ~5 GB ≈ PBs", "Ten thousand titles with dozens of encodes each puts storage in the petabytes.")],
 decisions=[("Own CDN inside ISPs", "cost and quality at this egress"), ("Pre-position popular titles off-peak", "cache hits at prime time"),
            ("Adaptive bitrate segments", "smooth playback on any network"), ("Control plane in cloud, data plane at edge", "each scales independently")])
D["08-design-the-uber-api"] = dict(
 flow=("Request a ride", [
  ("Rider", "1. Rider requests a ride", "Let's follow a ride request. The rider sends pickup and destination, and gets back a trip in the requested state."),
  ("API", "2. API creates the trip", "The API creates the trip record, which is a state machine starting at requested."),
  ("Matching service", "3. Find nearby drivers", "The matching service asks the location service for available drivers near the pickup point."),
  ("Location service - geo index", "4. Geo index lookup", "The location service, a geo index over recent driver positions, returns the closest candidates."),
  ("Push / websocket gateway", "5. Offer sent to a driver", "The best driver gets an offer over a websocket, with a timeout."),
  ("Driver", "6. Driver accepts", "When the driver accepts, the trip moves to accepted atomically, and the rider is notified.")]),
 capacity=[("1M active drivers, 1 location update / 4 s", "A million active drivers each send their location every four seconds."),
           ("1M ÷ 4 = 250k writes/s", "That's two hundred fifty thousand location writes a second."),
           ("Keep only latest position in memory (~100 B)", "We keep only the latest position per driver in memory, about a hundred bytes each."),
           ("1M × 100 B = 100 MB → shard by geo cell", "That's only a hundred megabytes total, but the write rate means we shard by geographic cell.")],
 decisions=[("In-memory geo index", "write rate too high for a DB"), ("Trip as a state machine", "no double assignment"),
            ("WebSockets for drivers", "low-latency offers"), ("Shard by city / geo cell", "locality of matching")])
D["09-design-slack"] = dict(
 flow=("Send a message", [
  ("Client", "1. User sends a message", "Let's follow a message. The client sends it with a client message ID, so retries can be de-duplicated."),
  ("REST API", "2. API persists it", "The API checks channel membership and writes the message."),
  ("Messages DB sharded by channel_id", "3. Stored in the channel shard", "It's stored in the shard for that channel, with a server timestamp that orders messages in the channel."),
  ("Pub/Sub by channel", "4. Published to the channel topic", "The API publishes the message to the channel's pub-sub topic."),
  ("Gateway servers", "5. Gateways push to members", "Gateway servers holding websocket connections for channel members receive it and push it instantly."),
  ("Read state: user, channel, last_read_ts", "6. Unread counts update", "Each member's read state determines unread badges, updated when they view the channel.")]),
 capacity=[("10M DAU × 100 msgs = 1B messages/day", "Ten million daily users sending a hundred messages each is a billion messages a day."),
           ("1B ÷ 86,400 ≈ 12k msgs/s (peak ~3× ≈ 35k)", "That's about twelve thousand messages a second, maybe thirty-five thousand at peak."),
           ("× 1 KB ≈ 1 TB/day ≈ 365 TB/year", "At a kilobyte each that's a terabyte a day, over three hundred terabytes a year."),
           ("Fan-out to ~10 online members ≈ 350k pushes/s", "If each message reaches about ten online members, gateways push around three hundred fifty thousand messages a second.")],
 decisions=[("Shard messages by channel", "channel reads stay on one shard"), ("WebSocket gateways + pub/sub", "real-time delivery"),
            ("Server timestamps per channel", "consistent ordering"), ("Client message IDs", "dedupe on retry")])
D["10-design-airbnb"] = dict(
 flow=("Book a stay", [
  ("Guest", "1. Guest searches", "Let's follow a booking. The guest searches a city and dates."),
  ("Search index - geo + filters", "2. Geo search", "Search runs against a geo and filter index, built from the listings database through change data capture."),
  ("API", "3. Guest books a listing", "The guest picks a listing and submits a booking with an idempotency key."),
  ("Bookings / availability DB", "4. Reserve the dates atomically", "The bookings service reserves the dates in a transaction, with a constraint that prevents overlapping bookings."),
  ("Payments", "5. Charge the guest", "Payment is authorised. If it fails, the hold on the dates is released."),
  ("Host", "6. Host is notified", "The booking is confirmed and the host is notified.")]),
 capacity=[("100M searches/day ÷ 86,400 ≈ 1.2k/s", "A hundred million searches a day is about twelve hundred a second."),
           ("Peak ~3× ≈ 3.5k searches/s", "Around three and a half thousand at peak, served by the search index."),
           ("1M bookings/day ≈ 12/s", "A million bookings a day is only about twelve a second."),
           ("Searches ≫ bookings → optimise reads, make writes correct", "So searches dominate load, while bookings must simply be correct.")],
 decisions=[("Separate search index (CDC)", "fast geo and filter queries"), ("DB constraint on date overlap", "no double booking"),
            ("Search can be slightly stale", "availability rechecked at booking"), ("Idempotent booking requests", "safe retries")],
 speech={"No double booking": "Deep dive: no double booking. In a single transaction, we lock the availability rows for the requested dates, with a select for update, and mark them reserved. An alternative is a unique constraint on listing and date, so a second insert for the same night simply fails. Temporary holds expire if payment doesn't go through."})
D["11-design-tinder"] = dict(
 flow=("Swipe right", [
  ("App", "1. User swipes right", "Let's follow a right swipe. The app sends the swipe for the profile shown."),
  ("API", "2. API records it", "The API records the swipe."),
  ("Swipes PK swiper, swipee", "3. Write the swipe row", "It writes a row keyed by swiper and swipee, which makes the write idempotent."),
  ("Match detector", "4. Check the reverse swipe", "The match detector looks up the reverse row: did the other person already swipe right on this user?"),
  ("Matches", "5. Create the match", "If so, it creates a match record exactly once."),
  ("Messaging service", "6. Both users can chat", "Both users are notified, and the messaging service opens a conversation.")]),
 capacity=[("50M DAU × 100 swipes = 5B swipes/day", "Fifty million daily users swiping a hundred times each is five billion swipes a day."),
           ("5B ÷ 86,400 ≈ 58k swipes/s avg", "That's about fifty-eight thousand swipes a second on average."),
           ("× ~20 B/row ≈ 100 GB/day", "At around twenty bytes per row that's a hundred gigabytes a day."),
           ("Partition swipes by swiper; reverse lookup by key", "Partition by swiper, and the reverse lookup is a direct key read.")],
 decisions=[("Precompute decks", "instant swiping"), ("Swipe key (swiper, swipee)", "O(1) match check"),
            ("Geo + preference filters first", "small candidate sets"), ("Separate messaging service", "scales on its own")])
D["12-design-amazon"] = dict(
 flow=("Check out", [
  ("U", "1. User clicks Place order", "Let's follow a checkout. The user clicks place order on their cart."),
  ("Checkout orchestrator", "2. Orchestrator starts a saga", "The checkout orchestrator starts a saga, a sequence of steps each with a compensating action."),
  ("Inventory", "3. Reserve inventory", "First it reserves inventory for each item, with a short expiry."),
  ("Payments", "4. Charge payment", "Next it charges the payment method with an idempotency key. If payment fails, the inventory reservation is released."),
  ("Orders", "5. Create the order", "Then the order is written in a confirmed state."),
  ("Fulfilment events", "6. Fulfilment begins", "Finally an event kicks off fulfilment, picking, packing and shipping.")]),
 capacity=[("10M orders/day ÷ 86,400 ≈ 120 orders/s", "Ten million orders a day is about a hundred twenty a second."),
           ("Peak events ~10× ≈ 1.2k orders/s", "Big sale events push that ten times, to about twelve hundred a second."),
           ("100M DAU × 20 page views ≈ 23k reads/s", "A hundred million daily users viewing twenty pages each is around twenty-three thousand reads a second."),
           ("Reads cached; checkout writes must be exact", "Catalogue reads are cached aggressively, while checkout writes must be exact.")],
 decisions=[("Saga, not a distributed transaction", "services stay independent"), ("Reserve inventory with expiry", "no oversell, no stuck stock"),
            ("Idempotent payments", "safe retries"), ("Event-driven fulfilment", "decoupled and scalable")])
D["13-design-the-twitch-api"] = dict(
 flow=("Send a chat message", [
  ("Clients", "1. Viewer sends a chat message", "Let's follow a chat message. The viewer's client sends it over its open websocket."),
  ("Chat WebSocket servers", "2. Chat server receives it", "The chat server holding that connection receives it."),
  ("Chat moderation service", "3. Moderation check", "It checks bans, slow mode and filters with the moderation service, cached in memory."),
  ("Pub/Sub per channel", "4. Publish to the channel topic", "The message is published once to the channel's pub-sub topic."),
  ("Chat WebSocket servers", "5. Fan out to viewers", "Every chat server with viewers of that channel receives it and pushes it to its local sockets, batching for huge channels.")]),
 capacity=[("Big channel: 100k viewers, 50 msgs/s", "Imagine a big channel with a hundred thousand viewers and fifty chat messages a second."),
           ("Fan-out: 50 × 100k = 5M deliveries/s", "That's five million message deliveries a second."),
           ("Server holds ~50k sockets → ≥2 servers, each 2.5M pushes/s", "With about fifty thousand sockets per server, that's at least two servers each pushing two and a half million messages a second."),
           ("Batch every 100 ms → 10 frames/s per viewer", "Batching every hundred milliseconds turns that into just ten frames a second per viewer.")],
 decisions=[("Pub/sub per channel", "publish once, fan out per server"), ("Approximate viewer counts", "cheap, a few seconds stale is fine"),
            ("Strong consistency for subscriptions", "money involved"), ("API serves playback URLs only", "video bytes go via CDN")])
