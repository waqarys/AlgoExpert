from enrich.kit import *

def CountSquares():
    pts = [(1, 1), (0, 0), (-4, 2), (-2, -1), (0, 1), (1, 0), (-1, 4)]; P = set(pts); st = []; found = []
    for i, a in enumerate(pts):
        for j, b in enumerate(pts):
            if i == j: continue
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2; dx, dy = a[0] - mx, a[1] - my
            c, d = (mx - dy, my + dx), (mx + dy, my - dx)
            if all(float(v).is_integer() for v in c + d) and (int(c[0]), int(c[1])) in P and (int(d[0]), int(d[1])) in P: found.append((a, b, c, d))
    pos = {p: [(p[0] + 5) / 7, (p[1] + 2) / 7] for p in pts}
    a, b, c, d = found[0]
    st.append(S("Worked example", [G({str(k): v for k, v in pos.items()}, [], w=0.6), TX([f"{len(pts)} points"], w=0.4, h=1)], "Input points", "Here are seven points. We'll treat each pair as a square's diagonal.", layout="cols"))
    st.append(S("Worked example", [G({str(k): v for k, v in pos.items()}, [(str(a), str(b))], hl={str(a): "cur", str(b): "cur"}, w=0.6), TX([f"diagonal {a} – {b}", f"midpoint ({(a[0]+b[0])/2}, {(a[1]+b[1])/2})"], w=0.4, h=1, size=18)], f"Pick diagonal {a} – {b}", f"Take {a} and {b} as a diagonal. The midpoint is the square's centre.", layout="cols"))
    st.append(S("Worked example", [G({str(k): v for k, v in pos.items()}, [(str(a), str(b))], hl={str(a): "cur", str(b): "cur", str((int(c[0]), int(c[1]))): "ok", str((int(d[0]), int(d[1]))): "ok"}, w=0.6), TX(["rotate half-diagonal 90°:", f"{(int(c[0]), int(c[1]))} ✓  {(int(d[0]), int(d[1]))} ✓"], w=0.4, h=1, size=18)], "Rotate 90° about the midpoint: both corners exist", "Rotating the half-diagonal ninety degrees gives the other two corners. Both are in the set, so this is a square.", layout="cols"))
    st.append(S("Worked example", [TX([f"ordered diagonal hits: {len(found)}", f"each square counted 4× → {len(found) // 4} square(s)"])], f"Answer: {len(found) // 4}", f"We found {len(found)} ordered diagonal pairs. Each square has two diagonals in two orders, so divide by four: {len(found) // 4}."))
    return E(["Brute force: all 4-point combinations → O(n⁴)", "Pairs as diagonals + hash set lookup → O(n²)", "Double coordinates to keep midpoints integral"],
             "Checking every group of four points is n to the fourth. Treating each pair as a diagonal and looking up the other two corners in a hash set is quadratic.",
             st, ["Divide by 4 (each square counted four times)", "Half-integer midpoints → scale coordinates by 2", "Duplicate points"],
             "Each square is counted four times, so divide. Doubling every coordinate keeps midpoints integral, avoiding floating-point keys.",
             ["Mention the side-based variant (pairs as edges)", "Tilted squares are counted too"],
             "This counts tilted squares too, not just axis-aligned ones. Mention the edge-based variant as an alternative.",
             ["We store doubled coordinates in a set. For each ordered pair, compute the midpoint and the half-diagonal, rotate it to get the other two corners, and count if both exist. Return count over four."])

def FourNumberSum():
    a, T = [7, 6, 4, -1, 1, 2], 16; pairs = {}; out = []; st = []
    for i in range(1, len(a) - 1):
        hits = []
        for j in range(i + 1, len(a)):
            for p in pairs.get(T - a[i] - a[j], []): out.append(p + [a[i], a[j]]); hits.append(p + [a[i], a[j]])
        for k in range(i): pairs.setdefault(a[i] + a[k], []).append([a[k], a[i]])
        st.append(S("Worked example", [A(a, hl={i: "cur", **{k: "done" for k in range(i)}}, ptr={"i": i}), TX([f"quads found: {hits or 'none'}", f"pair sums stored: {sorted(pairs)}"], size=18)],
                    f"i = {i}: look ahead, then store pairs ending at {a[i]}", f"At index {i}, value {a[i]}: we look for pairs after it whose sum plus a stored earlier pair makes sixteen" + (f", finding {hits}." if hits else ", finding nothing yet.") + f" Then we store every pair that ends at {a[i]}."))
    return E(["Brute force: four loops → O(n⁴)", "Sort + two pointers → O(n³)", "Pair-sum hash map → O(n²) average"],
             "Four nested loops is n to the fourth. Fixing two and two-pointering the rest is cubic. Storing pair sums in a hash map gives quadratic average time.",
             st, ["Only store pairs *before* i to avoid reusing elements", "Worst case O(n³) when many pairs share a sum", "Distinct quadruplets only"],
             "Add pairs ending at i only after looking ahead from i, so the two halves never overlap and each quadruplet is found once.",
             ["Explain the look-ahead/store ordering", "Follow-up: k-sum generalisation"],
             "The ordering trick is the heart of the solution; explain it. The k-sum generalisation recurses down to two-sum.",
             ["For each i from one, we look at every j after i and add each stored pair summing to target minus a i minus a j. Then we store all pairs of earlier elements with a i."])

def KnightConnection():
    from collections import deque
    a, b = (0, 0), (4, 2); mv = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    q = deque([(a, 0)]); seen = {a: None}; lv = {}
    while q:
        p, d = q.popleft(); lv.setdefault(d, []).append(p)
        if p == b: break
        for m in mv:
            n = (p[0] + m[0], p[1] + m[1])
            if n not in seen: seen[n] = p; q.append((n, d + 1))
    D = d; st = []
    for k in range(min(D, 3) + 1):
        st.append(S("Worked example", [TX([f"BFS level {k}: {len(lv[k])} squares", f"e.g. {lv[k][:6]}"], size=18)], f"Combined moves {k}: {len(lv[k])} positions", f"After {k} combined knight moves from the first knight, we've reached {len(lv[k])} new squares."))
    st.append(S("Worked example", [TX([f"reached {b} after {D} total moves", f"two knights meet halfway → ⌈{D}/2⌉ = {(D + 1) // 2} turns"])], f"Answer: {(D + 1) // 2}", f"We reach the second knight after {D} single-knight moves. Since both knights move each turn, they meet in {(D + 1) // 2} turns."))
    return E(["Move both knights simultaneously → state space squared", "BFS from one knight to the other, halve (round up) → O(d²) cells", "Infinite board: no bounds, use a seen set"],
             "Searching over both knights' positions squares the state space. Instead, BFS from one knight to the other, then halve the distance, rounding up, since both move each turn.",
             st, ["Round up odd distances", "Use a seen set (infinite board)", "Same square → 0"],
             "Round odd distances up. The board is infinite, so a seen set is essential.",
             ["Mention bidirectional BFS"],
             "Bidirectional BFS from both knights would explore far fewer squares.",
             ["We BFS from the first knight, storing x, y and distance. When we dequeue the second knight's square, we return distance plus one over two."])

def LargestRange():
    a = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]; s = set(a); best = (a[0], a[0]); st = []
    for x in sorted(s):
        if x - 1 in s: continue
        y = x
        while y + 1 in s: y += 1
        if y - x > best[1] - best[0]: best = (x, y)
        st.append(S("Worked example", [A(sorted(s), hl={**{k: "ok" for k, v in enumerate(sorted(s)) if x <= v <= y}}, idx=False, label="set (shown sorted for readability)"), TX([f"{x} starts a range (no {x - 1}) → [{x}, {y}]", f"best = {list(best)}"])], f"Range starting at {x}: [{x}, {y}]", f"{x} has no predecessor, so it starts a range. Walking up gives {x} to {y}. The best so far is {best[0]} to {best[1]}."))
    return E(["Sort then scan → O(n log n)", "Hash set + only expand from range starts → O(n)", "Each number visited at most twice"],
             "Sorting and scanning for consecutive runs is n log n. With a hash set, expand only from numbers with no predecessor; each number is touched at most twice, so it's linear.",
             st, ["Duplicates", "Single element → [x, x]", "Only start from range beginnings, or it's O(n²)"],
             "If you expand from every number, it's quadratic. Only start where x minus one is missing.",
             ["Same as Longest Consecutive Sequence"],
             "This is the longest consecutive sequence problem.",
             ["We put everything in a set. For each value with no predecessor, we walk up while the next exists, and keep the widest range."])

def LongestSubarrayWithSum():
    a, T = [1, 2, 3, 4, 3, 3, 1, 2, 1, 2], 10; l = s = 0; best = None; st = []
    for r in range(len(a)):
        s += a[r]
        while s > T and l < r: s -= a[l]; l += 1
        if s == T and (best is None or r - l > best[1] - best[0]): best = (l, r)
        st.append(S("Worked example", [A(a, window=(l, r), hl={k: "ok" for k in range(best[0], best[1] + 1)} if best else {}, ptr={"l": l, "r": r}), TX([f"window sum = {s}", f"best = {list(best) if best else 'none'}"])], f"r = {r}: sum {s}", f"Extend to {a[r]}; the window sum is {s}" + (", too big, so we shrink from the left." if s > T else ".") + (f" Best so far: indices {best[0]} to {best[1]}." if best else "")))
    return E(["Brute force: every subarray → O(n²)", "Sliding window (non-negative values) → O(n)", "Prefix sums + hash map for negatives"],
             "Checking every subarray is quadratic. Since values are non-negative, a sliding window works: grow right, shrink left when the sum is too big, in linear time.",
             pick(st, 6), ["Window only works for non-negatives", "Zeros extend windows", "No match → []"],
             "The window only works because values are non-negative; zeros can extend a match. With negatives, use prefix sums and a hash map.",
             ["Mention the prefix-sum variant"],
             "Mention the prefix-sum and hash-map version for negative numbers.",
             ["We grow r, add a r, shrink from l while the sum exceeds target, and record the window when it matches and is longer."])

def MinRewards():
    s = [8, 4, 2, 1, 3, 6, 7, 9, 5]; n = len(s); r = [1] * n; st = [S("Worked example", [A(s, label="scores"), A(r, label="rewards")], "Start: everyone gets 1", "Everyone starts with one reward.")]
    for i in range(1, n):
        if s[i] > s[i - 1]: r[i] = r[i - 1] + 1
    st.append(S("Worked example", [A(s, label="scores"), A(r, label="rewards after left→right")], "Left pass: beat left neighbour → +1", "Left to right: if a student beats their left neighbour, give them one more than that neighbour."))
    for i in range(n - 2, -1, -1):
        if s[i] > s[i + 1]: r[i] = max(r[i], r[i + 1] + 1)
    st.append(S("Worked example", [A(s, label="scores"), A(r, hl={0: "ok", 1: "ok", 2: "ok"}, label="rewards after right→left")], "Right pass: beat right neighbour → max(own, right + 1)", "Right to left: if a student beats their right neighbour, take the max of what they have and one more than the right neighbour."))
    st.append(S("Worked example", [A(r), TX([f"sum = {sum(r)}"])], f"Total = {sum(r)}", f"Summing gives {sum(r)} rewards, the minimum that satisfies both neighbours."))
    return E(["Brute force: repeat fixes until stable → O(n²)", "Expand from local minima → O(n)", "Two passes (left, right) → O(n)"],
             "Repeatedly fixing violations is quadratic. Two passes, one for each direction, satisfy left and right constraints in linear time.",
             st, ["Use max in the second pass", "Scores are unique", "Single student → 1"],
             "In the second pass, take the max, or you'll undo the left pass.",
             ["Same as LeetCode Candy"],
             "This is the candy problem.",
             ["We fill rewards with one, sweep left giving one more than the left neighbour when higher, sweep right taking the max with right plus one, and sum."])

