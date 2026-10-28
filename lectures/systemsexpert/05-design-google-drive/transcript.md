# SystemsExpert · Design Google Drive

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. Design Google Drive (0:00) — `slides/01.png`

In this lecture we design Google Drive. We'll follow the interview framework: clarify, set requirements, estimate, sketch the architecture, define the data and API, then dive into the hard parts and the trade-offs.

## 2. Clarifying questions (0:13) — `slides/02.png`

Start by clarifying the scope with your interviewer. Good questions here are: Only file storage, or also live collaborative editing? Max file size? Versioning? Sharing permissions required?

## 3. Functional requirements (0:28) — `slides/03.png`

The functional requirements. Upload, download, delete files and folders. Move or rename; list a folder. Share with read or write permissions. Sync across devices.

## 4. Non-functional requirements (0:42) — `slides/04.png`

The non-functional requirements. Durability (never lose a file), high availability. Large files resumable. Consistent metadata (no ghost files).

## 5. Capacity estimates (0:54) — `slides/05.png`

Now some rough capacity estimates, which drive the design. about 1B users x about 15 GB avg used about exabytes of blobs. Metadata: about 100 files per user to 100B rows; must be sharded. Uploads chunked (for example 4-8 MB) for resumability and dedup.

## 6. High-level architecture (1:15) — `slides/06.png`

Here's the high-level architecture. Client connects to LB. LB connects to Metadata service and Upload service. Metadata service connects to Metadata DB sharded by owner or folder and Change notifications. Upload service connects to Blob store, replicated, content-addressed chunks. Change notifications connects to Client.

## 7. Data model (1:37) — `slides/07.png`

Here is the data model. files(id, owner id, parent id, name, is folder, size, version, chunk ids , deleted). acl(file id, principal id, role). chunks(hash, size, ref count, locations).

## 8. API (1:54) — `slides/08.png`

The API. The main endpoints are: POST files upload-session; PUT upload by sessionId chunks by n; POST upload by sessionId commit; GET files by id content; GET folders by id children; PATCH files by id; POST files by id share. Each one is small, resource-oriented and easy to version.

## 9. Upload path (2:13) — `slides/09.png`

Deep dive: Upload path. Chunks are hashed client-side; the server skips chunks it already has (dedup). File metadata is committed only after all chunks are durable, so readers never see partial files.

## 10. Metadata consistency (2:27) — `slides/10.png`

Deep dive: Metadata consistency. Folder moves must be atomic: keep a user's tree on one shard (shard by owner) so moves are single-shard transactions.

## 11. Sync (2:37) — `slides/11.png`

Deep dive: Sync. Clients long-poll or websocket for change events with a per-user change log cursor; conflicts produce 'conflicted copy' files.

## 12. Trade-offs & alternatives (2:47) — `slides/12.png`

Finally, the key trade-offs. Content-addressed chunks save space but complicate deletion (ref counts plus GC). Sharding by owner makes shared-folder queries cross-shard. Erasure coding cheaper than 3x replication for cold data.

## 13. Recap (3:04) — `slides/13.png`

To recap Google Drive: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, LB, Metadata service, Metadata DB sharded by owner or folder, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
