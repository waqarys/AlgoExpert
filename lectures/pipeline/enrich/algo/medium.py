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

def LevenshteinDistance():
    a, b = "abc", "yabd"; R, C = len(a) + 1, len(b) + 1; dp = [[None] * C for _ in range(R)]; st = []
    for j in range(C): dp[0][j] = j
    for i in range(R): dp[i][0] = i
    st.append(S("Worked example", [T(dp, rowh=["", *a], colh=["", "", *b], hl={(0, j): "done" for j in range(C)} | {(i, 0): "done" for i in range(R)})], "Base row/column: edits from/to the empty string", "The first row and column are the cost of building a prefix from nothing: just insertions or deletions."))
    for i in range(1, R):
        for j in range(1, C):
            same = a[i - 1] == b[j - 1]; dp[i][j] = dp[i - 1][j - 1] if same else 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
            if (i, j) in [(1, 2), (2, 3), (3, 3), (3, 4)]:
                st.append(S("Worked example", [T([[x if x is not None else "" for x in r] for r in dp], rowh=["", *a], colh=["", "", *b], hl={(i, j): "ok" if same else "cur", (i - 1, j - 1): "warn"})],
                            f"'{a[:i]}' → '{b[:j]}': " + (f"'{a[i - 1]}' = '{b[j - 1]}' → copy diagonal {dp[i][j]}" if same else f"1 + min(neighbours) = {dp[i][j]}"),
                            f"Turning {a[:i]} into {b[:j]}: " + (f"the last letters are both {a[i - 1]}, so the cost equals the diagonal, {dp[i][j]}." if same else f"the last letters differ, so we pay one plus the cheapest of replace, delete or insert: {dp[i][j]}.")))
    return E(["Brute force: recursively try insert/delete/replace → O(3^(n+m))", "DP table over prefixes → O(n·m) time", "Keep only two rows → O(min(n, m)) space"],
             "Recursively trying every edit branches three ways at each step, which is exponential. The same subproblems repeat, so a table over prefixes solves it in n times m. Since each row only needs the previous one, two rows suffice.",
             st, ["Empty strings: distance = other length", "Swap so the shorter string defines the row length", "Off-by-one: dp is (n+1) × (m+1)"],
             "If either string is empty, the answer is the other's length. The table has one extra row and column for the empty prefix, a common off-by-one trap.",
             ["Explain the three neighbours: replace, delete, insert", "Follow-up: reconstruct the edits; weighted costs"],
             "Name the three neighbours explicitly: diagonal is replace, above is delete, left is insert. Follow-ups reconstruct the edit script or use weighted costs.",
             ["We swap so b is the shorter string, initialise the previous row to zero through m, and for each character of a fill the current row: equal characters copy the diagonal, otherwise one plus the min of the three neighbours. Then we swap rows and return the last value."])

def MaxSubsetSumNoAdjacent():
    a = [75, 105, 120, 75, 90, 135]; prev = cur = 0; st = []; dp = []
    for i, x in enumerate(a):
        nxt = max(cur, prev + x); take = prev + x > cur; prev, cur = cur, nxt; dp.append(cur)
        st.append(S("Worked example", [A(a, hl={i: "ok" if take else "bad"}, ptr={"i": i}, label="values"), A(dp + [""] * (len(a) - len(dp)), hl={i: "cur"}, label="best sum up to i"), TX([f"max(skip {prev}, take {(dp[i - 2] if i >= 2 else 0)} + {x})" ], h=0.4)],
                    f"best[{i}] = {cur} ({'take' if take else 'skip'} {x})", f"At {x}: skipping keeps {prev}; taking adds {x} to the best two back. " + (f"Taking wins, so the best is {cur}." if take else f"Skipping wins, so the best stays {cur}.")))
    return E(["Brute force: all subsets without neighbours → exponential", "DP array best[i] → O(n) time, O(n) space", "Only two previous values needed → O(1) space"],
             "Trying every non-adjacent subset is exponential. A DP where best i is the max of best i minus one and best i minus two plus the value is linear, and only the last two values are ever needed.",
             pick(st, 6), ["Empty array → 0", "Single element → itself", "Negative numbers: allow choosing nothing (0)"],
             "An empty array gives zero. With negatives, choosing nothing is allowed, which the zero initial values handle.",
             ["This is House Robber", "Follow-up: circular array (run twice)"],
             "This is the classic house robber problem. The circular version runs the algorithm twice, excluding the first or last house.",
             ["We keep prev and cur, both starting at zero. For each value, next is the max of cur and prev plus the value; then we slide: prev becomes cur and cur becomes next."])

def MinNumberOfCoinsForChange():
    n, den = 7, [1, 5, 10]; INF = "∞"; dp = [0] + [INF] * n; st = []
    for d in den:
        if d > n: st.append(S("Worked example", [A(dp), TX([f"coin {d} > {n}: no change"])], f"Coin {d} is too big", f"Coin {d} is bigger than {n}, so it can't help.")); continue
        for a_ in range(d, n + 1):
            if dp[a_ - d] != INF and (dp[a_] == INF or dp[a_ - d] + 1 < dp[a_]): dp[a_] = dp[a_ - d] + 1
        st.append(S("Worked example", [A(dp, hl={k: "ok" for k in range(d, n + 1)}, label="min coins for each amount 0…7"), TX([f"after coin {d}"])], f"After coin {d}: dp = {dp}", f"Processing coin {d}: each amount from {d} up tries using one {d}-coin plus the best for the remainder. Now seven needs {dp[7]} coins."))
    return E(["Greedy (largest coin first) can fail, e.g. coins [1, 3, 4], n = 6", "Recursion over choices → exponential", "Bottom-up DP → O(n · d) time, O(n) space"],
             "Greedy, always taking the biggest coin, fails for coins like one, three and four with six: greedy gives four, one, one, but three plus three is better. Recursion explores exponentially many choices. A bottom-up table over amounts takes n times the number of coins.",
             st, ["Amount 0 → 0 coins", "Unreachable → −1", "Guard INF + 1 overflow"],
             "Zero needs zero coins, unreachable amounts return minus one, and you must check for infinity before adding one, to avoid overflow.",
             ["Show the greedy counterexample", "Follow-up: return the actual coins (store choices)"],
             "Show the greedy counterexample early. A follow-up returns the coins themselves by storing the last coin used per amount.",
             ["We fill dp with max value and set dp of zero to zero. For each coin, for each amount from the coin up, if the remainder is reachable we take the min with one more coin. Finally we map max value to minus one."])

def NumberOfWaysToMakeChange():
    n, den = 6, [1, 5]; w = [1] + [0] * n; st = [S("Worked example", [A(w, label="ways to make 0…6")], "ways[0] = 1 (use no coins)", "There's exactly one way to make zero: use no coins.")]
    for d in den:
        for a_ in range(d, n + 1): w[a_] += w[a_ - d]
        st.append(S("Worked example", [A(w, hl={k: "ok" for k in range(d, n + 1)}, label="ways to make 0…6"), TX([f"after coin {d}: ways[a] += ways[a − {d}]"])], f"After coin {d}: {w}", f"Adding coin {d}: every amount from {d} up gains the ways to make the remainder. With coins one and five, there are {w[6]} ways to make six: six ones, or five plus one."))
    return E(["Recursion over coins → exponential and double-counts orders", "DP with coins in the OUTER loop → counts combinations", "O(n · d) time, O(n) space"],
             "Naive recursion is exponential and easily counts the same combination in different orders. Putting coins in the outer loop means each combination is built in a fixed coin order, so it's counted exactly once.",
             st, ["Loop order matters: amounts outer → counts permutations", "ways[0] = 1", "Large counts may overflow"],
             "If you swap the loops you count permutations instead of combinations, a very common bug.",
             ["Explain combinations vs permutations", "Follow-up: limited coin supply"],
             "Explain the combination versus permutation distinction clearly. A follow-up limits how many of each coin you have.",
             ["We set ways of zero to one. For each coin, for each amount from that coin to n, add the ways for amount minus coin. Return ways of n."])

def NumberOfWaysToTraverseGraph():
    W, H = 4, 3; g = [[1] * W for _ in range(H)]; st = []
    for r in range(H):
        for c in range(W):
            if r and c: g[r][c] = g[r - 1][c] + g[r][c - 1]
    st.append(S("Worked example", [T([[1] * W] + [[1] + [""] * (W - 1) for _ in range(H - 1)], hl={(0, c): "done" for c in range(W)} | {(r, 0): "done" for r in range(H)})], "Edges: exactly one way (straight line)", "Cells on the top row or left column can only be reached one way."))
    st.append(S("Worked example", [T(g, hl={(1, 1): "cur", (0, 1): "warn", (1, 0): "warn"})], "Each cell = above + left", "Every other cell adds the ways from above and from the left. Cell one-one is one plus one, two."))
    st.append(S("Worked example", [T(g, hl={(H - 1, W - 1): "ok"})], f"Bottom-right = {g[-1][-1]}", f"Filling the grid, the bottom-right cell holds {g[-1][-1]} paths."))
    st.append(S("Worked example", [TX([f"moves: {W - 1} right + {H - 1} down = {W + H - 2}", f"choose which {H - 1} are 'down': C({W + H - 2}, {H - 1}) = {g[-1][-1]}"])], "Shortcut: a binomial coefficient", "The solution here uses a shortcut: every path is some arrangement of three rights and two downs, so the count is five choose two, ten. That's constant space and linear time."))
    return E(["Recursion: ways(r,c) = ways(r−1,c) + ways(r,c−1) → exponential", "DP grid → O(w·h)", "Combinatorics: C(w+h−2, h−1) → O(min(w,h))"],
             "Plain recursion recomputes paths exponentially. A DP grid fills in w times h. Since every path is just an ordering of rights and downs, a binomial coefficient gives the answer directly.",
             st, ["1×n grids → 1", "Compute C(n,k) incrementally to avoid overflow", "Width and height are counts, not indices"],
             "A single row or column has one path. Compute the binomial incrementally, multiplying then dividing, to keep values exact and avoid overflow.",
             ["Present DP first, then the formula", "Follow-up: obstacles → DP is required"],
             "Present the DP first, then mention the formula. With obstacles, the formula breaks and DP is required.",
             ["We compute n as total moves and k as the smaller dimension minus one, then build the binomial coefficient incrementally: multiply by n minus k plus i and divide by i, which always stays an integer."])