def SubarraySort():
    a = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]; n = len(a)
    oo = [i for i in range(n) if (i and a[i] < a[i - 1]) or (i < n - 1 and a[i] > a[i + 1])]; mn = min(a[i] for i in oo); mx = max(a[i] for i in oo)
    l = 0
    while a[l] <= mn: l += 1
    r = n - 1
    while a[r] >= mx: r -= 1
    st = [S("Worked example", [A(a, hl={i: "bad" for i in oo})], "Find out-of-order elements", "Mark every element that's smaller than its left neighbour or bigger than its right."),
          S("Worked example", [A(a, hl={a.index(mn): "cur", oo[-1] if a[oo[-1]] == mx else a.index(mx): "warn"}), TX([f"min out of order = {mn}", f"max out of order = {mx}"])], f"Smallest = {mn}, largest = {mx}", f"Among them the smallest is {mn} and the largest is {mx}."),
          S("Worked example", [A(a, window=(l, r), ptr={"l": l, "r": r}), TX([f"{mn} belongs at index {l}; {mx} at index {r}"])], f"Answer: [{l}, {r}]", f"{mn} belongs right after the first value bigger than it, index {l}. {mx} belongs at index {r}. Sorting indices {l} to {r} sorts the array.")]
    return E(["Sort a copy and compare → O(n log n)", "Find min/max out of place, then their positions → O(n)", "O(1) space"],
             "Sorting a copy and finding the first and last differences is n log n. Finding the smallest and largest out-of-order values, then where they belong, is linear.",
             st, ["Already sorted → [−1, −1]", "Duplicates: use ≤ / ≥", "Out-of-order values may be far from the boundary"],
             "If nothing is out of order, return minus one, minus one. Use less-or-equal so duplicates are handled.",
             ["Explain why min/max determine the bounds"],
             "Explain why the extreme out-of-order values define the bounds.",
             ["We track the min and max of out-of-order elements, return minus ones if none, then move l right while values are at most min and r left while values are at least max."])

def ZigzagTraverse():
    m = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]; R, C = 4, 4; out = []; st = []
    for d in range(R + C - 1):
        lo, hi = max(0, d - C + 1), min(d, R - 1); rows = range(lo, hi + 1) if d % 2 == 0 else range(hi, lo - 1, -1)
        cells = [(r, d - r) for r in rows]; out += [m[r][c] for r, c in cells]
        if d in (0, 1, 2, 3, 5, 6): st.append(S("Worked example", [T(m, hl={**{(r, c): "done" for r in range(R) for c in range(C) if r + c < d}, **{x: "cur" for x in cells}}), TX([f"diagonal {d} ({'down' if d % 2 == 0 else 'up'}): {[m[r][c] for r, c in cells]}"])], f"Diagonal {d}", f"Diagonal {d} goes {'down' if d % 2 == 0 else 'up'}: {', '.join(str(m[r][c]) for r, c in cells)}."))
    return E(["Simulate direction changes cell by cell (error-prone)", "Iterate anti-diagonals r + c = d, alternate direction → O(n)", "Each cell once"],
             "Simulating with direction flags works but is fiddly at the edges. Iterating anti-diagonals, where row plus column is constant, and alternating direction is cleaner and still visits each cell once.",
             st, ["Clamp row bounds for each diagonal", "Non-square matrices", "Empty matrix"],
             "Clamp the row range per diagonal so it works for non-square matrices.",
             ["Draw the diagonals first"],
             "Draw the diagonals first; the indexing follows.",
             ["For each diagonal d, the rows run from max zero, d minus C plus one, to min d, R minus one. Even diagonals go down, odd go up, reading column d minus r."])

def RepairBst():
    vals = [10, 7, 20, 3, 12, 8, 22, 2, 14]; nodes, root = bst([10, 7, 20, 3, 12, 8, 22, 2, 14])
    # swap 7 and 20? we instead swap values 7 and 12 to break it
    sw = {v[0]: k for k, v in nodes.items()}; nodes[sw[7]][0], nodes[sw[12]][0] = 12, 7
    def ino(k): return [] if k is None else ino(nodes[k][1]) + [k] + ino(nodes[k][2])
    order = ino(root); seq = [nodes[k][0] for k in order]; bad = [i for i in range(1, len(seq)) if seq[i - 1] > seq[i]]
    first, second = order[bad[0] - 1], order[bad[-1]]
    st = [S("Worked example", [TR(nodes, root, hl={first: "bad", second: "bad"}, w=0.6), TX(["two values swapped"], w=0.4, h=1)], "A BST with two swapped values", "Two values in this BST were swapped. We need to find and fix them.", layout="cols"),
          S("Worked example", [A(seq, hl={bad[0] - 1: "bad", bad[-1]: "bad"}, label="in-order traversal")], f"In-order should be sorted: drops at {[seq[i - 1] for i in bad]} > {[seq[i] for i in bad]}", f"An in-order traversal of a BST is sorted. Here it drops: the first is the larger value before the first drop, {seq[bad[0] - 1]}, and the second is the smaller value after the last drop, {seq[bad[-1]]}."),
          ]
    nodes[first][0], nodes[second][0] = nodes[second][0], nodes[first][0]
    st.append(S("Worked example", [TR(nodes, root, hl={first: "ok", second: "ok"}, w=0.6), A([nodes[k][0] for k in order], label="in-order", w=0.4)], "Swap them back → valid BST", "Swap those two values back and the in-order traversal is sorted again.", layout="cols"))
    return E(["Copy in-order to array, sort, rewrite → O(n) space", "In-order with prev pointer, catch the two violations → O(h) space", "Morris traversal → O(1) space"],
             "Dumping the in-order traversal into an array, sorting it and writing it back uses linear space. Tracking the previous node during an in-order walk spots the violations with only the stack.",
             st, ["Adjacent swap → only one drop", "First = prev at first drop, second = cur at last drop", "Swap values, not nodes"],
             "If the swapped nodes are adjacent in order, there's only one drop; the rule still works.",
             ["Mention Morris traversal for O(1) space"],
             "Mention Morris traversal for constant space.",
             ["We do an iterative in-order traversal. When prev is greater than cur, the first time we record prev as first, and every time we record cur as second. Finally we swap their values."])

def SameBsts():
    a = [10, 15, 8, 12, 94, 81, 5, 2, 11]; b = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    st = [S("Worked example", [A(a, label="array A"), A(b, label="array B")], "Same root? 10 = 10 ✓", "Both arrays start with ten, so the roots match."),
          S("Worked example", [A([x for x in a if x < 10], label="A: smaller than 10"), A([x for x in b if x < 10], label="B: smaller than 10")], "Left subtrees: [8, 5, 2] vs [8, 5, 2]", "Values smaller than ten, in order, form the left subtree. Both start with eight; recurse."),
          S("Worked example", [A([x for x in a if x >= 10][1:], label="A: ≥ 10"), A([x for x in b if x >= 10][1:], label="B: ≥ 10")], "Right subtrees: first is 15 in both", "Values at least ten form the right subtree. Both begin with fifteen. Recursing all the way, everything matches."),
          S("Worked example", [TR(*bst(a))], "Same BST", "So both arrays build exactly this BST, without us ever building it.")]
    return E(["Build both BSTs and compare → O(n²) worst", "Split into smaller/larger lists recursively → O(n²) time and space", "Index-based recursion with bounds → O(n²) time, O(d) space"],
             "Building both trees and comparing is straightforward. Without building, we can recursively compare roots and split each array into smaller and larger values. Passing indices and bounds avoids copying.",
             st, ["Duplicates go right (≥)", "Different lengths → false", "Empty arrays → true"],
             "Duplicates go to the right subtree. Different lengths mean different trees.",
             ["Explain why relative order within subtrees matters"],
             "Explain that only relative order within each subtree matters.",
             ["Same compares the current roots, then recurses on the first smaller element in range and the first bigger element in range, for both arrays, narrowing the min and max bounds."])

def SumBsts():
    nodes, root = level_tree([8, 5, 2, 3, 7, None, 1, None, None, 6, 9]); st = []
    st.append(S("Worked example", [TR(nodes, root, w=0.6), TX(["post-order: each node returns", "(isBst, size, min, max, sum)"], w=0.4, h=1, size=18)], "Post-order: return BST info upward", "Each node returns whether its subtree is a BST, its size, min, max and sum, computed from its children.", layout="cols"))
    st.append(S("Worked example", [TR(nodes, root, hl={"4": "ok", "9": "ok", "10": "ok"}, w=0.6), TX(["subtree 7: {6, 7, 9}", "BST, size 3 → sum 22"], w=0.4, h=1)], "Subtree at 7 is a BST of size 3 → 22", "The subtree rooted at seven, with six and nine, is a BST with three nodes, sum twenty-two.", layout="cols"))
    st.append(S("Worked example", [TR(nodes, root, hl={"1": "ok", "3": "ok", "4": "ok", "9": "ok", "10": "ok"}, w=0.6), TX(["subtree 5: 3 < 5 ≤ 6 ✓", "BST, size 5 → sum 30", "(replaces the 22 inside it)"], w=0.4, h=1, size=18)], "Subtree at 5 is a bigger BST → 30", "At five, the left max is three and the right min is six, so it's a BST of five nodes summing to thirty. That replaces the twenty-two we counted inside it.", layout="cols"))
    st.append(S("Worked example", [TR(nodes, root, hl={"2": "bad", "6": "bad", "0": "bad"}, w=0.6), TX(["subtree 2: right child 1 < 2 ✗", "root 8: right side invalid ✗", "answer = 30"], w=0.4, h=1, size=18)], "Other subtrees fail → answer 30", "Two has a right child of one, which breaks the BST rule, so the root fails too. The answer is thirty.", layout="cols"))
    return E(["For each node validate subtree, then sum → O(n²)", "Single post-order pass returning (isBst, size, min, max, sum) → O(n)"],
             "Validating each subtree separately is quadratic. One post-order pass that returns validity, size, min, max and sum lets every node decide in constant time.",
             st, ["Only BSTs with ≥ 3 nodes count", "Don't double count nested BSTs", "Empty subtree = valid, size 0"],
             "Only subtrees with at least three nodes count, and a larger valid BST replaces the contributions of the smaller ones inside it.",
             ["State the returned tuple clearly"],
             "State the tuple you return from each call clearly; it's the whole trick.",
             ["Info recurses on both children, decides BST status from their max and min, and when the subtree is a BST of size three or more adds its sum, subtracting children already counted. It returns the tuple."])

def ValidateThreeNodes():
    nodes, root = bst([5, 2, 7, 1, 4, 6, 8, 0, 3]); ids = {v[0]: k for k, v in nodes.items()}
    st = [S("Worked example", [TR(nodes, root, hl={ids[5]: "cur", ids[2]: "warn", ids[3]: "ok"})], "nodeOne = 5, nodeTwo = 2, nodeThree = 3", "Is two between five and three: is five an ancestor of two, and two an ancestor of three, or the reverse?"),
          S("Worked example", [TR(nodes, root, hl={ids[5]: "done", ids[2]: "cur"})], "Search 2 from 5: 5 → 2 ✓", "Starting at five, search for two using BST order: go left, found it. So five is an ancestor of two."),
          S("Worked example", [TR(nodes, root, hl={ids[2]: "done", ids[4]: "done", ids[3]: "ok"})], "Search 3 from 2: 2 → 4 → 3 ✓ → true", "Now search for three from two: right to four, left to three. Found, so the answer is true.")]
    return E(["Find all paths from root, compare → O(n)", "BST searches between nodes → O(h)", "Search simultaneously from one and three for O(d) best case"],
             "Instead of exploring the whole tree, we can use BST searches: check whether one reaches two, then two reaches three, or the other way around. That's height time.",
             st, ["Either direction: one→two→three or three→two→one", "Compare node identity", "Node two must be strictly between"],
             "Check both directions, and compare node references, not just values.",
             ["Mention the simultaneous search optimisation"],
             "Mention the optimisation that searches from both ends at once, stopping early.",
             ["If two descends from one, return whether three descends from two. Otherwise if two descends from three, return whether one descends from two. Descends walks down using BST order until it hits the target or null."])

