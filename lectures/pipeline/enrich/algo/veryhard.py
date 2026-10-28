from enrich.kit import *

def _e(brute, bn, st, pits, pn, tips, tn, code): return E(brute, bn, st, pits, pn, tips, tn, [code])

def ApartmentHunting():
    blocks = [{"gym": 0, "school": 1, "store": 0}, {"gym": 1, "school": 0, "store": 0}, {"gym": 1, "school": 1, "store": 0}, {"gym": 0, "school": 1, "store": 0}, {"gym": 0, "school": 1, "store": 1}]; reqs = ["gym", "school", "store"]; n = 5; rows = []; worst = [0] * n
    for r in reqs:
        d = [min(abs(i - j) for j in range(n) if blocks[j][r]) for i in range(n)]; rows.append(d); worst = [max(a, b) for a, b in zip(worst, d)]
    b = worst.index(min(worst))
    st = [S("Worked example", [T([[r] + rows[k] for k, r in enumerate(reqs)], colh=["req", *range(n)])], "Distance to nearest requirement, per block", "For each requirement, two sweeps, left to right and right to left, give every block's distance to the nearest one."),
          S("Worked example", [T([[r] + rows[k] for k, r in enumerate(reqs)] + [["worst"] + worst], colh=["req", *range(n)], hl={(3, b + 1): "ok"})], f"Worst-case per block; minimum at block {b}", f"Each block's score is its farthest requirement. The minimum, {worst[b]}, is at block {b}.")]
    return _e(["For each block, scan all blocks for each req → O(b² · r)", "Two sweeps per requirement → O(b · r)"], "Scanning outward from every block is quadratic. Two linear sweeps per requirement give nearest distances, so the whole thing is blocks times requirements.",
              st, ["Requirement missing everywhere", "Ties → any index", "Use large sentinels"], "Use large sentinel distances before the first occurrence.", ["Explain min of max"], "Frame it as minimising the maximum distance.",
              "For each requirement, the forward sweep tracks the last block with it and the backward sweep the next one; each block keeps the min, and worst keeps the max across requirements. Return the index of the smallest worst.")

def CalendarMatching():
    st = [S("Worked example", [TX(["cal1: 9:00–10:30, 12:00–13:00, 16:00–18:00 (bounds 9–20)", "cal2: 10:00–11:30, 12:30–14:30, 14:30–15:00, 16:00–17:00 (bounds 10–18:30)"], size=16)], "Two calendars with daily bounds", "Each person has meetings and daily bounds. Treat time outside the bounds as busy."),
          S("Worked example", [TX(["sort all busy intervals by start", "merge overlaps: 0:00–11:30, 12:00–15:00, 16:00–18:00, 18:30–24:00"], size=16)], "Merge all busy intervals", "Convert to minutes, add the out-of-bounds time as busy, sort, and merge overlapping intervals."),
          S("Worked example", [TX(["gaps ≥ 30 min: 11:30–12:00, 15:00–16:00, 18:00–18:30"], size=18)], "Free gaps long enough", "The gaps between merged busy blocks that are at least the meeting length are the answer.")]
    return _e(["Check each minute of the day → O(1440)", "Merge sorted busy intervals → O((n+m) log)", "Bounds become busy blocks"], "You could check every minute, but merging busy intervals is cleaner: add bounds as busy, sort, merge, and read off gaps.",
              st, ["Convert times to minutes", "Back-to-back meetings merge", "Gap must be ≥ duration"], "Work in minutes and format back at the end.", ["Generalises to k calendars"], "This generalises to any number of calendars.",
              "We add each calendar's meetings plus before-start and after-end blocks, sort, merge overlapping intervals, and output gaps at least the duration long.")

def LineThroughPoints():
    from math import gcd
    pts = [(1, 1), (2, 2), (3, 3), (0, 4), (-2, 6), (4, 0), (2, 1)]; best = 1; st = []
    for i, a in enumerate(pts):
        sl = {}
        for b in pts[i + 1:]:
            dx, dy = b[0] - a[0], b[1] - a[1]; g = gcd(abs(dx), abs(dy)); dx //= g; dy //= g
            if dx < 0 or (dx == 0 and dy < 0): dx, dy = -dx, -dy
            sl[(dx, dy)] = sl.get((dx, dy), 0) + 1
        top = max(sl.items(), key=lambda kv: kv[1]) if sl else ((0, 0), 0); best = max(best, top[1] + 1)
        if i < 3: st.append(S("Worked example", [T([[f"{k[1]}/{k[0]}", v] for k, v in sl.items()], colh=["slope dy/dx", "points"]), TX([f"anchor {a}: best line has {top[1] + 1} points", f"overall best {best}"])], f"Anchor {a}", f"Anchor at {a}: group the other points by reduced slope. The biggest group plus the anchor gives {top[1] + 1} points on one line. Best so far {best}."))
    return _e(["Every pair defines a line, count points on it → O(n³)", "Anchor + slope hash map → O(n²)", "Reduce slopes by gcd to avoid floats"], "Checking each pair's line against every point is cubic. Anchoring at each point and grouping the others by slope is quadratic.",
              st, ["Use reduced (dx, dy), not floats", "Normalise sign", "Vertical lines"], "Floating-point slopes are risky; use reduced integer pairs with normalised signs.", ["Mention duplicates handling"], "If duplicates are allowed, count them separately.",
              "For each anchor, we compute reduced dx and dy to every later point, normalise the sign, count in a map, and track the best count plus one.")

def MinimumAreaRectangle():
    pts = [(1, 5), (5, 1), (4, 2), (2, 4), (2, 2), (1, 2), (4, 5), (2, 5), (-1, -2)]; P = set(pts); best = None; bp = None
    for i, a in enumerate(pts):
        for b in pts[i + 1:]:
            if a[0] != b[0] and a[1] != b[1] and (a[0], b[1]) in P and (b[0], a[1]) in P:
                ar = abs(a[0] - b[0]) * abs(a[1] - b[1])
                if best is None or ar < best: best, bp = ar, (a, b)
    a, b = bp
    st = [S("Worked example", [TX([str(pts)], size=16)], "Points", "Find the smallest axis-aligned rectangle using four of these points."),
          S("Worked example", [TX([f"diagonal {a} – {b}", f"need {(a[0], b[1])} and {(b[0], a[1])}: both present ✓"])], "Treat each pair as a diagonal", "Treat each pair as opposite corners. If the other two corners exist in the set, it's a rectangle."),
          S("Worked example", [TX([f"area {abs(a[0] - b[0])} × {abs(a[1] - b[1])} = {best}"])], f"Smallest area: {best}", f"The smallest such rectangle has area {best}.")]
    return _e(["All 4-point combos → O(n⁴)", "Pairs as diagonals + hash set → O(n²)", "Or group by columns"], "Checking all groups of four is n to the fourth. Treating pairs as diagonals with a hash set is quadratic.",
              st, ["Skip pairs sharing x or y", "None → 0", "Use long for area"], "Skip pairs on the same row or column; return zero if none.", ["Mention column-pair alternative"], "Grouping by columns is another quadratic approach.",
              "We store points in a set, and for each pair with different x and y, check the other two corners and keep the min area.")