def KadanesAlgorithm():
    a = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]; cur = best = a[0]; st = []
    for i in range(1, len(a)):
        restart = a[i] > cur + a[i]; cur = max(a[i], cur + a[i]); best = max(best, cur)
        if i in (2, 3, 8, 9, 13, 15):
            st.append(S("Worked example", [A(a, hl={i: "bad" if restart else "cur"}, ptr={"i": i}), TX([f"best ending here = {cur}" + (" (restart)" if restart else ""), f"best overall = {best}"])],
                        f"i={i}: cur = {cur}, best = {best}", f"At {a[i]}: " + ("starting fresh beats extending, so we restart here." if restart else f"extending the previous run gives {cur}.") + f" The best overall is {best}."))
    return E(["Brute force: all subarrays → O(n²) (O(n³) naive)", "Divide and conquer → O(n log n)", "Kadane: best ending here → O(n), O(1)"],
             "Summing every subarray is quadratic. Divide and conquer is n log n. Kadane's algorithm keeps the best sum ending at each index: either extend the previous run or start fresh, which is linear with constant space.",
             st, ["All negative → the largest single element", "Initialise with a[0], not 0", "Overflow with large values"],
             "If everything is negative, the answer is the largest single element, which is why we initialise with the first element rather than zero.",
             ["Follow-up: return the indices", "Follow-up: circular array, 2D max submatrix"],
             "Follow-ups return the start and end indices, handle circular arrays, or extend to two-dimensional submatrices.",
             ["Cur and best start at the first element. For each next element, cur becomes the max of the element alone or cur plus the element, and best tracks the max of cur."])

def StableInternships():
    interns = [[0, 1, 2], [0, 2, 1], [1, 2, 0]]; teams = [[2, 1, 0], [0, 1, 2], [0, 1, 2]]; n = 3
    rank = [[0] * n for _ in range(n)]
    for t in range(n):
        for r in range(n): rank[t][teams[t][r]] = r
    match = [-1] * n; nxt = [0] * n; free = [0, 1, 2]; st = []
    while free:
        i = free.pop(0); t = interns[i][nxt[i]]; nxt[i] += 1; cur = match[t]
        if cur == -1: match[t] = i; res = f"team {t} was free → accepts intern {i}"
        elif rank[t][i] < rank[t][cur]: match[t] = i; free.append(cur); res = f"team {t} prefers {i} over {cur} → {cur} is freed"
        else: free.append(i); res = f"team {t} keeps {cur}, rejects {i}"
        st.append(S("Worked example", [T(interns, rowh=[f"intern {k}" for k in range(n)], label="intern preferences", w=0.33), T(teams, rowh=[f"team {k}" for k in range(n)], label="team preferences", w=0.33), TX(["matches:"] + [f"team {k} ↔ {'–' if match[k] < 0 else 'intern ' + str(match[k])}" for k in range(n)] + [f"free: {free}"], w=0.34, h=1, size=18)],
                    f"Intern {i} proposes to team {t}: {res}", f"Intern {i} proposes to team {t}, their next choice. {res.capitalize()}.", layout="cols"))
    return E(["Brute force: check all n! matchings for stability", "Gale–Shapley proposals → O(n²)", "Precompute team rankings for O(1) comparisons"],
             "Checking all n factorial matchings is hopeless. Gale-Shapley has interns propose in preference order, and each team keeps the best proposal so far. Each intern proposes at most n times, so it's quadratic.",
             st, ["Precompute rank[team][intern] for O(1) comparisons", "Result is intern-optimal", "Always terminates with a perfect matching"],
             "Precompute each team's ranking of interns so comparisons are constant time. The result is the best stable matching for the proposing side.",
             ["Explain why it's stable (no blocking pair)", "Follow-up: who benefits — the proposing side"],
             "Be ready to argue stability: no intern and team both prefer each other over their matches. The proposing side gets its best stable outcome.",
             ["We build a rank table for teams, then a queue of free interns. Each free intern proposes to their next team. A free team accepts; otherwise the team keeps whichever intern it ranks higher and the other goes back in the queue. Finally we output intern-team pairs."])

def UnionFind():
    par = {k: k for k in range(5)}; rank = {k: 0 for k in range(5)}; st = []
    def find(v):
        if par[v] != v: par[v] = find(par[v])
        return par[v]
    def draw(cap, nar, hl=None):
        pos = {k: [0.1 + 0.2 * k, 0.75] for k in range(5)}
        for k in range(5):
            d = 0; x = k
            while par[x] != x: x = par[x]; d += 1
            pos[k] = [pos[k][0], 0.75 - 0.35 * d]
        return S("Worked example", [G(pos, [(k, par[k]) for k in range(5) if par[k] != k], hl=hl or {}, directed=True, w=0.65), TX(["parent: " + str([par[k] for k in range(5)]), "rank:   " + str([rank[k] for k in range(5)])], w=0.35, h=1, size=18)], cap, nar, layout="cols")
    st.append(draw("createSet(0…4): every node is its own root", "Create five sets. Every node is its own parent, so each is a root."))
    for a, b in [(0, 1), (2, 3), (0, 3)]:
        ra, rb = find(a), find(b)
        if rank[ra] < rank[rb]: par[ra] = rb
        elif rank[ra] > rank[rb]: par[rb] = ra
        else: par[rb] = ra; rank[ra] += 1
        st.append(draw(f"union({a}, {b}): roots {ra}, {rb} → attach by rank", f"Union {a} and {b}: their roots are {ra} and {rb}. " + ("Equal ranks, so the second root goes under the first and its rank grows." if rank[ra] and par[rb] == ra and rank[ra] > 0 else "The lower-rank root goes under the higher one."), {ra: "ok", rb: "cur"}))
    find(3); st.append(draw("find(3) → 0 with path compression", "Finding three walks up to the root, zero, and compresses the path so three points straight at zero next time.", {3: "cur", 0: "ok"}))
    return E(["Naive: label every element with its set ID → union is O(n)", "Plain parent trees → find can be O(n)", "Rank + path compression → nearly O(1) amortised (α(n))"],
             "Storing a set ID per element makes union linear, since you relabel a whole set. Parent pointers make union cheap, but trees can become long chains. Union by rank plus path compression keeps operations effectively constant, inverse-Ackermann time.",
             st, ["find on an unknown value → null", "Union of the same set → no-op", "Recursive find depth (iterative alternative)"],
             "Return null for unknown values, and make union a no-op when both are already in the same set.",
             ["Used in Kruskal's MST and connectivity queries", "Follow-up: union by size; count components"],
             "Union-find powers Kruskal's algorithm and dynamic connectivity. Union by size works as well as rank.",
             ["Create set makes a node its own parent with rank zero. Find recursively finds the root and rewrites the parent pointer to it, which is path compression. Union finds both roots and attaches the lower-rank root under the higher one, bumping rank on ties."])

def BreadthFirstSearch():
    g = {"A": ["B", "C", "D"], "B": ["E", "F"], "C": [], "D": ["G", "H"], "E": [], "F": ["I", "J"], "G": ["K"], "H": [], "I": [], "J": [], "K": []}
    pos = {"A": [.5, .9], "B": [.2, .65], "C": [.5, .65], "D": [.8, .65], "E": [.08, .4], "F": [.3, .4], "G": [.7, .4], "H": [.92, .4], "I": [.22, .12], "J": [.4, .12], "K": [.7, .12]}
    edges = [(a, b) for a in g for b in g[a]]; q = ["A"]; out = []; st = []
    while q:
        u = q.pop(0); out.append(u); q += g[u]
        st.append(S("Worked example", [G(pos, edges, hl={**{x: "done" for x in out[:-1]}, u: "cur", **{x: "warn" for x in q}}, directed=True, h=1.6), Q(q, h=0.6)],
                    f"Dequeue {u}; enqueue {', '.join(g[u]) or 'nothing'}", f"Dequeue {u} and record it. " + (f"Its children, {', '.join(g[u])}, join the back of the queue." if g[u] else "It has no children.")))
    return E(["Same O(V + E) as DFS — the order is what differs", "Queue (FIFO) instead of stack/recursion", "BFS gives shortest paths in unweighted graphs"],
             "Breadth-first search is linear, like depth-first search; what changes is using a queue, so nodes come out level by level. That's why BFS finds shortest paths in unweighted graphs.",
             pick(st, 6), ["Use a real queue (ArrayDeque), not list.remove(0)", "General graphs need a visited set", "Children enqueued left to right"],
             "Use a proper queue; removing from the front of an array list is linear. On general graphs, mark nodes visited when you enqueue them.",
             ["Follow-up: level-order with level boundaries", "Follow-up: shortest path in a grid"],
             "Follow-ups print each level separately or find shortest paths in a grid.",
             ["We push the start node onto an array deque. While it's non-empty, we poll a node, append its name, and add all its children to the back."])