def FindNodesDistanceK():
    nodes, root = level_tree([1, 2, 3, 4, 5, None, 6, None, None, None, None, None, None, 7, 8]); par = {}
    for k, (v, l, r) in nodes.items():
        for c in (l, r):
            if c: par[c] = k
    start = "2"; seen = {start}; q = [start]; st = [S("Worked example", [TR(nodes, root, hl={start: "cur"})], "Target = 3, k = 2: start BFS at 3", "We want nodes at distance two from three. First record each node's parent, then BFS from three.")]
    for d in range(2):
        nq = []
        for n in q:
            v, l, r = nodes[n]
            for x in (l, r, par.get(n)):
                if x and x not in seen: seen.add(x); nq.append(x)
        q = nq
        st.append(S("Worked example", [TR(nodes, root, hl={**{s: "done" for s in seen}, **{x: "ok" for x in q}, start: "cur"})], f"Distance {d + 1}: {[nodes[x][0] for x in q]}", f"At distance {d + 1}, moving to children and to the parent, we reach {', '.join(str(nodes[x][0]) for x in q)}."))
    return E(["Treat as graph: add parent pointers, BFS k levels → O(n)", "Recursive distance-from-target approach also O(n)", "Seen set prevents going back"],
             "A tree only lets you go down, but distance can go up too. Recording parents turns it into an undirected graph, and BFS k levels from the target gives the answer in linear time.",
             st, ["Target not found → []", "k = 0 → [target]", "Visited set to avoid bouncing back"],
             "If k is zero, return the target itself. The seen set stops you from walking back along the same edge.",
             ["Mention the recursive O(1)-extra-space version"],
             "There's also a recursive solution without parent maps.",
             ["We DFS to build the parent map and locate the target, then BFS k levels, enqueuing unseen children and parent, and return the values in the queue."])

def MaxPathSumInBinaryTree():
    nodes, root = level_tree([1, 2, 3, 4, 5, 6, 7]); memo = {}; best = [float("-inf")]; st = []
    def br(k):
        if k is None: return 0
        v, l, r = nodes[k]; L = max(0, br(l)); R = max(0, br(r)); best[0] = max(best[0], v + L + R); memo[k] = (v + max(L, R), v + L + R)
        st.append(S("Worked example", [TR(nodes, root, hl={k: "cur", **{x: "done" for x in memo if x != k}}, notes={x: f"↑{memo[x][0]}" for x in memo}), TX([f"node {v}: through = {v + L + R}, returns {v + max(L, R)}", f"best = {best[0]}"])], f"Node {v}: path through = {v + L + R}", f"At {v}, the best path bending through here is {v + L + R}. We return {v + max(L, R)} upward, a single branch. The best so far is {best[0]}."))
        return v + max(L, R)
    br(root)
    return E(["Brute force: every pair of nodes as endpoints → O(n²)", "Post-order: return best single branch, update best bend → O(n)"],
             "Trying every pair of endpoints is quadratic. In one post-order pass, each node returns its best downward branch and updates a global best for paths that bend through it.",
             pick(st, 6), ["Clamp negative branches to 0", "All-negative tree: answer is the max node", "Return a single branch, not both"],
             "Clamp negative branches to zero, and initialise the best with minus infinity so an all-negative tree returns its largest node.",
             ["Explain 'return branch vs record bend'"],
             "Explain the difference between what you return, a branch, and what you record, a bend.",
             ["Branch returns zero for null, clamps both children at zero, updates best with value plus both, and returns value plus the larger."])

def DiceThrows():
    D, Sd, T = 2, 6, 7; w = [1] + [0] * T; st = [S("Worked example", [A(w, label="ways to reach each total (0 dice)")], "0 dice: one way to make 0", "With zero dice, there's one way to make a total of zero.")]
    for d in range(D):
        nx = [0] * (T + 1)
        for t in range(T + 1):
            if w[t]:
                for s in range(1, Sd + 1):
                    if t + s <= T: nx[t + s] += w[t]
        w = nx
        st.append(S("Worked example", [A(w, label=f"ways after {d + 1} dice", hl={T: "ok"} if d == D - 1 else {})], f"After die {d + 1}: ways[7] = {w[T]}", f"Adding die {d + 1}, each total spreads to the next one to six totals. Now there are {w[T]} ways to make seven."))
    return E(["Recurse over each die's face → O(sides^dice)", "DP over (dice, total) → O(dice · target · sides)", "Rolling array"],
             "Trying every face combination is sides to the power dice. A DP over number of dice and total counts them in dice times target times sides.",
             st, ["Target out of range → 0", "Use long / mod for big counts", "Skip zero entries"],
             "Targets below the number of dice or above dice times sides have zero ways.",
             ["Follow-up: probability = ways / sides^dice"],
             "Dividing by sides to the dice gives the probability.",
             ["Ways starts with one at zero. For each die, a new array spreads every reachable total to total plus one through total plus sides. Return ways of target."])

def DiskStacking():
    d = sorted([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]], key=lambda x: x[2]); n = len(d); h = [x[2] for x in d]; prev = [-1] * n; st = []
    for i in range(n):
        for j in range(i):
            if all(d[j][k] < d[i][k] for k in range(3)) and h[j] + d[i][2] > h[i]: h[i] = h[j] + d[i][2]; prev[i] = j
        st.append(S("Worked example", [T([[*x, h[k] if k <= i else ""] for k, x in enumerate(d)], colh=["w", "d", "h", "best height"], hl={(i, 3): "cur"}), TX([f"disk {d[i]}: best stack height {h[i]}"])], f"Disk {d[i]}: {h[i]}", f"Disk {d[i]}: the tallest stack with it on the bottom is {h[i]}" + (f", placing it under {d[prev[i]]}." if prev[i] >= 0 else ", alone.")))
    b = max(range(n), key=lambda i: h[i]); seq = []
    while b != -1: seq.insert(0, d[b]); b = prev[b]
    st.append(S("Worked example", [TX([f"stack: {seq}", f"height {sum(x[2] for x in seq)}"])], f"Best stack height {sum(x[2] for x in seq)}", f"Following the back-pointers gives {seq}, height {sum(x[2] for x in seq)}."))
    return E(["Try all subsets/orders → exponential", "Sort by height, LIS-style DP → O(n²)", "Back-pointers rebuild the stack"],
             "Trying every order is exponential. Sorting by height and running a longest-increasing-subsequence style DP over strictly smaller disks is quadratic.",
             pick(st, 6), ["All three dimensions strictly smaller", "Sorting by one dimension is enough", "Track prev to rebuild"],
             "All three dimensions must be strictly smaller.",
             ["Relate to Box Stacking / LIS"],
             "Relate it to longest increasing subsequence.",
             ["We sort by height. For each disk, start with its own height, and for each earlier strictly smaller disk extend if taller. Track the best index, then follow prev to build the answer."])

def JuiceBottling():
    p = [0, 1, 3, 2]; n = len(p); best = [0] * n; cut = [0] * n; st = []
    for s in range(1, n):
        for k in range(1, s + 1):
            if p[k] + best[s - k] > best[s]: best[s] = p[k] + best[s - k]; cut[s] = k
        st.append(S("Worked example", [A(p, label="price per bottle size"), A(best, label="best revenue for amount", hl={s: "ok"})], f"Amount {s}: best {best[s]} (first bottle {cut[s]})", f"For {s} units, try every first bottle size. The best is {best[s]}, starting with a bottle of {cut[s]}."))
    out = []; s = n - 1
    while s > 0: out.append(cut[s]); s -= cut[s]
    st.append(S("Worked example", [TX([f"bottles: {out}", f"revenue {best[-1]}"])], f"Answer: {out}", f"Following the cuts gives bottles of {out}, revenue {best[-1]}."))
    return E(["Try all partitions → exponential", "Rod-cutting DP → O(n²)", "Store the first cut to rebuild"],
             "Trying every partition is exponential. This is rod cutting: best of s is the max over first bottle k of price k plus best of s minus k, quadratic.",
             st, ["prices[0] = 0", "Rebuild from cut[]", "Ties: any order fine"],
             "Price zero is always zero. Store the first cut so you can rebuild.",
             ["Name it: rod cutting"],
             "Name it the rod-cutting problem.",
             ["For each amount s and each first size k, update best and cut. Then walk down from n minus one subtracting cuts."])

def KnapsackProblem():
    items, cap = [[1, 2], [4, 3], [5, 6], [6, 7]], 10; n = len(items); dp = [[0] * (cap + 1) for _ in range(n + 1)]; st = []
    for i in range(1, n + 1):
        v, w = items[i - 1]
        for c in range(cap + 1):
            dp[i][c] = dp[i - 1][c]
            if w <= c: dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)
        st.append(S("Worked example", [T([r for r in dp[:i + 1]], rowh=["–"] + [f"[{a},{b}]" for a, b in items[:i]], colh=["", *range(cap + 1)], hl={(i, c): "ok" for c in range(cap + 1) if dp[i][c] != dp[i - 1][c]})], f"Item [{v} value, {w} weight]", f"Add the item worth {v} weighing {w}. Green cells improved by taking it. Best for capacity ten is now {dp[i][cap]}."))
    ch = []; c = cap
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]: ch.insert(0, i - 1); c -= items[i - 1][1]
    st.append(S("Worked example", [TX([f"max value {dp[n][cap]}", f"items {ch}"])], f"Answer: {dp[n][cap]} using items {ch}", f"Backtracking from the bottom-right, the chosen items are {ch}, worth {dp[n][cap]}."))
    return E(["Try all 2ⁿ subsets", "DP table (items × capacity) → O(n·C)", "1-D array iterating capacity downward → O(C) space"],
             "Trying all subsets is exponential. A table over items and capacity is n times C, pseudo-polynomial, and backtracking recovers the items.",
             st, ["Pseudo-polynomial in capacity", "1-D version must iterate capacity downward", "Backtrack to recover items"],
             "This is pseudo-polynomial. The one-dimensional version must iterate capacity downward.",
             ["Mention unbounded vs 0/1 knapsack"],
             "Contrast zero-one with unbounded knapsack.",
             ["Dp of i, c is either skipping the item, or taking it if it fits. Then from the bottom-right, a change between rows means the item was taken."])

def LongestCommonSubsequence():
    a, b = "ZXVVYZW", "XKYKZPW"; n, m = len(a), len(b); dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1): dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    path = []; i, j = n, m; out = []
    while i and j:
        path.append((i, j))
        if a[i - 1] == b[j - 1]: out.insert(0, a[i - 1]); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]: i -= 1
        else: j -= 1
    st = [S("Worked example", [T(dp, rowh=["", *a], colh=["", "", *b], hl={(r, c): "ok" for r in range(1, n + 1) for c in range(1, m + 1) if a[r - 1] == b[c - 1]})], "Fill: match → diagonal + 1, else max(up, left)", "Fill the table: matching letters take the diagonal plus one; otherwise the max of above and left. Green cells are matches."),
          S("Worked example", [T(dp, rowh=["", *a], colh=["", "", *b], hl={p: "cur" for p in path})], "Backtrack from the bottom-right", "Backtrack from the bottom-right: on a match, take the letter and go diagonally; otherwise move toward the larger neighbour."),
          S("Worked example", [TX([f"LCS = {''.join(out)} (length {dp[n][m]})"])], f"LCS = {''.join(out)}", f"The longest common subsequence is {', '.join(out)}, length {dp[n][m]}.")]
    return E(["Brute force: all subsequences of one string → O(2ⁿ · m)", "DP over prefixes → O(n·m)", "Backtrack to recover the sequence"],
             "Enumerating subsequences is exponential. A DP over prefixes is n times m, and backtracking recovers the actual letters.",
             st, ["Off-by-one with the padding row/column", "Ties in backtracking: any choice valid", "Empty string → []"],
             "Mind the padding row and column. Ties during backtracking can go either way.",
             ["Relate to edit distance and diff tools"],
             "Relate it to diff tools and edit distance.",
             ["We fill the table with the match-or-max rule, then walk back from n, m, prepending matching characters."])

def MaxSumIncreasingSubsequence():
    a = [10, 70, 20, 30, 50, 11, 30]; n = len(a); s = a[:]; prev = [-1] * n; st = []
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and s[j] + a[i] > s[i]: s[i] = s[j] + a[i]; prev[i] = j
        st.append(S("Worked example", [A(a, hl={i: "cur", **({prev[i]: "warn"} if prev[i] >= 0 else {})}), A(s[:i + 1] + [""] * (n - i - 1), label="best sum ending here", hl={i: "ok"})], f"{a[i]}: best sum ending here = {s[i]}", f"For {a[i]}, extend the best earlier smaller value" + (f", {a[prev[i]]}, giving {s[i]}." if prev[i] >= 0 else f"; there's none, so it's just {s[i]}.")))
    b = max(range(n), key=lambda i: s[i]); seq = []
    while b != -1: seq.insert(0, a[b]); b = prev[b]
    st.append(S("Worked example", [TX([f"sum {max(s)}: {seq}"])], f"Answer: {max(s)} via {seq}", f"The best is {max(s)}: {seq}."))
    return E(["All increasing subsequences → exponential", "LIS-style DP on sums → O(n²)", "prev[] to rebuild"],
             "Enumerating subsequences is exponential. A longest-increasing-subsequence style DP on sums is quadratic.",
             pick(st, 6), ["Strictly increasing", "Negatives: single element might win", "Track prev"],
             "Keep it strictly increasing; with negatives, a single element may be best.",
             ["Follow-up: O(n log n) with a BIT keyed by value"],
             "A Fenwick tree keyed by value gets it to n log n.",
             ["Sums starts as a copy. For each i and each earlier smaller j, extend if better and record prev. Rebuild from the best index."])

