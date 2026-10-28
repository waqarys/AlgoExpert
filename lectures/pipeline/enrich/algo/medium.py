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