def CycleInGraph():
    edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]; pos = {0: [.15, .75], 1: [.45, .75], 2: [.45, .25], 3: [.8, .75], 4: [.8, .25], 5: [.95, .5]}
    E_ = [(u, v) for u in range(6) for v in edges[u]]; color = [0] * 6; st = []; found = [False]
    def dfs(v):
        color[v] = 1
        st.append(S("Worked example", [G(pos, E_, hl={k: ("cur" if c == 1 else "done") for k, c in enumerate(color) if c}, directed=True, w=0.65), TX(["grey = on stack", "dark = finished", "colors: " + str(color)], w=0.35, h=1, size=18)], f"Enter {v} (grey = on the recursion stack)", f"Enter node {v} and colour it grey, meaning it's on the current path.", layout="cols"))
        for w in edges[v]:
            if color[w] == 1:
                st.append(S("Worked example", [G(pos, E_, hl={k: ("cur" if c == 1 else "done") for k, c in enumerate(color) if c}, ehl=[(v, w)], directed=True, w=0.65), TX([f"edge {v} → {w}", f"{w} is grey → back edge", "cycle!"], w=0.35, h=1)], f"Edge {v} → {w} hits a grey node → cycle", f"Node {v} has an edge to {w}, which is still grey, on the current path. That's a back edge, so there's a cycle.", layout="cols"))
                found[0] = True; return True
            if color[w] == 0 and dfs(w): return True
        color[v] = 2; return False
    dfs(0)
    return E(["Brute force: from each node, DFS to see if you return → O(V·(V+E))", "Single DFS with three colours → O(V + E)", "Alternative: Kahn's topological sort fails ⇒ cycle"],
             "Running a separate search from every node to see if it returns is slow. One depth-first search with three colours finds a cycle in linear time: an edge to a node that's still on the recursion stack is a back edge. Kahn's algorithm is an alternative.",
             st, ["Visited ≠ on-stack: finished (black) nodes are safe", "Self-loops count as cycles", "Disconnected graphs: start DFS from every node"],
             "Don't confuse visited with on the stack: reaching a finished node isn't a cycle. Self-loops count, and you must start from every unvisited node to cover disconnected parts.",
             ["Explain white/grey/black clearly", "Follow-up: undirected graphs (ignore the parent edge)"],
             "Explain the three colours clearly. For undirected graphs, the rule changes: ignore the edge back to the parent.",
             ["We colour every node white, then DFS from each unvisited node. DFS marks the node grey, returns true if any neighbour is grey or if recursing into a white neighbour finds a cycle, and marks the node black when finished."])

def MinimumPassesOfMatrix():
    m = [[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]]; R, C = 3, 5; q = [(r, c) for r in range(R) for c in range(C) if m[r][c] > 0]; passes = 0; st = []
    st.append(S("Worked example", [T(m, hl={x: "ok" for x in q})], "Start: all positives in the queue", "Every positive cell starts in the queue. Each pass, they flip their negative neighbours."))
    while q:
        nq = []
        for r, c in q:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0 <= cc < C and m[rr][cc] < 0: m[rr][cc] = -m[rr][cc]; nq.append((rr, cc))
        if nq:
            passes += 1
            st.append(S("Worked example", [T(m, hl={x: "cur" for x in nq})], f"Pass {passes}: {len(nq)} cell(s) flipped", f"Pass {passes}: {len(nq)} negative cells next to positives become positive. They join the queue for the next pass."))
        q = nq
    left = any(v < 0 for row in m for v in row)
    st.append(S("Worked example", [T(m)], f"No negatives left → {passes} passes" if not left else "Negatives remain → −1", f"No negatives remain, so the answer is {passes} passes."))
    return E(["Simulate passes by rescanning the whole matrix → O((w·h)²)", "Multi-source BFS: one level per pass → O(w·h)", "Zeros block propagation"],
             "Simulating each pass by rescanning the whole matrix can be quadratic in the number of cells. Multi-source breadth-first search starts from all positives at once, and each BFS level is exactly one pass.",
             st, ["Negatives unreachable (walled by zeros) → −1", "No negatives at all → 0", "Only count passes that flip something"],
             "If some negatives are surrounded by zeros, return minus one. With no negatives, the answer is zero, so only count passes that flip something.",
             ["Same pattern: Rotting Oranges", "Explain why BFS levels = passes"],
             "This is the rotting oranges pattern. Explain that BFS levels correspond exactly to passes.",
             ["We enqueue all positive cells. Each round processes the current queue size, flips negative neighbours and enqueues them, and counts the pass if anything flipped. At the end, any remaining negative means minus one."])

def RemoveIslands():
    m = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1]]; R, C = 6, 6
    safe = set(); stack = [(r, c) for r in range(R) for c in range(C) if (r in (0, R - 1) or c in (0, C - 1)) and m[r][c] == 1]; safe |= set(stack)
    st = [S("Worked example", [T(m, hl={x: "ok" for x in safe})], "Border 1s are safe (not islands)", "Any one on the border, and anything connected to it, isn't an island. Start a flood fill from every border one.")]
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C and m[rr][cc] == 1 and (rr, cc) not in safe: safe.add((rr, cc)); stack.append((rr, cc))
    st.append(S("Worked example", [T(m, hl={**{x: "ok" for x in safe}, **{(r, c): "bad" for r in range(R) for c in range(C) if m[r][c] == 1 and (r, c) not in safe}})], "Flood fill done: red cells are islands", "After the flood fill, the green ones are connected to the border. The red ones are islands."))
    out = [[1 if (r, c) in safe else 0 for c in range(C)] for r in range(R)]
    st.append(S("Worked example", [T(out, hl={(r, c): "bad" for r in range(R) for c in range(C) if m[r][c] == 1 and (r, c) not in safe})], "Islands removed", "Turn the islands into zeros. Everything connected to the border stays."))
    return E(["Brute force: DFS from each interior 1 to see if it reaches the border → O((w·h)²)", "Flip the question: flood-fill from the border → O(w·h)", "Mark safe cells in place (2), then rewrite"],
             "Checking each interior one separately for a path to the border repeats work. Flipping the question, flood-filling from the border to mark safe cells, solves it in one linear pass.",
             st, ["Diagonals don't connect (4-directional)", "Recursive DFS can overflow on large grids → use a stack", "Restore marks at the end"],
             "Only four directions count. Use an explicit stack to avoid recursion depth problems, and convert the temporary marks back at the end.",
             ["Same idea: Surrounded Regions", "Follow-up: count islands (River Sizes)"],
             "This is the surrounded regions pattern; counting islands is the River Sizes problem.",
             ["We push every border one onto a stack and mark it two. Popping cells, we mark and push neighbouring ones. Finally, cells marked two become one and everything else becomes zero."])

def RiverSizes():
    m = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]; R, C = 5, 5; seen = set(); sizes = []; st = []
    for r in range(R):
        for c in range(C):
            if m[r][c] != 1 or (r, c) in seen: continue
            comp = []; stack = [(r, c)]; seen.add((r, c))
            while stack:
                x = stack.pop(); comp.append(x)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    y = (x[0] + dr, x[1] + dc)
                    if 0 <= y[0] < R and 0 <= y[1] < C and m[y[0]][y[1]] == 1 and y not in seen: seen.add(y); stack.append(y)
            sizes.append(len(comp))
            st.append(S("Worked example", [T(m, hl={**{x: "done" for x in seen}, **{x: "ok" for x in comp}}, w=0.5), TX(["sizes:", str(sizes)], w=0.5, h=1)], f"River at ({r},{c}) → size {len(comp)}", f"Scanning reaches an unvisited one at row {r}, column {c}. A flood fill finds a river of size {len(comp)}.", layout="cols"))
    return E(["Brute force: re-explore from every 1 → repeated work", "Visited matrix + DFS/BFS → each cell once, O(w·h)", "Iterative stack avoids recursion limits"],
             "Exploring from every one without remembering visits repeats work. With a visited matrix, each cell is processed once, linear in the grid size.",
             pick(st, 6), ["Mark visited when pushing, not popping", "4-directional adjacency", "Empty grid / no rivers → []"],
             "Mark cells visited when you push them, otherwise the same cell can be pushed twice and counted twice.",
             ["Mention union-find alternative", "Follow-up: largest island after flipping one 0 (Largest Island)"],
             "Union-find is an alternative. The hard follow-up flips one zero to maximise an island.",
             ["We scan every cell. On an unvisited one, we start a stack-based flood fill, counting popped cells and pushing unvisited neighbouring ones, then record the size."])

def SingleCycleCheck():
    a = [2, 3, 1, -4, -4, 2]; n = len(a); idx = 0; vis = []; st = []
    for k in range(n):
        if k > 0 and idx == 0: break
        nxt = (idx + a[idx]) % n; vis.append(idx)
        st.append(S("Worked example", [A(a, hl={**{x: "done" for x in vis[:-1]}, idx: "cur", nxt: "warn"}, ptr={"at": idx}), TX([f"jump {a[idx]:+d}: {idx} → {nxt}", f"jumps so far: {k + 1}"])], f"{idx} → {nxt}", f"From index {idx}, jump {a[idx]} to index {nxt}, wrapping around if needed."))
        idx = nxt
    st.append(S("Worked example", [A(a, hl={x: "ok" for x in range(n)}, ptr={"at": idx})], f"After {n} jumps we're back at 0 → single cycle", f"After exactly {n} jumps, we're back at index zero, and we never returned early. It's a single cycle."))
    return E(["Visited array → O(n) space", "Count jumps instead: n jumps, no early return to 0 → O(1) space", "Floor-mod handles negative jumps"],
             "A visited array works but uses extra space. Counting is enough: if we make n jumps, never land on index zero early, and end at zero, every index was visited exactly once.",
             pick(st, 6), ["Negative jumps: use floorMod", "Large jumps wrap multiple times", "Returning to 0 early → false"],
             "Use floor mod so negative jumps wrap correctly, and remember that returning to zero too early means a smaller cycle.",
             ["Explain why n jumps + end at 0 suffices", "Follow-up: detect any cycle from any start"],
             "Explain the counting argument carefully; that's what interviewers look for.",
             ["We loop n times. If we land back on zero after at least one jump but before n jumps, we return false. Each step moves the index by the value with floor mod. Finally we check we're at zero."])

