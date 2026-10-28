from enrich.kit import *

def ArrayOfProducts():
    a = [5, 1, 4, 2]; n = len(a); out = [None] * n; run = 1; st = []
    for i in range(n):
        out[i] = run
        st.append(S("Worked example", [A(a, hl={i: "cur", **{k: "done" for k in range(i)}}, ptr={"i": i}, label="input"), A(out, hl={i: "ok"}, label="output after left pass"), TX([f"left product before {i} = {run}"], h=0.4)],
                    f"Left pass: out[{i}] = product of everything left = {run}", f"Left pass, index {i}: everything to the left multiplies to {run}, so out {i} becomes {run}.")); run *= a[i]
    run = 1
    for i in range(n - 1, -1, -1):
        out[i] *= run
        if i in (3, 0):
            st.append(S("Worked example", [A(a, hl={i: "cur", **{k: "done" for k in range(i + 1, n)}}, ptr={"i": i}, label="input"), A(out, hl={i: "ok"}, label="output after right pass"), TX([f"right product after {i} = {run}"], h=0.4)],
                        f"Right pass: out[{i}] ×= {run} → {out[i]}", f"Right pass, index {i}: everything to the right multiplies to {run}, so out {i} becomes {out[i]}."))
        run *= a[i]
    return E(["Brute force: for each i, multiply all others → O(n²)", "Total product ÷ a[i] → O(n), but breaks on zeros (and is disallowed)", "Prefix × suffix products → O(n), no division"],
             "The brute force recomputes a product of n minus one numbers for every index, which is quadratic. Dividing the total product by each element is linear, but it breaks on zeros and the problem forbids it. Prefix and suffix products give linear time without division.",
             pick(st, 6), ["Zeros: one zero → only its index is non-zero", "Two zeros → everything is 0", "Overflow for large products"],
             "Zeros are the classic trap: with one zero, only that position gets a non-zero product; with two, everything is zero. The prefix-suffix method handles both automatically. Watch for overflow with big inputs.",
             ["Mention the division idea and why it fails", "Follow-up: O(1) extra space (reuse the output array)"],
             "Bring up the division idea and explain why it fails. Our version already uses the output array for the prefix pass, so extra space is constant beyond the output.",
             ["The first loop writes the running product of everything to the left into each slot, then multiplies the running value by a i. The second loop goes right to left with a fresh running product and multiplies it into each slot."])