def WaterfallStreams():
    st = [S("Worked example", [TX(["water enters column 3 at the top", "falls until it hits a block (1)"])], "Water falls straight down", "Water falls straight down from the source until it hits a block."),
          S("Worked example", [TX(["on a block: split 50/50 left and right", "each half slides until it finds a gap below"])], "Splits on a block", "On a block, it splits in half, and each half flows sideways until it can fall again, or is trapped by a wall."),
          S("Worked example", [TX(["bottom row collects percentages", "e.g. [0, 0, 0, 25, 25, 0, 0]"])], "Percentages at the bottom", "Row by row, we carry water amounts down. The bottom row's amounts, as percentages, are the answer.")]
    return _e(["Simulate each droplet → slow", "Row-by-row simulation of amounts → O(w² · h)"], "Simulating individual droplets is slow. Carrying amounts row by row, splitting on blocks, is simple and fast enough.",
              st, ["Water trapped by walls is lost", "Use negatives or a separate array to distinguish water from blocks", "Floating-point percentages"], "Water that hits a side wall is lost.", ["Draw a small example"], "Draw a small grid first.",
              "For each row, water above an open cell falls in; above a block, it splits and each half moves sideways until there's an opening above the next row or a block stops it. Finally we scale the last row to percentages.")

def RightSmallerThan():
    a = [8, 5, 11, -1, 3, 4, 2]; out = [sum(1 for y in a[i + 1:] if y < a[i]) for i in range(len(a))]; st = []
    for i in range(len(a) - 1, -1, -1):
        if i in (6, 4, 2, 0): st.append(S("Worked example", [A(a, hl={i: "cur", **{k: "done" for k in range(i + 1, len(a))}}), A(out[i:] if True else [], label=f"answers from index {i}")], f"Insert {a[i]}: {out[i]} smaller to its right", f"Moving right to left, insert {a[i]} into a BST of everything to its right. Every time we go right, we add the left-subtree size plus one: {out[i]} smaller values."))
    return _e(["For each element, scan right → O(n²)", "BST with left-subtree sizes → O(n log n) average", "Merge-sort counting or BIT → O(n log n) worst"], "Scanning right from every element is quadratic. Inserting right to left into a BST that tracks left-subtree sizes counts smaller values during insertion.",
              st, ["Unbalanced BST → O(n²) worst", "Duplicates go right without counting", "Empty input"], "A sorted input makes the BST degenerate; a Fenwick tree avoids that.", ["Mention BIT / merge sort alternatives"], "Mention the Fenwick-tree and merge-sort alternatives.",
              "We insert from the end. Going left increments that node's left size; going right adds left size plus one, unless equal. The accumulated count is the answer for that index.")

def AllKindsOfNodeDepths():
    nodes, root = level_tree([1, 2, 3, 4, 5, 6, 7, 8, 9]); info = {}
    def f(k):
        if k is None: return (0, 0, 0)
        v, l, r = nodes[k]; L, R = f(l), f(r); size = 1 + L[0] + R[0]; dep = L[1] + L[0] + R[1] + R[0]; info[k] = (size, dep, dep + L[2] + R[2]); return info[k]
    f(root)
    st = [S("Worked example", [TR(nodes, root, notes={k: f"s{v[0]} d{v[1]}" for k, v in info.items() if nodes[k][1] is None and nodes[k][2] is None}), TX(["leaf: size 1, depth-sum 0"], h=0.35)], "Leaves: size 1, depth sum 0", "Each node returns its subtree size, the sum of depths below it, and the running total."),
          S("Worked example", [TR(nodes, root, hl={"3": "cur"}, notes={"3": f"s{info['3'][0]} d{info['3'][1]}"}), TX(["depths = left depths + left size + right depths + right size"], h=0.35, size=18)], "Moving up adds 1 per node below", "Moving up one level adds one to every node's depth below, so depth sum is children's sums plus their sizes."),
          S("Worked example", [TR(nodes, root, hl={"0": "ok"}, notes={"0": f"total {info['0'][2]}"}), TX([f"answer = Σ depth sums of all subtrees = {info['0'][2]}"], h=0.35)], f"Answer: {info['0'][2]}", f"Adding every subtree's depth sum gives {info['0'][2]}.")]
    return _e(["Compute depth sum for every subtree separately → O(n²)", "Single post-order returning (size, depthSum, total) → O(n)"], "Computing each subtree's depth sum separately is quadratic. One post-order pass returning size, depth sum and total is linear.",
              st, ["Use long for large trees", "Null → zeros"], "Use longs on big trees.", ["Explain the +size trick"], "Explain why adding the size shifts depths by one.",
              "Info returns zeros for null. Otherwise it combines children: size is one plus both, depths is each child's depth sum plus its size, and total adds the children's totals.")

def CompareLeafTraversal():
    st = [S("Worked example", [TX(["tree 1 leaves: 4, 7, 8, 6", "tree 2 leaves: 4, 7, 8, 6"])], "Compare leaves left to right", "Two trees match if their leaves, read left to right, are the same sequence."),
          S("Worked example", [TX(["two stacks: pop until a leaf; push right then left", "compare one leaf at a time"])], "Generate leaves lazily with stacks", "Use one stack per tree to produce the next leaf on demand, and compare leaf by leaf, stopping at the first mismatch."),
          S("Worked example", [TX(["4 = 4, 7 = 7, 8 = 8, 6 = 6, both done → true"])], "All equal → true", "All four leaves match, and both run out together, so it's true.")]
    return _e(["Collect both leaf lists, compare → O(n + m) space", "Lazy stacks → O(h1 + h2) space, early exit", "Or link leaves in place"], "Collecting both leaf lists works but uses linear space. Lazy generation with stacks uses only height space and can stop early.",
              st, ["Different number of leaves → false", "Single-node trees", "Push right before left"], "Push right before left so leaves come out left to right.", ["Mention early termination"], "Point out the early exit on mismatch.",
              "Next leaf pops nodes, pushing right then left children, until it pops a leaf. The main loop compares leaves until either runs out, returning true only if both run out together.")