def TwoColorable():
    edges = [[1, 2], [0, 2], [0, 1]]; pos = {0: [.25, .8], 1: [.75, .8], 2: [.5, .2]}; E_ = [(0, 1), (1, 2), (0, 2)]; st = []
    st.append(S("Worked example", [G(pos, E_, hl={0: "acc"}), TX(["0: blue"], h=0.4)], "Colour 0 blue", "Start by colouring node zero blue."))
    st.append(S("Worked example", [G(pos, E_, hl={0: "acc", 1: "warn", 2: "warn"}, ehl=[(0, 1), (0, 2)]), TX(["1, 2: pink (opposite of 0)"], h=0.4)], "Neighbours 1 and 2 get pink", "Its neighbours, one and two, must get the opposite colour, pink."))
    st.append(S("Worked example", [G(pos, E_, hl={0: "acc", 1: "bad", 2: "bad"}, ehl=[(1, 2)]), TX(["edge 1–2: both pink ✗"], h=0.4)], "Edge 1–2 joins two pink nodes → not 2-colourable", "But one and two are connected, and both are pink. A triangle is an odd cycle, so it can't be two-coloured."))
    return E(["Brute force: try all 2ⁿ colourings", "BFS/DFS assigning alternating colours → O(V + E)", "Bipartite ⇔ no odd cycle"],
             "Trying every colouring is exponential. Instead, colour a node, give each neighbour the opposite colour, and look for a conflict, in linear time. A graph is two-colourable exactly when it has no odd cycle.",
             st, ["Disconnected graphs: start from every uncoloured node", "Self-loop → false", "Undirected edges appear in both lists"],
             "Start a search from every uncoloured node for disconnected graphs. A self-loop makes it impossible.",
             ["Explain the odd-cycle characterisation", "Applications: scheduling into two groups"],
             "Mention the odd-cycle characterisation and practical uses like splitting into two conflict-free groups.",
             ["We keep a colour per node. For each uncoloured start, colour it one and push it. Popping a node, uncoloured neighbours get the opposite colour; a neighbour with the same colour returns false."])

def YoungestCommonAncestor():
    nodes = {"A": ["A", "B", "C"], "B": ["B", "D", "E"], "C": ["C", "F", "G"], "D": ["D", "H", "I"], "E": ["E", None, None], "F": ["F", None, None], "G": ["G", None, None], "H": ["H", None, None], "I": ["I", None, None]}
    st = [S("Worked example", [TR(nodes, "A", hl={"E": "cur", "I": "cur"}), TX(["depth(E) = 2, depth(I) = 3"], h=0.35)], "Descendants E and I; depths 2 and 3", "Find the youngest common ancestor of E and I. E is at depth two, I at depth three."),
          S("Worked example", [TR(nodes, "A", hl={"E": "cur", "D": "cur", "I": "done"}), TX(["lift I one level → D"], h=0.35)], "Lift the deeper one: I → D", "First lift the deeper node, I, by one level to D, so both are at depth two."),
          S("Worked example", [TR(nodes, "A", hl={"B": "ok"}), TX(["E → B, D → B: equal"], h=0.35)], "Move both up: E → B, D → B → answer B", "Now move both up together. E goes to B, D goes to B. They meet: the answer is B.")]
    return E(["Store all ancestors of one node in a set, walk up the other → O(d) space", "Equalise depths, then climb together → O(d) time, O(1) space", "d = depth of the deeper node"],
             "One approach stores all of one node's ancestors in a set, then walks up from the other until it finds one. Equalising depths and then climbing both in lockstep avoids extra memory.",
             st, ["One node is the ancestor of the other", "Both nodes are the same", "The answer may be the top ancestor"],
             "If one node is the ancestor of the other, the algorithm returns it naturally. The same node twice returns itself.",
             ["Follow-up: binary tree without parent pointers (LCA)", "Follow-up: many queries → binary lifting"],
             "Without parent pointers, use the recursive lowest common ancestor. For many queries, binary lifting answers each in log time.",
             ["We compute both depths by walking up to the top. Then we lift the deeper node until depths match, and finally move both up together until they're the same node."])

def TaskAssignment():
    k, t = 3, [1, 3, 5, 3, 1, 4]; idx = sorted(range(len(t)), key=lambda i: t[i]); st = [S("Worked example", [A(t, label="task durations"), A(idx, label="indices sorted by duration")], "Sort task indices by duration", "Sort the task indices by duration, keeping the original indices so we can report them.")]
    for i in range(k):
        a, b = idx[i], idx[-1 - i]
        st.append(S("Worked example", [A([t[x] for x in idx], hl={i: "ok", len(t) - 1 - i: "ok", **{j: "done" for j in list(range(i)) + list(range(len(t) - i, len(t)))}}, label="sorted durations"), TX([f"worker {i + 1}: tasks {a} & {b} → {t[a]} + {t[b]} = {t[a] + t[b]}"])],
                    f"Pair shortest with longest: {t[a]} + {t[b]}", f"Worker {i + 1} gets the shortest remaining task, {t[a]}, with the longest, {t[b]}, for a total of {t[a] + t[b]}."))
    return E(["Brute force: try every pairing → (2k)! / (2^k · k!)", "Greedy: sort, pair ends → O(n log n)", "Exchange argument proves optimality"],
             "Trying every pairing explodes combinatorially. Sorting and pairing the shortest with the longest balances the load in n log n. An exchange argument shows any other pairing can't lower the maximum.",
             st, ["Keep original indices (sort indices, not values)", "Duplicate durations", "Exactly 2k tasks"],
             "Sort indices rather than values, so duplicates still map to the right task numbers.",
             ["Sketch the exchange argument", "Follow-up: workers take more than two tasks (harder, partition-like)"],
             "Sketch the exchange argument briefly. If each worker can take more than two tasks, it becomes a much harder partition problem.",
             ["We build a list of indices, sort it by task duration, and for i from zero to k pair the i-th smallest with the i-th largest."])