def MaximizeExpression():
    a = [3, 6, 1, -3, 2, 7]; NEG = float("-inf"); s1 = s2 = s3 = s4 = NEG; st = []
    for i, x in enumerate(a):
        if i >= 3: s4 = max(s4, s3 - x)
        if i >= 2: s3 = max(s3, s2 + x)
        if i >= 1: s2 = max(s2, s1 - x)
        s1 = max(s1, x)
        f = lambda v: "–" if v == NEG else v
        st.append(S("Worked example", [A(a, hl={i: "cur"}), T([[f(s1), f(s2), f(s3), f(s4)]], colh=["max a", "max a−b", "max a−b+c", "max a−b+c−d"])], f"i={i}: best a−b+c−d = {f(s4)}", f"At {x}, update each stage from the previous one, right to left. The best full expression so far is {f(s4)}."))
    return E(["Brute force: all i<j<k<l → O(n⁴)", "Four DP arrays → O(n)", "Four running scalars → O(1) space"],
             "Checking every quadruple is n to the fourth. Building the expression in stages, max a, then max a minus b, and so on, is linear, and four running values suffice.",
             st, ["Fewer than 4 elements → 0", "Update later stages before earlier ones", "Avoid overflow with sentinels"],
             "With fewer than four elements, return zero. Update in reverse stage order so each uses the previous index's values.",
             ["Explain the staged DP"],
             "Explain the staged DP; it generalises to any alternating expression.",
             ["We keep four stage values. For each index, update stage four from three minus x, three from two plus x, two from one minus x, and one from x."])

def MaximumSumSubmatrix():
    m = [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]; k = 2; R, C = 4, 4
    p = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        for c in range(C): p[r + 1][c + 1] = m[r][c] + p[r][c + 1] + p[r + 1][c] - p[r][c]
    best = None; bp = None
    for r in range(k, R + 1):
        for c in range(k, C + 1):
            v = p[r][c] - p[r - k][c] - p[r][c - k] + p[r - k][c - k]
            if best is None or v > best: best, bp = v, (r, c)
    st = [S("Worked example", [T(m, label="matrix", w=0.5), T(p, label="prefix sums", w=0.5)], "Build 2-D prefix sums", "Build prefix sums: each cell holds the sum of everything above and to the left.", layout="cols"),
          S("Worked example", [T(m, hl={(r, c): "ok" for r in range(bp[0] - k, bp[0]) for c in range(bp[1] - k, bp[1])}), TX([f"sum = P[r][c] − P[r−2][c] − P[r][c−2] + P[r−2][c−2] = {best}"], size=18)], f"Best {k}×{k}: {best}", f"Any k by k sum is four lookups. The best two-by-two block sums to {best}.")]
    return E(["Sum every k×k block directly → O(R·C·k²)", "2-D prefix sums → O(R·C)", "Inclusion–exclusion per block"],
             "Summing each block directly costs k squared per block. With two-dimensional prefix sums, each block is four lookups, linear overall.",
             st, ["Add back the double-subtracted corner", "Off-by-one with padding", "Negative values"],
             "Remember to add back the corner you subtracted twice.",
             ["Follow-up: max submatrix of any size (Kadane in 2-D)"],
             "For any size, combine column compression with Kadane.",
             ["We build the padded prefix table, then for each bottom-right corner compute the block via inclusion-exclusion and keep the max."])

def MinNumberOfJumps():
    a = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]; j = end = far = 0; st = []
    for i in range(len(a) - 1):
        far = max(far, i + a[i])
        if i == end:
            j += 1; end = far
            st.append(S("Worked example", [A(a, window=(i, min(end, len(a) - 1)), ptr={"i": i}), TX([f"reached the end of this jump's range → jump #{j}", f"new range ends at {end}"])], f"Jump {j}: reach up to index {end}", f"At index {i}, we've used up the range of the current jump. Take jump number {j}, extending the reach to index {end}."))
    return E(["DP: for each i, check all earlier j → O(n²)", "Greedy BFS by ranges → O(n)", "Track current range end and farthest reach"],
             "A DP checking every earlier index is quadratic. Greedily, think of ranges like BFS levels: within each jump's range, track the farthest reach, and jump when you exhaust the range.",
             st, ["Don't process the last index", "Single element → 0", "Always reachable (given)"],
             "Stop before the last index, or you'll count an extra jump.",
             ["Explain the BFS-levels view"],
             "Explain it as BFS levels over ranges.",
             ["We track jumps, current end and farthest. For each index before the last, extend farthest; when i reaches end, count a jump and move end to farthest."])

def NumbersInPi():
    pi = "3141592"; nums = ["3141", "5", "31", "2", "4159", "9", "42"]; S_ = set(nums); n = len(pi); INF = float("inf"); dp = [INF] * (n + 1); dp[n] = -1; st = []
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if dp[j] != INF and pi[i:j] in S_: dp[i] = min(dp[i], dp[j] + 1)
        if dp[i] != INF or i in (5,): st.append(S("Worked example", [A(list(pi), hl={i: "cur"}, idx=False), A(["∞" if x == INF else x for x in dp], label="min spaces from i")], f"i={i}: {'∞' if dp[i] == INF else dp[i]}", f"From index {i}, try every favourite number starting here" + (f": the fewest spaces for the rest is {dp[i]}." if dp[i] != INF else ": none fits, so it's impossible.")))
    return E(["Try every split → exponential", "Memoised suffix DP → O(n² + m)", "Hash set for O(1) lookups"],
             "Trying every split is exponential. A DP over suffixes, the fewest spaces from index i onward, is quadratic with a hash set of numbers.",
             st, ["dp[n] = −1 (no space after the last number)", "Impossible → −1", "Substring cost"],
             "Seed the end with minus one, because there's no space after the last number.",
             ["Same as Word Break (min pieces)"],
             "This is word break, minimising the pieces.",
             ["Dp of n is minus one. From the end backward, for each j, if the rest is solvable and pi from i to j is a favourite, take dp j plus one. Return dp zero or minus one."])

def WaterArea():
    h = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]; l, r = 0, len(h) - 1; lm = rm = w = 0; st = []; k = 0
    while l < r:
        if h[l] < h[r]: lm = max(lm, h[l]); w += lm - h[l]; mv = ("l", l, lm - h[l]); l += 1
        else: rm = max(rm, h[r]); w += rm - h[r]; mv = ("r", r, rm - h[r]); r -= 1
        k += 1
        if k in (1, 3, 5, 8, 11, 13): st.append(S("Worked example", [A(h, ptr={"l": l, "r": r}, hl={mv[1]: "acc"}), TX([f"index {mv[1]} holds {mv[2]}", f"total = {w}"])], f"Index {mv[1]}: +{mv[2]} → {w}", f"The {'left' if mv[0] == 'l' else 'right'} side is lower, so its max bounds the water at index {mv[1]}: {mv[2]} units. Total {w}."))
    return E(["Per index: scan left and right for maxes → O(n²)", "Prefix max arrays → O(n) time, O(n) space", "Two pointers → O(n), O(1)"],
             "Scanning both sides for every index is quadratic. Prefix and suffix max arrays make it linear. Two pointers do it in constant space: the lower side's max is the binding limit.",
             st, ["Empty / short arrays → 0", "Move the lower side", "Water = max − height (never negative)"],
             "Always move the side with the smaller height; its max is the limit.",
             ["Same as Trapping Rain Water"],
             "This is trapping rain water.",
             ["While l is less than r, move the smaller side: update its max, add max minus height, and step inward."])

_GP = {0: [.1, .7], 1: [.4, .9], 2: [.4, .4], 3: [.7, .75], 4: [.7, .25], 5: [.95, .5]}

def DijkstrasAlgorithm():
    import heapq
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]; INF = float("inf"); d = [INF] * 6; d[0] = 0; pq = [(0, 0)]; done = set(); st = []
    E_ = [(u, v) for u in range(6) for v, w in edges[u]]; names = {(u, v): w for u in range(6) for v, w in edges[u]}
    while pq:
        c, u = heapq.heappop(pq)
        if c > d[u]: continue
        done.add(u); upd = []
        for v, w in edges[u]:
            if c + w < d[v]: d[v] = c + w; heapq.heappush(pq, (d[v], v)); upd.append(v)
        st.append(S("Worked example", [G(_GP, E_, hl={**{x: "done" for x in done}, u: "cur", **{x: "ok" for x in upd}}, ehl=[(u, v) for v in upd], directed=True, notes={k: ("∞" if d[k] == INF else str(d[k])) for k in range(6)}, w=0.65), TX(["dist: " + str(["∞" if x == INF else x for x in d])], w=0.35, h=1, size=16)],
                    f"Pop {u} (dist {c}); relax {', '.join(map(str, upd)) or 'nothing'}", f"Pop vertex {u}, the closest unfinished one at distance {c}." + (f" Relaxing its edges improves {', '.join(map(str, upd))}." if upd else " No edge improves anything."), layout="cols"))
    return E(["Bellman–Ford: relax all edges V−1 times → O(V·E)", "Dijkstra with array scan → O(V²)", "Dijkstra with a min-heap → O((V + E) log V)"],
             "Bellman-Ford relaxes every edge repeatedly and handles negative weights, but it's V times E. Dijkstra always finalises the closest unfinished vertex; with a heap that's E log V.",
             st, ["Negative weights break Dijkstra", "Skip stale heap entries", "Unreachable → −1"],
             "Dijkstra needs non-negative weights. Lazy deletion means skipping heap entries whose distance is stale.",
             ["Explain why the greedy choice is safe", "Follow-up: path reconstruction, A*"],
             "Explain why the closest vertex can be finalised. Follow-ups reconstruct paths or add a heuristic, which is A star.",
             ["Distances start at max except the start. We poll the heap, skip stale entries, and relax each edge, pushing improved distances. Finally we map max value to minus one."])

def KruskalsAlgorithm():
    edges = [(0, 1, 3), (0, 2, 5), (1, 2, 1), (1, 3, 4), (2, 3, 2), (3, 4, 6), (2, 4, 7)]; pos = {0: [.1, .5], 1: [.35, .85], 2: [.35, .15], 3: [.65, .5], 4: [.9, .5]}
    par = list(range(5))
    def f(x):
        while par[x] != x: x = par[x]
        return x
    mst = []; st = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        a, b = f(u), f(v); ok = a != b
        if ok: par[a] = b; mst.append((u, v))
        st.append(S("Worked example", [G(pos, [(u_, v_) for u_, v_, _ in edges], ehl=mst + ([] if ok else []), hl={u: "ok" if ok else "bad", v: "ok" if ok else "bad"}, notes=None, w=0.65), TX([f"edge {u}–{v} (w {w})", "add ✓" if ok else "would form a cycle ✗", f"MST weight {sum(w_ for u_, v_, w_ in edges if (u_, v_) in mst)}"], w=0.35, h=1, size=18)],
                    f"Edge {u}–{v} ({w}): " + ("add" if ok else "skip (cycle)"), f"Next cheapest edge: {u} to {v}, weight {w}. " + ("They're in different components, so add it." if ok else "They're already connected, so it would form a cycle; skip it."), layout="cols"))
    return E(["Try all spanning trees → exponential", "Kruskal: sort edges + union-find → O(E log E)", "Prim: grow from a vertex with a heap"],
             "Enumerating spanning trees is exponential. Kruskal sorts edges and adds each cheapest one that doesn't form a cycle, checked with union-find, in E log E.",
             pick(st, 6), ["Undirected edges appear twice — dedupe", "Disconnected graph → spanning forest", "Use path compression"],
             "Each undirected edge appears in both lists; add it once. A disconnected graph yields a forest.",
             ["Cut property explains correctness", "Kruskal vs Prim trade-offs"],
             "The cut property explains why the cheapest crossing edge is safe. Kruskal suits sparse graphs; Prim with a heap suits dense ones.",
             ["We collect each edge once, sort by weight, and for each edge union the two roots if different, recording it in both adjacency lists."])

