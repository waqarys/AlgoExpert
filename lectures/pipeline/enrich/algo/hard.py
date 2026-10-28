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