def ValidStartingCity():
    d, f, mpg = [5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10; miles = 0; mn = 0; start = 0; hist = [0]; st = []
    for i in range(1, len(d)):
        miles += f[i - 1] * mpg - d[i - 1]; hist.append(miles)
        if miles < mn: mn = miles; start = i
        st.append(S("Worked example", [A(d, label="distance to next", ptr={"city": i}), A(hist + [""] * (len(d) - len(hist)), hl={start: "ok", i: "cur"}, label="miles left on arrival (starting at city 0)")],
                    f"Arrive at city {i} with {miles} miles; lowest so far at city {start}", f"Arriving at city {i}, starting from city zero, we'd have {miles} miles of fuel. The lowest point so far is at city {start}."))
    return E(["Brute force: simulate from every city → O(n²)", "Track running fuel; start where it's lowest → O(n)", "Guaranteed exactly one valid city"],
             "Simulating the trip from every city is quadratic. Instead, run the trip once from city zero, allowing negative fuel. The city where the running total hits its minimum is the right start: starting there, the tank never dips below zero.",
             st, ["Fuel is gallons × mpg", "Start at the minimum *arrival* point", "Input guarantees a solution"],
             "Remember to multiply fuel by miles per gallon, and choose the city where you arrive with the least fuel.",
             ["Same as LeetCode Gas Station", "Explain why the minimum point works"],
             "This is the gas station problem. Explain the minimum-point argument: shifting the start shifts the whole curve up.",
             ["We track miles remaining, the minimum and its city. For each city from one, add the fuel from the previous city times mpg minus the distance, and update the minimum and start."])

def MinHeapConstruction():
    a = [30, 102, 23, 17, 18, 9, 44, 12]; h = a[:]; st = [S("Worked example", [TR(*heap_tree(h)), A(h)], "Start: arbitrary array as a tree", "View the array as a complete binary tree: children of index i are at two i plus one and two i plus two.")]
    def sd(i, end):
        while 2 * i + 1 <= end:
            c = 2 * i + 1
            if c + 1 <= end and h[c + 1] < h[c]: c += 1
            if h[c] >= h[i]: return
            h[i], h[c] = h[c], h[i]; i = c
    for i in range((len(h) - 2) // 2, -1, -1):
        v = h[i]; sd(i, len(h) - 1)
        st.append(S("Worked example", [TR(*heap_tree(h), hl={str(i): "cur"}), A(h, hl={i: "cur"})], f"siftDown index {i} (value {v})", f"Sift down the value {v} at index {i}, swapping with its smaller child until it's no bigger than both children."))
    return E(["Insert one by one with siftUp → O(n log n)", "Bottom-up siftDown from the last parent → O(n)", "Most nodes are near the bottom and barely move"],
             "Inserting elements one at a time costs n log n. Building bottom-up, sifting down from the last parent to the root, is linear, because most nodes sit near the bottom and move only a little.",
             pick(st, 6), ["Last parent is (n − 2) / 2", "Pick the smaller child", "Remove: swap root with last, pop, siftDown"],
             "The last parent is at n minus two over two. Always swap with the smaller child. Remove swaps the root with the last element, pops, and sifts down.",
             ["Explain why build-heap is O(n)", "Follow-up: k-th largest, merge k sorted lists"],
             "Be ready to explain the linear build. Heaps power k-th largest and merging k sorted lists.",
             ["Build heap sifts down from the last parent to index zero. Sift down picks the smaller child, stops if it isn't smaller, otherwise swaps and continues. Sift up swaps with the parent while the parent is bigger."])

def LinkedListConstruction():
    st = []; L = []
    for op, cap, nar in [("setHead(1)", [1], "Set head to one: the list was empty, so one is both head and tail."), ("setTail(4)", [1, 4], "Set tail to four: insert after the current tail."),
                         ("insertBefore(4, 3)", [1, 3, 4], "Insert three before four: rewire three's prev to one and next to four, then fix both neighbours."),
                         ("insertAtPosition(2, 2)", [1, 2, 3, 4], "Insert two at position two, walking from the head to the node currently there."),
                         ("removeNodesWithValue(3)", [1, 2, 4], "Remove nodes with value three: unlink by connecting its prev and next, and clear its pointers.")]:
        st.append(S("Worked example", [LL(cap, ptr={"head": 0, "tail": len(cap) - 1}), TX([op])], op, nar))
    return E(["Singly linked → removing needs the previous node (O(n))", "Doubly linked: O(1) insert/remove given a node", "Searching is still O(n)"],
             "With a singly linked list, removing a node needs its predecessor, which means a scan. Doubly linked nodes know both neighbours, so inserting and removing a known node is constant time.",
             st, ["Inserting a node already in the list: remove it first", "Update head/tail when touching the ends", "Clear removed node's pointers"],
             "If the node being inserted is already in the list, remove it first. Always update head and tail when operating at the ends.",
             ["Draw pointer changes before coding", "Used in LRU cache"],
             "Draw the pointer changes before coding. This structure is the backbone of an LRU cache.",
             ["Set head and set tail handle the empty case and otherwise delegate to insert before or after. Insert before removes the node, wires its prev and next, and updates either head or the previous node's next."])

def MergingLinkedLists():
    a = [2, 3, 1, 4]; b = [8, 7, 1, 4]; st = []
    st.append(S("Worked example", [LL(a, label="list A", hl={2: "ok", 3: "ok"}), LL(b, label="list B (shares 1 → 4)", hl={2: "ok", 3: "ok"})], "Both lists share the tail 1 → 4", "The two lists merge at the node with value one and share everything after it."))
    pa = a + [None] + b; pb = b + [None] + a
    for step in (0, 2, 5, 7):
        st.append(S("Worked example", [TX([f"p walks A then B: step {step} → {pa[step] if pa[step] is not None else 'null → switch'}", f"q walks B then A: step {step} → {pb[step] if pb[step] is not None else 'null → switch'}"])], f"Step {step}", f"After {step} steps, p is at {pa[step] if pa[step] is not None else 'the end, switching lists'} and q is at {pb[step] if pb[step] is not None else 'the end, switching lists'}."))
    st.append(S("Worked example", [TX(["both travel lenA + lenB → they meet at the shared node", "meet at node 1 (the shared one)"])], "They meet at the shared node", "Each pointer travels the length of both lists, so they line up and meet at the shared node."))
    return E(["Brute force: for each A node, scan B → O(n·m)", "Hash set of A nodes → O(n + m) time, O(n) space", "Two pointers switching lists → O(1) space"],
             "Comparing every pair is quadratic. A hash set of A's nodes is linear but uses memory. Two pointers that switch to the other list at the end both travel the same total distance, so they meet at the intersection with constant space.",
             st, ["Compare node identity, not value", "No intersection → both reach null together", "Different lengths are fine"],
             "Compare node references, not values; two different nodes can share a value. With no intersection, both reach null together and we return null.",
             ["Explain why the distances equalise", "Alternative: compute lengths and align"],
             "Explain the equal-distance argument, and mention aligning by length difference as an alternative.",
             ["Two pointers start at each head. While they differ, each moves to next, or to the other list's head when it hits null. Return either."])

def RemoveKthNodeFromEnd():
    v = list(range(10)); k = 4; st = [S("Worked example", [LL(v, ptr={"fast": k, "slow": 0})], f"Move fast {k} steps ahead", f"Move fast {k} nodes ahead, so the gap between fast and slow is exactly k.")]
    f, s = k, 0
    while f < len(v) - 1:
        f += 1; s += 1
        if f in (6, 9): st.append(S("Worked example", [LL(v, ptr={"fast": f, "slow": s})], f"Advance both: slow at {v[s]}", f"Move both together. Slow is at {v[s]}, fast at {v[f]}."))
    st.append(S("Worked example", [LL(v, ptr={"slow": s}, hl={s + 1: "bad"})], f"slow.next = slow.next.next removes {v[s + 1]}", f"Fast is at the last node, so slow is just before the k-th from the end. Skip over {v[s + 1]} to remove it."))
    return E(["Two passes: count length, then walk to n − k", "One pass with a k-gap between two pointers", "Both O(n) time, O(1) space"],
             "Two passes, one to count and one to walk, works fine. The single-pass trick keeps two pointers exactly k apart, so when the leading one reaches the end, the trailing one is right before the target.",
             st, ["Removing the head (k = length): copy next into head", "k is always valid here", "Stop fast at the last node, not null"],
             "Removing the head is the special case: fast becomes null, so we copy the second node into the head and skip it.",
             ["Dummy node simplifies head removal", "Follow-up: return the new head instead"],
             "Using a dummy node avoids the head special case. Mention it.",
             ["Fast moves k steps. If it's null, the head is the target, so we overwrite the head with its next. Otherwise we advance both until fast is the last node and skip slow's next."])

def SumOfLinkedLists():
    a, b = [2, 4, 7, 1], [9, 4, 5]; out = []; carry = 0; st = []
    for i in range(max(len(a), len(b)) + 1):
        x = a[i] if i < len(a) else 0; y = b[i] if i < len(b) else 0
        if i >= len(a) and i >= len(b) and carry == 0: break
        s = x + y + carry; out.append(s % 10); carry = s // 10
        st.append(S("Worked example", [LL(a, hl={i: "cur"}, label="1742 (reversed)"), LL(b, hl={i: "cur"}, label="549 (reversed)"), LL(out, label="result", hl={i: "ok"})], f"{x} + {y} + carry → digit {s % 10}, carry {carry}", f"Add {x} and {y} plus the carry: {s}. Write {s % 10} and carry {carry}."))
    return E(["Convert to integers, add, convert back → overflows for long lists", "Digit-by-digit with carry → O(max(n, m))", "Dummy head simplifies building"],
             "Converting to integers overflows on long lists. Adding digit by digit with a carry, like on paper, works for any length.",
             st, ["Final carry creates an extra node", "Lists of different lengths", "Use a dummy head"],
             "Don't forget the final carry, which may add a new node. Treat a finished list as zeros.",
             ["Follow-up: digits stored most-significant first (use stacks or reverse)"],
             "If digits are stored most significant first, reverse the lists or use stacks.",
             ["We loop while either list or the carry remains, compute the sum, append its last digit, keep the carry, and advance the lists. Return dummy's next."])

def BlackjackProbability():
    target, start = 21, 15; memo = {}
    def bust(h):
        if h > target: return 1.0
        if h + 4 >= target: return 0.0
        if h in memo: return memo[h]
        p = sum(0.1 * bust(h + c) for c in range(1, 11)); memo[h] = p; return p
    r = bust(start); st = []
    for h in sorted(memo, reverse=True):
        st.append(S("Worked example", [A([f"{memo[x]:.3f}" if x in memo else ("stand" if 17 <= x <= 21 else "") for x in range(15, 22)], hl={h - 15: "cur"}, label="P(bust) for hands 15…21", idx=False), TX([f"P(bust | {h}) = 0.1 × Σ P(bust | {h} + card)", f"= {memo[h]:.3f}"])],
                    f"Hand {h}: P(bust) = {memo[h]:.3f}", f"With a hand of {h}, average over the ten possible cards. Hands of seventeen to twenty-one stand, and anything over twenty-one busts. That gives {memo[h]:.3f}."))
    return E(["Plain recursion re-explores the same hands → exponential", "Memoise by hand value → O(target) states × 10 cards", "Bottom-up DP works equally well"],
             "Plain recursion explores the same hand totals repeatedly. Memoising by hand value makes it linear in the target, times ten cards.",
             st, ["Stand when hand ≥ target − 4", "Each card 1–10 has probability 0.1", "Round to 3 decimals at the end only"],
             "The dealer stands at target minus four or more. Round only the final answer, not intermediate values.",
             ["Explain the state: just the hand total", "Follow-up: realistic deck (cards without replacement)"],
             "The state is only the hand total because cards are drawn with replacement. A real deck adds card counts to the state.",
             ["Bust returns one above the target, zero when the dealer would stand, otherwise the memoised average of bust over the ten next cards. The answer is rounded to three decimals."])

def Permutations():
    a = [1, 2, 3]; out = []; st = []
    def perm(i, arr):
        if i == len(arr) - 1:
            out.append(arr[:]); st.append(S("Worked example", [A(arr, hl={k: "ok" for k in range(len(arr))}), TX([f"permutations: {out}"], size=18)], f"Leaf → record {arr}", f"All positions are fixed, so we record {', '.join(map(str, arr))}.")); return
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            if j > i: st.append(S("Worked example", [A(arr, hl={i: "cur", j: "warn"}), TX([f"fix position {i}: swap {i} ↔ {j}"])], f"Swap positions {i} and {j}", f"At position {i}, swap in the element from position {j}, then recurse on the rest."))
            perm(i + 1, arr); arr[i], arr[j] = arr[j], arr[i]
    perm(0, a)
    return E(["Build by inserting into every position → O(n!·n²)", "Swap-based backtracking → O(n!·n)", "Output size n! is the true lower bound"],
             "Inserting each element into every position of smaller permutations works but copies a lot. Swap-based backtracking fixes one position at a time in place. Either way the output itself is n factorial.",
             pick(st, 6), ["Empty input → []", "Undo the swap after recursing", "Copy the array when recording"],
             "Always undo the swap after recursing, and copy the array when you record it, or every result ends up the same list.",
             ["Follow-up: duplicates → skip repeated values per position", "Next permutation (lexicographic)"],
             "With duplicates, skip values already used at a position. Next permutation is a common sibling question.",
             ["If the array is non-empty we call permute from zero. At the last index we record a copy. Otherwise, for each j from i, swap i and j, recurse, and swap back."])

def PhoneNumberMnemonics():
    keys = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]; p = "1905"; out = []
    def b(i, s):
        if i == len(p): out.append(s); return
        for c in keys[int(p[i])]: b(i + 1, s + c)
    b(0, "")
    st = [S("Worked example", [T([[d, keys[int(d)]] for d in p], colh=["digit", "letters"])], "1905 → letters per digit", "For one-nine-zero-five, one and zero map to themselves, nine to w, x, y, z, and five to j, k, l."),
          S("Worked example", [TX(["1 → 1w → 1w0 → 1w0j, 1w0k, 1w0l", "      → 1x0 → 1x0j …"])], "Depth-first: one letter per digit", "Recursion picks one letter per digit, depth first, then backtracks to try the next letter."),
          S("Worked example", [TX([", ".join(out[:6]), ", ".join(out[6:])], size=18)], f"{len(out)} mnemonics = 1 × 4 × 1 × 3", f"In total there are {len(out)} mnemonics: one times four times one times three.")]
    return E(["Iterative: expand a list digit by digit (BFS)", "Backtracking with a StringBuilder (DFS)", "Both O(4ⁿ · n)"],
             "You can expand a list of partial strings digit by digit, or backtrack depth first with one string builder. Both are bounded by four to the n times n, the size of the output.",
             st, ["0 and 1 map to themselves here", "Undo the append after recursing", "Empty input → [\"\"]"],
             "In this version zero and one map to themselves. Remove the last character after each recursive call.",
             ["State the output-size bound", "Follow-up: only dictionary words (use a trie)"],
             "State the output-size bound clearly. Restricting to real words is a nice trie follow-up.",
             ["Build recurses on the digit index. At the end it records the string; otherwise for each letter of the current key it appends, recurses and removes the letter."])

def Powerset():
    a = [1, 2, 3]; subs = [[]]; st = [S("Worked example", [TX(["subsets: [ [] ]"])], "Start with the empty set", "Start with just the empty subset.")]
    for x in a:
        subs += [s + [x] for s in subs]
        st.append(S("Worked example", [TX([f"add {x} to each existing subset:", str(subs)], size=18)], f"After {x}: {len(subs)} subsets", f"For {x}, copy every existing subset and add {x} to the copy. That doubles the count to {len(subs)}."))
    return E(["Bitmask: each of 2ⁿ masks picks a subset", "Iterative doubling or recursion", "O(n · 2ⁿ) time and space either way"],
             "Each subset corresponds to an n-bit mask, so there are two to the n of them. Iteratively doubling the list, or recursion, produces them all in n times two to the n.",
             st, ["Iterate over the size *before* adding", "Include the empty set", "Duplicates in input → dedupe"],
             "Capture the list size before the inner loop, or you'll loop forever on subsets you just added. Remember the empty set.",
             ["Mention bitmask enumeration", "Follow-up: subsets with duplicates, subsets summing to k"],
             "Mention the bitmask view. Follow-ups handle duplicates or restrict to a target sum.",
             ["We start with one empty subset. For each value, we take the current size and, for each existing subset, add a copy with the value appended."])

def RevealMinesweeper():
    b = [["H", "H", "H", "H"], ["H", "M", "H", "H"], ["H", "H", "H", "H"], ["H", "H", "H", "M"]]; R, C = 4, 4; order = []
    def rv(r, c):
        if b[r][c] != "H": return
        m = sum(1 for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C and b[r + dr][c + dc] == "M")
        b[r][c] = str(m); order.append(((r, c), [x[:] for x in b]))
        if m: return
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if 0 <= r + dr < R and 0 <= c + dc < C: rv(r + dr, c + dc)
    rv(0, 3); st = [S("Worked example", [T(b0, hl={p: ("ok" if b0[p[0]][p[1]] == "0" else "cur")})], f"Reveal ({p[0]},{p[1]}) → {b0[p[0]][p[1]]}", f"Cell row {p[0]}, column {p[1]} has {b0[p[0]][p[1]]} adjacent mines." + (" Zero, so we reveal all its neighbours." if b0[p[0]][p[1]] == "0" else " Non-zero, so we stop here.")) for p, b0 in order]
    return E(["Click a mine → X and stop", "Count neighbours; if 0, flood-fill recursively", "Each cell revealed once → O(w·h)"],
             "If the click is a mine, mark it and stop. Otherwise count adjacent mines; if there are none, recursively reveal every neighbour. Each cell is revealed at most once.",
             pick(st, 6), ["8-directional neighbours", "Only recurse on hidden cells (no re-visits)", "Only recurse from zeros"],
             "Neighbours include diagonals. Only hidden cells recurse, which prevents infinite loops, and only zero cells spread.",
             ["Mention BFS to avoid deep recursion", "Follow-up: generate a board, first click safe"],
             "On huge boards, a queue avoids deep recursion.",
             ["If the clicked cell is a mine we mark it X. Reveal returns for non-hidden cells, counts mines in the eight neighbours, writes the count, and recurses on neighbours only when the count is zero."])

def StaircaseTraversal():
    H, K = 4, 2; w = [1] + [0] * H; win = 0; st = []
    for h in range(1, H + 1):
        win += w[h - 1]
        if h - K - 1 >= 0: win -= w[h - K - 1]
        w[h] = win
        st.append(S("Worked example", [A(w, hl={h: "ok", **{j: "warn" for j in range(max(0, h - K), h)}}, label="ways to reach each step"), TX([f"ways[{h}] = sum of the last {K} = {w[h]}"])], f"ways[{h}] = {w[h]}", f"To reach step {h}, the last move came from one of the previous {K} steps, so we sum them: {w[h]}."))
    return E(["Recursion over step sizes → O(kⁿ)", "Memo/DP summing last k → O(n·k)", "Sliding window sum → O(n)"],
             "Plain recursion branches k ways per step. A DP summing the previous k entries is n times k, and keeping a running window sum makes it linear.",
             st, ["ways[0] = 1", "Subtract the element leaving the window", "maxSteps > height"],
             "Ways of zero is one. When the window slides, subtract the value falling out of it.",
             ["Notice Fibonacci for k = 2", "Follow-up: forbidden steps"],
             "With k equal to two, it's Fibonacci. Forbidden steps are a nice follow-up.",
             ["Ways of zero is one. For each height, add ways of h minus one to the window, subtract the value that left the window, and store the window as ways of h."])

def SearchInSortedMatrix():
    m = [[1, 4, 7, 12, 15, 1000], [2, 5, 19, 31, 32, 1001], [3, 8, 24, 33, 35, 1002], [40, 41, 42, 44, 45, 1003], [99, 100, 103, 106, 128, 1004]]; tgt = 44; r, c = 0, 5; st = []
    while True:
        v = m[r][c]
        st.append(S("Worked example", [T(m, hl={(r, c): "ok" if v == tgt else "cur"}), TX([f"{v} {'=' if v == tgt else ('>' if v > tgt else '<')} {tgt} → " + ("found" if v == tgt else ("move left" if v > tgt else "move down"))])], f"({r},{c}) = {v}", f"At {v}: " + ("found it." if v == tgt else ("too big, so everything below is too, move left." if v > tgt else "too small, so everything left is too, move down."))))
        if v == tgt: break
        if v > tgt: c -= 1
        else: r += 1
    return E(["Scan every cell → O(r·c)", "Binary search each row → O(r log c)", "Start top-right, eliminate a row or column per step → O(r + c)"],
             "Scanning everything ignores the sorting. Binary-searching each row is better. Starting at the top-right corner, every comparison eliminates a whole row or column, so it's r plus c.",
             pick(st, 6), ["Target absent → [−1, −1]", "Bottom-left start also works", "Top-left doesn't (both moves increase)"],
             "Top-right or bottom-left both work, because one move increases and the other decreases. From top-left both increase, so you can't decide.",
             ["Explain why the corner choice matters"],
             "Explain why the corner matters; that's the insight.",
             ["We start at row zero and the last column. While in bounds, return on a match, move left if the value is too big, otherwise move down."])

def ThreeNumberSort():
    a = [1, 0, 0, -1, -1, 0, 1, 1]; order = [0, 1, -1]; lo = mid = 0; hi = len(a) - 1; st = []
    while mid <= hi:
        v = a[mid]
        if v == order[0]: a[lo], a[mid] = a[mid], a[lo]; lo += 1; mid += 1; act = "first → swap to lo"
        elif v == order[1]: mid += 1; act = "second → leave it"
        else: a[mid], a[hi] = a[hi], a[mid]; hi -= 1; act = "third → swap to hi"
        st.append(S("Worked example", [A(a, ptr={"lo": lo, "mid": mid, "hi": hi}), TX([f"saw {v}: {act}"])], f"{v}: {act}", f"Mid saw {v}, the {act.split(' ')[0]} value, so we {act.split('→ ')[1]}."))
    return E(["Sort → O(n log n)", "Counting pass + rewrite → O(n), two passes", "Dutch national flag → O(n), one pass, O(1) space"],
             "Sorting is n log n. Counting each value and rewriting is linear but two passes. The Dutch national flag algorithm does it in one pass with three pointers.",
             pick(st, 6), ["Don't advance mid after swapping with hi", "Values may be missing", "Loop while mid ≤ hi"],
             "After swapping with hi, don't advance mid: the swapped-in value hasn't been examined.",
             ["Name the Dutch national flag problem"],
             "Name the Dutch national flag problem; interviewers like hearing it.",
             ["Lo, mid and hi start at the ends. While mid is at most hi, first-order values swap to lo and both advance, second-order values just advance mid, and third-order values swap with hi, which moves down."])

def BalancedBrackets():
    s = "([])(){}(())"; stk = []; st = []
    for i, ch in enumerate(s):
        if ch in "([{": stk.append(ch); act = "push"
        else: stk.pop(); act = "pop & match"
        if i in (0, 2, 3, 6, 11): st.append(S("Worked example", [A(list(s), hl={i: "cur"}, idx=False), ST(stk[::-1] or ["(empty)"], w=0.3)], f"'{ch}': {act}", f"{'An opening bracket: push it.' if act == 'push' else 'A closing bracket: it must match the top, so we pop.'}"))
    return E(["Repeatedly delete '()', '[]', '{}' → O(n²)", "Stack of openers → O(n)", "Only brackets matter; ignore other chars"],
             "Repeatedly deleting matched pairs is quadratic. A stack of opening brackets checks each closer against the most recent opener in linear time.",
             st, ["Closer on empty stack → false", "Leftover openers → false", "Non-bracket characters ignored"],
             "A closer with an empty stack fails, and leftover openers at the end fail too.",
             ["Follow-up: minimum insertions to balance"],
             "A follow-up asks for the minimum insertions to balance a string.",
             ["We push openers. For closers, we fail if the stack is empty or the popped opener doesn't correspond. At the end the stack must be empty."])

def BestDigits():
    n, k = "462839", 2; stk = []; st = []
    for ch in n:
        rem = []
        while k > 0 and stk and stk[-1] < ch: rem.append(stk.pop()); k -= 1
        stk.append(ch)
        st.append(S("Worked example", [ST(stk[::-1], w=0.4), TX([f"read {ch}" + (f": pop {', '.join(rem)}" if rem else ""), f"removals left: {k}"], w=0.6, h=1)], f"Read {ch}" + (f", remove {''.join(rem)}" if rem else ""), f"Read {ch}." + (f" It's bigger than {', '.join(rem)} on the stack, so removing those makes the number larger." if rem else " Keep it."), layout="cols"))
    return E(["Try all C(n, k) removals → exponential", "Monotonic stack: pop smaller digits while removals remain → O(n)", "Remove from the end if removals remain"],
             "Trying every set of removals is exponential. A greedy monotonic stack pops smaller digits whenever a bigger one arrives, because a bigger digit earlier always makes a bigger number.",
             pick(st, 6), ["Leftover removals: drop from the end", "Equal digits: don't pop", "Result length is n − k"],
             "If removals remain after the scan, drop digits from the end.",
             ["Mirror: Remove K Digits for the smallest number"],
             "The mirror problem, remove k digits for the smallest number, flips the comparison.",
             ["For each digit, while removals remain and the top is smaller, pop and decrement. Push the digit. Then pop from the end any remaining removals and join."])

def CollidingAsteroids():
    a = [-3, 5, -8, 6, 7, -4, -7]; stk = []; st = []
    for x in a:
        alive = True; ev = []
        while alive and x < 0 and stk and stk[-1] > 0:
            t = stk[-1]
            if t < -x: stk.pop(); ev.append(f"{x} destroys {t}")
            else:
                if t == -x: stk.pop(); ev.append(f"{x} and {t} both explode")
                else: ev.append(f"{t} destroys {x}")
                alive = False
        if alive: stk.append(x)
        st.append(S("Worked example", [A(a, hl={a.index(x): "cur"}), A(stk or ["∅"], label="survivors (stack)", idx=False), TX(["; ".join(ev) or "no collision"], h=0.35)], f"{x}: " + ("; ".join(ev) or "no collision"), f"Asteroid {x}: " + ("; ".join(ev) if ev else "nothing to collide with, push it") + "."))
    return E(["Simulate repeatedly until stable → O(n²)", "Stack of survivors → each pushed/popped once, O(n)", "Collisions only: right-mover then left-mover"],
             "Re-simulating until nothing changes is quadratic. A stack of survivors handles each asteroid in amortised constant time, since each is pushed and popped at most once. Only a right-mover followed by a left-mover collides.",
             pick(st, 6), ["Left then right never collide", "Equal sizes: both explode", "Negative on empty stack survives"],
             "A left-mover before a right-mover never collides. Equal sizes destroy both.",
             ["State the collision condition first"],
             "State the collision condition first; the rest follows.",
             ["For each asteroid we loop while it's alive, moving left, and the top moves right. A smaller top is popped; otherwise equal sizes pop the top and either way the current one dies. Survivors are pushed."])

def MinMaxStackConstruction():
    s = []; st = []
    for op in ["push 5", "push 7", "push 2", "pop", "push 9"]:
        if op == "pop": s.pop()
        else:
            v = int(op.split()[1]); s.append((v, min(v, s[-1][1]), max(v, s[-1][2])) if s else (v, v, v))
        st.append(S("Worked example", [T([list(x) for x in s[::-1]] or [["", "", ""]], colh=["value", "min", "max"]), TX([op, f"min = {s[-1][1]}, max = {s[-1][2]}"])], f"{op} → min {s[-1][1]}, max {s[-1][2]}", f"{op.capitalize()}. Each entry stores the min and max of everything at or below it, so the top answers min {s[-1][1]} and max {s[-1][2]} instantly."))
    return E(["Scan the stack for min/max → O(n)", "Store (value, min, max) per entry → O(1) all ops", "Extra O(n) space"],
             "Scanning for min and max is linear per query. Storing the running min and max with each entry makes every operation constant time; popping automatically restores the old values.",
             st, ["Empty stack behaviour", "Pop restores previous min/max automatically"],
             "Popping needs no special handling, because the entry below already stores the correct min and max.",
             ["Follow-up: min-stack with O(1) extra space (encoding trick)"],
             "A follow-up uses an encoding trick to avoid storing extra values.",
             ["Each push stores the value with the min and max of itself and the previous top. Peek and pop read the value; get min and get max read the top's stored fields."])

def NextGreaterElement():
    a = [2, 5, -3, -4, 6, 7, 2]; n = len(a); out = [-1] * n; stk = []; st = []
    for i in range(2 * n):
        j = i % n; res = []
        while stk and a[stk[-1]] < a[j]: k = stk.pop(); out[k] = a[j]; res.append(k)
        if i < n: stk.append(j)
        if res or i in (0, n + 1):
            st.append(S("Worked example", [A(a, hl={j: "cur", **{k: "ok" for k in res}}, ptr={"i": j}), A(out, label="answer"), TX([f"stack (indices): {stk}"], h=0.35)], f"{'Pass 2: ' if i >= n else ''}{a[j]} resolves {[a[k] for k in res]}" if res else f"Push index {j}", f"{'In the second pass, ' if i >= n else ''}{a[j]} is greater than " + (", ".join(str(a[k]) for k in res) + " on the stack, so it's their answer." if res else "nothing waiting; push it.")))
    return E(["For each element scan forward (wrapping) → O(n²)", "Monotonic decreasing stack, two passes for wrap → O(n)", "Each index pushed and popped once"],
             "Scanning forward from every element is quadratic. A decreasing stack of unresolved indices resolves them as soon as a bigger value appears. Looping twice handles the circular wrap.",
             pick(st, 6), ["Push indices, not values", "Only push in the first pass", "No greater → −1"],
             "Store indices so you can write the answer. Only push during the first pass.",
             ["Same pattern: daily temperatures, stock span"],
             "The same pattern solves daily temperatures and stock span.",
             ["We fill the output with minus one and loop i to two n, using j equal i mod n. While the top's value is smaller than a of j, pop and set its answer. Push j only in the first pass."])

def ReversePolishNotation():
    toks = ["50", "3", "17", "+", "2", "-", "/"]; stk = []; st = []
    for t in toks:
        if t in "+-*/":
            b = stk.pop(); a = stk.pop(); r = {"+": a + b, "-": a - b, "*": a * b, "/": int(a / b)}[t]; stk.append(r); msg = f"{a} {t} {b} = {r}"
        else: stk.append(int(t)); msg = f"push {t}"
        st.append(S("Worked example", [A(toks, hl={toks.index(t): "cur"}, idx=False), ST(stk[::-1], w=0.3)], msg, (f"Operator {t}: pop {b} and {a}, compute {msg}, push it." if t in "+-*/" else f"Number: push {t}.")))
    return E(["Build an expression tree then evaluate → extra structure", "Stack evaluation → O(n) time and space"],
             "You could build an expression tree, but a single stack is enough: numbers are pushed, operators pop two and push the result.",
             pick(st, 7), ["Operand order for − and /: second pop is the left operand", "Integer division truncates toward zero", "Negative numbers are tokens too"],
             "For minus and divide, the first pop is the right operand. Division truncates toward zero.",
             ["Follow-up: convert infix → RPN (shunting-yard)"],
             "A follow-up converts infix to RPN with the shunting-yard algorithm.",
             ["For each token: plus and times push the result of two pops; minus and divide pop b first then compute a op b; anything else is parsed and pushed. Return the final pop."])

def SortStack():
    s = [-5, 2, -2, 4, 3, 1]; st = [S("Worked example", [ST(s[::-1], w=0.4), TX(["pop everything recursively…"], w=0.6, h=1)], "Recursively pop until empty", "Sort stack pops the top and recursively sorts the rest, until the stack is empty.", layout="cols")]
    cur = []
    for v in s:
        cur.append(v); cur.sort()
        st.append(S("Worked example", [ST(cur[::-1], hl={len(cur) - 1 - cur.index(v): "cur"}, w=0.4), TX([f"insert {v} into sorted stack"], w=0.6, h=1)], f"Insert {v} into position", f"Unwinding, insert {v}: pop larger tops, place it, and push them back.", layout="cols"))
    return E(["Use an auxiliary stack → O(n²)", "Recursion only (no extra structures) → O(n²) time, O(n) call stack", "Insertion sort on a stack"],
             "With only stack operations, this is insertion sort: sort the rest recursively, then insert the top into place. That's quadratic time and linear recursion depth.",
             pick(st, 6), ["Base case: empty stack", "Insert pops while top > value", "Recursion depth = n"],
             "Insert pops while the top is bigger than the value, places it, and pushes the popped values back.",
             ["Mention the auxiliary-stack iterative version"],
             "Mention the iterative two-stack version as well.",
             ["Sort stack removes the top, sorts the rest, and inserts the top. Insert adds the value if the stack is empty or the top is smaller or equal; otherwise it removes the top, inserts recursively and pushes the top back."])

def SunsetViews():
    h = [3, 5, 4, 4, 3, 1, 3, 2]; out = []; mx = float("-inf"); st = []
    for i in range(len(h) - 1, -1, -1):
        sees = h[i] > mx
        if sees: out.append(i); mx = h[i]
        if i in (7, 6, 4, 3, 1, 0): st.append(S("Worked example", [A(h, hl={i: "ok" if sees else "bad", **{k: "done" for k in out if k != i}}, ptr={"i": i}), TX([f"tallest to the east so far = {mx}"])], f"Building {i} (height {h[i]}): " + ("sees sunset" if sees else "blocked"), f"Scanning from the east, building {i} has height {h[i]}. " + ("It's taller than everything east of it, so it sees the sunset." if sees else f"Something east of it is at least {mx} tall, so it's blocked.")))
    return E(["For each building check all ahead → O(n²)", "Scan from the sunset side tracking the max → O(n)", "Or a stack scanning the other way"],
             "Checking every building against all the ones in front is quadratic. Scanning from the sunset side and tracking the tallest seen so far is linear.",
             st, ["Equal heights block", "Return indices in ascending order", "Direction EAST vs WEST"],
             "Equal height blocks the view. Return the indices in ascending order, so reverse when scanning east.",
             ["Mention the stack version"],
             "Mention the stack-based alternative scanning in the opposite direction.",
             ["We scan from the sunset side, adding an index whenever its height beats the running max, then reverse the list when facing east."])

def GroupAnagrams():
    w = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]; g = {}; st = []
    for x in w:
        k = "".join(sorted(x)); g.setdefault(k, []).append(x)
        if x in ("yo", "tac", "cat", "oy", "olfp"): st.append(S("Worked example", [T([[kk, ", ".join(v)] for kk, v in g.items()], colh=["sorted key", "words"]), TX([f"'{x}' → key '{k}'"])], f"'{x}' → '{k}'", f"Sort the letters of {x} to get the key {k}, and add it to that group."))
    return E(["Compare every pair with a frequency check → O(w²·n)", "Sorted-letters key in a hash map → O(w · n log n)", "Count-array key → O(w · n)"],
             "Comparing every pair of words is quadratic. Using the sorted letters as a hash key groups anagrams in one pass. A 26-letter count key avoids the sort.",
             st, ["Empty list → []", "Keep insertion order if required", "Case sensitivity"],
             "Handle the empty list, and decide on case sensitivity.",
             ["Mention the count-key optimisation"],
             "Mention the count-array key as a further optimisation.",
             ["For each word we sort its characters to form a key, and add the word to that key's list in a linked hash map, then return the lists."])