def FlattenBinaryTree():
    st = [S("Worked example", [TR(*level_tree([1, 2, 3, 4, 5, 6]))], "Flatten in in-order into a doubly linked list", "Flatten the tree into a doubly linked list in in-order, using left as previous and right as next."),
          S("Worked example", [TX(["flatten(left) → (leftmost, rightmost)", "link rightmost ↔ node; node ↔ leftmost of right"])], "Recursively return both ends", "Each call returns the leftmost and rightmost of its flattened subtree, so the parent can link its left list's tail and right list's head to itself."),
          S("Worked example", [LL([4, 2, 5, 1, 6, 3])], "Result: 4 ⇄ 2 ⇄ 5 ⇄ 1 ⇄ 6 ⇄ 3", "The result is four, two, five, one, six, three, linked both ways.")]
    return _e(["In-order into an array, then relink → O(n) space", "Recursive returning (leftmost, rightmost) → O(h) space"], "Collecting nodes in order and relinking uses linear space. Returning both ends of each flattened subtree lets us link in place with only the recursion stack.",
              st, ["Return the leftmost as the new head", "Single node", "Rewire both directions"], "Return the leftmost node as the head.", ["Mention Morris-style alternative"], "A Morris-style approach avoids recursion.",
              "Flatten recurses left, links its rightmost to the node, recurses right, links its leftmost to the node, and returns the outer ends.")

def IterativeInOrderTraversal():
    st = [S("Worked example", [TR(*level_tree([1, 2, 3, 4, None, 6, 7]))], "Use parent pointers, no stack", "With parent pointers, we can traverse in-order using only prev and current."),
          S("Worked example", [TX(["came from parent → go left if possible, else visit & go right/up", "came from left child → visit, go right or up", "came from right child → go up"], size=18)], "Three cases by where we came from", "If we came from the parent, go left if we can, else visit and go right or up. From the left child, visit and go right or up. From the right child, go up."),
          S("Worked example", [TX(["visit order: 4, 2, 1, 6, 3, 7"])], "Visit order 4, 2, 1, 6, 3, 7", "That yields the in-order sequence four, two, one, six, three, seven.")]
    return _e(["Recursion → O(h) stack", "Explicit stack → O(h)", "Parent pointers + prev → O(1) space"], "Recursion and explicit stacks both use height space. With parent pointers, tracking the previous node is enough for constant space.",
              st, ["Distinguish arriving from left vs right", "Missing children", "Stop when we step past the root's parent"], "Carefully distinguish arriving from the left child versus the right.", ["Mention Morris traversal"], "Morris traversal does constant space without parent pointers.",
              "We loop while current exists, choose next by the three cases, calling the callback at the right moments, then shift prev and current.")

def RightSiblingTree():
    nodes, root = level_tree([1, 2, 3, 4, 5, 6, 7])
    st = [S("Worked example", [TR(nodes, root)], "Point every node's right to its right neighbour", "Rewire every node so its right pointer points to the next node on the same level."),
          S("Worked example", [TX(["level 1: 1 → null", "level 2: 2 → 3 → null", "level 3: 4 → 5 → 6 → 7 → null"])], "Process level by level", "Gather each level's nodes first, from the old pointers, then rewire right pointers along the level."),
          S("Worked example", [TX(["children collected before rewiring → no data lost"])], "Collect children before rewiring", "Collecting the next level before overwriting right pointers is what keeps the right children reachable.")]
    return _e(["BFS level order with a queue → O(n) time, O(w) space", "Recursive with parent sibling pointers → O(h)"], "Level-order processing is straightforward and linear. The recursive version uses the parent's new sibling pointer to reach cousins, saving space.",
              st, ["Don't lose right children while rewiring", "Last node on a level → null", "Missing children"], "Grab the children before you overwrite right.", ["Mention the O(1)-space recursive approach"], "Mention the recursive variant.",
              "We build each next level from the current level's children, then set each node's right to the following node in the level.")

def LongestIncreasingSubsequence():
    import bisect
    a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]; tails = []; st = []
    for i, x in enumerate(a):
        j = bisect.bisect_left(tails, x)
        if j == len(tails): tails.append(x)
        else: tails[j] = x
        if i in (0, 2, 3, 5, 7, 9, 10): st.append(S("Worked example", [A(a, hl={i: "cur"}), A(tails, hl={j: "ok"}, label="smallest tail for each length")], f"{x} → tails[{j}]", f"Binary search where {x} fits among the tails: position {j}. " + ("It extends the longest so far." if j == len(tails) - 1 else "It replaces a larger tail, keeping that length's tail as small as possible.")))
    return _e(["DP: for each i check all j < i → O(n²)", "Patience sorting tails + binary search → O(n log n)", "prev pointers rebuild the sequence"], "The classic DP is quadratic. Keeping the smallest possible tail for each length, and binary-searching where each value goes, is n log n.",
              st, ["tails isn't the LIS itself — rebuild with prev", "Strictly increasing → lower bound", "Empty input"], "The tails array isn't the sequence; keep prev pointers to rebuild it.", ["Explain why small tails help"], "Explain why smaller tails leave room to extend.",
              "For each i, binary search tails for the first value not less than a i, set prev to the index before, store i, and grow length if at the end. Then follow prev from the last tail.")

def LongestStringChain():
    ws = sorted(["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"], key=len); L = {}; nx = {}
    for s in ws:
        L[s] = 1
        for i in range(len(s)):
            t = s[:i] + s[i + 1:]
            if t in L and L[t] + 1 > L[s]: L[s] = L[t] + 1; nx[s] = t
    b = max(L, key=L.get); ch = [b]
    while ch[-1] in nx: ch.append(nx[ch[-1]])
    st = [S("Worked example", [T([[s, L[s]] for s in ws], colh=["string (by length)", "chain length"])], "Process by length; try deleting each char", "Sort by length. For each string, delete each character in turn; if the shorter string exists, extend its chain."),
          S("Worked example", [TX([" → ".join(ch)])], f"Longest chain: {len(ch)}", f"The longest chain is {', '.join(ch)}.")]
    return _e(["Compare all pairs for one-deletion → O(n² · L)", "Sort by length + hash map, try each deletion → O(n · L²)"], "Comparing every pair is quadratic in the number of strings. Sorting by length and trying each single deletion with a hash map is n times L squared.",
              st, ["Chain must have ≥ 2 strings", "Track next for reconstruction", "Duplicates"], "A single string isn't a chain; return empty if the best is one.", ["Relate to LIS"], "It's longest increasing subsequence on a different relation.",
              "We sort by length; each string starts at length one, and for each deletion that exists we extend and remember the link. Then we follow links from the best start.")

