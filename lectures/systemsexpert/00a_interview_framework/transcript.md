# SystemsExpert · Interview Framework

Video: [lecture.mp4](lecture.mp4) · Slides: [slides.pdf](slides.pdf) · Voice: en-US-GuyNeural

## 1. System Design Interviews (0:00) — `slides/01.png`

Welcome to the SystemsExpert series. Before the individual designs, here's the framework to run every system design interview, and the numbers you should know for quick estimates.

## 2. The 45-minute framework (0:11) — `slides/02.png`

Run every interview in the same order. Step 1: Clarify the scope and the users. Step 2: Functional and non-functional requirements. Step 3: Rough estimates. Step 4: Entities and API. Step 5: High-level diagram. Step 6: Deep dives on bottlenecks. Step 7: Trade-offs and failure modes. Keep the interviewer involved at every step.

## 3. Back-of-envelope numbers (0:39) — `slides/03.png`

Some numbers worth memorising. 1 day about 86,400 s about 10^5 s; 1M requests per day about 12 Q P S; peak about 2–3× the average. Character 1 B; tweet-size text about 300 B; photo about 200 KB–2 MB; 1 min of HD video about 50–100 MB. One server handles about 10k concurrent connections and about 1k–10k simple Q P S; Redis does about 100k ops per s. A disk sequential read is about 100× faster than random; reading 1 MB from memory takes about 250 µs, from SSD about 1 ms.

## 4. Recap (1:17) — `slides/04.png`

To recap: use the same structure every time, settle requirements before drawing boxes, let estimates size the design, and always finish with trade-offs and failure modes. Next, the fundamentals, in four parts.