def LongestPalindromicSubstring():
    s = "abaxyzzyxf"; bs = be = 0; st = []
    for i in range(len(s)):
        for j in (i, i + 1):
            l, r = i, j
            while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1
            if r - l - 1 > be - bs:
                bs, be = l + 1, r
                st.append(S("Worked example", [A(list(s), hl={k: "ok" for k in range(bs, be)}, ptr={"centre": i}, idx=False), TX([f"{'odd' if j == i else 'even'} centre at {i} → '{s[bs:be]}'"])], f"New best: '{s[bs:be]}'", f"Expanding around {'the letter' if j == i else 'the gap after'} index {i} gives {' '.join(s[bs:be])}, the longest so far."))
    return E(["Check every substring → O(n³)", "DP table → O(n²) time and space", "Expand around 2n − 1 centres → O(n²) time, O(1) space"],
             "Checking every substring is cubic. A DP table is quadratic in time and space. Expanding around each of the two n minus one centres is quadratic time but constant space.",
             st, ["Even-length palindromes need gap centres", "Single char string", "Manacher's for O(n)"],
             "Don't forget even-length palindromes, centred between letters.",
             ["Mention Manacher's algorithm"],
             "Mention Manacher's algorithm for linear time.",
             ["For each i we expand from i,i and i,i plus one while the ends match, then compare the length r minus l minus one with the best and update."])