def BestSeat():
    seats = [1, 0, 1, 0, 0, 0, 1]; st = []; best, bg, l = -1, 0, 0
    while l < len(seats):
        r = l + 1
        while r < len(seats) and seats[r] == 0: r += 1
        gap = r - l - 1
        if r < len(seats):
            if gap > bg: bg, best = gap, (l + r) // 2
            st.append(S("Worked example", [A(seats, hl={l: "done", r: "done", **({(l + r) // 2: "ok"} if gap else {})}, window=(l, r) if gap else None, ptr={"l": l, "r": r}), TX([f"gap = {gap}", f"best seat = {best}"])],
                        f"Run of {gap} empty seat(s) between {l} and {r} → best {best}", f"Between occupied seats {l} and {r} there {'are' if gap != 1 else 'is'} {gap} empty seat{'s' if gap != 1 else ''}. " + (f"The middle is seat {(l + r) // 2}." if gap else "")))
        l = r
    return E(["Brute force: for each empty seat, scan both ways for neighbours → O(n²)", "Optimal: find runs of zeros in one pass → O(n)", "Middle of the longest run is the answer"],
             "Brute force checks each empty seat and scans outward for the nearest people, which is quadratic. Instead we walk once, measuring each run of empty seats between occupied ones, and keep the middle of the longest.",
             st, ["No empty seat → −1", "Ties: keep the leftmost (strictly greater)", "Even-length runs: (l + r) / 2 picks the left middle"],
             "If there's no empty seat, return minus one. Using a strictly greater comparison keeps the leftmost seat on ties, and for an even run, integer division picks the left middle.",
             ["Clarify ends: seats at both ends are occupied", "Follow-up: seat many people one by one (heap of gaps)"],
             "Clarify that both ends are occupied. A follow-up seats people one after another, which calls for a heap of gaps.",
             ["We start at an occupied seat l, move r forward past zeros, compute the gap as r minus l minus one, and if it's the best so far, record the middle seat. Then l jumps to r."])

def FirstDuplicateValue():
    a = [2, 1, 5, 2, 3, 3, 4]; w = a[:]; st = []
    for x in a:
        v = abs(x) if False else None
    for k in range(len(w)):
        v = abs(w[k]); i = v - 1
        if w[i] < 0:
            st.append(S("Worked example", [A(w, hl={i: "bad", k: "cur"}, ptr={"k": k, "v-1": i}), TX([f"value {v}: slot {i} already negative → duplicate!"])], f"Answer: {v}", f"Value {v} points to slot {i}, which is already negative, so {v} has been seen before. It's the first duplicate.")); break
        w[i] = -w[i]
        st.append(S("Worked example", [A(w, hl={i: "ok", k: "cur"}, ptr={"k": k, "v-1": i}), TX([f"value {v}: flip slot {i} negative"])], f"Mark {v} as seen by negating index {i}", f"Value {v} marks its own slot, index {i}, by flipping it negative."))
    return E(["Brute force: for each element, scan ahead → O(n²)", "Hash set of seen values → O(n) time, O(n) space", "Values are 1…n → mark by negating a[v−1] → O(1) space"],
             "Comparing every pair is quadratic. A hash set is linear but uses extra memory. Since values are between one and n, each value can mark its own slot by negating it, giving linear time and constant space.",
             pick(st, 6), ["Use abs() — the slot may already be negated", "No duplicate → −1", "Mutates the input; mention or restore it"],
             "Always take the absolute value, because the current element may already have been negated. Return minus one if there's no duplicate, and mention that this mutates the input.",
             ["Ask whether modifying the input is allowed", "Follow-up: read-only array → Floyd's cycle detection"],
             "Ask if you're allowed to modify the input. If not, Floyd's cycle detection on the index graph also works in constant space.",
             ["For each value, we take its absolute value v and look at slot v minus one. If it's negative, v was seen before, so we return it. Otherwise we negate the slot."])

def LongestPeak():
    a = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]; st = []; best = 0; i = 1
    while i < len(a) - 1:
        if a[i - 1] < a[i] > a[i + 1]:
            l, r = i - 1, i + 1
            while l > 0 and a[l - 1] < a[l]: l -= 1
            while r < len(a) - 1 and a[r + 1] < a[r]: r += 1
            best = max(best, r - l + 1)
            st.append(S("Worked example", [A(a, hl={i: "cur"}, window=(l, r), ptr={"tip": i}), TX([f"peak {l}..{r}, length {r - l + 1}", f"best = {best}"])],
                        f"Tip {a[i]} at {i} → peak spans {l}…{r} (length {r - l + 1})", f"Index {i}, value {a[i]}, is higher than both neighbours, so it's a tip. Expanding left while values fall and right while values fall gives a peak from {l} to {r}, length {r - l + 1}."))
            i = r
        else: i += 1
    return E(["Brute force: from every index, expand a peak → O(n²)", "Optimal: only expand from tips, skip past each peak → O(n)", "Each element is visited at most twice"],
             "Expanding from every index is quadratic. Instead, only tips, values higher than both neighbours, can be peaks. Expanding from each tip and then jumping to the peak's end means each element is touched a constant number of times.",
             st, ["Strict inequalities: plateaus (3, 3) aren't peaks", "Need ≥ 3 elements; only rising or only falling → 0", "Jump i to r to avoid rescanning"],
             "Inequalities are strict, so a plateau breaks a peak. A purely increasing array has no peak and returns zero.",
             ["Draw the array as a mountain range while explaining", "Follow-up: longest valley; count peaks"],
             "Sketching the values as a mountain range makes this easy to explain. Variants ask for the longest valley.",
             ["We scan from index one. When the current value is a tip, we walk l left while values keep increasing toward the tip and r right while they keep decreasing, update the best length, and jump i to r. Otherwise i moves on."])

def MajorityElement():
    a = [1, 2, 3, 2, 2, 1, 2]; cand = None; cnt = 0; st = []
    for i, x in enumerate(a):
        if cnt == 0: cand = x
        cnt += 1 if x == cand else -1
        st.append(S("Worked example", [A(a, hl={i: "ok" if x == cand else "bad", **{k: "done" for k in range(i)}}, ptr={"i": i}), TX([f"candidate = {cand}", f"count = {cnt}"])],
                    f"{x} {'matches' if x == cand else 'cancels'} → candidate {cand}, count {cnt}", f"Element {x} {'matches the candidate, so the count goes up' if x == cand else 'differs from the candidate, so it cancels one vote'}. Candidate {cand}, count {cnt}."))
    return E(["Brute force: count each value → O(n²)", "Hash map counts → O(n) time, O(n) space", "Sort and take the middle → O(n log n)", "Boyer–Moore voting → O(n) time, O(1) space"],
             "Counting each value separately is quadratic. A hash map is linear but uses memory, and sorting puts the majority in the middle in n log n. Boyer-Moore voting gets linear time with constant space, by letting different values cancel each other out.",
             pick(st, 6), ["Guaranteed majority exists here; otherwise verify with a 2nd pass", "Count resets don't lose the answer", "Single element"],
             "This problem guarantees a majority exists. Without that guarantee, you'd need a second pass to verify the candidate.",
             ["Explain the cancellation intuition", "Follow-up: elements appearing > n/3 times (two candidates)"],
             "Explain the intuition: the majority has more votes than everything else combined, so it survives the cancellations. The follow-up finds elements appearing more than n over three times with two candidates.",
             ["We keep a candidate and a count. When the count is zero, the current value becomes the candidate. Then the count goes up for a match and down otherwise. The final candidate is returned."])

def MergeOverlappingIntervals():
    iv = sorted([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]); out = []; st = []
    for s, e in iv:
        if out and out[-1][1] >= s: out[-1][1] = max(out[-1][1], e); act = f"overlaps → extend to {out[-1]}"
        else: out.append([s, e]); act = "no overlap → start new interval"
        st.append(S("Worked example", [T([[f"[{a},{b}]" for a, b in iv]], hl={(0, iv.index([s, e])): "cur"}, label="sorted intervals"), T([[f"[{a},{b}]" for a, b in out]], hl={(0, len(out) - 1): "ok"}, label="merged")],
                    f"[{s},{e}] {act}", f"Interval {s} to {e}: " + ("it starts before the last merged interval ends, so we extend that interval's end to " + str(out[-1][1]) + "." if act.startswith("overlaps") else "it starts after the last merged interval ends, so it begins a new one.")))
    return E(["Brute force: repeatedly merge any overlapping pair → O(n²) or worse", "Optimal: sort by start, single sweep → O(n log n)", "After sorting, only the last merged interval can overlap"],
             "Repeatedly scanning for any overlapping pair is at least quadratic. Once intervals are sorted by start, an interval can only overlap the most recent merged one, so a single sweep finishes the job after an n log n sort.",
             st, ["Touching intervals [3,5] and [5,7] overlap (≥)", "Fully contained intervals: take max of ends", "Don't mutate the caller's array"],
             "Touching endpoints count as overlapping, which is why we compare with greater-or-equal. A contained interval is handled by taking the max of the ends.",
             ["Follow-up: insert a new interval into a sorted list", "Follow-up: minimum meeting rooms (Laptop Rentals)"],
             "Follow-ups include inserting one interval into an already merged list, or counting overlapping meetings.",
             ["We clone and sort by start. For each interval, if the last merged interval's end reaches its start, we extend that end to the max; otherwise we append a copy."])

def MissingNumbers():
    nums = [1, 4, 3]; n = len(nums) + 2; total = n * (n + 1) // 2 - sum(nums); avg = total // 2
    lowE = avg * (avg + 1) // 2; lowA = sum(x for x in nums if x <= avg); a = lowE - lowA; b = total - a
    st = [S("Worked example", [A(list(range(1, n + 1)), hl={x - 1: "done" for x in nums}, idx=False, label="1…n (grey = present)"), TX([f"n = {n}", f"missing sum = {n * (n + 1) // 2} − {sum(nums)} = {total}"])], f"Missing pair sums to {total}", f"With three numbers given, n is five. One through five sums to fifteen, the input sums to {sum(nums)}, so the two missing numbers add up to {total}."),
          S("Worked example", [TX([f"split at average = {total} // 2 = {avg}", "one missing number is ≤ avg, the other > avg"])], f"Split at {avg}", f"The two missing numbers are different, so one is at most the average, {avg}, and the other is above it."),
          S("Worked example", [TX([f"expected sum 1…{avg} = {lowE}", f"actual sum of inputs ≤ {avg} = {lowA}", f"first missing = {lowE} − {lowA} = {a}"])], f"First missing = {a}", f"The numbers one to {avg} should sum to {lowE}; the inputs at most {avg} sum to {lowA}. The difference, {a}, is the first missing number."),
          S("Worked example", [A(list(range(1, n + 1)), hl={**{x - 1: "done" for x in nums}, a - 1: "ok", b - 1: "ok"}, idx=False), TX([f"second = {total} − {a} = {b}"])], f"Answer: [{a}, {b}]", f"The second is {total} minus {a}, which is {b}. So the answer is {a} and {b}.")]
    return E(["Brute force: check each 1…n for membership → O(n²)", "Hash set → O(n) time, O(n) space", "Math (sums, or XOR) → O(n) time, O(1) space"],
             "Checking each candidate against the array is quadratic. A hash set makes it linear with extra space. Using sums, we can get constant space: the total tells us the missing pair's sum, and splitting at the average separates them.",
             st, ["Use long for big sums", "Missing numbers may be 1 or n", "Empty input → [1, 2]"],
             "Use a long for the sums. The missing numbers might be the very first or last, and an empty input means the answer is one and two.",
             ["Mention the XOR variant", "Follow-up: k missing numbers → cyclic sort / bitset"],
             "The XOR version works the same way, splitting on a set bit. For k missing numbers, a cyclic sort or bitset generalises.",
             ["We compute n as length plus two, subtract every input from the expected total to get the missing sum, split it at the average, and compare the expected and actual sums of the lower half to find the first number. The second is the total minus the first."])

def MonotonicArray():
    a = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]; inc = dec = True; st = []
    for i in range(1, len(a)):
        if a[i] < a[i - 1]: inc = False
        if a[i] > a[i - 1]: dec = False
        if i in (1, 3, 4, 7):
            st.append(S("Worked example", [A(a, hl={i - 1: "done", i: "cur"}, ptr={"i": i}), TX([f"{a[i - 1]} → {a[i]}", f"non-decreasing possible: {inc}", f"non-increasing possible: {dec}"])],
                        f"{a[i - 1]} → {a[i]}: inc={inc}, dec={dec}", f"From {a[i - 1]} to {a[i]}: " + ("it drops, so the array can't be non-decreasing." if a[i] < a[i - 1] else "equal values don't break either direction." if a[i] == a[i - 1] else "it rises, so it can't be non-increasing.")))
    return E(["Naive: determine direction from the first unequal pair, then re-scan", "Simpler: track two flags in one pass → O(n)", "No sorting or extra memory needed"],
             "A common first attempt finds the direction from the first unequal pair, then checks everything again. Tracking two flags, can-still-be-increasing and can-still-be-decreasing, does it in a single pass.",
             st, ["Empty or 1-element arrays are monotonic", "Equal neighbours are allowed", "Leading equal values before the trend"],
             "Empty and single-element arrays are monotonic, equal neighbours are fine, and leading equal values don't fix a direction prematurely.",
             ["Early exit when both flags are false", "Follow-up: strictly monotonic"],
             "You can return early once both flags are false. A follow-up asks for strict monotonicity.",
             ["We keep increasing and decreasing flags. Any drop clears increasing, any rise clears decreasing, and we return whether either survives."])

def MoveElementToEnd():
    a = [2, 1, 2, 2, 2, 3, 4, 2]; t = 2; l, r = 0, len(a) - 1; st = []
    while l < r:
        while l < r and a[r] == t: r -= 1
        sw = a[l] == t
        if sw: a[l], a[r] = a[r], a[l]
        st.append(S("Worked example", [A(a, hl={l: "ok" if sw else "done", r: "warn"}, ptr={"L": l, "R": r})], (f"swap a[{l}] ↔ a[{r}]" if sw else f"a[{l}] = {a[l]} ≠ {t}, keep"), (f"The right pointer skips trailing twos and stops at index {r}. The left value was a two, so we swap it to the right." if sw else f"The value at index {l} isn't a two, so it stays.")))
        l += 1
    return E(["Build a new list: non-targets then targets → O(n) space", "Bubble targets one step at a time → O(n²)", "Two pointers in place → O(n), O(1) space"],
             "You could build a new list, or bubble each two to the end one step at a time, which is quadratic. Two pointers swap targets from the left with non-targets from the right in a single pass, in place.",
             pick(st, 6), ["Order of other elements need not be kept", "All targets or no targets", "Check l < r inside the inner loop"],
             "The problem doesn't require preserving order of the other elements. Guard the inner loop with l less than r so it never crosses.",
             ["Follow-up: keep relative order (stable) → write pointer", "Related: Dutch flag partitioning"],
             "If order must be preserved, use a write pointer that copies non-targets forward, then fill the tail with targets.",
             ["While l is less than r, we move r left past targets, swap if the left element is the target, then advance l."])

def SmallestDifference():
    a, b = sorted([-1, 5, 10, 20, 28, 3]), sorted([26, 134, 135, 15, 17]); i = j = 0; best = None; st = []
    while i < len(a) and j < len(b):
        d = abs(a[i] - b[j])
        if best is None or d < best[0]: best = (d, a[i], b[j])
        st.append(S("Worked example", [A(a, hl={i: "cur"}, ptr={"i": i}, label="A sorted"), A(b, hl={j: "cur"}, ptr={"j": j}, label="B sorted"), TX([f"|{a[i]} − {b[j]}| = {d}", f"best = {best[1]}, {best[2]} ({best[0]})"], h=0.5)],
                    f"diff {d}; move the smaller side", f"Comparing {a[i]} and {b[j]}: difference {d}. The best so far is {best[1]} and {best[2]}. We advance the pointer at the smaller value to close the gap."))
        if a[i] < b[j]: i += 1
        elif a[i] > b[j]: j += 1
        else: break
    return E(["Brute force: every pair → O(n·m)", "Sort both + two pointers → O(n log n + m log m)", "Moving the larger value can only widen the gap"],
             "Checking every pair costs n times m. After sorting both arrays, two pointers walk forward, always advancing the smaller value, because moving the larger one can only make the difference bigger.",
             pick(st, 6), ["Equal values → difference 0, stop early", "Overflow on subtraction (use long)", "Negative numbers"],
             "If the values are equal, the difference is zero and we can stop. Use a long for the subtraction to avoid overflow.",
             ["Explain why advancing the smaller is safe", "Follow-up: closest pair across 3 arrays"],
             "Explain clearly why moving the smaller pointer never misses the answer.",
             ["We sort both arrays, then loop while both pointers are in range. We compute the absolute difference as a long, keep the best pair, and advance whichever side is smaller, breaking on an exact match."])

def SpiralTraverse():
    m = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]; out = []; st = []
    sr, er, sc, ec = 0, 3, 0, 3; layer = 0
    while sr <= er and sc <= ec:
        cells = [(sr, c) for c in range(sc, ec + 1)] + [(r, ec) for r in range(sr + 1, er + 1)] + [(er, c) for c in range(ec - 1, sc - 1, -1) if sr < er] + [(r, sc) for r in range(er - 1, sr, -1) if sc < ec]
        for name, part in [("top row", [x for x in cells if x[0] == sr]), ("right col, bottom row, left col", [x for x in cells if x[0] != sr])]:
            out += [m[r][c] for r, c in part]
            st.append(S("Worked example", [T(m, hl={**{(r, c): "done" for r in range(4) for c in range(4) if m[r][c] in out}, **{x: "cur" for x in part}}, w=0.45), TX(["output:", " ".join(map(str, out))], w=0.55, h=1)],
                        f"Layer {layer}: {name}", f"Layer {layer}, {name}: we add {', '.join(str(m[r][c]) for r, c in part)}.", layout="cols"))
        sr += 1; er -= 1; sc += 1; ec -= 1; layer += 1
    return E(["Simulation with a visited matrix and direction turns → O(n) time, O(n) space", "Layer by layer with four boundaries → O(n), O(1) extra", "Both touch every cell once"],
             "One approach walks with a direction and turns when it hits a visited cell, which needs a visited matrix. Shrinking four boundaries layer by layer avoids that extra memory.",
             st, ["Single row or single column — don't double count", "Non-square matrices", "Empty matrix"],
             "The trickiest cases are a single remaining row or column, where the bottom and left passes would repeat cells. The guards sr less than er and sc less than ec prevent that.",
             ["Know recursive and iterative forms", "Follow-up: generate a spiral matrix 1…n²"],
             "A natural follow-up is the reverse: filling an n by n matrix with one to n squared in spiral order.",
             ["We keep start and end row and column. Each loop walks the top row, the right column, then the bottom row and left column with guards for single rows or columns, and finally shrinks all four boundaries."])

def SweetAndSavory():
    dishes, t = [-3, -5, 1, 7], 8; sw = sorted([d for d in dishes if d < 0], reverse=True); sv = sorted([d for d in dishes if d > 0]); i = j = 0; best = [0, 0]; bd = None; st = []
    while i < len(sw) and j < len(sv):
        s = sw[i] + sv[j]
        if s <= t:
            if bd is None or t - s < bd: bd, best = t - s, [sw[i], sv[j]]
            act = "fits → record, try bigger savory"; j += 1
        else: act = "too big → sweeter dish"; i += 1
        st.append(S("Worked example", [A(sw, hl={min(i, len(sw) - 1): "cur"}, label="sweet (mildest first)"), A(sv, hl={min(j, len(sv) - 1): "cur"}, label="savory (smallest first)"), TX([f"sum = {s} vs target {t}: {act}", f"best = {best}"], h=0.5)],
                    f"{s} ≤ {t}? {act}", f"The pair sums to {s}. " + ("That's within the target, so we record it if it's closer, and try a bigger savory dish." if act.startswith("fits") else "That's over the target, so we need a sweeter dish.")))
    return E(["Brute force: all sweet × savory pairs → O(n²)", "Sort each side + two pointers → O(n log n)", "Never exceed the target"],
             "Trying every sweet and savory pair is quadratic. Sorting sweets from mildest to sweetest and savories from smallest to largest lets two pointers converge on the best pair in linear time after sorting.",
             st, ["No valid pair → [0, 0]", "Zero-flavour dishes are ignored", "Sum must not exceed target"],
             "If no pair fits, return zero, zero. Dishes with zero flavour belong to neither group.",
             ["Explain pointer movement carefully", "Follow-up: allow exceeding target by closest absolute diff"],
             "Explain why each pointer move is safe. A follow-up allows sums above the target and minimises absolute difference.",
             ["We split dishes into sweet and savory lists, sort sweet descending so the mildest is first and savory ascending, then while both pointers are valid, a sum within target updates the best and advances savory; otherwise we move to a sweeter dish."])

def ThreeNumberSum():
    a = sorted([12, 3, 1, 2, -6, 5, -8, 6]); t = 0; res = []; st = []
    for i in range(len(a) - 2):
        l, r = i + 1, len(a) - 1
        while l < r:
            s = a[i] + a[l] + a[r]
            if s == t: res.append([a[i], a[l], a[r]])
            if i in (0, 1) and len(st) < 6:
                st.append(S("Worked example", [A(a, hl={i: "warn", l: "cur", r: "cur"}, ptr={"i": i, "L": l, "R": r}), TX([f"{a[i]} + {a[l]} + {a[r]} = {s}", f"triplets: {res}"])],
                            f"sum {s} " + ("= 0 ✓" if s == t else "< 0 → L++" if s < t else "> 0 → R−−"), f"With {a[i]} fixed, {a[l]} plus {a[r]} gives {s}. " + ("That's a match; record it and move both pointers." if s == t else "Too small, so move left forward." if s < t else "Too big, so move right back.")))
            if s == t: l += 1; r -= 1
            elif s < t: l += 1
            else: r -= 1
    return E(["Brute force: three nested loops → O(n³)", "Fix one + hash set for the pair → O(n²) time, O(n) space", "Sort + fix one + two pointers → O(n²), O(1) extra"],
             "Three nested loops are cubic. Fixing one number and using a hash set for the other two is quadratic with extra memory. Sorting, fixing one number, and closing in with two pointers is quadratic with constant extra space, and naturally sorted output.",
             st, ["Distinct values here; with duplicates, skip repeats", "Move both pointers after a match", "Fewer than 3 elements → empty"],
             "This problem has distinct values. With duplicates you'd skip repeated values to avoid duplicate triplets. After a match, move both pointers.",
             ["Mention generalisation to k-sum", "Follow-up: closest 3-sum"],
             "Mention that this generalises to k-sum, and a common follow-up is the closest three-sum.",
             ["We sort, then for each index i set l right after it and r at the end. We compute the sum; on a match we record and move both, otherwise move l forward if too small or r back if too big."])

def ZeroSumSubarray():
    a = [4, 2, -1, -1, 3]; s = 0; seen = [0]; st = []
    for i, x in enumerate(a):
        s += x
        hit = s in seen
        st.append(S("Worked example", [A(a, hl={i: "bad" if hit else "cur", **({k: "ok" for k in range(seen.index(s), i + 1)} if hit else {})}, ptr={"i": i}), TX([f"prefix sum = {s}", f"seen = {{{', '.join(map(str, seen))}}}" + ("  ✓ repeat!" if hit else "")])],
                    (f"Prefix {s} seen before → zero-sum subarray" if hit else f"Prefix sum {s} is new"), (f"The prefix sum is {s} again, so the elements in between sum to zero. Return true." if hit else f"Adding {x}, the prefix sum is {s}, which we haven't seen. Add it to the set.")))
        if hit: break
        seen.append(s)
    return E(["Brute force: all subarrays → O(n²) (or O(n³) naive sums)", "Prefix sums + hash set → O(n)", "Repeated prefix ⇒ zero-sum in between"],
             "Checking every subarray is at least quadratic. With prefix sums, if the same running total appears twice, everything between those positions sums to zero. A hash set detects that in linear time.",
             st, ["Seed the set with 0 (subarray starting at index 0)", "A single 0 element is a zero-sum subarray", "Use long for sums"],
             "Seed the set with zero so a subarray starting at index zero is detected. A single zero element counts.",
             ["Follow-up: count zero-sum subarrays (map of counts)", "Follow-up: subarray sum = k"],
             "Follow-ups count zero-sum subarrays with a map of counts, or look for a target sum k.",
             ["We seed a set with zero, keep a running sum, and return true as soon as adding a sum to the set fails because it's already there."])

def _tw(nodes, root, hl, cap, nar, side=None, notes=None):
    p = [TR(nodes, root, hl=hl, notes=notes, w=0.68 if side else None)]
    if side: p.append(TX(side, w=0.32, h=1))
    return S("Worked example", p, cap, nar, layout="cols" if side else "rows")

def BstConstruction():
    vals = [10, 5, 15, 2, 5, 13, 22, 1]; nodes, root = bst(vals); st = []
    nodes2, root2 = bst(vals + [14]); path = ["0", "2", "5"]
    st.append(_tw(nodes, root, {}, "Start: BST built from 10, 5, 15, 2, 5, 13, 22, 1", "Here's a BST built by inserting ten, five, fifteen, two, five, thirteen, twenty-two and one. Equal values go right."))
    for k, pid in enumerate(path):
        st.append(_tw(nodes2 if k == 2 else nodes, root, {**{p: "done" for p in path[:k]}, pid: "cur"}, f"insert(14): at {nodes[pid][0]} → go {'right' if 14 >= nodes[pid][0] else 'left'}", f"To insert fourteen, compare with {nodes[pid][0]}: fourteen is {'larger' if 14 >= nodes[pid][0] else 'smaller'}, so go {'right' if 14 >= nodes[pid][0] else 'left'}."))
    st.append(_tw(nodes2, root, {"8": "ok"}, "14 becomes 13's right child", "Thirteen has no right child, so fourteen goes there."))
    # remove 10: replace with min of right subtree (13), then remove 13 from right subtree
    st.append(_tw(nodes2, root, {"0": "bad", "5": "ok"}, "remove(10): two children → copy min of right subtree (13)", "Removing the root, ten, which has two children: copy the smallest value of its right subtree, thirteen, into the root, then remove thirteen from the right subtree, where it has at most one child."))
    n3 = {k: v[:] for k, v in nodes2.items()}; n3["0"][0] = 13; n3["2"][1] = "8"; del n3["5"]
    st.append(_tw(n3, root, {"0": "ok", "8": "cur"}, "Result: 13 at the root; 14 moves up", "The result: thirteen at the root, and fourteen takes thirteen's old place."))
    return E(["Unbalanced BST ops: O(h) — O(log n) average, O(n) worst", "Alternative: sorted array → O(log n) search but O(n) insert", "Self-balancing trees (AVL, red-black) guarantee O(log n)"],
             "A sorted array gives fast search but slow inserts. A BST makes insert, search and remove all proportional to the height: log n on average, but linear if the tree degenerates. Self-balancing trees guarantee log n.",
             st, ["Remove the root when it has one child (no parent to relink)", "Equal values go right — be consistent", "Remove a value that doesn't exist → no-op"],
             "The nastiest case is removing the root when it has only one child, since there's no parent to relink. Be consistent that equal values go right.",
             ["Iterative versions use O(1) space", "Follow-up: make it self-balancing; add size for rank queries"],
             "Iterative versions avoid recursion overhead. Follow-ups include balancing and augmenting nodes with subtree sizes.",
             ["Insert walks down comparing values, going left for smaller and right otherwise, and attaches a new node at the first empty spot. Contains walks the same way and returns true on equality.",
              "Remove finds the node while tracking its parent. With two children, it copies the right subtree's minimum and removes that. With one child, it splices the child in, handling the root specially by copying the child's value and pointers."])

def BstTraversal():
    nodes, root = bst([10, 5, 15, 2, 5, 22, 1]); st = []; outs = {}
    def ino(i, o):
        if i is None: return
        ino(nodes[i][1], o); o.append(i); ino(nodes[i][2], o)
    def pre(i, o):
        if i is None: return
        o.append(i); pre(nodes[i][1], o); pre(nodes[i][2], o)
    def post(i, o):
        if i is None: return
        post(nodes[i][1], o); post(nodes[i][2], o); o.append(i)
    for name, f, rule in [("In-order", ino, "left, node, right"), ("Pre-order", pre, "node, left, right"), ("Post-order", post, "left, right, node")]:
        o = []; f(root, o); vals = [nodes[i][0] for i in o]
        st.append(_tw(nodes, root, {o[0]: "cur", o[-1]: "ok"}, f"{name} ({rule}): {vals}", f"{name}, {rule}: {', '.join(map(str, vals))}." + (" Notice in-order gives sorted values." if name == "In-order" else ""), side=[name, " ".join(map(str, vals))], notes={i: str(k + 1) for k, i in enumerate(o)}))
    return E(["All three are O(n) time, O(h) stack", "Only the position of 'visit' changes", "Iterative versions use an explicit stack"],
             "All three traversals visit every node once, linear time, with recursion depth equal to the height. The only difference is when we record the node relative to its children.",
             st, ["In-order of a BST = sorted order", "Empty tree → unchanged list", "Deep trees can overflow the call stack"],
             "In-order traversal of a BST yields sorted values. Very deep trees can overflow the call stack, so know the iterative versions.",
             ["Pre-order serialises/copies a tree; post-order deletes/evaluates", "Follow-up: Morris traversal with O(1) space"],
             "Pre-order is used to copy or serialise a tree; post-order to delete it or evaluate expressions. Morris traversal achieves constant space.",
             ["Each method checks for null, then the only difference is the line that adds the value: between the recursive calls for in-order, before them for pre-order, and after them for post-order."])

def FindKthLargestValueInBst():
    nodes, root = bst([15, 5, 20, 2, 5, 17, 22, 1, 3]); k = 3; order = []; st = []
    def rev(i):
        if i is None or len(order) >= k: return
        rev(nodes[i][2])
        if len(order) < k:
            order.append(i)
            st.append(_tw(nodes, root, {**{x: "done" for x in order[:-1]}, i: "ok" if len(order) == k else "cur"}, f"Visit #{len(order)}: {nodes[i][0]}" + (" ← k-th largest" if len(order) == k else ""), f"Reverse in-order visit number {len(order)} is {nodes[i][0]}." + (" That's the third largest, so we stop." if len(order) == k else ""), side=[f"k = {k}", "visited: " + " ".join(str(nodes[x][0]) for x in order)]))
            rev(nodes[i][1])
    rev(root)
    return E(["In-order into a list, take list[n−k] → O(n) time and space", "Reverse in-order, stop at k → O(h + k)", "Only visits what's needed"],
             "The simple approach collects all values in sorted order and indexes from the end, costing linear time and space. A reverse in-order traversal visits values from largest down and stops after k, so it costs only height plus k.",
             st, ["Duplicates count separately (5, 5)", "k = 1 → the maximum", "Stop recursion once k values are seen"],
             "Duplicate values count separately. Make sure recursion stops as soon as the k-th value is found.",
             ["Follow-up: many queries → augment nodes with subtree sizes", "Iterative reverse in-order with a stack"],
             "For repeated queries, store subtree sizes in each node to answer in log n.",
             ["The walk function returns early if the node is null or we've already seen k values. It recurses right first, then counts the current node, records it as the answer if it's the k-th, and only then goes left."])

def MinHeightBst():
    a = [1, 2, 5, 7, 10, 13, 14, 15, 22]; nodes = {}; st = []
    def build(lo, hi):
        if lo > hi: return None
        mid = (lo + hi) // 2; nid = str(mid); nodes[nid] = [a[mid], None, None]
        st.append(S("Worked example", [A(a, hl={mid: "ok"}, window=(lo, hi), ptr={"mid": mid}), TR({k: v[:] for k, v in nodes.items()}, "4", hl={nid: "cur"})], f"Range [{lo}, {hi}] → root {a[mid]}", f"In the range from {lo} to {hi}, the middle element {a[mid]} becomes the root of this subtree."))
        nodes[nid][1] = build(lo, mid - 1); nodes[nid][2] = build(mid + 1, hi); return nid
    build(0, len(a) - 1)
    return E(["Insert in sorted order → a linked-list-shaped tree, height n", "Insert values one by one in a smart order → O(n log n)", "Build directly from midpoints → O(n), height ⌈log₂(n+1)⌉"],
             "Inserting sorted values one at a time creates a chain of height n. Picking the middle element as the root and recursing on each half yields minimum height, and building nodes directly takes linear time.",
             pick(st, 6), ["Even-length ranges: either middle works", "Empty array → null", "Build nodes directly; don't call insert (O(n log n))"],
             "With an even range, either middle is fine. Creating nodes directly instead of calling insert keeps it linear.",
             ["Prove the height is minimal", "Follow-up: sorted linked list → BST in O(n)"],
             "A good follow-up converts a sorted linked list into a balanced BST in linear time by building in in-order.",
             ["Build takes a low and high index. If the range is empty it returns null. Otherwise it creates a node from the middle value and recursively builds its left from the lower half and its right from the upper half."])

def ReconstructBst():
    pre = [10, 4, 2, 1, 5, 17, 19, 18]; nodes = {}; st = []; idx = [0]
    def build(lo, hi, parent=None):
        if idx[0] == len(pre): return None
        v = pre[idx[0]]
        if not (lo <= v < hi): return None
        nid = str(idx[0]); idx[0] += 1; nodes[nid] = [v, None, None]
        st.append(S("Worked example", [A(pre, hl={int(nid): "cur", **{k: "done" for k in range(int(nid))}}, ptr={"idx": int(nid)}), TR({k: x[:] for k, x in nodes.items()}, "0", hl={nid: "cur"}), TX([f"bounds [{'-∞' if lo < -10**9 else lo}, {'∞' if hi > 10**9 else hi})"], h=0.35)],
                    f"{v} fits bounds → new node", f"The next value, {v}, fits within the bounds, so it becomes a node here. Its left subtree accepts values below {v}, its right subtree values from {v} up."))
        nodes[nid][1] = build(lo, v); nodes[nid][2] = build(v, hi); return nid
    build(-10**18, 10**18)
    return E(["Insert each value into a BST → O(n²) worst, O(n log n) average", "For each node, scan for where the right subtree starts → O(n²)", "Bounds recursion with a shared index → O(n)"],
             "Inserting each value from the root is quadratic in the worst case. Scanning for where the right subtree begins is also quadratic. Passing value bounds down and consuming the pre-order list with one shared index builds the tree in linear time.",
             pick(st, 6), ["Duplicates go right: use [lo, hi) bounds", "Use long bounds to avoid overflow", "Reset the shared index per call"],
             "Duplicates belong on the right, so the left bound is inclusive and the right exclusive. Use long bounds for infinity.",
             ["Explain why the index only moves forward", "Follow-up: from post-order; from in-order + pre-order (general tree)"],
             "Explain that each value is consumed exactly once. Follow-ups rebuild from post-order, or a general binary tree from in-order and pre-order.",
             ["We keep a shared index. Build returns null if the list is exhausted or the next value falls outside the current bounds. Otherwise it consumes the value, creates a node, builds the left with upper bound v, then the right with lower bound v."])

def ValidateBst():
    nodes, root = bst([10, 5, 15, 2, 5, 13, 22, 1]); nodes["5"][0] = 9  # make invalid: 9 in right subtree of 10? no: node5 is 13's slot
    nodes, root = bst([10, 5, 15, 2, 5, 13, 22, 1]); nodes["6"][0] = 22
    nodes["5"] = [8, None, None]  # 13 replaced by 8 → violates lower bound 10
    st = []
    for nid, lo, hi in [("0", "-∞", "∞"), ("1", "-∞", 10), ("2", 10, "∞"), ("5", 10, 15)]:
        v = nodes[nid][0]; ok = not ((lo != "-∞" and v < lo) or (hi != "∞" and v >= hi))
        st.append(_tw(nodes, root, {nid: "ok" if ok else "bad"}, f"{v} must be in [{lo}, {hi}) → {'ok' if ok else 'INVALID'}", f"Node {v} must be at least {lo} and less than {hi}. " + ("It is, so we continue." if ok else "It isn't: eight is in ten's right subtree, so the tree is not a valid BST."), side=[f"node {v}", f"bounds [{lo}, {hi})"]))
    return E(["Naive: compare each node only with its children — WRONG", "In-order traversal must be sorted → O(n)", "Bounds passed down → O(n), early exit"],
             "The tempting mistake is to compare each node only with its direct children, which misses violations deeper down. Either check that in-order traversal is sorted, or pass down bounds inherited from all ancestors, which lets us stop at the first violation.",
             st, ["Grandchild violations (the classic bug)", "Duplicates go right: left bound inclusive", "Use long bounds for Integer.MIN/MAX values"],
             "The classic bug is a grandchild that's fine relative to its parent but violates an ancestor. Duplicates go right, and long bounds handle extreme integer values.",
             ["Draw the counterexample before coding", "Follow-up: fix a BST with two swapped nodes (Repair BST)"],
             "Draw a counterexample for the naive approach before coding. The hard follow-up repairs a BST with two swapped nodes.",
             ["Valid returns true for null. It fails if the value is below the minimum or at least the maximum. Then it recurses left with the max tightened to the node's value, and right with the min raised to it."])

def BinaryTreeDiameter():
    nodes, root = level_tree([1, 3, 2, 7, 4, None, None, 8, None, None, 5, None, None, None, None, 9, None, None, None, None, None, 6]); best = [0]; st = []
    def h(i):
        if i is None: return 0
        l, r = h(nodes[i][1]), h(nodes[i][2])
        if l + r > best[0]: best[0] = l + r
        if l + r >= 1: st.append(_tw(nodes, root, {i: "cur"}, f"At {nodes[i][0]}: left {l} + right {r} = {l + r}; best {best[0]}", f"At node {nodes[i][0]}, the left height is {l} and the right height is {r}. A path through here has {l + r} edges. Best so far: {best[0]}.", side=[f"h(left) = {l}", f"h(right) = {r}", f"best = {best[0]}"]))
        return 1 + max(l, r)
    h(root)
    return E(["Brute force: diameter through each node via separate height calls → O(n²)", "Post-order computing height once per node → O(n)", "Diameter need not pass through the root"],
             "Computing heights separately for every node repeats work and is quadratic. A single post-order pass returns each subtree's height and, along the way, checks the path that bends through each node.",
             pick(st, 5), ["Diameter counts edges, not nodes", "Longest path may avoid the root", "Single node → 0"],
             "The diameter counts edges, and it often doesn't pass through the root, as in this example.",
             ["Return height, track best in a field/array", "Follow-up: max path SUM (Hard)"],
             "Return the height and track the best in a shared variable. The hard follow-up maximises path sum instead of length.",
             ["Height returns zero for null. It computes left and right heights, updates the best diameter with their sum, and returns one plus the larger height."])

def FindSuccessor():
    nodes, root = level_tree([1, 2, 3, 4, 5, None, None, 6]); st = []
    st.append(_tw(nodes, root, {"4": "cur"}, "Successor of 5: no right child", "Find the in-order successor of five. Five has no right child, so the successor is above it.", side=["in-order:", "6 4 2 5 1 3"]))
    st.append(_tw(nodes, root, {"4": "done", "1": "cur"}, "5 is 2's RIGHT child → keep climbing", "Five is its parent two's right child, so two comes before it. Keep climbing.", side=["in-order:", "6 4 2 5 1 3"]))
    st.append(_tw(nodes, root, {"1": "done", "0": "ok"}, "2 is 1's LEFT child → successor is 1", "Two is the left child of one, so one is the successor.", side=["in-order:", "6 4 2 5 1 3"]))
    st.append(_tw(nodes, root, {"0": "cur", "2": "ok"}, "Successor of 1: leftmost of right subtree → 3", "For node one, which has a right subtree, the successor is the leftmost node of that subtree: three.", side=["in-order:", "6 4 2 5 1 3"]))
    return E(["In-order traversal into a list, find node, take next → O(n)", "Parent pointers: two cases → O(h) time, O(1) space", "No full traversal needed"],
             "The simple approach does a full in-order traversal and returns the next element, linear time and space. With parent pointers, we only need two cases, costing at most the tree's height and constant space.",
             st, ["Last node in order → null", "Node with right subtree → leftmost of it", "Climb while we're a right child"],
             "The last node in order has no successor, so return null. Climb only while the current node is its parent's right child.",
             ["Follow-up: predecessor (mirror image)", "Follow-up: without parent pointers in a BST"],
             "The predecessor is the mirror image. In a BST without parent pointers, search from the root tracking the last left turn.",
             ["If the node has a right child, we go right once and then all the way left. Otherwise we climb while the current node is its parent's right child and return the parent, which is null if we ran off the top."])

def HeightBalancedBinaryTree():
    nodes, root = level_tree([1, 2, 3, 4, 5, None, 6, None, None, 7, 8]); st = []
    def h(i):
        if i is None: return 0
        l, r = h(nodes[i][1]), h(nodes[i][2]); bad = l == -1 or r == -1 or abs(l - r) > 1; res = -1 if bad else 1 + max(l, r)
        st.append(_tw(nodes, root, {i: "bad" if bad else "ok"}, f"Node {nodes[i][0]}: heights {l} and {r} → " + ("unbalanced" if bad else f"height {res}"), f"At node {nodes[i][0]}, the subtree heights are {l} and {r}. " + ("They differ by more than one, so it's unbalanced." if bad else f"That's balanced, with height {res}.")))
        return res
    ok = h(root) != -1
    return E(["Naive: compute height separately at every node → O(n²)", "Single post-order returning height or −1 → O(n)", "Fail fast propagates up immediately"],
             "Calling a separate height function at every node repeats work and is quadratic on skewed trees. A single post-order pass that returns the height, or minus one for unbalanced, checks everything in linear time.",
             pick(st, 5), ["Empty tree is balanced", "Check every node, not just the root", "Use a sentinel (−1) to short-circuit"],
             "An empty tree is balanced, and the condition must hold at every node, not just the root.",
             ["Follow-up: rebalance via rotations (AVL)", "Return a small object instead of a sentinel"],
             "In a real codebase, return a small object with height and balanced flag. A follow-up is how AVL trees rebalance with rotations.",
             ["The helper returns zero for null. It computes both child heights; if either is minus one or they differ by more than one, it returns minus one. Otherwise it returns one plus the larger."])

def InvertBinaryTree():
    nodes, root = level_tree([1, 2, 3, 4, 5, 6, 7]); st = [_tw(nodes, root, {}, "Original tree", "Here's the original tree.")]
    for i in ["0", "1", "2"]:
        nodes[i][1], nodes[i][2] = nodes[i][2], nodes[i][1]
        st.append(_tw(nodes, root, {i: "cur"}, f"Swap children of {nodes[i][0]}", f"At node {nodes[i][0]}, swap its left and right children."))
    return E(["Every node must be swapped once → O(n) is optimal", "Recursive (O(h) stack) or BFS queue (O(w) space)", "Order of visiting doesn't matter"],
             "Every node's children must be swapped, so linear time is optimal. Recursion uses stack space proportional to height; a breadth-first queue uses space proportional to the widest level. Order doesn't matter.",
             st, ["Null children are swapped too", "Swap before or after recursion — both fine", "Deep trees: prefer iterative"],
             "Swapping a null child is fine. For very deep trees, prefer the iterative version.",
             ["Mention the iterative BFS version", "Follow-up: check if two trees are mirrors (Symmetrical Tree)"],
             "Mention the iterative version, and relate it to checking whether two trees are mirrors.",
             ["If the node is null, return. Otherwise swap left and right with a temporary, then invert both subtrees."])

def MergeBinaryTrees():
    a, ra = level_tree([1, 3, 2, 7, 4]); b, rb = level_tree([1, 5, 9, 2, None, 7, 6]); st = []
    st.append(S("Worked example", [TR(a, ra, label="tree 1", w=0.5), TR(b, rb, label="tree 2", w=0.5)], "Two trees to overlay", "We overlay two trees: where both have a node, add the values; otherwise keep whichever exists.", layout="cols"))
    m = {k: v[:] for k, v in a.items()}
    for k, v in b.items():
        if k in m: m[k][0] += v[0]
        else: m[k] = v[:]
        p = (int(k) - 1) // 2
        if k != "0": m[str(p)][1 if int(k) % 2 else 2] = k
    st.append(S("Worked example", [TR(m, "0", hl={k: "ok" for k in a if k in b})], "Overlapping nodes summed", "Root one plus one gives two; three plus five gives eight; two plus nine gives eleven; seven plus two gives nine."))
    st.append(S("Worked example", [TR(m, "0", hl={k: "warn" for k in m if (k in a) != (k in b)})], "Missing on one side → reuse the other subtree", "Where only one tree has a node, like four from tree one, or seven and six from tree two, we simply reuse that subtree."))
    return E(["Build a brand-new tree → O(n + m) extra space", "Merge into tree 1 in place → O(min(n, m)) time", "Reuse subtrees where only one side exists"],
             "Building a new tree copies everything. Merging into the first tree in place is cheaper: we only recurse where both trees have nodes, and reuse a subtree whenever one side is missing.",
             st, ["Either tree may be null", "Mutates tree 1 (mention it)", "Reused subtrees are shared"],
             "Handle either tree being null, and mention that the result mutates and shares structure with the inputs.",
             ["Ask if inputs may be modified", "Iterative with a stack of pairs"],
             "Ask whether modifying the inputs is acceptable; otherwise build new nodes.",
             ["If either tree is null, return the other. Otherwise add the second value into the first, merge the left children, merge the right children, and return the first tree."])

def SplitBinaryTree():
    nodes, root = level_tree([1, 3, -2, 6, -5, 5, 2, 2]); st = []; sums = {}
    def s(i):
        if i is None: return 0
        v = nodes[i][0] + s(nodes[i][1]) + s(nodes[i][2]); sums[i] = v; return v
    tot = s(root); half = tot // 2
    st.append(_tw(nodes, root, {}, f"Total sum = {tot} → need a subtree summing to {half}", f"The whole tree sums to {tot}, which is even, so we need some subtree summing to exactly {half}.", notes={k: f"Σ{v}" for k, v in sums.items()}))
    hit = [k for k, v in sums.items() if v == half and k != root][0]
    st.append(_tw(nodes, root, {hit: "ok"}, f"Subtree at {nodes[hit][0]} sums to {half} → cut its edge", f"The subtree rooted at {nodes[hit][0]} sums to {half}. Cutting the edge above it splits the tree into two halves of {half} each.", notes={k: f"Σ{v}" for k, v in sums.items()}))
    return E(["Brute force: try cutting each edge, re-sum both parts → O(n²)", "Two passes: total, then post-order subtree sums → O(n)", "Need a subtree (not the whole tree) = total / 2"],
             "Cutting each edge and re-summing both parts is quadratic. Instead compute the total once, then a post-order pass gives every subtree sum; if any non-root subtree equals half the total, we can split.",
             st, ["Odd total → impossible (return 0)", "Exclude the root's own sum", "Negative values make greedy pruning unsafe"],
             "An odd total can't split. Exclude the root, since cutting nothing isn't a split. With negative values, you can't prune early.",
             ["Return the half-sum (problem's convention)", "Follow-up: maximise product of the two parts"],
             "This version returns the half sum, or zero. A popular follow-up maximises the product of the two parts.",
             ["We sum the whole tree; if the total is odd we return zero. Then check computes each subtree sum in post-order and sets a flag when a non-root subtree equals half."])

def SymmetricalTree():
    nodes, root = level_tree([1, 2, 2, 3, 4, 4, 3, 5, 6, None, None, None, None, 6, 5]); st = []
    for a, b in [("1", "2"), ("3", "6"), ("4", "5"), ("7", "14")]:
        st.append(_tw(nodes, root, {a: "cur", b: "cur"}, f"Compare {nodes[a][0]} (left) with {nodes[b][0]} (right) ✓", f"Compare the mirrored pair: {nodes[a][0]} on the left with {nodes[b][0]} on the right. They match, so continue with outer and inner children."))
    return E(["Build the mirror tree and compare → O(n) time, O(n) space", "Recursive pairwise mirror check → O(n), O(h) space", "Or BFS checking each level is a palindrome"],
             "You could build a mirrored copy and compare, using extra memory. Better is checking pairs directly: the left subtree's outer child pairs with the right subtree's outer child, and inner with inner.",
             st, ["One side null, the other not → false", "Values must match, not just shapes", "Empty tree → symmetric"],
             "If one side is null and the other isn't, return false. Both structure and values must mirror.",
             ["Iterative with a queue of pairs", "Relation to Invert Binary Tree"],
             "An iterative version uses a queue of node pairs. Note that a tree is symmetric when it equals its own inversion.",
             ["Mirror returns true if both nodes are null and false if just one is. Otherwise values must be equal, and we recursively compare left's left with right's right, and left's right with right's left."])