def PrimsAlgorithm():
    import heapq
    edges = [(0, 1, 3), (0, 2, 5), (1, 2, 1), (1, 3, 4), (2, 3, 2), (3, 4, 6), (2, 4, 7)]; pos = {0: [.1, .5], 1: [.35, .85], 2: [.35, .15], 3: [.65, .5], 4: [.9, .5]}
    adj = {i: [] for i in range(5)}
    for u, v, w in edges: adj[u].append((v, w)); adj[v].append((u, w))
    inn = {0}; pq = [(w, 0, v) for v, w in adj[0]]; heapq.heapify(pq); mst = []; st = [S("Worked example", [G(pos, [(u, v) for u, v, _ in edges], hl={0: "ok"}, w=0.65), TX(["tree = {0}"], w=0.35, h=1)], "Start the tree at vertex 0", "Start with vertex zero in the tree, and its edges in a min-heap.", layout="cols")]
    while pq:
        w, u, v = heapq.heappop(pq)
        if v in inn: continue
        inn.add(v); mst.append((min(u, v), max(u, v)))
        for x, ww in adj[v]:
            if x not in inn: heapq.heappush(pq, (ww, v, x))
        st.append(S("Worked example", [G(pos, [(a, b) for a, b, _ in edges], hl={k: "ok" for k in inn} | {v: "cur"}, ehl=mst, w=0.65), TX([f"cheapest crossing edge {u}–{v} ({w})", f"tree = {sorted(inn)}"], w=0.35, h=1, size=18)], f"Add {u}–{v} ({w})", f"The cheapest edge leaving the tree is {u} to {v}, weight {w}. Add {v} and push its edges.", layout="cols"))
    return E(["Try all spanning trees → exponential", "Prim with array scan → O(V²)", "Prim with a heap → O(E log V)"],
             "Prim grows one tree, always adding the cheapest edge that leaves it. With a heap, that's E log V.",
             st, ["Skip edges into vertices already in the tree", "Disconnected graph", "Store edges both ways in the result"],
             "Lazy deletion again: skip heap edges that lead back into the tree.",
             ["Cut property", "Compare with Kruskal"],
             "Same cut property argument as Kruskal.",
             ["We mark zero as in, push its edges, and repeatedly poll the cheapest; if its endpoint is new, add the edge both ways and push that vertex's outgoing edges."])

def TopologicalSort():
    jobs = [1, 2, 3, 4]; deps = [(1, 2), (1, 3), (3, 2), (4, 2), (4, 3)]; g = {j: [] for j in jobs}; ind = {j: 0 for j in jobs}
    for a, b in deps: g[a].append(b); ind[b] += 1
    q = [j for j in jobs if ind[j] == 0]; out = []; st = []
    pos = {1: [.2, .8], 4: [.2, .2], 3: [.55, .5], 2: [.9, .5]}
    while q:
        j = q.pop(0); out.append(j); fr = []
        for k in g[j]:
            ind[k] -= 1
            if ind[k] == 0: q.append(k); fr.append(k)
        st.append(S("Worked example", [G(pos, deps, directed=True, hl={**{x: "done" for x in out}, j: "cur", **{x: "ok" for x in q}}, notes={k: f"in {ind[k]}" for k in jobs if k not in out}, w=0.6), TX([f"order: {out}", f"queue: {q}"], w=0.4, h=1)], f"Take {j}" + (f"; {fr} now free" if fr else ""), f"Job {j} has no remaining prerequisites, so it goes next. " + (f"That frees {', '.join(map(str, fr))}." if fr else "It frees nothing new."), layout="cols"))
    return E(["Repeatedly scan for a job with no prerequisites → O(V²)", "Kahn's algorithm with in-degrees → O(V + E)", "DFS post-order also works"],
             "Scanning repeatedly for a free job is quadratic. Kahn's algorithm keeps in-degrees and a queue of free jobs, linear time. A depth-first post-order also works.",
             st, ["Cycle → fewer jobs output → []", "Multiple valid orders", "Isolated jobs"],
             "If a cycle exists, some jobs never reach in-degree zero, so return an empty list.",
             ["Mention DFS-based alternative and cycle detection"],
             "Mention the DFS approach and how it detects cycles with colours.",
             ["We build adjacency lists and in-degrees, queue jobs with zero, and repeatedly output one, decrementing its dependents and queuing any that hit zero. If not everything is output, return empty."])

def BoggleBoard():
    b = [list("this"), list("wats"), list("oahg"), list("fgdt")]; path = [(0, 0), (0, 1), (0, 2), (0, 3)]
    st = [S("Worked example", [T(b), TX(["words: this, two, fat, that…"], h=0.35)], "Board and dictionary (built into a trie)", "Put every word in a trie, then search the board from each cell."),
          S("Worked example", [T(b, hl={(0, 0): "cur"}), TX(["t → trie has 't' ✓"], h=0.35)], "Start at 't'", "From the t in the corner, the trie has a branch for t, so continue."),
          S("Worked example", [T(b, hl={p: "ok" for p in path}), TX(["t-h-i-s → word 'this' ✓"], h=0.35)], "t → h → i → s: found 'this'", "Moving to neighbours h, i, s, we reach a trie node marking the word this."),
          S("Worked example", [T(b, hl={(0, 0): "cur", (1, 0): "warn"}), TX(["t → w: trie has 'tw' ✓ (two)", "t → a: … prune if no branch"], h=0.5)], "Prune when the trie has no branch", "Any time the trie has no branch for the next letter, we stop exploring that path. That pruning is what makes it fast.")]
    return E(["Search each word separately on the board → O(words · cells · 8^L)", "Trie + single DFS from each cell → prunes shared prefixes", "Mark cells used on the current path"],
             "Searching for each word separately repeats work for shared prefixes. A trie of all words lets one DFS from each cell explore them together and prune early.",
             st, ["8-directional moves", "Don't reuse a cell in one word", "Dedupe found words"],
             "Moves include diagonals, a cell can't be reused in one word, and the same word may be found twice.",
             ["Explain why the trie prunes", "Follow-up: remove found words from the trie"],
             "Explain the pruning. Removing found words from the trie speeds things up further.",
             ["We build a trie with words at terminal nodes. DFS from every cell follows the trie child for the cell's letter, records any word, marks the cell, recurses in eight directions, then unmarks it."])

def LargestIsland():
    m = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]
    st = [S("Worked example", [T(m)], "0 = land, 1 = water: flip one 1 to maximise the island", "Here zeros are land and ones are water. We may flip one water cell to land; what's the largest island?"),
          S("Worked example", [T([["A", 1, 1], ["A", "A", 1], [1, 1, "B"]], hl={(0, 0): "acc", (1, 0): "acc", (1, 1): "acc", (2, 2): "warn"})], "Label islands: A = 3, B = 1", "First label each island and record its size: A has three cells, B has one."),
          S("Worked example", [T(m, hl={(1, 2): "ok", (1, 1): "acc", (2, 2): "warn"}), TX(["flip (1,2): touches A (3) + B (1) → 1 + 3 + 1 = 5"], h=0.4)], "Flip (1,2): 1 + A + B = 5", "Now for each water cell, add one plus the sizes of the distinct islands next to it. Flipping row one, column two joins A and B: five.")]
    return E(["Flip each water cell and recount → O((w·h)²)", "Label islands once, then check each water cell's distinct neighbours → O(w·h)", "Use a set so an island isn't counted twice"],
             "Flipping each water cell and flood-filling again is quadratic in the grid size. Label islands once with their sizes, then each water cell just sums its distinct neighbouring islands.",
             st, ["Count each neighbouring island once (set of IDs)", "No water → whole grid", "No land → 1"],
             "Use a set of island IDs so an island touching a cell from two sides isn't counted twice. If there's no water, the answer is the whole grid.",
             ["Same as LeetCode Making a Large Island"],
             "This is making a large island.",
             ["We label each land component with an ID from two upward and record its size. Then for each water cell we collect distinct neighbouring IDs, sum one plus their sizes, and keep the best."])

def ContinuousMedian():
    import heapq
    lo = []; hi = []; st = []
    for x in [5, 10, 100, 200, 6, 13, 14]:
        if not lo or x < -lo[0]: heapq.heappush(lo, -x)
        else: heapq.heappush(hi, x)
        if len(lo) > len(hi) + 1: heapq.heappush(hi, -heapq.heappop(lo))
        elif len(hi) > len(lo) + 1: heapq.heappush(lo, -heapq.heappop(hi))
        med = (-lo[0] + hi[0]) / 2 if len(lo) == len(hi) else (-lo[0] if len(lo) > len(hi) else hi[0])
        st.append(S("Worked example", [A(sorted(-v for v in lo), label="lower half (max-heap)"), A(sorted(hi) or ["∅"], label="upper half (min-heap)"), TX([f"insert {x} → median {med:g}"])], f"Insert {x}: median {med:g}", f"Insert {x} into the {'lower' if -x in lo or x in [-v for v in lo] else 'upper'} half and rebalance so the sizes differ by at most one. The median is {med:g}."))
    return E(["Keep a sorted list, insert in place → O(n) per insert", "Two heaps (max-heap low, min-heap high) → O(log n) insert, O(1) median", "Balance sizes within 1"],
             "Inserting into a sorted list is linear each time. Two heaps, a max-heap for the lower half and a min-heap for the upper, give log n inserts and constant-time median.",
             pick(st, 6), ["Rebalance after every insert", "Even count → average", "Use double division"],
             "Rebalance after every insert, and average the two tops when the sizes are equal.",
             ["Follow-up: sliding-window median"],
             "A follow-up is the sliding-window median, which needs deletions.",
             ["Insert adds to the lower heap if empty or smaller than its top, otherwise upper. Then we move one element if sizes differ by two, and compute the median from the tops."])

def LaptopRentals():
    import heapq
    t = sorted([[0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]]); ends = []; st = []
    for s, e in t:
        reuse = ends and ends[0] <= s
        if reuse: heapq.heappop(ends)
        heapq.heappush(ends, e)
        st.append(S("Worked example", [A([f"{a}–{b}" for a, b in t], hl={t.index([s, e]): "cur"}, idx=False), A(sorted(ends), label="laptop free times (min-heap)"), TX([("reuse a laptop" if reuse else "need a new laptop") + f" → {len(ends)} laptops"])], f"[{s}, {e}]: " + ("reuse" if reuse else "new laptop"), f"Interval {s} to {e}: " + ("the earliest laptop is free by then, so reuse it." if reuse else "no laptop is free yet, so we need another.") + f" That's {len(ends)} in use."))
    return E(["Check overlaps for every pair → O(n²)", "Sort by start + min-heap of end times → O(n log n)", "Or sweep sorted starts/ends"],
             "Counting overlaps pairwise is quadratic. Sorting by start and keeping a min-heap of end times reuses the laptop that frees up earliest, in n log n.",
             pick(st, 6), ["End == start can reuse", "Sort by start time", "Empty → 0"],
             "A laptop returned at time t can be reused for a rental starting at t.",
             ["Same as Meeting Rooms II"],
             "This is meeting rooms two.",
             ["We sort by start, and for each interval pop the heap if its earliest end is at most the start, then push the end. The heap size is the answer."])

def SortKSortedArray():
    import heapq
    a, k = [3, 2, 1, 5, 4, 7, 6, 5], 3; pq = []; out = []; st = []
    for i, x in enumerate(a):
        heapq.heappush(pq, x)
        if len(pq) > k: out.append(heapq.heappop(pq))
        st.append(S("Worked example", [A(a, hl={i: "cur"}), A(sorted(pq), label=f"heap (size ≤ {k + 1})"), A(out or ["∅"], label="sorted output")], f"Add {x}" + (f", pop {out[-1]}" if len(pq) == k and i >= k else ""), f"Push {x}. " + (f"The heap has more than {k}, so pop the smallest, {out[-1]}, which must be in its final place." if i >= k else "The heap isn't full yet.")))
    while pq: out.append(heapq.heappop(pq))
    st.append(S("Worked example", [A(out, hl={i: "ok" for i in range(len(out))})], "Drain the heap → sorted", "Drain the rest of the heap. The array is sorted."))
    return E(["Full sort → O(n log n)", "Insertion sort → O(n·k)", "Min-heap of size k + 1 → O(n log k)"],
             "A full sort ignores the structure. Since each element is at most k away from its spot, the smallest of the next k plus one elements is always next, so a heap of size k plus one gives n log k.",
             pick(st, 6), ["k = 0 → already sorted", "k ≥ n", "Write back in place"],
             "With k zero it's already sorted.",
             ["Explain why the min of k+1 is safe"],
             "Explain why the minimum of the window is safe to place.",
             ["We push each element, and once the heap exceeds k, poll into the next write slot. Then drain the heap."])