def MinimumCharactersForWords():
    from collections import Counter
    w = ["this", "that", "did", "deed", "them!", "a"]; need = Counter(); st = []
    for x in w:
        need |= Counter(x)
        if x in ("this", "that", "deed", "them!"): st.append(S("Worked example", [T([[c, n] for c, n in sorted(need.items())], colh=["char", "max needed"]), TX([f"after '{x}'"])], f"After '{x}'", f"After {x}, each character's count is the max it needs in any single word."))
    return E(["Concatenate everything → too many chars", "Per-char max frequency across words → O(total chars)"],
             "Counting all characters together overcounts. What matters is, for each character, the maximum number of times any single word uses it.",
             st, ["Take max, not sum", "Special characters count", "Output order doesn't matter"],
             "Take the max per character, not the sum. Punctuation counts too.",
             ["Follow-up: minimum chars to type words sequentially"],
             "Explain why max is correct: one word at a time.",
             ["For each word we count its characters and merge into need with max. Then we expand need into a character array."])

def OneEdit():
    st = []
    for a, b, res in [("hello", "hollo", "one replace → true"), ("hello", "helo", "one delete → true"), ("hello", "hlelo", "two mismatches → false")]:
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), None)
        st.append(S("Worked example", [A(list(a), hl={i: "cur"}, idx=False), A(list(b), hl={i: "cur"}, idx=False), TX([res])], f"'{a}' vs '{b}': {res}", f"{a} versus {b}: the first difference is at index {i}. {res.capitalize()}."))
    return E(["Compute full edit distance → O(n·m)", "Single scan with one allowed mismatch → O(n)"],
             "Computing the full Levenshtein distance is overkill. A single scan allowing one mismatch, skipping in the longer string when lengths differ, is linear.",
             st, ["Length differs by > 1 → false", "Identical strings → true (zero edits)", "Mismatch at the end"],
             "If lengths differ by more than one, return false immediately.",
             ["Relate to Levenshtein distance"],
             "Relate it to Levenshtein distance, then explain why one pass is enough.",
             ["We bail if lengths differ by more than one. Scanning, the first mismatch sets edited and skips in the longer string, or both if equal; a second mismatch returns false."])