def MaxProfitWithKTransactions():
    p = [5, 11, 3, 50, 60, 90]; k = 2; prev = [0] * len(p); rows = [prev[:]]
    for t in range(k):
        cur = [0] * len(p); bb = float("-inf")
        for d in range(len(p)): bb = max(bb, prev[d] - p[d]); cur[d] = max(cur[d - 1] if d else 0, bb + p[d])
        prev = cur; rows.append(cur)
    st = [S("Worked example", [T(rows[:t + 1], rowh=[f"{r} tx" for r in range(t + 1)], colh=["", *p], hl={(t, len(p) - 1): "ok"}), TX([f"best with {t} transactions: {rows[t][-1]}"])], f"{t} transaction(s): {rows[t][-1]}", f"Row {t}: the best profit by each day using at most {t} transactions. By the last day it's {rows[t][-1]}.") for t in (1, 2)]
    st.insert(0, S("Worked example", [A(p, label="prices")], "Prices; k = 2", "Prices five, eleven, three, fifty, sixty, ninety; at most two transactions."))
    return _e(["Try all buy/sell combos → exponential", "DP[t][d] with inner loop → O(k·n²)", "Track best buy → O(k·n), two rows"], "The naive DP checks every buy day for every sell day. Tracking the best value of previous profit minus price makes each row linear.",
              st, ["k ≥ n/2 → unlimited transactions", "Empty prices → 0", "Rolling rows"], "If k is at least half the days, it's the unlimited case.", ["Explain bestBuy"], "Explain best buy as the max of prior profit minus price.",
              "For each transaction count, we sweep days, updating best buy with prev profit minus price, and cur as the max of yesterday or selling today. Then swap rows.")

def PalindromePartitioningMinCuts():
    s = "noonabbad"; n = len(s); pal = [[False] * n for _ in range(n)]; cuts = [0] * n
    for j in range(n):
        cuts[j] = j
        for i in range(j + 1):
            if s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1]): pal[i][j] = True; cuts[j] = 0 if i == 0 else min(cuts[j], cuts[i - 1] + 1)
    st = [S("Worked example", [A(list(s), idx=False), A(cuts, label="min cuts for prefix ending here")], "cuts[j] = min over palindromes s[i..j] of cuts[i−1] + 1", "For each end j, consider every palindrome ending there; the cuts are one more than the best for the prefix before it."),
          S("Worked example", [A(list(s), hl={0: "ok", 1: "ok", 2: "ok", 3: "ok", 5: "acc", 6: "acc", 7: "acc", 8: "acc"}, idx=False), TX([f"noon | a | bbad? → 'noon' 'a' 'bb' 'a' 'd' … min cuts = {cuts[-1]}"], size=18)], f"Answer: {cuts[-1]} cuts", f"The minimum is {cuts[-1]} cuts.")]
    return _e(["Try all partitions → exponential", "Palindrome table + cuts DP → O(n²)", "Expand-around-centre variant"], "Trying every partition is exponential. A palindrome table plus a min-cuts DP is quadratic.",
              st, ["Whole string palindrome → 0", "Single chars always palindromes"], "If the whole string is a palindrome, zero cuts.", ["Mention centre-expansion O(1) space for pal"], "Centre expansion avoids the table.",
              "For each end j, cuts starts at j; for each start i where s i to j is a palindrome, mark it and update cuts j with zero or cuts i minus one plus one.")

def SquareOfZeroes():
    m = [[1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 1]]
    st = [S("Worked example", [T(m)], "Find a square whose border is all 0s", "Is there a square, at least two by two, whose border is entirely zeros?"),
          S("Worked example", [TX(["precompute right[r][c]: zeros to the right", "and down[r][c]: zeros downward"])], "Precompute zero runs", "Precompute how many consecutive zeros extend right and down from every cell."),
          S("Worked example", [T(m, hl={(r, c): "ok" for r in range(1, 6) for c in range(0, 5) if r in (1, 5) or c in (0, 4)})], "Check corners in O(1) per square", "For each top-left corner and size, four lookups check all four sides. Here, the five-by-five square from row one, column zero works.")]
    return _e(["Check every square's border cell by cell → O(n⁴)", "Precomputed runs → O(n³)", "O(1) side checks"], "Checking every border cell by cell is n to the fourth. Precomputing zero runs right and down makes each square a constant-time check, n cubed overall.",
              st, ["Size ≥ 2", "1×1 doesn't count", "Pad arrays by one"], "Squares must be at least two by two.", ["Explain the four checks"], "Spell out the four checks: top, left, bottom, right.",
              "We fill right and down from the bottom-right, then for each corner and size check right and down at the top-left, right at the bottom-left, and down at the top-right.")

def AStarAlgorithm():
    st = [S("Worked example", [TX(["f = g + h", "g: steps from start; h: Manhattan distance to end"])], "Priority = cost so far + heuristic", "A star orders the frontier by f, the cost so far plus a heuristic estimate to the goal; here Manhattan distance."),
          S("Worked example", [TX(["expand lowest f; skip walls (1)", "update g if a shorter path is found"])], "Expand the most promising cell", "Pop the cell with the lowest f, relax its four neighbours, skipping walls, and push improvements."),
          S("Worked example", [TX(["reach end → follow 'from' pointers back", "return the path; unreachable → []"])], "Rebuild the path", "When we pop the end, follow back-pointers to rebuild the path.")]
    return _e(["BFS explores uniformly → many cells", "Dijkstra (h = 0)", "A* with admissible heuristic → far fewer expansions"], "BFS and Dijkstra explore in all directions. A star adds a heuristic that pulls the search toward the goal while staying optimal if it never overestimates.",
              st, ["Heuristic must be admissible", "Skip stale entries", "Unreachable → []"], "Manhattan distance is admissible on a four-direction grid.", ["Compare with Dijkstra"], "Dijkstra is A star with a zero heuristic.",
              "We set g to max, push the start with its heuristic, and loop: pop, stop at the end, and for each open neighbour with a better g, update it, record from, and push with g plus h. Then rebuild the path.")

def KnuthMorrisPrattAlgorithm():
    sub = "aabaab"; fail = [0] * len(sub); k = 0
    for i in range(1, len(sub)):
        while k and sub[i] != sub[k]: k = fail[k - 1]
        if sub[i] == sub[k]: k += 1
        fail[i] = k
    st = [S("Worked example", [A(list(sub), idx=False), A(fail, label="failure (longest proper prefix = suffix)")], "Build the failure table", "The failure table stores, for each prefix, the longest proper prefix that's also a suffix."),
          S("Worked example", [TX(["text: aabaaxaabaab", "mismatch at x → jump using fail, don't restart"])], "On mismatch, fall back via the table", "Scanning the text, a mismatch doesn't restart from scratch; we fall back to the failure value and keep going."),
          S("Worked example", [TX(["k reaches len(sub) → found ✓"])], "Match found", "When the matched length reaches the pattern's length, we've found it.")]
    return _e(["Naive matching → O(n·m)", "KMP → O(n + m)", "Failure table avoids re-scanning"], "Naive matching can rescan the same text many times. KMP's failure table lets the text pointer only move forward, linear overall.",
              st, ["Empty pattern → true", "Build fail with the same loop", "Off-by-one in fail[k−1]"], "Building the table uses the same fallback loop as matching.", ["Mention Z-algorithm / Rabin–Karp"], "Mention Rabin-Karp and the Z algorithm as alternatives.",
              "We build fail with a k pointer that falls back on mismatches. Then we scan the text with the same logic, returning true when k equals the pattern length.")