def FindLoop():
    v = list(range(10)); cyc = 4; nxt = lambda i: i + 1 if i < 9 else cyc; s, f = nxt(0), nxt(nxt(0)); st = [S("Worked example", [LL(v, cycle_to=cyc, ptr={"slow": s, "fast": f})], "Loop back to node 4; slow 1 step, fast 2", "The tail points back to node four. Slow moves one step, fast two.")]
    while s != f:
        s, f = nxt(s), nxt(nxt(f))
    st.append(S("Worked example", [LL(v, cycle_to=cyc, ptr={"slow": s, "fast": f}, hl={s: "cur"})], f"They meet at {s}", f"They meet inside the loop, at node {s}."))
    s = 0; k = 0
    while s != f: s, f = nxt(s), nxt(f); k += 1
    st.append(S("Worked example", [LL(v, cycle_to=cyc, ptr={"slow": 0, "fast": st and f}, hl={0: "warn"})], "Reset slow to head; both move 1 step", "Reset slow to the head; now both move one step at a time."))
    st.append(S("Worked example", [LL(v, cycle_to=cyc, ptr={"both": s}, hl={s: "ok"})], f"Meet again at {s}: loop start", f"After {k} steps they meet at node {s}, the start of the loop. The distance from head to loop start equals the distance from the meeting point to loop start."))
    return E(["Hash set of visited nodes → O(n) space", "Floyd's tortoise and hare → O(1) space", "Second phase finds the loop start"],
             "Storing visited nodes finds the loop start but uses memory. Floyd's algorithm uses two speeds to meet inside the loop, then a reset finds the start with constant space.",
             st, ["Input always has a loop here", "Start both at head.next/next.next correctly", "Compare nodes, not values"],
             "Initialise the pointers carefully and compare nodes by identity.",
             ["Prove the reset trick (distance argument)"],
             "Be ready to prove why the reset works.",
             ["Slow and fast start one and two steps in and move until equal. Then slow restarts at the head and both move one step until they meet at the loop start."])

def MergeLinkedLists():
    a, b = [2, 6, 7, 8], [1, 3, 4, 5, 9, 10]; i = j = 0; out = []; st = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: out.append(a[i]); i += 1; src = "first"
        else: out.append(b[j]); j += 1; src = "second"
        if len(out) in (1, 2, 4, 6, 8): st.append(S("Worked example", [LL(a, ptr={"p": i} if i < len(a) else None, label="list 1"), LL(b, ptr={"q": j} if j < len(b) else None, label="list 2"), LL(out, label="merged")], f"Take {out[-1]} from the {src} list", f"Compare the heads; the smaller, {out[-1]}, comes from the {src} list."))
    out += a[i:] + b[j:]
    st.append(S("Worked example", [LL(out, hl={k: "ok" for k in range(len(out))}, label="merged")], "Attach the remainder", "When one list runs out, attach the rest of the other in one step."))
    return E(["Copy into an array, sort, rebuild → O((n+m) log)", "Iterative merge with a dummy head → O(n+m), O(1)", "Recursive merge → O(n+m) stack"],
             "Copying everything and sorting ignores that both lists are sorted. A merge with a dummy head relinks nodes in linear time and constant space.",
             st, ["Empty list", "Use ≤ for stability", "Attach the leftover directly"],
             "Handle empty inputs, and attach the leftover in one assignment.",
             ["Follow-up: merge k lists (heap)"],
             "Merging k lists uses a heap.",
             ["With a dummy tail we repeatedly link the smaller head and advance. Then we attach whichever list remains and return dummy's next."])

def ReverseLinkedList():
    v = [0, 1, 2, 3, 4, 5]; st = []
    for k in range(0, len(v) + 1, 2):
        rev = v[:k][::-1]; rest = v[k:]
        st.append(S("Worked example", [LL(rev or ["∅"], label="reversed (prev)"), LL(rest or ["∅"], label="remaining (head)")], f"After {k} steps", f"After reversing {k} nodes, prev heads {rev[0] if rev else 'nothing'} and the remaining list starts at {rest[0] if rest else 'null'}."))
    return E(["Copy into array, rebuild → O(n) space", "Recursive → O(n) stack", "Iterative three pointers → O(1)"],
             "Rebuilding from an array uses extra memory. The iterative version flips one pointer at a time with prev, current and next.",
             st, ["Save next before overwriting", "Empty / single node", "Return prev, not head"],
             "Save next before you overwrite the pointer, and return prev at the end.",
             ["Follow-up: reverse in groups of k"],
             "A follow-up reverses in groups of k.",
             ["While head isn't null, save next, point head at prev, move prev to head and head to next. Return prev."])

def ShiftLinkedList():
    v = [0, 1, 2, 3, 4, 5]; k = 2; n = len(v); s = k % n; out = v[n - s:] + v[:n - s]
    st = [S("Worked example", [LL(v, ptr={"tail": n - 1})], f"Length {n}; shift {k} → effective {s}", f"Find the length, {n}, and the tail. Shifting by {k} is the same as {s} modulo the length."),
          S("Worked example", [LL(v, ptr={"new tail": n - s - 1, "new head": n - s}, hl={n - s - 1: "cur", n - s: "ok"})], f"New tail at index {n - s - 1}", f"The new tail is {n - s - 1} steps from the start: node {v[n - s - 1]}. Its next, {v[n - s]}, becomes the new head."),
          S("Worked example", [LL(out, ptr={"head": 0})], "Cut and reconnect", "Cut after the new tail and connect the old tail to the old head.")]
    return E(["Shift one node at a time k times → O(n·k)", "Length + one cut → O(n)", "Negative k: floor mod"],
             "Rotating one step at a time is n times k. Computing the length and cutting once is linear.",
             st, ["k ≥ length → mod", "Negative k shifts backward", "Shift 0 → same list"],
             "Take k mod length, using floor mod so negative k works.",
             ["Same as Rotate List"],
             "This is rotate list.",
             ["We walk to the tail counting length, compute the effective shift, walk to the new tail, cut, link the old tail to the old head, and return the new head."])

def AmbiguousMeasurements():
    cups = [[200, 210], [450, 465], [800, 850]]; low, high = 2100, 2300
    st = [S("Worked example", [T(cups, colh=["min", "max"], rowh=["cup A", "cup B", "cup C"]), TX([f"target range [{low}, {high}]"])], "Can we always land in [2100, 2300]?", "Each cup measures somewhere between its min and max. Can we guarantee a total between twenty-one hundred and twenty-three hundred?"),
          S("Worked example", [TX([f"use C: [{low}, {high}] → [{low - 800}, {high - 850}]", "use C again: → [500, 600]", "use B: → [50, 135] ... then A: covers ✓"], size=18)], "Subtract a cup's range and recurse", "Using a cup shrinks the remaining range by its min and max. Recurse on the remaining range."),
          S("Worked example", [TX(["remaining [low, high] fits a cup: min ≥ low and max ≤ high → done", "memoise (low, high)"])], "Memoise on (low, high)", "We succeed when one cup's range fits inside the remaining range. The same remaining range repeats, so memoise on low and high.")]
    return E(["Try all cup sequences → exponential", "Memoised recursion on (low, high) → O(low · high · cups)", "Clamp at 0"],
             "Trying every sequence of cups is exponential. Memoising on the remaining low and high bounds collapses repeats.",
             st, ["Clamp low at 0", "Both ≤ 0 → fail", "Zero-capacity cups"],
             "Clamp at zero, and skip cups that never make progress, to avoid infinite recursion.",
             ["Explain the state choice"],
             "Explain why low and high fully describe the state.",
             ["Can memoises on low and high. A cup succeeds if its range fits; otherwise we recurse with the range reduced by the cup, clamped at zero."])

def GenerateDivTags():
    out = []
    def g(o, c, s):
        if c == 0: out.append(s); return
        if o: g(o - 1, c, s + "(")
        if c > o: g(o, c - 1, s + ")")
    g(3, 3, "")
    st = [S("Worked example", [TX(["state: opens left, closes left", "add <div> if opens > 0", "add </div> if closes > opens"])], "Two rules keep tags valid", "Track how many opening and closing tags remain. Open if any opens remain; close only if more closes than opens remain."),
          S("Worked example", [TX(["(((  →  ((()  →  ((())  →  ((()))"], size=22)], "Depth-first: open, open, open, close…", "Depth first, we open three times, then close three times: the first answer."),
          S("Worked example", [TX([" ".join(out).replace("(", "<").replace(")", ">")], size=20)], f"n = 3 → {len(out)} combinations", f"Backtracking yields all {len(out)} valid combinations, shown here with angle brackets for div tags.")]
    return E(["Generate all 2^(2n) strings and filter → O(4ⁿ·n)", "Backtracking with counts → O(Catalan(n))", "Output size is the Catalan number"],
             "Generating every string and filtering valid ones is wasteful. Backtracking with remaining counts only builds valid prefixes; the output size is the Catalan number.",
             st, ["Close only when closes > opens", "n = 0 → [\"\"]", "Undo appends"],
             "Only close when more closes than opens remain.",
             ["Mention Catalan numbers"],
             "Mention Catalan numbers.",
             ["Gen records the string when no closes remain. It appends an opening tag if opens remain and recurses, and a closing tag if closes exceed opens, undoing each append."])

def InterweavingStrings():
    a, b, c = "algo", "frog", "fralgogo"; n, m = len(a), len(b); dp = [[False] * (m + 1) for _ in range(n + 1)]; dp[0][0] = True
    for i in range(n + 1):
        for j in range(m + 1):
            if i and a[i - 1] == c[i + j - 1] and dp[i - 1][j]: dp[i][j] = True
            if j and b[j - 1] == c[i + j - 1] and dp[i][j - 1]: dp[i][j] = True
    tf = [["✓" if x else "·" for x in r] for r in dp]
    st = [S("Worked example", [TX([f"one = {a}, two = {b}", f"three = {c}"])], "Is three an interleaving of one and two?", "Can we build fralgogo by interleaving algo and frog, keeping each in order?"),
          S("Worked example", [T(tf, rowh=["", *a], colh=["", "", *b])], "dp[i][j]: first i of one + first j of two make the first i+j of three", "Dp i, j says whether the first i letters of one and j letters of two make the first i plus j letters of three. A cell is reachable from above if one's letter matches, or from the left if two's does."),
          S("Worked example", [T(tf, rowh=["", *a], colh=["", "", *b], hl={(n, m): "ok" if dp[n][m] else "bad"})], f"dp[{n}][{m}] = {dp[n][m]}", f"The bottom-right cell is {'true' if dp[n][m] else 'false'}, so the answer is {'yes' if dp[n][m] else 'no'}.")]
    return E(["Recursion choosing a or b at each step → O(2^(n+m))", "Memoise on (i, j) → O(n·m)", "Bottom-up table"],
             "Recursing on which string supplies the next letter is exponential. The state is just i and j, so memoising makes it n times m.",
             st, ["Lengths must add up", "Both strings may match the same letter", "Empty strings"],
             "If lengths don't add up, return false immediately.",
             ["Mention 1-D DP"],
             "A one-dimensional DP row is enough.",
             ["We check lengths, then recurse on i and j with a memo: if one's letter matches the next of three try advancing i, and if two's matches try advancing j."])