def ReverseWordsInString():
    s = "AlgoExpert is the best!"; toks = []; cur = ""
    for ch in s:
        if cur and (ch == " ") != (cur[-1] == " "): toks.append(cur); cur = ""
        cur += ch
    toks.append(cur)
    st = [S("Worked example", [TX([repr(s)])], "Input", "Reverse the words, keeping the spaces exactly as they are."),
          S("Worked example", [A([t.replace(" ", "␣") for t in toks], idx=False)], "Tokens: words and space runs", "Split into words and runs of spaces."),
          S("Worked example", [A([t.replace(" ", "␣") for t in toks[::-1]], idx=False), TX([repr("".join(toks[::-1]))])], "Reverse token order", "Reverse the tokens and join: best, is, the... reversed with spacing preserved.")]
    return E(["split + reverse + join (library) → O(n)", "Manual scan from the end collecting tokens → O(n)", "In-place: reverse all, then reverse each word"],
             "The library approach is fine but may lose spacing. Scanning from the end, collecting words and space runs, is linear. In place, reverse the whole string then each word.",
             st, ["Multiple spaces preserved", "Leading/trailing spaces", "Empty string"],
             "Preserve runs of spaces and leading or trailing spaces.",
             ["Mention the in-place two-reversal trick"],
             "Mention the in-place two-reversal trick.",
             ["We scan from the end, and whenever we switch between space and non-space we append the token from i plus one to end, then move end."])

def ValidIpAddresses():
    s = "1921680"; out = []
    def ok(p): return 0 < len(p) <= 3 and not (len(p) > 1 and p[0] == "0") and int(p) <= 255
    for i in range(1, min(4, len(s))):
        for j in range(i + 1, min(i + 4, len(s))):
            for k in range(j + 1, min(j + 4, len(s))):
                p = [s[:i], s[i:j], s[j:k], s[k:]]
                if all(ok(x) for x in p): out.append(".".join(p))
    st = [S("Worked example", [TX(["1.9.2.1680 ✗ (1680 > 255)", "1.92.168.0 ✓", "19.216.8.0 ✓"])], "Try three dot positions", "Place three dots. Each part must be one to three digits, at most 255, with no leading zero."),
          S("Worked example", [TX(["192.168.0 → but '0' fine; '01' ✗ (leading zero)"])], "Leading zeros are invalid", "Parts like zero one are invalid because of the leading zero, but a single zero is fine."),
          S("Worked example", [TX([", ".join(out[:5]), ", ".join(out[5:])], size=18)], f"{len(out)} valid addresses", f"In total there are {len(out)} valid addresses for one-nine-two-one-six-eight-zero.")]
    return E(["All dot placements: at most 3·3·3 = 27 → O(1)", "Validate each part", "Input length > 12 → none"],
             "There are at most twenty-seven ways to place three dots, so brute force is already constant time. The work is validating each part.",
             st, ["Leading zeros", "Parts > 255", "Length < 4 or > 12"],
             "Watch for leading zeros and parts over 255.",
             ["Show the bounded search clearly"],
             "Explain why brute force is bounded and fine here.",
             ["Three nested loops choose the dot positions, limited to three digits per part. Each split is kept if all four parts pass valid, which checks length, leading zero and the 255 limit."])

def SuffixTrieConstruction():
    s = "babc"; st = []
    for i in range(len(s)):
        st.append(S("Worked example", [TX([f"insert suffix '{s[i:]}*'"] + [f"suffixes so far: {[s[k:] for k in range(i + 1)]}"])], f"Insert suffix '{s[i:]}'", f"Insert the suffix {' '.join(s[i:])}, followed by an end marker."))
    st.append(S("Worked example", [TX(["contains('abc'): b? no — a → b → c → * ✓", "contains('ab'): a → b, no * ✗"])], "Lookup walks the trie, then checks the end marker", "Contains walks the characters; it's true only if the final node has the end marker, so ab is not a suffix but abc is."))
    return E(["Store suffixes in a list → O(n·m) lookup", "Suffix trie → O(n²) build, O(m) lookup", "Suffix tree/array → near-linear space"],
             "Storing suffixes in a list makes each lookup scan everything. A suffix trie builds in quadratic time and space and answers lookups in the length of the query.",
             st, ["End marker distinguishes suffix from substring", "Quadratic space", "Empty string"],
             "The end marker distinguishes a true suffix from just a substring.",
             ["Mention suffix trees / arrays"],
             "Mention suffix trees and arrays for linear-space alternatives.",
             ["The constructor inserts every suffix character by character, creating nodes as needed, then adds the end marker. Contains walks the characters and checks the end marker."])