def AirportConnections():
    st = [S("Worked example", [TX(["airports + one-way routes; start LGA", "goal: fewest new routes so every airport is reachable"])], "Fewest new routes from the start", "We want the fewest extra one-way routes so every airport is reachable from the start."),
          S("Worked example", [TX(["collapse strongly connected components", "→ a DAG of components"])], "Collapse SCCs", "First collapse strongly connected components, since airports inside one can already reach each other."),
          S("Worked example", [TX(["count components with no incoming edge", "(excluding the start's component) → answer"])], "Answer = sources other than start", "In the component DAG, every component with no incoming edge, other than the start's, needs exactly one new route.")]
    return _e(["Greedy: repeatedly add route to largest unreachable set → O(V·(V+E))", "SCC condensation + count zero in-degree → O(V + E)"], "The greedy approach repeatedly searches. Condensing strongly connected components with Tarjan and counting sources is linear.",
              st, ["Exclude start's component", "Self-loops", "Already all reachable → 0"], "Don't count the start's own component.", ["Explain why sources suffice"], "Explain why each source needs exactly one edge and that's enough.",
              "We build the graph, label components with Tarjan, mark components with incoming cross edges, and count the rest, excluding the start's.")

def DetectArbitrage():
    import math
    st = [S("Worked example", [T([[1, 0.8631, 0.5903], [1.1586, 1, 0.6849], [1.6939, 1.46, 1]], rowh=["USD", "CAD", "GBP"], colh=["", "USD", "CAD", "GBP"])], "Exchange rates", "Is there a cycle of trades that multiplies money above one?"),
          S("Worked example", [TX(["product > 1 ⇔ Σ −log(rate) < 0", "→ negative cycle detection"])], "Take −log: product > 1 becomes a negative cycle", "Taking minus log turns multiplication into addition, and a product above one into a negative-weight cycle."),
          S("Worked example", [TX([f"USD→CAD→GBP→USD: {0.8631 * 0.6849 * 1.6939:.4f} > 1 ✓", "Bellman–Ford still relaxing after n−1 passes → true"], size=18)], "Bellman–Ford finds it", f"Bellman-Ford keeps improving after n minus one passes, so there's a negative cycle: arbitrage. For example, USD to CAD to GBP and back gives {0.8631 * 0.6849 * 1.6939:.4f}.")]
    return _e(["Try all cycles → exponential", "−log weights + Bellman–Ford → O(n³)", "Floating-point tolerance"], "Trying all cycles is exponential. Converting to minus log weights and detecting a negative cycle with Bellman-Ford is n cubed for a complete graph.",
              st, ["Use an epsilon", "Complete graph → n³", "Start from any node"], "Use a small epsilon in comparisons.", ["Explain the log transform"], "The log transform is the key insight.",
              "Distances start at max except zero. We relax every pair n times with minus log rates; if anything still changes on the last pass, return true.")

def RectangleMania():
    pts = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 1), (2, 0), (3, 1), (3, 0)]; P = set(pts); cnt = sum(1 for a in pts for b in pts if b[0] > a[0] and b[1] > a[1] and (a[0], b[1]) in P and (b[0], a[1]) in P)
    st = [S("Worked example", [TX([str(pts)], size=18)], "Points", "Count axis-aligned rectangles formed by these points."),
          S("Worked example", [TX(["pair (a, b) with b up-right of a = a diagonal", "check the other two corners in a set"])], "Bottom-left & top-right as diagonal", "Treat each pair where the second is strictly up and right of the first as a diagonal, and check the other corners."),
          S("Worked example", [TX([f"rectangles: {cnt}"])], f"Answer: {cnt}", f"Each rectangle is counted exactly once this way: {cnt} in total.")]
    return _e(["All 4-point combos → O(n⁴)", "Diagonal pairs + hash set → O(n²)"], "Choosing four points is n to the fourth. Using strictly up-right pairs as diagonals counts each rectangle once in quadratic time.",
              st, ["Strictly up-right avoids double counting", "Duplicate points"], "Requiring up-right ordering is what avoids counting each rectangle four times.", ["Contrast with Count Squares"], "Contrast with count squares, which allows tilts.",
              "We store points, and for each ordered pair with b up and right of a, count when both other corners exist.")

def TwoEdgeConnectedGraph():
    st = [S("Worked example", [TX(["2-edge-connected: connected, and no bridge", "bridge = edge whose removal disconnects"])], "Definition", "A graph is two-edge-connected if it's connected and removing any single edge keeps it connected, meaning no bridges."),
          S("Worked example", [TX(["DFS: disc[v] = visit time", "low[v] = earliest disc reachable via one back edge"], size=18)], "Discovery and low times", "During DFS, track discovery time and low link: the earliest discovery time reachable from v's subtree with one back edge."),
          S("Worked example", [TX(["edge (v, w) is a bridge if low[w] > disc[v]", "any bridge or unvisited vertex → false"], size=18)], "Bridge test", "If a child's low is greater than the parent's discovery time, the edge between them is a bridge. Also fail if DFS didn't reach everything.")]
    return _e(["Remove each edge, test connectivity → O(E·(V+E))", "Tarjan's bridge-finding DFS → O(V + E)"], "Removing each edge and re-checking connectivity is E times V plus E. Tarjan's single DFS finds bridges in linear time.",
              st, ["Skip the parent edge once", "Disconnected → false", "Empty graph → true"], "Skip the edge back to the parent, and check every vertex was visited.", ["Relate to articulation points"], "The same DFS finds articulation points.",
              "Has bridge assigns disc and low, recurses into unvisited neighbours, returns true if low of the child exceeds disc of v, and updates low from children and back edges. Then we check all vertices were visited.")

