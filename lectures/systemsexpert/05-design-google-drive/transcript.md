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

## 6. Capacity: worked out (1:15) — `slides/06.png`

Let's actually work the numbers. A billion users at fifteen gigabytes each is fifteen exabytes of data. With three replicas that's about forty-five exabytes raw, before deduplication saves a chunk. A hundred files per user means a hundred billion metadata rows. At about a kilobyte per row that's a hundred terabytes, so the metadata store must be sharded, by owner.

## 7. High-level architecture (1:39) — `slides/07.png`

Here's the high-level architecture. Client connects to LB. LB connects to Metadata service and Upload service. Metadata service connects to Metadata DB sharded by owner or folder and Change notifications. Upload service connects to Blob store, replicated, content-addressed chunks. Change notifications connects to Client.

## 8. Request flow: Upload a file (2:01) — `slides/08.png`

Let's follow an upload. The client splits the file into chunks of a few megabytes and hashes each one.

## 9. Request flow: Upload a file (2:08) — `slides/09.png`

It asks the metadata service which chunk hashes the server doesn't already have, enabling dedup and resumable uploads.

## 10. Request flow: Upload a file (2:16) — `slides/10.png`

The client uploads just the missing chunks to the upload service.

## 11. Request flow: Upload a file (2:20) — `slides/11.png`

Chunks land in the blob store, addressed by their hash and replicated across zones.

## 12. Request flow: Upload a file (2:26) — `slides/12.png`

Then the metadata service commits the new file version, the ordered list of chunk hashes, in one transaction.

## 13. Request flow: Upload a file (2:33) — `slides/13.png`

A change notification goes out, and the user's other devices pull the new metadata and fetch only changed chunks.

## 14. Data model (2:40) — `slides/14.png`

Here is the data model. The files record holds id, owner id, parent id, name, is folder, size, version, chunk ids , deleted. The acl record holds file id, principal id, role. The chunks record holds hash, size, ref count, locations.

## 15. API (2:58) — `slides/15.png`

The API. The main endpoints are: POST files upload-session; PUT upload by sessionId chunks by n; POST upload by sessionId commit; GET files by id content; GET folders by id children; PATCH files by id; POST files by id share. Each one is small, resource-oriented and easy to version.

## 16. Upload path (3:17) — `slides/16.png`

Deep dive: Upload path. Chunks are hashed client-side; the server skips chunks it already has (dedup). File metadata is committed only after all chunks are durable, so readers never see partial files.

## 17. Metadata consistency (3:31) — `slides/17.png`

Deep dive: Metadata consistency. Folder moves must be atomic: keep a user's tree on one shard (shard by owner) so moves are single-shard transactions.

## 18. Sync (3:42) — `slides/18.png`

Deep dive: Sync. Clients long-poll or websocket for change events with a per-user change log cursor; conflicts produce 'conflicted copy' files.

## 19. Key decisions (3:52) — `slides/19.png`

Let's pull together the key decisions. Separate metadata from blobs, because different scale and consistency needs. Content-addressed chunks, because dedup and resumable uploads. Strongly consistent metadata, because no lost edits. Push change notifications, because fast sync without polling.

## 20. Trade-offs & alternatives (4:12) — `slides/20.png`

Finally, the key trade-offs. Content-addressed chunks save space but complicate deletion (ref counts plus GC). Sharding by owner makes shared-folder queries cross-shard. Erasure coding cheaper than 3x replication for cold data.

## 21. Recap (4:29) — `slides/21.png`

To recap Google Drive: we clarified the scope, set functional and non-functional requirements, estimated the load, sketched an architecture built around Client, LB, Metadata service, Metadata DB sharded by owner or folder, and walked through the deep dives and trade-offs. Practise explaining each decision out loud.