def LowestCommonManager():
    nodes = {"A": ["A", "B", "C"], "B": ["B", "D", "E"], "C": ["C", "F", "G"], "D": ["D", "H", "I"], "E": ["E", None, None], "F": ["F", None, None], "G": ["G", None, None], "H": ["H", None, None], "I": ["I", None, None]}
    st = [S("Worked example", [TR(nodes, "A", hl={"E": "cur", "I": "cur"})], "Reports E and I: who's their lowest common manager?", "Find the lowest manager above both E and I."),
          S("Worked example", [TR(nodes, "A", hl={"D": "warn", "E": "warn"}, notes={"D": "1 found", "E": "1 found", "H": "0", "I": "1"})], "Post-order: each manager returns how many reports it covers", "Recursively, each manager returns how many of the two reports are in its subtree. D covers I, so one; E is itself one."),
          S("Worked example", [TR(nodes, "A", hl={"B": "ok"}, notes={"B": "2 → answer"})], "First manager with count 2 → B", "B's subtree covers both, so B is the first manager to reach two. It's the answer, and we pass it upward unchanged.")]
    return E(["Find each report's path from top, compare → O(n) + paths", "Single post-order counting reports → O(n)", "Return the first node reaching count 2"],
             "Building both paths from the top and comparing works. A single post-order pass that counts how many target reports each subtree contains finds the lowest common manager directly.",
             st, ["A report may be the manager of the other", "Org charts are n-ary", "Stop after found"],
             "A report can itself be the manager of the other; the count still works.",
             ["Relate to LCA in binary trees"],
             "This is lowest common ancestor generalised to n-ary trees.",
             ["The helper visits each direct report, summing counts and returning early if a child already found the answer. It adds one if the current node is a target, and if the count hits two, records itself."])

def SolveSudoku():
    st = [S("Worked example", [TX(["rows[r], cols[c], boxes[b] as bitmasks of used digits", "box = r/3·3 + c/3"])], "Track used digits per row, column, box", "Keep a bitmask of used digits for every row, column and three-by-three box, so checking a digit is constant time."),
          S("Worked example", [TX(["cell (0,2): row uses {5,3,7}, col {8}, box {5,3,6,9,8}", "candidates: 1, 2, 4"])], "Try candidates in an empty cell", "At the first empty cell, the digits not used in its row, column or box are one, two and four. Try them in order."),
          S("Worked example", [TX(["place 1 → recurse → dead end later", "undo 1, try 2 …"])], "Backtrack on dead ends", "Place a digit and recurse to the next cell. If we hit a cell with no candidates, undo and try the next digit.")]
    return E(["Try all fillings → 9^(empty cells)", "Backtracking with constraint checks → prunes heavily", "Bitmasks make checks O(1)"],
             "Trying every filling is astronomically large. Backtracking with row, column and box checks prunes almost everything. Bitmasks make each check constant time.",
             st, ["Undo bits when backtracking", "Box index formula", "Given board is valid"],
             "Always clear the bits when you backtrack.",
             ["Mention most-constrained-cell heuristic"],
             "Choosing the cell with the fewest candidates first speeds it up a lot.",
             ["We initialise the masks from the given digits, then solve recursively over positions zero to eighty: skip filled cells, try each digit whose bit is free in row, column and box, set the bits, recurse, and clear on failure."])

def IndexEqualsValue():
    a = [-5, -3, 0, 3, 4, 5, 9]; lo, hi, ans = 0, len(a) - 1, -1; st = []
    while lo <= hi:
        m = (lo + hi) // 2; v = a[m]
        if v < m: msg = f"a[{m}] = {v} < {m} → go right"; lo = m + 1
        else:
            if v == m: ans = m
            msg = f"a[{m}] = {v} {'=' if v == m else '>'} {m} → " + ("record, look left" if v == m else "go left"); hi = m - 1
        st.append(S("Worked example", [A(a, ptr={"mid": m}, window=(lo, hi) if lo <= hi else None, hl={ans: "ok"} if ans >= 0 else {}), TX([msg])], msg, msg.replace("→", ", so").replace("a[", "a at ").replace("]", "") + "."))
    return E(["Linear scan → O(n)", "Binary search on a[i] − i (non-decreasing) → O(log n)", "Keep searching left for the first"],
             "A linear scan works. Because values are distinct sorted integers, a i minus i never decreases, so binary search finds the first index where they match.",
             st, ["Return the first such index", "None → −1", "Distinct integers required"],
             "Keep searching left after a match to get the first one.",
             ["Explain why a[i] − i is monotone"],
             "Explain why a i minus i is non-decreasing.",
             ["Binary search: if a mid is less than mid, go right; otherwise record a match and go left."])

def Quickselect():
    a = [8, 5, 2, 9, 7, 6, 3]; k = 3; tgt = k - 1; lo, hi = 0, len(a) - 1; st = []
    while True:
        p, l, r = lo, lo + 1, hi
        while l <= r:
            if a[l] > a[p] and a[r] < a[p]: a[l], a[r] = a[r], a[l]
            if a[l] <= a[p]: l += 1
            if a[r] >= a[p]: r -= 1
        a[p], a[r] = a[r], a[p]
        st.append(S("Worked example", [A(a, hl={r: "ok", **{i: "done" for i in range(lo, hi + 1) if i != r}}, ptr={"pivot": r}), TX([f"pivot {a[r]} lands at index {r}; target index {tgt}"])], f"Pivot {a[r]} → index {r}", f"Partition around {a[r]}: it lands at index {r}. " + ("That's the target!" if r == tgt else f"The target is {'right' if r < tgt else 'left'} of it, so we only recurse there.")))
        if r == tgt: break
        if r < tgt: lo = r + 1
        else: hi = r - 1
    return E(["Sort → O(n log n)", "Heap of size k → O(n log k)", "Quickselect → O(n) average"],
             "Sorting finds the k-th smallest in n log n. A heap of size k is n log k. Quickselect partitions and recurses into one side only, linear on average.",
             st, ["Worst case O(n²) — randomise the pivot", "k is 1-indexed", "Duplicates"],
             "Worst case is quadratic; randomise the pivot. Remember k is one-indexed.",
             ["Mention median-of-medians O(n) worst case"],
             "Median of medians guarantees linear worst case.",
             ["We partition with the first element as pivot, swapping out-of-place pairs, place the pivot at r, and narrow lo or hi toward the target."])

def SearchForRange():
    a = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]; t = 45
    def bound(x):
        lo, hi = 0, len(a)
        while lo < hi:
            m = (lo + hi) // 2
            if a[m] < x: lo = m + 1
            else: hi = m
        return lo
    l, r = bound(t), bound(t + 1) - 1
    st = [S("Worked example", [A(a, ptr={"lower": l}, hl={l: "ok"}), TX([f"first index with a[i] ≥ {t} → {l}"])], f"Lower bound of {t}: {l}", f"Binary search for the first index whose value is at least {t}: index {l}."),
          S("Worked example", [A(a, ptr={"lower": l, "upper−1": r}, hl={r: "ok"}), TX([f"first index with a[i] ≥ {t + 1} → {r + 1}, minus 1 = {r}"])], f"Upper end: {r}", f"Search again for {t + 1}: index {r + 1}. One before it, {r}, is the last {t}."),
          S("Worked example", [A(a, window=(l, r)), TX([f"answer [{l}, {r}]"])], f"Answer: [{l}, {r}]", f"So {t} occupies indices {l} to {r}.")]
    return E(["Linear scan → O(n)", "Binary search then expand → O(n) worst", "Two lower-bound searches → O(log n)"],
             "Scanning, or finding one match and expanding, can be linear with many duplicates. Two lower-bound searches give both ends in log n.",
             st, ["Target absent → [−1, −1]", "Half-open bounds", "Overflow-safe mid"],
             "Check the target actually exists at the lower bound.",
             ["Mention lower/upper bound terminology"],
             "Use the lower-bound and upper-bound vocabulary.",
             ["Bound returns the first index whose value is at least t. The range is bound of t through bound of t plus one minus one, if the value at the lower bound equals t."])

def ShiftedBinarySearch():
    a = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]; t = 33; lo, hi = 0, len(a) - 1; st = []
    while lo <= hi:
        m = (lo + hi) // 2
        if a[m] == t: st.append(S("Worked example", [A(a, ptr={"mid": m}, hl={m: "ok"})], f"Found at {m}", f"Mid is {a[m]}: found it at index {m}.")); break
        left_sorted = a[lo] <= a[m]
        if left_sorted: go = "left" if a[lo] <= t < a[m] else "right"
        else: go = "right" if a[m] < t <= a[hi] else "left"
        st.append(S("Worked example", [A(a, window=(lo, hi), ptr={"mid": m}), TX([f"{'left' if left_sorted else 'right'} half sorted; {t} {'in' if (go == 'left') == left_sorted else 'not in'} it → go {go}"])], f"mid {a[m]}: go {go}", f"Mid is {a[m]}. The {'left' if left_sorted else 'right'} half is sorted, and {t} {'is' if (go == 'left') == left_sorted else 'is not'} within it, so go {go}."))
        if go == "left": hi = m - 1
        else: lo = m + 1
    return E(["Linear scan → O(n)", "Find the pivot, then binary search → O(log n)", "One-pass: identify the sorted half → O(log n)"],
             "A linear scan ignores sorting. At every mid, one half is sorted; check if the target lies within that half and discard the other, log n.",
             st, ["Use ≤ when comparing a[lo] and a[mid]", "Duplicates break the guarantee", "Not found → −1"],
             "Use less-or-equal when deciding which half is sorted. Duplicates can force linear time.",
             ["Follow-up: with duplicates"],
             "With duplicates, worst case degrades to linear.",
             ["While lo is at most hi: return on a match; if the left half is sorted, go left when the target is in its range, else right; otherwise mirror for the right half."])

def HeapSort():
    a = [8, 5, 2, 9, 5, 6, 3]; n = len(a); st = []
    def sift(i, m):
        while 2 * i + 1 < m:
            c = 2 * i + 1
            if c + 1 < m and a[c + 1] > a[c]: c += 1
            if a[i] >= a[c]: return
            a[i], a[c] = a[c], a[i]; i = c
    for i in range(n // 2 - 1, -1, -1): sift(i, n)
    st.append(S("Worked example", [TR(*heap_tree(a)), A(a)], "Build a max-heap", "First build a max-heap bottom-up. The largest, nine, is at the root."))
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]; sift(0, end)
        if end in (6, 5, 4, 2, 1): st.append(S("Worked example", [A(a, hl={k: "ok" for k in range(end, n)}, window=(0, end - 1))], f"Swap max to index {end}, sift down", f"Swap the root into position {end}; that part is sorted. Sift the new root down to restore the heap."))
    return E(["Selection sort → O(n²)", "Heap sort → O(n log n), in place", "Not stable"],
             "Selection sort finds the max by scanning each time. A heap finds it in log n, giving n log n in place.",
             st, ["Build bottom-up in O(n)", "Shrink the heap each step", "Not stable"],
             "Build bottom-up, and shrink the heap boundary each step.",
             ["Compare with quick/merge sort"],
             "Heap sort guarantees n log n with constant memory, but is cache-unfriendly and unstable.",
             ["We sift down from the last parent to build the heap, then repeatedly swap the root with end and sift the root down within end."])

def QuickSort():
    a = [8, 5, 2, 9, 5, 6, 3]; st = []
    def srt(lo, hi):
        if lo >= hi: return
        p, l, r = lo, lo + 1, hi
        while l <= r:
            if a[l] > a[p] and a[r] < a[p]: a[l], a[r] = a[r], a[l]
            if a[l] <= a[p]: l += 1
            if a[r] >= a[p]: r -= 1
        a[p], a[r] = a[r], a[p]
        st.append(S("Worked example", [A(a, window=(lo, hi), hl={r: "ok"})], f"Pivot {a[r]} placed at {r}", f"Partition indices {lo} to {hi} around {a[r]}: smaller to the left, larger to the right. It's now in its final spot, index {r}."))
        srt(lo, r - 1); srt(r + 1, hi)
    srt(0, len(a) - 1)
    return E(["Bubble/insertion → O(n²)", "Quick sort → O(n log n) average, O(log n) stack", "Recurse on smaller side first"],
             "Quadratic sorts compare everything. Quick sort partitions around a pivot and recurses, n log n on average.",
             pick(st, 6), ["Worst case O(n²) on sorted input → random pivot", "Recurse smaller side to bound stack", "Duplicates"],
             "Sorted input with a first-element pivot is quadratic; randomise. Recurse into the smaller side first to keep the stack logarithmic.",
             ["Mention 3-way partition for duplicates"],
             "Three-way partitioning handles many duplicates well.",
             ["Sort loops while lo is below hi: partition, place the pivot at r, recurse on the smaller side and loop on the larger."])