def MergeSortedArrays():
    import heapq
    arrs = [[1, 5, 9, 21], [-1, 0], [-124, 81, 121], [3, 6, 12, 20, 150]]; pq = [(a[0], i, 0) for i, a in enumerate(arrs)]; heapq.heapify(pq); out = []; st = []
    while pq:
        v, i, j = heapq.heappop(pq); out.append(v)
        if j + 1 < len(arrs[i]): heapq.heappush(pq, (arrs[i][j + 1], i, j + 1))
        if len(out) in (1, 3, 5, 8, 13): st.append(S("Worked example", [A(sorted(x[0] for x in pq) or ["∅"], label="heap (one per array)"), A(out, label="output")], f"Pop {v} from array {i}", f"Pop the smallest, {v}, from array {i}, and push that array's next element."))
    return _e(["Concatenate and sort → O(N log N)", "Repeated two-way merges → O(N·k)", "Min-heap of k heads → O(N log k)"], "Concatenating and sorting ignores the existing order. A min-heap holding one element per array always yields the next smallest in log k.",
              st, ["Empty arrays", "Store (value, array, index)"], "Skip empty arrays when seeding the heap.", ["Mention divide-and-conquer merging"], "Pairwise divide-and-conquer merging is also N log k.",
              "We seed the heap with each array's first element, then poll, append, and push that array's next element.")

def LinkedListPalindrome():
    v = [0, 1, 2, 2, 1, 0]
    st = [S("Worked example", [LL(v, ptr={"slow": 3, "fast": 5})], "Find the middle with slow/fast", "Slow and fast pointers find the middle."),
          S("Worked example", [LL(v[:3], label="first half"), LL(v[3:][::-1], label="second half reversed")], "Reverse the second half", "Reverse the second half in place."),
          S("Worked example", [LL(v[:3], hl={0: "ok", 1: "ok", 2: "ok"}), LL(v[3:][::-1], hl={0: "ok", 1: "ok", 2: "ok"})], "Compare node by node → true", "Compare the halves node by node. All match, so it's a palindrome. Then reverse back to restore the list.")]
    return _e(["Copy into array, two pointers → O(n) space", "Recursion → O(n) stack", "Reverse second half in place → O(1) space"], "Copying values uses linear space. Finding the middle, reversing the second half and comparing uses constant space.",
              st, ["Odd length: middle node ignored", "Restore the list afterwards", "Single node → true"], "Restore the list afterwards; mutating input is rude.", ["Mention the recursive approach"], "Mention the recursive outer-pointer approach.",
              "Slow and fast find the middle, we reverse from slow, compare against the head, reverse back, and return the result.")

def LruCache():
    from collections import OrderedDict
    c = OrderedDict(); cap = 3; st = []
    for op in [("put", "b", 2), ("put", "a", 1), ("put", "c", 3), ("get", "a"), ("put", "d", 4)]:
        if op[0] == "put":
            c[op[1]] = op[2]; c.move_to_end(op[1]); ev = None
            if len(c) > cap: ev = c.popitem(last=False)[0]
        else: c.move_to_end(op[1]); ev = None
        st.append(S("Worked example", [LL([f"{k}:{v}" for k, v in reversed(c.items())], label="most → least recent"), TX([f"{op[0]}({', '.join(map(str, op[1:]))})" + (f" → evict {ev}" if ev else "")])], f"{op[0]} {op[1]}" + (f", evict {ev}" if ev else ""), f"{'Insert' if op[0] == 'put' else 'Read'} {op[1]} and move it to the front." + (f" Over capacity, so evict the least recent, {ev}." if ev else "")))
    return _e(["List with linear search → O(n) ops", "Hash map + doubly linked list → O(1) all ops"], "A list needs a scan to find and move keys. A hash map pointing into a doubly linked list gives constant-time lookup, move-to-front and eviction.",
              st, ["Update existing key moves it to front", "Capacity ≥ 1", "Sentinel head/tail"], "Updating an existing key also refreshes it.", ["Mention LinkedHashMap"], "Java's linked hash map can do this with access order.",
              "Insert updates and moves an existing node, otherwise evicts the tail's previous node if full and adds a new node at the front. Get moves the node to the front and returns its value.")

def NodeSwap():
    v = [0, 1, 2, 3, 4, 5]; st = []
    for k in (0, 2, 4, 6):
        w = v[:]
        for i in range(0, k, 2): w[i], w[i + 1] = w[i + 1], w[i]
        st.append(S("Worked example", [LL(w, hl={k: "cur", k + 1: "cur"} if k < 6 else {})], f"After {k // 2} swaps", f"After {k // 2} swaps." + (f" Next, swap {w[k]} and {w[k + 1]} by relinking." if k < 6 else " Done.")))
    return _e(["Swap values → not allowed", "Recursion → O(n) stack", "Iterative with dummy → O(1)"], "Swapping values is usually disallowed. Relinking pairs with a dummy head is constant space.",
              st, ["Odd length leaves last node", "Return dummy.next"], "An odd final node stays put.", ["Follow-up: reverse in k-groups"], "Generalises to reversing in groups of k.",
              "With p at the dummy, while two nodes follow, we relink a and b: a's next to b's next, b's next to a, p's next to b, then move p to a.")

def RearrangeLinkedList():
    v = [3, 0, 5, 2, 1, 4]; k = 3; lo = [x for x in v if x < k]; eq = [x for x in v if x == k]; hi = [x for x in v if x > k]
    st = [S("Worked example", [LL(v), TX([f"k = {k}"], h=0.3)], "Partition around k, keeping order", f"Rearrange so values less than {k} come first, then equal, then greater, keeping relative order."),
          S("Worked example", [LL(lo, label="< k"), LL(eq, label="= k"), LL(hi, label="> k")], "Three tail-appended lists", "Walk once, appending each node to one of three lists."),
          S("Worked example", [LL(lo + eq + hi)], "Concatenate", "Join the three lists, carefully handling empty ones.")]
    return _e(["Copy values into arrays → O(n) space", "Three dummy lists → O(n), O(1) space"], "Three dummy-headed lists collect nodes in order, then concatenate, linear time and constant space.",
              st, ["Empty partitions", "Terminate the last list", "Stable order"], "Terminate the high list with null, and skip empty partitions when linking.", ["Mention stability"], "Mention that it's stable.",
              "We append each node to low, equal or high, terminate high, link equal to high, and low to equal or high if equal is empty.")

def ZipLinkedList():
    v = [1, 2, 3, 4, 5, 6]
    st = [S("Worked example", [LL(v, ptr={"mid": 2})], "Find the middle", "Find the middle with slow and fast pointers."),
          S("Worked example", [LL(v[:3], label="first"), LL(v[3:][::-1], label="second reversed")], "Split and reverse the second half", "Split there and reverse the second half."),
          S("Worked example", [LL([1, 6, 2, 5, 3, 4])], "Interleave", "Interleave the two halves: one, six, two, five, three, four.")]
    return _e(["Array of nodes, two pointers → O(n) space", "Middle + reverse + merge → O(1)"], "Storing nodes in an array is simple but uses space. Find the middle, reverse the second half, and interleave in place.",
              st, ["Cut the first half's tail", "Odd lengths", "Short lists"], "Cut the first half's tail, or you'll create a cycle.", ["Same as Reorder List"], "This is reorder list.",
              "We find the middle, cut, reverse the second half, then alternate links from each half.")

def NonAttackingQueens():
    st = [S("Worked example", [TX(["one queen per row", "bitmasks: used columns, ↘ diagonals, ↙ diagonals"])], "Place row by row with bitmasks", "Place one queen per row. Three bitmasks track blocked columns and both diagonals."),
          S("Worked example", [TX(["free = ~(cols | d1 | d2) & full", "take lowest bit, recurse with shifted diagonals"], size=18)], "Iterate over free columns", "Free positions are the bits not blocked. Take each lowest set bit, recurse, shifting the diagonal masks for the next row."),
          S("Worked example", [TX(["n=4 → 2 solutions", "n=8 → 92"])], "Results", "For four queens there are two solutions; for eight, ninety-two.")]
    return _e(["Try all placements → C(n², n)", "Backtracking row by row with sets → O(n!)", "Bitmasks make checks O(1)"], "Trying every placement is hopeless. Backtracking one row at a time with blocked sets prunes hard; bitmasks make it very fast.",
              st, ["Shift diagonals each row", "Mask to n bits", "n = 2, 3 → 0"], "Mask to n bits after shifting.", ["Mention symmetry pruning"], "Mirror symmetry halves the work.",
              "Place returns one when all rows are filled. Otherwise it loops over free bits, recursing with the column added and diagonals shifted left and right.")

def NumberOfBinaryTreeTopologies():
    n = 4; c = [1] + [0] * n; st = []
    for m in range(1, n + 1):
        for l in range(m): c[m] += c[l] * c[m - 1 - l]
        st.append(S("Worked example", [A(c[:m + 1], label="topologies for 0…m nodes", hl={m: "ok"}), TX([f"c[{m}] = Σ c[left]·c[{m}−1−left] = {c[m]}"])], f"{m} nodes → {c[m]}", f"With {m} nodes, choose how many go left; multiply the left and right counts and sum: {c[m]}."))
    return _e(["Recursion without memo → exponential", "DP over sizes → O(n²)", "Closed form: Catalan number"], "Plain recursion recomputes sizes. A DP over sizes is quadratic, and the answer is the Catalan number.",
              st, ["c[0] = 1", "Overflow for large n"], "The empty tree counts as one topology.", ["Mention Catalan closed form"], "Mention the closed form, two n choose n over n plus one.",
              "C of zero is one. For each m, sum c of left times c of m minus one minus left over all left sizes.")

def MedianOfTwoSortedArrays():
    a, b = [1, 3, 4, 5], [2, 3.5, 4.5, 6, 7, 8]
    st = [S("Worked example", [A(a, label="a (shorter)"), A(b, label="b")], "Partition both so the left halves have half the elements", "We want to cut both arrays so the left parts together have half the elements, and everything left is at most everything right."),
          S("Worked example", [A(a, window=(0, 1), label="a"), A(b, window=(0, 2), label="b"), TX(["i=2, j=3: aL=3 ≤ bR=6, bL=4.5 > aR=4 → move right"], size=18)], "Binary search the cut in the shorter array", "Binary search the cut in the shorter array. If b's left max exceeds a's right min, move a's cut right."),
          S("Worked example", [A(a, window=(0, 2), label="a"), A(b, window=(0, 1), label="b"), TX(["i=3, j=2: aL=4 ≤ 4.5, bL=3.5 ≤ 5 ✓", "even total → (max(4, 3.5) + min(5, 4.5)) / 2 = 4.25"], size=18)], "Valid cut → median 4.25", "Now the cut is valid. With an even total, the median is the average of the max left and min right: four point two five.")]
    return _e(["Merge then pick middle → O(n + m)", "Binary search partition in the shorter array → O(log min(n, m))"], "Merging is linear. Binary-searching a partition in the shorter array finds the median in log of the smaller length.",
              st, ["Search the shorter array", "Sentinels at the edges", "Odd vs even totals"], "Always search the shorter array and use sentinels at the ends.", ["Explain the partition condition"], "Explain the two cross conditions clearly.",
              "We swap so a is shorter, binary search i, set j to half minus i, read the four border values with sentinels, adjust, and return the median when both conditions hold.")

def OptimalAssemblyLine():
    steps, k = [15, 15, 30, 30, 45], 3
    def stations(cap):
        c, cur = 1, 0
        for s in steps:
            if cur + s > cap: c += 1; cur = 0
            cur += s
        return c
    lo, hi = max(steps), sum(steps); st = []
    while lo < hi:
        m = (lo + hi) // 2; s = stations(m)
        st.append(S("Worked example", [A(steps), TX([f"max time {m}: needs {s} stations", f"range [{lo}, {hi}] → " + ("hi = mid" if s <= k else "lo = mid + 1")])], f"Try {m}: {s} stations", f"With a max of {m} per station, we'd need {s} stations, " + ("which fits, so try smaller." if s <= k else "too many, so go larger.")))
        if s <= k: hi = m
        else: lo = m + 1
    st.append(S("Worked example", [TX([f"answer: {lo}"])], f"Answer: {lo}", f"The smallest feasible maximum is {lo}."))
    return _e(["Try all partitions → exponential", "DP → O(k·n²)", "Binary search on the answer + greedy check → O(n log Σ)"], "Trying every split is exponential and the DP is k n squared. Binary search on the answer with a greedy feasibility check is n log of the sum.",
              pick(st, 6), ["lo = max step", "Greedy check is optimal for a fixed cap"], "The lower bound is the largest single step.", ["Same as Split Array Largest Sum"], "This is split array largest sum.",
              "We binary search between the max and the sum; the greedy count of stations decides which half to keep.")

def CountInversions():
    a = [2, 3, 3, 1, 9, 5, 6]; inv = [(i, j) for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j]]
    st = [S("Worked example", [A(a), TX([f"inversions: {inv}"], size=16)], f"{len(inv)} inversions", f"An inversion is a pair where the earlier value is bigger. There are {len(inv)} here."),
          S("Worked example", [A([2, 3, 3, 1], label="left half (sorted: 1,2,3,3)"), A([9, 5, 6], label="right half (sorted: 5,6,9)")], "Merge sort: count within halves recursively", "Merge sort counts inversions within each half recursively."),
          S("Worked example", [TX(["merging: when right element is taken first,", "add (number of remaining left elements)"])], "Count cross inversions while merging", "While merging, each time a right element goes before remaining left elements, those left elements each form an inversion with it.")]
    return _e(["Check all pairs → O(n²)", "Merge sort counting → O(n log n)", "BIT over values → O(n log n)"], "Checking all pairs is quadratic. Counting during merge sort is n log n.",
              st, ["Use ≤ to avoid counting equals", "long for large counts", "Don't mutate input"], "Take from the left on ties so equal values aren't counted.", ["Mention Fenwick tree"], "A Fenwick tree also works.",
              "Count recursively sorts both halves, copies to aux, and merges; when taking from the right, it adds mid minus i plus one.")