def RadixSort():
    a = [8762, 654, 3008, 345, 87, 65, 234, 12, 2]; st = []; exp = 1
    while max(a) // exp:
        a = sorted(a, key=lambda x: x // exp % 10)
        st.append(S("Worked example", [A(a), TX([f"stable counting sort by digit {len(str(exp)) - 1} (×{exp})"])], f"Sort by the {['ones', 'tens', 'hundreds', 'thousands'][len(str(exp)) - 1]} digit", f"Stable counting sort on the {['ones', 'tens', 'hundreds', 'thousands'][len(str(exp)) - 1]} digit. Earlier digit orderings are preserved within ties."))
        exp *= 10
    return E(["Comparison sorts → Ω(n log n)", "Radix sort with counting sort per digit → O(d · (n + 10))", "Requires stable per-digit sort"],
             "Comparison sorts can't beat n log n. Radix sort processes one digit at a time with a stable counting sort, d times n plus ten.",
             st, ["Stability is essential", "Iterate counts from the end", "Negative numbers need special handling"],
             "Each pass must be stable, which is why we fill from the end.",
             ["When radix beats comparison sorts"],
             "Radix wins when keys are short relative to log n.",
             ["For each digit place up to the max, we count digits, prefix-sum the counts, place elements from the end into out, and copy back."])

def LargestRectangleUnderSkyline():
    h = [1, 3, 3, 2, 4, 1, 5, 3, 2]; stk = []; best = 0; st = []
    for i in range(len(h) + 1):
        cur = 0 if i == len(h) else h[i]
        while stk and h[stk[-1]] >= cur:
            ht = h[stk.pop()]; left = stk[-1] if stk else -1; area = ht * (i - left - 1)
            if area > best: best = area; st.append(S("Worked example", [A(h, window=(left + 1, i - 1), ptr={"i": min(i, len(h) - 1)}), TX([f"height {ht} × width {i - left - 1} = {area}", f"best = {best}"])], f"Pop {ht}: area {area}", f"A lower bar arrives, so pop height {ht}. It extends from index {left + 1} to {i - 1}, width {i - left - 1}, area {area}, the best so far."))
        stk.append(i)
    return E(["Every pair of bars → O(n²)", "For each bar expand left/right → O(n²)", "Monotonic stack → O(n)"],
             "Checking every range is quadratic. A monotonic increasing stack finds, for each bar, how far it can extend in both directions, and each bar is pushed and popped once.",
             st, ["Sentinel 0 at the end flushes the stack", "Width uses the new top as left boundary", "Equal heights"],
             "A zero sentinel at the end flushes remaining bars.",
             ["Follow-up: maximal rectangle in a binary matrix"],
             "Apply it row by row for the maximal rectangle in a binary matrix.",
             ["For i up to n, with height zero at the end, pop while the top is at least the current height, computing height times i minus new top minus one. Push i."])

def ShortenPath():
    p = "/foo/../test/../test/../foo//bar/./baz"; stk = []; st = []
    for t in p.split("/"):
        if t in ("", "."): continue
        if t == "..": stk.pop() if stk else None; act = "pop"
        else: stk.append(t); act = "push"
        st.append(S("Worked example", [ST(stk[::-1] or ["(empty)"], w=0.4), TX([f"token '{t}': {act}"], w=0.6, h=1)], f"'{t}': {act}", f"Token {t}: " + ("go up a directory, pop." if act == "pop" else "a directory name, push."), layout="cols"))
    st.append(S("Worked example", [TX(["/" + "/".join(stk)])], "Join the stack", "Join the stack with slashes: slash foo, bar, baz."))
    return E(["String replacement loops → fragile, O(n²)", "Stack of path tokens → O(n)", "Handle absolute vs relative paths"],
             "Repeated string replacement is fragile. Splitting on slashes and using a stack handles dots and double dots cleanly in linear time.",
             pick(st, 6), ["'..' at root of absolute path → ignore", "Relative paths keep leading '..'", "Empty tokens from '//'"],
             "At the root of an absolute path, dot-dot does nothing; in relative paths, leading dot-dots are kept.",
             ["Same as Simplify Path"],
             "This is simplify path.",
             ["We split on slash, skip empty and dot tokens, pop on dot-dot unless the stack is empty or ends in dot-dot (then push it for relative paths), and push names. Join and prefix a slash if absolute."])

def LongestSubstringWithoutDuplication():
    s = "clementisacap"; last = {}; start = 0; bs = be = 0; st = []
    for i, ch in enumerate(s):
        jump = ch in last and last[ch] >= start
        if jump: start = last[ch] + 1
        last[ch] = i
        if i + 1 - start > be - bs: bs, be = start, i + 1
        if jump or i in (0, 6, 12): st.append(S("Worked example", [A(list(s), window=(start, i), hl={k: "ok" for k in range(bs, be)}, idx=False), TX([f"window '{s[start:i + 1]}'", f"best '{s[bs:be]}'"])], f"'{ch}' at {i}" + (" repeats → move start" if jump else ""), f"At {ch}, " + (f"it already appeared in the window, so the start jumps past it to index {start}." if jump else "no repeat.") + f" The best is {s[bs:be]}."))
    return E(["Check every substring → O(n³)", "Sliding window with a set → O(n)", "Last-seen map lets start jump directly"],
             "Checking every substring for duplicates is cubic. A sliding window with a last-seen map lets the start jump past a repeat directly, linear time.",
             pick(st, 6), ["Only jump if last ≥ start", "Empty string", "Return the substring, not length"],
             "Only move the start if the previous occurrence is inside the window.",
             ["Mention the array[128] map"],
             "A fixed-size array works as the map for ASCII.",
             ["For each index, if the character's last position is within the window, move start past it. Update last and the best."])

def PatternMatcher():
    pat, s = "xxyxxy", "gogopowerrangergogopowerranger"
    st = [S("Worked example", [TX([f"pattern {pat}: 4 × x, 2 × y", f"string length {len(s)}"])], "Count x and y", "The pattern has four x's and two y's. The string is thirty characters."),
          S("Worked example", [TX(["try len(x)=1: y = (30 − 4)/2 = 13 → x='g' … ✗", "try len(x)=2: y = 11 → x='go', y='powerranger' ✓"], size=18)], "Try each length of x", "For each length of x, the length of y follows. Take x from the start and y from its first position, then rebuild and compare."),
          S("Worked example", [TX(["go go powerranger go go powerranger ✓", "→ ['go', 'powerranger']"], size=20)], "Match: x = go, y = powerranger", "With x equal to go and y equal to powerranger, the rebuilt string matches.")]
    return E(["Try all (len x, len y) pairs → O(n² · m)", "Fix len(x); len(y) is determined → O(n · m)", "Swap x/y if pattern starts with y"],
             "Trying every pair of lengths is wasteful, since once x's length is fixed, y's length is determined. That's n times m.",
             st, ["Pattern starting with y: swap and swap back", "Pattern with only x", "Return in [x, y] order"],
             "If the pattern starts with y, swap the letters, then swap the answer back.",
             ["Explain why len(y) is determined"],
             "Explain why y's length is forced.",
             ["We normalise so the pattern starts with x, count x's and y's, then for each x length compute y's length, extract both, rebuild, and compare."])

def UnderscorifySubstring():
    s, sub = "testthis is a testtest to see if testestest it works", "test"; mark = [False] * len(s); i = s.find(sub)
    while i != -1:
        for j in range(i, i + len(sub)): mark[j] = True
        i = s.find(sub, i + 1)
    out = ""
    for k, ch in enumerate(s):
        if mark[k] and (k == 0 or not mark[k - 1]): out += "_"
        out += ch
        if mark[k] and (k == len(s) - 1 or not mark[k + 1]): out += "_"
    st = [S("Worked example", [TX([s], size=18)], "Find every occurrence of 'test'", "Find every occurrence of test, including overlapping ones like in testestest."),
          S("Worked example", [TX(["".join("^" if m else " " for m in mark)], size=18), TX([s], size=18)], "Mark covered characters", "Mark every covered character. Overlapping and adjacent occurrences merge automatically."),
          S("Worked example", [TX([out], size=18)], "Underscore each marked run", "Put an underscore before and after each marked run.")]
    return E(["Insert underscores per occurrence then merge → messy", "Mark covered chars, then emit runs → O(n · m)", "Or merge intervals"],
             "Inserting underscores per occurrence and fixing overlaps is messy. Marking covered characters and wrapping each run is clean.",
             st, ["Overlapping occurrences", "Adjacent occurrences merge", "No occurrences → unchanged"],
             "Search from i plus one to catch overlaps, and adjacent occurrences merge.",
             ["Mention the interval-merge approach"],
             "Mention collecting intervals and merging them.",
             ["We mark characters covered by each occurrence, then emit underscores at the start and end of each marked run."])

def LongestMostFrequentPrefix():
    w = ["algoexpert", "algorithm", "frontendexpert", "mlexpert"]
    from collections import Counter
    c = Counter(x[:i] for x in w for i in range(1, len(x) + 1)); bc = max(c.values()); best = max((p for p in c if c[p] == bc), key=len)
    st = [S("Worked example", [TX(w)], "Insert words into a trie with prefix counts", "Insert every word into a trie, incrementing a count on each node passed."),
          S("Worked example", [T([[p, c[p]] for p in ["a", "al", "alg", "algo", "algoe", "f", "m"]], colh=["prefix", "count"])], "Counts per prefix", "Prefixes a through algo each appear twice; others once."),
          S("Worked example", [TX([f"max count {bc}; longest such prefix: '{best}'"])], f"Answer: {best}", f"The highest count is {bc}, and the longest prefix with that count is {best}.")]
    return E(["Count all prefixes in a hash map → O(total chars²) strings", "Trie with counts → O(total chars)", "Track best by (count, length)"],
             "Counting every prefix as a separate string costs quadratic memory. A trie with counts does it in total characters.",
             st, ["Tie → longest prefix", "Empty input → ''"],
             "On ties in count, prefer the longer prefix.",
             ["Explain trie node counts"],
             "Explain that node counts are prefix frequencies.",
             ["We insert each string, incrementing counts. Then we walk each string again, updating the best when a node's count is higher, or equal with a longer prefix."])

def MultiStringSearch():
    big = "this is a big string"; smalls = ["this", "yo", "is", "a", "bigger", "string", "kappa"]; res = [x in big for x in smalls]
    st = [S("Worked example", [TX(smalls, size=18)], "Build a trie of the small strings", "Put all the small strings in a trie."),
          S("Worked example", [TX([big, "start at each index, walk the trie"])], "Walk the trie from each start index", "From each index of the big string, walk the trie as far as letters match, recording any word endings."),
          S("Worked example", [T([[x, "✓" if r else "✗"] for x, r in zip(smalls, res)], colh=["small", "found"])], "Results", "This, is, a and string are found; yo, bigger and kappa aren't.")]
    return E(["indexOf per small string → O(b · Σs)", "Trie of smalls, walk from each index of big → O(b · maxS + Σs)", "Aho–Corasick → linear"],
             "Searching for each small string separately repeats scans. A trie of the small strings lets each start index check all of them at once. Aho-Corasick makes it linear.",
             st, ["Overlapping matches", "Duplicate small strings", "Small longer than big"],
             "Duplicates and overlaps are handled naturally by the set of found words.",
             ["Mention Aho–Corasick"],
             "Mention Aho-Corasick for true linear time.",
             ["We build a trie with words at terminal nodes. For each start index, follow children while they exist, adding words. Then map each small to whether it was found."])

def ShortestUniquePrefixes():
    w = ["foo", "bar", "cat", "cape", "foam"]; from collections import Counter; c = Counter(x[:i] for x in w for i in range(1, len(x) + 1))
    out = [next((x[:i] for i in range(1, len(x) + 1) if c[x[:i]] == 1), x) for x in w]
    st = [S("Worked example", [T([[p, c[p]] for p in ["f", "fo", "foo", "foa", "c", "ca", "cat", "cap", "b"]], colh=["prefix", "count"])], "Trie with prefix counts", "Insert each word, counting how many words pass through each node."),
          S("Worked example", [T([[x, o] for x, o in zip(w, out)], colh=["word", "shortest unique prefix"])], "First node with count 1", "For each word, the shortest unique prefix ends at the first node with count one.")]
    return E(["Compare each word with all others → O(n² · L)", "Trie with counts → O(total chars)"],
             "Comparing every pair of words is quadratic. A trie with counts finds each word's first unique node in its own length.",
             st, ["A word that's a prefix of another → whole word", "Duplicates"],
             "If a word is a prefix of another, the answer is the whole word.",
             ["Explain the count invariant"],
             "Explain that the count is how many words share the prefix.",
             ["We insert all words with counts, then for each word walk until a node's count is one, returning the prefix up to there or the whole word."])