def MergeSort():
    a = [8, 5, 2, 9, 5, 6, 3]
    st = [S("Worked example", [A(a)], "Split in half recursively", "Split the array in half repeatedly until pieces have one element."),
          S("Worked example", [A([2, 5, 8, 9], label="sorted left"), A([3, 5, 6], label="sorted right")], "Sort both halves", "After recursion, both halves are sorted."),
          S("Worked example", [A(sorted(a), hl={i: "ok" for i in range(7)})], "Merge with two pointers", "Merge by repeatedly taking the smaller front element.")]
    return _e(["Quadratic sorts → O(n²)", "Merge sort → O(n log n), stable", "O(n) auxiliary"], "Merge sort guarantees n log n and is stable, at the cost of an auxiliary array.",
              st, ["Allocate aux once", "≤ for stability", "Base case size 1"], "Allocate the auxiliary array once, not per call.", ["Compare with quick sort"], "Contrast with quick sort's average speed and in-place nature.",
              "Sort recurses on both halves, copies the range to aux, and merges back taking the smaller of the two fronts.")

def LargestPark():
    land = [[0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0]]; h = [0] * 4; st = []
    for r, row in enumerate(land):
        h = [0 if x else h[c] + 1 for c, x in enumerate(row)]
        best = max(min(h[i:j + 1]) * (j - i + 1) for i in range(4) for j in range(i, 4))
        st.append(S("Worked example", [T(land, hl={(r, c): "cur" for c in range(4)}), A(h, label="free heights"), TX([f"largest rectangle in histogram: {best}"])], f"Row {r}: histogram {h}", f"After row {r}, each column's height counts free cells above. The best rectangle in this histogram is {best}."))
    return _e(["Check every rectangle → O(R²C²)", "Histogram per row + monotonic stack → O(R·C)"], "Checking every rectangle is huge. Treating each row as the base of a histogram and using the skyline stack is linear in the grid.",
              st, ["Reset height on obstacles", "Empty grid → 0"], "A blocked cell resets that column's height to zero.", ["Same as Maximal Rectangle"], "This is maximal rectangle.",
              "For each row, update heights, then compute the largest rectangle under that histogram with the stack method, tracking the best.")

def LongestBalancedSubstring():
    s = "())()(()())"; best = 0
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1, 2):
            t = s[i:j]; b = 0; ok = True
            for ch in t:
                b += 1 if ch == "(" else -1
                if b < 0: ok = False; break
            if ok and b == 0: best = max(best, len(t))
    st = [S("Worked example", [A(list(s), idx=False)], "Find the longest balanced substring", "Find the longest balanced substring of parentheses."),
          S("Worked example", [TX(["left→right: count opens/closes", "equal → candidate; closes > opens → reset"])], "Left-to-right scan", "Scan left to right counting opens and closes. Equal counts give a candidate; more closes means reset."),
          S("Worked example", [TX(["right→left scan catches extra '(' cases", f"answer: {best}"])], f"Answer: {best}", f"A second scan from the right catches cases with surplus opens. The answer is {best}.")]
    return _e(["Check every substring → O(n³)", "Stack of indices → O(n), O(n) space", "Two counter scans → O(n), O(1)"], "Checking every substring is cubic. A stack of indices is linear; two counting scans in opposite directions are linear with constant space.",
              st, ["Need both directions", "Reset correctly", "Empty → 0"], "One direction alone misses cases like extra opens.", ["Mention the stack approach"], "Mention the stack alternative.",
              "Scan counts opens and closes, records two times closes when equal, and resets when closes exceed opens; reverse mode swaps the roles.")

def SmallestSubstringContaining():
    big, small = "abcd$ef$axb$c$", "$$abf"
    st = [S("Worked example", [TX(["big: " + big.replace("$", r"\$"), "small: " + small.replace("$", r"\$")])], "Smallest window containing all chars of small", "Find the smallest substring of big containing every character of small, with multiplicity."),
          S("Worked example", [TX(["expand r until nothing is missing", "then shrink l while still valid"])], "Expand right, shrink left", "Expand the right end until nothing is missing, then shrink from the left while it stays valid, recording the best."),
          S("Worked example", [TX([r"answer: f\$axb\$"])], r"Answer: f\$axb\$", "The smallest such window is f, dollar, a, x, b, dollar.")]
    return _e(["Check every substring → O(n² · m)", "Sliding window with need counts → O(n + m)"], "Checking every substring is quadratic or worse. A sliding window with a count of missing characters is linear.",
              st, ["Multiplicity matters", "None → ''", "Track 'missing' to avoid map scans"], "Duplicates in small must be matched in count.", ["Same as Minimum Window Substring"], "This is minimum window substring.",
              "We count needs, decrement missing as r covers needed characters, and while missing is zero record the window and advance l, restoring needs.")

def StringsMadeUpOfStrings():
    ss, subs = ["bar", "are", "foo", "ba", "b", "barely"], ["b", "a", "r", "ba", "ar", "ely"]; D = set(subs)
    def pieces(s):
        p = [-1] * (len(s) + 1); p[0] = 0
        for j in range(1, len(s) + 1):
            for i in range(j):
                if p[i] >= 0 and s[i:j] in D: p[j] = max(p[j], p[i] + 1)
        return p[-1]
    st = [S("Worked example", [TX([f"strings: {ss}", f"substrings: {subs}"], size=18)], "Which strings are built from ≥ 2 substrings?", "Which strings can be built from at least two of the substrings?"),
          S("Worked example", [T([[s, pieces(s)] for s in ss], colh=["string", "max pieces"])], "Word-break DP per string", "For each string, a word-break DP finds whether it splits into dictionary pieces, and how many."),
          S("Worked example", [TX([str([s for s in ss if pieces(s) >= 2])])], "Answer", "Strings with at least two pieces qualify.")]
    return _e(["Try all splits → exponential", "Word-break DP per string → O(L²) each", "Trie can speed lookups"], "Trying every split is exponential. A word-break DP per string is quadratic in its length.",
              st, ["Need ≥ 2 pieces", "Unreachable → −1", "Substring hashing cost"], "A string equal to a single substring doesn't count.", ["Same as Concatenated Words"], "This resembles concatenated words.",
              "For each string we fill pieces from zero, extending when a dictionary substring ends at j, and keep strings with at least two pieces.")
