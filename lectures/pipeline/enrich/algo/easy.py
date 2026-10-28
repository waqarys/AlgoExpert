from enrich.kit import *

def NonConstructibleChange():
    coins = sorted([5, 7, 1, 1, 2, 3, 22]); ch = 0; st = []
    for i, c in enumerate(coins):
        if c > ch + 1:
            st.append(S("Worked example", [A(coins, hl={i: "bad"}, ptr={"coin": i}, dim=range(i + 1, len(coins))), TX([f"change = {ch}", f"coin {c} > {ch} + 1"])],
                        f"Coin {c} > {ch + 1}: we can never make {ch + 1}", f"Now coin {c} is bigger than {ch} plus one. There's no way to make {ch + 1}, so that's our answer.")); break
        st.append(S("Worked example", [A(coins, hl={**{j: "done" for j in range(i)}, i: "cur"}, ptr={"coin": i}), TX([f"change before = {ch}", f"{c} ≤ {ch} + 1 → change = {ch + c}"])],
                    f"Every amount 1…{ch + c} is now reachable", f"Coin {c} is at most {ch} plus one, so it extends our reach: every amount up to {ch + c} can be made."))
        ch += c
    return E(["Brute force: try amounts 1, 2, 3… and check each with subset sums", "Each check is exponential (2ⁿ subsets)", "Optimal: sort once, then one greedy pass → O(n log n)"],
             "The brute-force idea is to test amounts one, two, three and so on, checking each against every subset of coins. That's exponential. Sorting first lets a single greedy pass track the largest reachable amount, so the whole thing is n log n.",
             [S("Worked example", [A(coins, label="sorted coins"), TX(["change = 0  (we can make every amount up to 0)"])], "Coins: [5, 7, 1, 1, 2, 3, 22] → sorted", "Let's use the coins five, seven, one, one, two, three and twenty-two. After sorting, we start with change equal to zero.")] + pick(st, 5),
             ["No coins → answer is 1", "Duplicates are fine (1, 1 → reach 2)", "Must sort first; unsorted order breaks the invariant", "Use long if values can be large"],
             "Edge cases: with no coins the answer is one. Duplicates are fine. The invariant only holds if coins are processed in ascending order, so forgetting to sort is the classic bug. And with big values, use a long for the running total.",
             ["Explain the invariant: all of 1…change are buildable", "Follow-up: what if coins can be reused? (answer changes)", "Mention it's a greedy proof by induction"],
             "In the interview, state the invariant clearly: every amount from one to change is buildable. That's an induction proof. A good follow-up is what changes if coins can be reused.",
             ["The whole solution is a few lines. We sort the array, keep a running total called reach, and for each coin break out as soon as the coin exceeds reach plus one. Otherwise we add it. Whatever reach plus one is at the end is the answer."])

def SortedSquaredArray():
    a = [-7, -3, 1, 4, 8]; n = len(a); out = [None] * n; l, r = 0, n - 1; st = []
    for k in range(n - 1, -1, -1):
        if abs(a[l]) > abs(a[r]): v = a[l] * a[l]; who = "left"; i = l; l += 1
        else: v = a[r] * a[r]; who = "right"; i = r; r -= 1
        out[k] = v
        st.append(S("Worked example", [A(a, hl={i: "cur"}, ptr={"L": l if who == "right" else l - 1, "R": r if who == "left" else r + 1}, label="input"), A(["" if x is None else x for x in out], hl={k: "ok"}, label="output (filled from the back)")],
                    f"|{a[i]}| is larger → write {v} at index {k}", f"Compare the absolute values at the two ends. The {who} one, {a[i]}, is larger, so its square, {v}, goes into position {k}, and we move that pointer inward."))
    return E(["Brute force: square everything, then sort → O(n log n)", "Optimal: largest squares are at the ends → two pointers, O(n)"],
             "The brute-force approach squares every value and sorts the result, which is n log n. But since the input is sorted, the largest square must come from one of the two ends, so two pointers fill the output from the back in linear time.",
             pick(st, 5),
             ["All negatives: squares come out reversed", "Zeros and duplicates are fine", "Fill the output from the back, not the front", "Don't modify the input in place"],
             "Watch out for an all-negative input, where the order fully reverses, and remember that the output must be filled from the back, because we always find the largest remaining square.",
             ["State the brute force first, then improve", "Follow-up: do it in place? (not easily — need extra array)", "Generalise: merge of two sorted sequences"],
             "Mention the sort-based solution first, then improve it. This is really a merge of two sorted sequences, the negatives reversed and the non-negatives, which is a nice way to explain it.",
             ["We keep left and right pointers and an output array. Walking k from the last index down, we compare absolute values at both ends, write the larger square at k, and move that pointer inward."])

def TournamentWinner():
    comps = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]; res = [0, 0, 1]; sc = {}; best = ""; st = []
    for (h, a), r in zip(comps, res):
        w = h if r == 1 else a; sc[w] = sc.get(w, 0) + 3
        if sc[w] > sc.get(best, 0): best = w
        st.append(S("Worked example", [T([[h, a, r, w]], colh=["home", "away", "result", "winner"], hl={(0, 3): "ok"}), T([[k, v] for k, v in sc.items()], colh=["team", "points"], hl={(list(sc).index(best), 0): "cur"})],
                    f"{w} wins (+3) → leader: {best}", f"{h} plays {a}, and the result is {r}, so {w} wins and gets three points. The current leader is {best}."))
    return E(["Brute force: recount every team's points at the end — still O(n)", "Simplest optimal: one hash map + running leader", "Avoid a second pass by updating the leader on the fly"],
             "There isn't a slow brute force here so much as a clumsy one: tally everything, then scan the table for the max. We can do it in a single pass by updating the leader whenever a team's score passes it.",
             st,
             ["result = 1 means the HOME team won", "Ties can't happen (problem guarantees one winner)", "Initialise the leader with an empty team at 0 points"],
             "The main pitfall is reading the result backwards: one means the home team won. Initialise the leader as an empty name with zero points so the first winner takes over.",
             ["Clarify the meaning of result before coding", "Follow-up: handle ties (e.g. alphabetical)", "Mention O(k) space for k teams"],
             "Clarify the result encoding before you start. A natural follow-up is how you'd break ties, for example alphabetically.",
             ["We loop over competitions and results together, pick the winner, add three points in the map, and update the leader if this team now has more points than the current leader."])

def TransposeMatrix():
    m = [[1, 2, 3], [4, 5, 6]]; R, C = 2, 3; t = [[None] * R for _ in range(C)]; st = []
    for i in range(R):
        for j in range(C):
            t[j][i] = m[i][j]
            if (i, j) in [(0, 0), (0, 2), (1, 1), (1, 2)]:
                st.append(S("Worked example", [T(m, hl={(i, j): "cur"}, label="input 2×3", w=0.45), T([["" if x is None else x for x in r] for r in t], hl={(j, i): "ok"}, label="output 3×2", w=0.55)],
                            f"m[{i}][{j}] = {m[i][j]} → t[{j}][{i}]", f"The value {m[i][j]} at row {i}, column {j} moves to row {j}, column {i} of the result.", layout="cols"))
    return E(["Only one sensible approach: copy every cell once", "Must allocate a new C×R matrix (shape changes)", "In-place only works for square matrices"],
             "There's no faster approach than touching every cell once, so the question is really about getting indices right. Because the shape changes from R by C to C by R, we need a new matrix; an in-place swap only works when the matrix is square.",
             st,
             ["Swap the dimensions when allocating", "1×n and n×1 inputs", "Don't mix up rows and columns in the loop"],
             "The classic bug is allocating the result with the original dimensions. Test a single row and a single column input to catch it.",
             ["Follow-up: in-place transpose of a square matrix (swap i<j)", "Follow-up: rotate 90° = transpose + reverse rows"],
             "Good follow-ups are an in-place transpose for square matrices, swapping only cells above the diagonal, and rotating an image by ninety degrees, which is a transpose plus reversing each row.",
             ["We allocate a matrix with columns and rows swapped, then two nested loops copy matrix i j into result j i."])

def TwoNumberSum():
    a = [3, 5, -4, 8, 11, 1, -1, 6]; t = 10; seen = []; st = []
    for i, x in enumerate(a):
        need = t - x
        if need in seen:
            st.append(S("Worked example", [A(a, hl={i: "ok", a.index(need): "ok"}, ptr={"i": i}), TX([f"x = {x}, need {t} − {x} = {need}", f"seen = {{{', '.join(map(str, seen))}}}  ✓ contains {need}"])],
                        f"Found: {need} + {x} = {t}", f"At {x} we need {need}, and it's already in the set. We return {need} and {x}.")); break
        st.append(S("Worked example", [A(a, hl={**{j: "done" for j in range(i)}, i: "cur"}, ptr={"i": i}), TX([f"x = {x}, need {need}", f"seen = {{{', '.join(map(str, seen))}}}  ✗ → add {x}"])],
                    f"{need} not seen yet → remember {x}", f"At index {i} the value is {x}, so we need {need}. It isn't in the set yet, so we add {x} and move on."))
        seen.append(x)
    return E(["Brute force: check every pair → O(n²)", "Sorting + two pointers → O(n log n), O(1) space", "Hash set of seen values → O(n) time, O(n) space"],
             "The brute force checks every pair, which is n squared. Sorting and using two pointers gets n log n with constant extra space. The hash-set approach is linear: for each number, we just ask whether its partner has already appeared.",
             [S("Worked example", [A(a), TX([f"target = {t}"])], "array = [3, 5, -4, 8, 11, 1, -1, 6], target = 10", "Let's trace the array three, five, minus four, eight, eleven, one, minus one, six, with a target of ten.")] + pick(st, 5),
             ["No pair → return an empty array", "Don't pair a number with itself (check before adding)", "Negative numbers work the same way"],
             "If there's no pair, return an empty array. Checking the set before adding the current number guarantees we never pair a number with itself.",
             ["Mention all three approaches and their trade-offs", "Follow-up: return indices; or all pairs; or 3-sum", "Ask whether the input fits in memory"],
             "Walk through all three approaches and their trade-offs. Common follow-ups are returning indices, finding all pairs, or extending to three-number sum.",
             ["We create a hash set, loop over the array, and for each value x check whether target minus x is in the set. If it is, we return the pair right away; otherwise we add x. Falling out of the loop means no pair exists."])

def ValidateSubsequence():
    a = [5, 1, 22, 25, 6, -1, 8, 10]; seq = [1, 6, -1, 10]; j = 0; st = []
    for i, x in enumerate(a):
        if j < len(seq) and x == seq[j]:
            j += 1
            st.append(S("Worked example", [A(a, hl={i: "ok"}, ptr={"i": i}, label="array"), A(seq, hl={k: "ok" for k in range(j)}, ptr={"j": j} if j < len(seq) else {}, label="sequence")],
                        f"{x} matches → advance j to {j}", f"The array value {x} matches the next sequence item, so j advances to {j}."))
    return E(["Brute force: try every way to pick positions → exponential", "Optimal: one greedy pass, matching in order", "Greedy is safe: matching early never hurts"],
             "A brute-force approach would try every way of choosing positions in the array, which is exponential. But matching each sequence element at its earliest opportunity is always safe, so one pass with two indices is enough.",
             pick(st, 5) + [S("Worked example", [A(seq, hl={k: "ok" for k in range(len(seq))}, label="sequence")], f"j = {j} = len(sequence) → valid", "We matched every element of the sequence, so it's a valid subsequence.")],
             ["Sequence longer than array → false", "Repeated values: each array element used once", "Single-element sequence"],
             "If the sequence is longer than the array it can't be a subsequence. Each array element can only be used once, which the single forward pass guarantees.",
             ["Clarify: subsequence ≠ subarray (no contiguity)", "Follow-up: check many sequences against one array"],
             "Clarify the difference between a subsequence and a subarray: subsequences don't have to be contiguous. A follow-up is checking many sequences quickly, where you'd preprocess positions of each value.",
             ["We keep an index into the sequence. Scanning the array, whenever the current value equals the next sequence element, we advance that index. The answer is whether the index reached the sequence length."])

def FindClosestValueInBst():
    vals = [10, 5, 15, 2, 5, 13, 22, 1, 14]; nodes, root = bst(vals); t = 12; cur = root; best = nodes[root][0]; st = []; path = []
    while cur is not None:
        v = nodes[cur][0]
        if abs(v - t) < abs(best - t): best = v
        path.append(cur)
        nxt = nodes[cur][1] if t < v else nodes[cur][2] if t > v else None
        st.append(S("Worked example", [TR(nodes, root, hl={**{p: "done" for p in path[:-1]}, cur: "cur"}, w=0.7), TX([f"target = {t}", f"node = {v}", f"closest = {best}", "go " + ("left" if t < v else "right" if t > v else "stop")], w=0.3, h=1)],
                    f"At {v}: closest so far {best}; {t} {'<' if t < v else '>'} {v} → go {'left' if t < v else 'right'}", f"At node {v}, the closest value so far is {best}. The target {t} is {'smaller' if t < v else 'larger'}, so we go {'left' if t < v else 'right'} and ignore the other subtree.", layout="cols"))
        cur = nxt
    return E(["Brute force: visit every node → O(n)", "Optimal: follow the BST ordering → O(log n) average", "Worst case O(n) on a skewed tree"],
             "Brute force visits every node and tracks the closest, which is linear. Using the BST property, each comparison discards an entire subtree, so on a balanced tree we only walk one root-to-leaf path, log n on average.",
             st,
             ["Exact match → stop early", "Skewed (linked-list-like) tree → O(n)", "Use absolute difference; watch integer overflow"],
             "Stop early on an exact match. On a skewed tree the path can be n long. And compute differences carefully if values are near the integer limits.",
             ["Prefer the iterative version: O(1) space", "Follow-up: k closest values (in-order + window)"],
             "Mention that the iterative version uses constant space while recursion uses the call stack. A follow-up is finding the k closest values.",
             ["We start at the root with the closest set to its value. In the loop we update closest if this node is nearer, then move left if the target is smaller, right if it's larger, and return immediately on an exact match."])

def BranchSums():
    nodes, root = level_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]); sums = []; st = []
    def dfs(i, s, path):
        if i is None: return
        s += nodes[i][0]; path = path + [i]
        if nodes[i][1] is None and nodes[i][2] is None:
            sums.append(s)
            st.append(S("Worked example", [TR(nodes, root, hl={**{p: "cur" for p in path}, i: "ok"}, notes={i: f"Σ={s}"}, w=0.7), TX(["sums:"] + [str(x) for x in sums], w=0.3, h=1)],
                        f"Leaf {nodes[i][0]}: branch sum {' + '.join(str(nodes[p][0]) for p in path)} = {s}", f"Reaching leaf {nodes[i][0]}, the running total along this path is {s}, so we record it.", layout="cols"))
            return
        dfs(nodes[i][1], s, path); dfs(nodes[i][2], s, path)
    dfs(root, 0, [])
    return E(["Naive: collect each root-to-leaf path, then sum it → O(n·h)", "Optimal: carry the running sum down → O(n)", "Pre-order DFS keeps left-to-right order"],
             "A naive approach stores each full path and sums it at the leaf, repeating work for shared prefixes. Instead we pass the running sum down the recursion, so each node is added exactly once.",
             pick(st, 5),
             ["A node is a leaf only if BOTH children are null", "Single-node tree → [root.value]", "Recursion depth = tree height"],
             "The common bug is treating a node with one child as a leaf. A node is a leaf only when both children are null.",
             ["Follow-up: return the paths themselves", "Follow-up: path sum equals target?", "Iterative version with an explicit stack"],
             "Follow-ups include returning the paths, or checking whether any path sums to a target. You can also do it iteratively with a stack of node and sum pairs.",
             ["The helper takes a node, the running sum and the result list. It adds the node's value, records the sum at a leaf, and otherwise recurses left then right."])

def EvaluateExpressionTree():
    # -1 add, -2 sub, -3 div, -4 mul
    vals = [-1, -2, -3, -4, 2, 8, 3, 2, 3, None, None, None, None, None, None]; nodes, root = level_tree(vals)
    op = {-1: "+", -2: "−", -3: "÷", -4: "×"}; disp = {k: [op.get(v[0], v[0]), v[1], v[2]] for k, v in nodes.items()}; st = []; done = {}
    def ev(i):
        v = nodes[i][0]
        if v >= 0: return v
        l, r = ev(nodes[i][1]), ev(nodes[i][2])
        res = l + r if v == -1 else l - r if v == -2 else int(l / r) if v == -3 else l * r
        done[i] = res
        st.append(S("Worked example", [TR(disp, root, hl={**{k: "done" for k in done}, i: "cur"}, notes={k: f"={x}" for k, x in done.items()})],
                    f"{l} {op[v]} {r} = {res}", f"Both children of this {op[v]} node are evaluated: {l} and {r}. Applying the operator gives {res}."))
        return res
    ev(root)
    return E(["There's no faster way: every node must be evaluated once", "Key is post-order: children before the operator", "Recursion depth = height of the tree"],
             "Every node must be evaluated once, so linear time is optimal. The trick is the order: an operator can only be applied after both of its children, which is a post-order traversal.",
             st,
             ["Division truncates toward zero (−7 / 2 = −3)", "Leaves are non-negative operands", "Avoid recomputing subtrees"],
             "Be careful that division truncates toward zero, which Java's integer division already does. Leaves are always non-negative numbers, and negative values encode operators.",
             ["Follow-up: print the infix expression with parentheses", "Follow-up: iterative post-order with a stack"],
             "Natural follow-ups are printing the expression in infix form with parentheses, or evaluating iteratively with a stack.",
             ["If the node's value is non-negative, it's a leaf, so return it. Otherwise evaluate the left and right subtrees, then switch on the operator code to add, subtract, divide or multiply."])

def NodeDepths():
    nodes, root = level_tree([1, 2, 3, 4, 5, 6, 7, 8, 9]); st = []; total = [0]; vis = []
    def dfs(i, d):
        if i is None: return
        total[0] += d; vis.append(i)
        st.append(S("Worked example", [TR(nodes, root, hl={**{p: "done" for p in vis[:-1]}, i: "cur"}, notes={i: f"d={d}"}, w=0.7), TX([f"node {nodes[i][0]}", f"depth {d}", f"total = {total[0]}"], w=0.3, h=1)],
                    f"Node {nodes[i][0]} at depth {d} → total {total[0]}", f"Node {nodes[i][0]} sits at depth {d}, so the running total becomes {total[0]}.", layout="cols"))
        dfs(nodes[i][1], d + 1); dfs(nodes[i][2], d + 1)
    dfs(root, 0)
    return E(["Naive: compute each node's depth by walking up from it → O(n·h)", "Optimal: pass depth down in one traversal → O(n)", "BFS by levels also works: depth × level size"],
             "A naive approach finds each node's depth separately. Passing the depth down during one traversal gives linear time. A breadth-first version multiplies each level's size by its depth.",
             pick(st, 5),
             ["Root has depth 0", "Empty tree → 0", "Deep trees: recursion depth = height"],
             "Remember the root has depth zero, and an empty tree sums to zero.",
             ["Mention iterative stack/queue version", "Follow-up: sum of depths for every subtree (All Kinds Of Node Depths)"],
             "Mention the iterative version. The very hard follow-up, All Kinds of Node Depths, sums this value for every subtree.",
             ["The helper returns zero for a null node, otherwise the current depth plus the results for both children at depth plus one."])

def DepthFirstSearch():
    g = {"A": ["B", "C", "D"], "B": ["E", "F"], "C": [], "D": ["G", "H"], "E": [], "F": ["I", "J"], "G": ["K"], "H": [], "I": [], "J": [], "K": []}
    pos = {"A": [.5, .9], "B": [.2, .65], "C": [.5, .65], "D": [.8, .65], "E": [.08, .4], "F": [.3, .4], "G": [.7, .4], "H": [.92, .4], "I": [.22, .12], "J": [.4, .12], "K": [.7, .12]}
    edges = [(a, b) for a in g for b in g[a]]; order = []; st = []
    def dfs(u):
        order.append(u)
        st.append(S("Worked example", [G(pos, edges, hl={**{x: "done" for x in order[:-1]}, u: "cur"}, directed=True, w=0.7), TX(["visited:", " ".join(order)], w=0.3, h=1)],
                    f"Visit {u} → order: {' '.join(order)}", f"We visit {u} and append it. Then we dive into its first child before touching its siblings.", layout="cols"))
        for v in g[u]: dfs(v)
    dfs("A")
    return E(["DFS is already linear: O(V + E)", "Alternative: BFS gives a different (level) order", "Iterative DFS needs children pushed in reverse"],
             "Depth-first search is already linear in vertices plus edges. What matters is the order: we go as deep as possible before backtracking, unlike breadth-first search, which goes level by level.",
             pick(st, 6),
             ["Child order matters: left to right", "Iterative: push children reversed onto the stack", "General graphs need a visited set (trees don't)"],
             "Children must be visited left to right. If you use an explicit stack, push children in reverse. On general graphs, add a visited set to avoid cycles.",
             ["Know recursive and iterative versions", "Follow-up: detect a cycle, topological sort"],
             "Know both the recursive and iterative versions; DFS underpins cycle detection and topological sort.",
             ["The method appends this node's name, then calls depth-first search on each child in order, passing the same list, and returns it."])

def ClassPhotos():
    red, blue = sorted([5, 8, 1, 3, 4], reverse=True), sorted([6, 9, 2, 4, 5], reverse=True)
    back, front = (blue, red) if blue[0] > red[0] else (red, blue); st = []
    st.append(S("Worked example", [A(red, label="red (sorted desc)"), A(blue, label="blue (sorted desc)")], "Sort both groups; tallest blue 9 > tallest red 8", "Sort both groups by height. The tallest blue student, nine, beats the tallest red, eight, so blue must be the back row."))
    for i in range(len(back)):
        ok = back[i] > front[i]
        if i in (0, 2, 4):
            st.append(S("Worked example", [A(back, hl={i: "ok" if ok else "bad"}, ptr={"i": i}, label="back row (blue)"), A(front, hl={i: "ok" if ok else "bad"}, ptr={"i": i}, label="front row (red)")],
                        f"{back[i]} {'>' if ok else '≤'} {front[i]} ✓" if ok else f"{back[i]} ≤ {front[i]} ✗", f"Position {i}: back {back[i]} versus front {front[i]}. The back student is strictly taller, so this pair works."))
    return E(["Brute force: try every arrangement → factorial time", "Optimal: sort both, compare pairwise → O(n log n)", "Pairing sorted with sorted is the best possible matching"],
             "Trying every arrangement would be factorial. If any arrangement works, pairing the sorted groups position by position works too, so we sort and compare, in n log n.",
             st,
             ["Strictly taller required: equal heights fail", "Decide back row from the tallest of each group", "Groups have equal size"],
             "Heights must be strictly greater, so equal heights fail. Decide which colour goes in the back from the tallest students, then never switch.",
             ["Explain why sorted pairing is optimal (exchange argument)", "Follow-up: count arrangements, or allow mixed rows"],
             "Justify the greedy with an exchange argument: swapping any pair out of sorted order can't help.",
             ["We sort both lists in descending order, choose the back row by comparing the first elements, then check every position strictly. Any failure returns false."])

def MinimumWaitingTime():
    q = sorted([3, 2, 1, 2, 6]); total = 0; st = []
    for i, d in enumerate(q):
        left = len(q) - i - 1; total += d * left
        st.append(S("Worked example", [A(q, hl={**{j: "done" for j in range(i)}, i: "cur"}, ptr={"i": i}), TX([f"duration {d} × {left} waiting = {d * left}", f"total = {total}"])],
                    f"{d} s is waited on by {left} queries → total {total}", f"Query {i} takes {d} seconds, and the {left} queries after it all wait for it, adding {d * left}. The total is now {total}."))
    return E(["Brute force: try every order → n! permutations", "Greedy: shortest first is optimal → O(n log n)", "Each duration counts once per query behind it"],
             "Trying every execution order is factorial. Exchange argument: if a longer query runs before a shorter one, swapping them reduces total waiting. So shortest first is optimal, and sorting costs n log n.",
             [S("Worked example", [A([3, 2, 1, 2, 6], label="queries"), A(q, label="sorted")], "Sort: [3, 2, 1, 2, 6] → [1, 2, 2, 3, 6]", "Take the queries three, two, one, two, six. Sorted, they become one, two, two, three, six.")] + pick(st, 4),
             ["The last query adds 0 (nobody waits for it)", "Sorting in place mutates input (mention it)", "Use long for large totals"],
             "The last query contributes nothing. Sorting in place mutates the input, which you should mention. Use a long if totals can be large.",
             ["Prove with an exchange argument", "Follow-up: weighted queries (Smith's rule: sort by time/weight)"],
             "Prove the greedy with an exchange argument. A follow-up adds weights, where you sort by duration divided by weight.",
             ["We sort the array, then for each index multiply the duration by the number of queries left after it and add it to the total."])

def OptimalFreelancing():
    jobs = [("A", 1, 1), ("B", 2, 1), ("C", 3, 2), ("D", 2, 2)]; jobs.sort(key=lambda j: -j[2]); days = [None] * 7; st = []; earned = 0
    for name, dl, pay in jobs:
        d = min(dl, 7) - 1
        while d >= 0 and days[d] is not None: d -= 1
        if d >= 0: days[d] = f"{name}:{pay}"; earned += pay
        st.append(S("Worked example", [T([[f"{n}" for n, _, _ in jobs], [dl_ for _, dl_, _ in jobs], [p for _, _, p in jobs]], rowh=["job", "deadline", "pay"], hl={(0, [j[0] for j in jobs].index(name)): "cur"}),
                                       A(["" if x is None else x for x in days], hl={d: "ok"} if d >= 0 else {}, label="days 1–7 (index = day − 1)")],
                    f"Job {name} (pay {pay}, deadline {dl}) → " + (f"day {d + 1}" if d >= 0 else "no free day, skip") + f"; earned {earned}",
                    f"Job {name} pays {pay} with deadline {dl}. " + (f"The latest free day on or before the deadline is day {d + 1}, so we book it." if d >= 0 else "Every day up to its deadline is taken, so we skip it.") + f" Earnings so far: {earned}."))
    return E(["Brute force: try every subset and order of jobs → exponential", "Greedy: highest pay first, as late as possible → O(n log n)", "Scheduling late keeps early days free for tight deadlines"],
             "Brute force would try every subset and ordering. Instead, take jobs from highest pay to lowest and place each on the latest free day before its deadline. Placing late keeps early days open for jobs with tight deadlines.",
             st,
             ["Deadlines beyond 7 → cap at day 7", "Equal payments: any order works", "No jobs → 0"],
             "Cap deadlines at seven since the week only has seven days. With no jobs, the answer is zero.",
             ["Explain why 'as late as possible' matters", "Follow-up: n days instead of 7 → union-find for free slots"],
             "Explain why scheduling late matters. With many days instead of seven, a union-find of free slots makes the search fast.",
             ["We sort jobs by payment descending and keep a seven-slot boolean array. For each job, we scan backwards from its capped deadline for a free day, mark it, and add the payment."])

def TandemBicycle():
    red, blue = [5, 5, 3, 9, 2], [3, 6, 7, 2, 1]; r, b = sorted(red), sorted(blue, reverse=True); tot = 0; st = []
    for i in range(5):
        tot += max(r[i], b[i])
        if i in (0, 2, 4):
            st.append(S("Worked example", [A(r, hl={i: "cur"}, ptr={"i": i}, label="red ascending"), A(b, hl={i: "cur"}, ptr={"i": i}, label="blue descending"), TX([f"max({r[i]}, {b[i]}) = {max(r[i], b[i])}", f"total = {tot}"], h=0.5)],
                        f"Pair {r[i]} with {b[i]} → +{max(r[i], b[i])} (total {tot})", f"Pair red {r[i]} with blue {b[i]}. The tandem goes at the faster speed, {max(r[i], b[i])}, so the total becomes {tot}."))
    return E(["Brute force: try all n! pairings", "Fastest total: pair big with small (opposite orders)", "Slowest total: pair big with big (same order) → O(n log n)"],
             "Trying all pairings is factorial. Since each pair counts only its faster rider, the fastest total wastes as few fast riders as possible: pair each fast rider with a slow one. For the slowest total, pair fast with fast.",
             st,
             ["fastest flag flips the sort order of one list", "Sorting mutates inputs", "Equal speeds are fine"],
             "The fastest flag decides whether one list is reversed. Sorting mutates the inputs, so mention it or copy.",
             ["Justify with an exchange argument", "Follow-up: k riders per bike"],
             "Justify the pairing with an exchange argument, and be ready to discuss bikes with more riders.",
             ["We sort both arrays. If we want the fastest total, we read one of them backwards. Then for each index we add the max of the two speeds."])

def MiddleNode():
    v = [2, 7, 3, 5, 9]; s = f = 0; st = []
    st.append(S("Worked example", [LL(v, ptr={"slow": s, "fast": f})], "slow and fast start at the head", "Both pointers start at the head, the node with value two."))
    while f + 1 < len(v):
        s += 1; f += 2
        st.append(S("Worked example", [LL(v, ptr={"slow": s, "fast": min(f, len(v) - 1)}, hl={s: "cur"})], f"slow → {v[s]}, fast → {v[min(f, len(v) - 1)]}", f"Slow moves one step to {v[s]}; fast moves two steps to {v[min(f, len(v) - 1)]}."))
    st.append(S("Worked example", [LL(v, ptr={"slow": s}, hl={s: "ok"})], f"fast can't move: middle is {v[s]}", f"Fast is at the last node, so slow is at the middle: {v[s]}."))
    return E(["Two passes: count length, then walk n/2 → O(n)", "Or copy into an array → O(n) space", "One pass: slow/fast pointers → O(n), O(1) space"],
             "You could count the length and then walk half of it, which takes two passes, or copy the nodes into an array. The slow and fast pointer trick finds the middle in one pass with constant space.",
             st,
             ["Even length: return the SECOND middle", "Single node → itself", "Check fast and fast.next before moving"],
             "For an even length, the problem wants the second middle node, which this loop naturally returns. Always check fast and fast dot next before jumping.",
             ["The same trick detects cycles (Floyd)", "Follow-up: split the list in half for merge sort"],
             "The same pattern powers cycle detection and splitting a list in half for merge sort.",
             ["Slow and fast start at the head. While fast and fast dot next aren't null, slow moves one step and fast moves two. Return slow."])

def RemoveDuplicatesFromLinkedList():
    v = [1, 1, 3, 4, 4, 4, 5, 6, 6]; out = []; st = []; i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and v[j + 1] == v[i]: j += 1
        out.append(v[i])
        st.append(S("Worked example", [LL(v, hl={**{k: "bad" for k in range(i + 1, j + 1)}, i: "cur"}, ptr={"cur": i}, label="original"), LL(out, label="result so far")],
                    f"Value {v[i]}: skip {j - i} duplicate(s)", f"At value {v[i]}, " + (f"the next {j - i} node{'s are' if j - i > 1 else ' is'} the same, so we bypass {'them' if j - i > 1 else 'it'}." if j > i else "the next node is different, so we just move on.")))
        i = j + 1
    return E(["With a hash set: works for unsorted lists, O(n) space", "Sorted list: duplicates are adjacent → O(1) space", "Rewire next pointers in place"],
             "A hash set would work even for unsorted lists, but costs extra space. Because this list is sorted, duplicates are always adjacent, so we can just skip over them in place.",
             pick(st, 5),
             ["Empty list or single node", "Runs of 3+ duplicates (loop, don't just skip one)", "Last node duplicates"],
             "Handle long runs of duplicates with an inner loop, not a single skip, and make sure the end of the list works.",
             ["Follow-up: remove ALL nodes that had duplicates", "Follow-up: unsorted list"],
             "A tricky follow-up removes every value that had duplicates entirely. For unsorted lists, use a hash set.",
             ["For each node, we find the next node with a different value, point current dot next at it, and move current forward."])

def NthFibonacci():
    n = 7; a, b = 0, 1; st = []
    for k in range(3, n + 1):
        a, b = b, a + b
        st.append(S("Worked example", [A([0, 1, None, None, None, None, None][:2] + [None] * 5, idx=False, label="") if False else A(["F1=0", "F2=1"] + [f"F{j}" for j in range(3, n + 1)], hl={k - 3: "done", k - 2: "cur", k - 1: "ok"}), TX([f"last two = ({a}, {b})", f"F{k} = {b}"])],
                    f"F{k} = {a} + {b - a} = {b}", f"To get F {k}, add the last two values: {b - a} plus {a} equals {b}. Then slide the window forward."))
    return E(["Naive recursion: fib(n−1) + fib(n−2) → O(2ⁿ)", "Memoisation → O(n) time, O(n) space", "Iterate with two variables → O(n) time, O(1) space"],
             "Naive recursion recomputes the same values exponentially many times. Memoising fixes that with linear space. The best version just keeps the last two numbers and slides forward.",
             pick(st, 5),
             ["This problem is 1-indexed: F(1) = 0, F(2) = 1", "Overflow for large n (use long / BigInteger)", "n = 1 and n = 2 base cases"],
             "Note this problem's indexing: the first Fibonacci number is zero and the second is one. For large n, values overflow, so use a long or a big integer.",
             ["Show the recursion tree to explain the blow-up", "Follow-up: O(log n) via matrix exponentiation"],
             "Draw the recursion tree to explain the exponential blow-up. A strong follow-up is the log n matrix-power method.",
             ["We return zero and one for the base cases. Otherwise we keep two variables and loop n minus two times, replacing them with the next pair."])

def ProductSum():
    arr = "[5, 2, [7, −1], 3, [6, [−13, 8], 4]]"; st = []
    for lines, cap, nar in [
        (["depth 1: 5 + 2 + 3 = 10 (+ nested)"], "Depth 1: add plain numbers 5, 2, 3", "At depth one, we add the plain numbers five, two and three, and recurse into each nested list."),
        (["[7, −1] at depth 2: (7 − 1) × 2 = 12"], "Nested [7, −1]: sum 6 × depth 2 = 12", "The list seven, minus one sums to six. It's at depth two, so it contributes twelve."),
        (["[−13, 8] at depth 3: (−5) × 3 = −15"], "Innermost [−13, 8]: −5 × 3 = −15", "The innermost list sums to minus five, times depth three gives minus fifteen."),
        (["[6, [−13, 8], 4] at depth 2: (6 − 15 + 4) × 2 = −10"], "Middle list: (6 + (−15) + 4) × 2 = −10", "Back in the list six, the inner list, four: that's six minus fifteen plus four, minus five, times two, minus ten."),
        (["total: (5 + 2 + 12 + 3 − 10) × 1 = 12"], "Answer: 12", "At the top: five plus two plus twelve plus three minus ten is twelve, times depth one. The answer is twelve.")]:
        st.append(S("Worked example", [TX([arr], h=0.5, size=26), TX(lines, size=26)], cap, nar))
    return E(["Only real approach: recursive descent, O(n) total elements", "Mistake to avoid: multiplying by depth too early or twice", "Iterative version uses a stack of (list, depth)"],
             "There's no shortcut: every element must be visited once. The key is where the multiplication happens. Each list sums its elements, including nested results, and multiplies once by its own depth.",
             st,
             ["Empty nested lists contribute 0", "Multiply nested results by their own depth only", "Negative numbers"],
             "Empty lists contribute zero. Make sure each nested result is multiplied only by its own depth, not by every ancestor's.",
             ["Clarify the input type (Object list in Java)", "Follow-up: weight inversely by depth"],
             "In Java the input is a list of objects, so you need an instanceof check. A follow-up flips the weighting so deeper lists count less.",
             ["We loop over the list. Integers are added directly. Nested lists recurse with depth plus one. At the end we multiply the sum by the current depth."])

def BinarySearch():
    a = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]; t = 33; l, r = 0, len(a) - 1; st = []
    while l <= r:
        m = (l + r) // 2
        st.append(S("Worked example", [A(a, hl={m: "ok" if a[m] == t else "cur"}, ptr={"L": l, "M": m, "R": r}, dim=[i for i in range(len(a)) if i < l or i > r]), TX([f"target = {t}", f"a[{m}] = {a[m]}"])],
                    (f"a[{m}] = {t} → found" if a[m] == t else f"{a[m]} {'<' if a[m] < t else '>'} {t} → search {'right' if a[m] < t else 'left'} half"),
                    (f"The middle value is {t}. Found it at index {m}." if a[m] == t else f"The middle is index {m} with value {a[m]}, which is {'smaller' if a[m] < t else 'larger'} than {t}, so we discard the {'left' if a[m] < t else 'right'} half.")))
        if a[m] == t: break
        if a[m] < t: l = m + 1
        else: r = m - 1
    return E(["Linear scan: O(n)", "Binary search: halve the range each step → O(log n)", "1,000,000 items → about 20 comparisons"],
             "A linear scan checks every element. Binary search halves the remaining range with each comparison, so a million items need only about twenty steps.",
             st,
             ["Loop condition is left ≤ right", "Mid as left + (right − left) / 2 avoids overflow", "Not found → −1"],
             "Use left less than or equal to right, compute mid without overflow, and return minus one if not found.",
             ["Know recursive + iterative", "Follow-ups: first/last occurrence, rotated arrays, search on answer"],
             "Know both versions. Variations like first occurrence, rotated arrays, and binary search on the answer appear constantly.",
             ["We keep left and right. While left is at most right, compute mid. Return mid on a match, otherwise move left past mid or right before it. Return minus one at the end."])

def FindThreeLargestNumbers():
    a = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]; top = [None] * 3; st = []
    for x in a:
        changed = None
        if top[2] is None or x > top[2]: top = [top[1], top[2], x]; changed = 2
        elif top[1] is None or x > top[1]: top = [top[1], x, top[2]]; changed = 1
        elif top[0] is None or x > top[0]: top = [x, top[1], top[2]]; changed = 0
        if changed is not None:
            st.append(S("Worked example", [A(a, hl={a.index(x): "cur"}), A(["–" if v is None else v for v in top], hl={changed: "ok"}, label="three largest (ascending)")],
                        f"{x} goes into slot {changed}", f"{x} beats slot {changed}, so it goes there, and smaller values shift down."))
    return E(["Sort the array and take the last three → O(n log n)", "Optimal: one pass with three slots → O(n)", "No sorting, no extra memory"],
             "Sorting and taking the last three costs n log n. A single pass that maintains three slots does it in linear time with constant space.",
             pick(st, 5),
             ["Duplicates can fill several slots (7, 7)", "Negative numbers: start slots as empty, not 0", "Shift order matters: move down before overwriting"],
             "Initialise slots as empty rather than zero, or negatives break. Duplicates may occupy multiple slots, and shifting must happen before you overwrite.",
             ["Follow-up: k largest → min-heap of size k, O(n log k)", "Quickselect for O(n) average"],
             "For k largest, use a min-heap of size k, or quickselect.",
             ["For each number we compare against the largest slot first, then the middle, then the smallest, and a small shift-and-insert helper moves the smaller values down."])

def BubbleSort():
    a = [8, 5, 2, 9, 5, 6, 3]; st = []; n = len(a); end = n
    while True:
        sw = False
        for i in range(end - 1):
            if a[i] > a[i + 1]: a[i], a[i + 1] = a[i + 1], a[i]; sw = True
        end -= 1
        st.append(S("Worked example", [A(a, hl={k: "ok" for k in range(end, n)})], f"After pass {n - end}: {a[end]} bubbled to index {end}", f"After pass {n - end}, the largest remaining value, {a[end]}, has bubbled to position {end}. Green cells are final."))
        if not sw: break
    return E(["Bubble sort is O(n²) — fine for learning, not for production", "Better: merge/quick/heap sort → O(n log n)", "Early exit makes sorted input O(n)"],
             "Bubble sort is quadratic, so in practice you'd use an n log n sort. Its one strength is the early exit: if a pass makes no swaps, the array is sorted, so already-sorted input takes linear time.",
             pick(st, 5),
             ["Shrink the inner range each pass", "Stop when a pass makes no swaps", "Stable: equal elements keep order"],
             "Shrink the range each pass and stop early when nothing swaps. Bubble sort is stable, so equal elements keep their order.",
             ["Know the complexity of all simple sorts", "Follow-up: why is it stable? how many swaps = inversions?"],
             "Be ready to compare it with insertion and selection sort. The number of swaps equals the number of inversions.",
             ["The outer loop repeats until no swaps happen. The inner loop compares each adjacent pair and swaps if out of order, and the range shrinks by one each pass."])

def InsertionSort():
    a = [8, 5, 2, 9, 5, 6, 3]; st = []
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j] < a[j - 1]: a[j], a[j - 1] = a[j - 1], a[j]; j -= 1
        st.append(S("Worked example", [A(a, hl={**{k: "done" for k in range(i + 1)}, j: "cur"}, ptr={"i": i})], f"Insert into sorted prefix → lands at index {j}", f"We take element {i} and swap it left until it's no smaller than its neighbour. It lands at index {j}, and the first {i + 1} elements are now sorted."))
    return E(["O(n²) in the worst case (reverse sorted)", "O(n) on nearly-sorted data — its big advantage", "Used inside hybrid sorts like TimSort for small runs"],
             "Insertion sort is quadratic in the worst case, but on nearly-sorted data it's close to linear, which is why real libraries use it for small or almost-sorted runs.",
             pick(st, 5),
             ["Compare with strict < to stay stable", "Start from index 1", "Shift instead of swap to save writes"],
             "Use a strict comparison to keep it stable. Shifting elements instead of swapping reduces writes.",
             ["Explain the sorted-prefix invariant", "Follow-up: binary search for the insert position"],
             "Explain the invariant: the prefix is always sorted. A follow-up uses binary search to find the insert position, though shifting is still linear.",
             ["For each index from one, we swap the element left while it's smaller than the one before it."])

def SelectionSort():
    a = [8, 5, 2, 9, 5, 6, 3]; st = []
    for i in range(len(a) - 1):
        m = min(range(i, len(a)), key=lambda k: a[k]); a[i], a[m] = a[m], a[i]
        st.append(S("Worked example", [A(a, hl={**{k: "ok" for k in range(i)}, i: "cur"}, ptr={"i": i})], f"Min of suffix = {a[i]} → swap into index {i}", f"The smallest value in the unsorted part is {a[i]}, so we swap it into index {i}."))
    return E(["Always O(n²) comparisons, even if sorted", "At most n−1 swaps (useful when writes are expensive)", "Use an O(n log n) sort in practice"],
             "Selection sort always does quadratic comparisons, even on sorted input. Its niche is making at most n minus one swaps, which matters when writes are expensive.",
             pick(st, 5),
             ["Not stable (long-distance swaps)", "Stop at n − 1", "Track the index of the min, not the value"],
             "Selection sort isn't stable because of its long-distance swaps. Track the index of the minimum, not just its value.",
             ["Compare with bubble and insertion sort", "Follow-up: make it stable (shift instead of swap)"],
             "Compare it with bubble and insertion sort, and know how to make it stable by shifting instead of swapping.",
             ["For each starting index we scan the rest to find the smallest index, then swap it into the start position."])

def CaesarCipherEncryptor():
    s, k = "xyz", 2; st = []; out = ""
    for i, ch in enumerate(s):
        nc = chr((ord(ch) - 97 + k) % 26 + 97); out += nc
        st.append(S("Worked example", [A(list(s), hl={i: "cur"}, label="input"), A(list(out), hl={i: "ok"}, label="output"), TX([f"'{ch}' = {ord(ch) - 97}; ({ord(ch) - 97} + {k}) mod 26 = {(ord(ch) - 97 + k) % 26} → '{nc}'"])],
                    f"'{ch}' shifted by {k} → '{nc}'", f"The letter {ch} is position {ord(ch) - 97}. Adding {k} and taking modulo twenty-six gives {(ord(ch) - 97 + k) % 26}, which is {nc}."))
    return E(["Naive: shift one letter step by step k times → O(n·k)", "Optimal: arithmetic with modulo 26 → O(n)", "Reduce k mod 26 first (k can be huge)"],
             "A naive version steps each letter forward k times. With modular arithmetic, each letter is shifted in one step, and reducing k modulo twenty-six handles huge keys.",
             st,
             ["Wrap-around: 'z' + 1 = 'a'", "Large k (e.g. 54 ≡ 2)", "Lowercase only per problem"],
             "Remember wrap-around from z back to a and reduce large keys first.",
             ["Use a StringBuilder / char array, not string concatenation", "Follow-up: decrypt, uppercase, non-letters"],
             "Build the result with a character array or StringBuilder. Follow-ups include decryption and handling uppercase or punctuation.",
             ["We reduce the key modulo twenty-six, then map each character to its zero-based position, add the key, wrap with modulo, and convert back to a character."])

def CommonCharacters():
    words = ["abc", "bcd", "cbad"]; cnt = {}; st = []
    for w in words:
        for ch in set(w): cnt[ch] = cnt.get(ch, 0) + 1
        st.append(S("Worked example", [TX([f"word: {w}"], h=0.4), T([[k, v] for k, v in sorted(cnt.items())], colh=["char", "#strings"], hl={(i, 1): "ok" for i, (k, v) in enumerate(sorted(cnt.items())) if v == len(words)})],
                    f"After '{w}': counts updated", f"Process {w}: each distinct character's count goes up by one. Characters with count {len(words)} appear in every word so far."))
    st.append(S("Worked example", [T([[k, v] for k, v in sorted(cnt.items())], colh=["char", "#strings"], hl={(i, 1): "ok" for i, (k, v) in enumerate(sorted(cnt.items())) if v == len(words)})],
                f"Answer: {', '.join(sorted(k for k, v in cnt.items() if v == len(words)))}", "Characters that reached the number of words, b and c, are common to all of them."))
    return E(["Brute force: for each char of word 1, scan every other word", "Optimal: count distinct chars per word → O(total chars)", "Use a set per word so repeats count once"],
             "Brute force would check each character of the first word against every other word. Counting how many words contain each distinct character does it in one pass over all the characters.",
             st,
             ["Count each char once per word (use a set)", "Single word → all its unique chars", "Empty string → no common chars"],
             "Use a set per word so repeated letters count once. A single word returns all its unique characters.",
             ["Optimise: start from the shortest word's chars", "Follow-up: include multiplicity (min counts)"],
             "An optimisation starts from the shortest word. A follow-up includes multiplicity, keeping minimum counts per character.",
             ["We loop over the strings, build a set of each string's characters, and increment counts in a map. Finally, we collect characters whose count equals the number of strings."])

def FirstNonRepeatingCharacter():
    s = "abcdcaf"; cnt = {}
    for ch in s: cnt[ch] = cnt.get(ch, 0) + 1
    st = [S("Worked example", [A(list(s)), T([[k, v] for k, v in cnt.items()], colh=["char", "count"])], "Pass 1: count every character", "First pass: count each character. a and c appear twice; b, d and f once.")]
    for i, ch in enumerate(s):
        ok = cnt[ch] == 1
        st.append(S("Worked example", [A(list(s), hl={i: "ok" if ok else "bad"}, ptr={"i": i}), TX([f"count['{ch}'] = {cnt[ch]}"])], f"'{ch}' count {cnt[ch]}" + (f" → answer index {i}" if ok else " → skip"), f"Second pass: {ch} at index {i} has count {cnt[ch]}" + (f", so the answer is {i}." if ok else ", so skip it.")))
        if ok: break
    return E(["Brute force: for each char, scan the whole string → O(n²)", "Optimal: count, then scan → O(n)", "Space O(1): alphabet is fixed (26)"],
             "The brute force checks each character against every other, which is quadratic. Counting first and scanning second is linear, and the count table is constant size because the alphabet is fixed.",
             st,
             ["No unique char → −1", "Second pass must follow original order", "Single-character string → 0"],
             "Return minus one if every character repeats, and make sure the second pass follows the original order.",
             ["Follow-up: streaming input → LinkedHashMap / queue"],
             "For a stream of characters, keep a queue of candidates or an ordered map.",
             ["First we count characters in a map. Then we loop over the string again and return the first index whose count is one, or minus one."])

def GenerateDocument():
    chars, doc = "Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"; cnt = {}
    for ch in chars: cnt[ch] = cnt.get(ch, 0) + 1
    st = [S("Worked example", [TX([f'available: "{chars}"', f'document:  "{doc}"'], h=0.6)], "Count the available characters first", "We count every available character, including spaces and punctuation.")]
    for i, ch in enumerate(doc):
        cnt[ch] = cnt.get(ch, 0) - 1
        if cnt[ch] < 0:
            st.append(S("Worked example", [A(list(doc), hl={i: "bad"}, ptr={"i": i}, idx=False), TX([f"'{ch}' needed but count is now {cnt[ch]}"])], f"Out of '{ch}' → false", f"We need {ch}, but none are left. The document can't be generated.")); break
        if i in (0, 4, 9, 15):
            st.append(S("Worked example", [A(list(doc), hl={**{j: "done" for j in range(i)}, i: "ok"}, ptr={"i": i}, idx=False), TX([f"use '{ch}' → {cnt[ch]} left"])], f"Use '{ch}'", f"Use one {ch}; {cnt[ch]} left."))
    else:
        st.append(S("Worked example", [A(list(doc), hl={j: "ok" for j in range(len(doc))}, idx=False)], "Every character was available → true", "Every character of the document was available, so the answer is true."))
    return E(["Brute force: for each doc char, count it in both strings → O(m·(n+m))", "Optimal: one frequency map → O(n + m)", "Fail fast as soon as a count goes negative"],
             "Recounting each character in both strings is quadratic. Counting the available characters once and decrementing for the document is linear, and we can stop as soon as a count goes negative.",
             pick(st, 5),
             ["Case-sensitive; spaces and punctuation count", "Empty document → true", "Unicode beyond ASCII → use a map"],
             "Matching is case-sensitive and spaces count. An empty document can always be generated.",
             ["Ask about character set size", "Follow-up: many documents from one pool"],
             "Ask about the character set. If you need to answer for many documents, reuse the counts.",
             ["We count the available characters in a map, then for each document character decrement its count and return false if it drops below zero."])

def PalindromeCheck():
    s = "abcdcba"; l, r = 0, len(s) - 1; st = []
    while l < r:
        st.append(S("Worked example", [A(list(s), hl={l: "ok", r: "ok", **{k: "done" for k in range(l)}, **{k: "done" for k in range(r + 1, len(s))}}, ptr={"L": l, "R": r})], f"'{s[l]}' = '{s[r]}' → move inward", f"Left {s[l]} matches right {s[r]}, so both pointers move inward."))
        l += 1; r -= 1
    st.append(S("Worked example", [A(list(s), hl={k: "ok" for k in range(len(s))}, ptr={"L": l, "R": r})], "Pointers met → palindrome", "The pointers meet in the middle with no mismatch, so it's a palindrome."))
    return E(["Reverse the string and compare → O(n) time, O(n) space", "Naive concatenation in a loop → O(n²)", "Two pointers → O(n) time, O(1) space"],
             "Reversing and comparing works but needs extra space, and building the reverse with repeated concatenation is quadratic. Two pointers from both ends need no extra space.",
             st,
             ["Empty / single char → true", "Even vs odd length", "Clarify case and non-letters"],
             "Empty and single-character strings are palindromes. Clarify whether to ignore case and punctuation.",
             ["Follow-up: valid palindrome with one deletion", "Longest palindromic substring"],
             "A common follow-up allows deleting one character, or asks for the longest palindromic substring.",
             ["Left starts at zero and right at the end. While left is less than right, mismatching characters return false; otherwise both move inward. Return true."])

def RunLengthEncoding():
    s = "AAAAAAAAAAAABBCCCCDD"; out = ""; run = 1; st = []
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1] or run == 9:
            out += f"{run}{s[i - 1]}"
            st.append(S("Worked example", [A(list(s), hl={i - 1: "cur"}, ptr={"i": min(i, len(s) - 1)}, idx=False), TX([f"flush {run}{s[i - 1]}" + ("  (cap at 9)" if run == 9 and i < len(s) and s[i] == s[i - 1] else ""), f'output = "{out}"'])],
                        f"Flush run → {run}{s[i - 1]}", f"The run of {s[i - 1]} ends" + (" because it hit nine" if run == 9 and i < len(s) and s[i] == s[i - 1] else "") + f", so we write {run} {s[i - 1]}."))
            run = 0
        run += 1
    return E(["Naive: string concatenation in a loop → O(n²)", "Optimal: StringBuilder, single pass → O(n)", "Cap runs at 9 so counts stay one digit"],
             "Concatenating strings in a loop is quadratic in Java. A single pass with a string builder is linear. The twist is capping runs at nine, so the encoded counts are always a single digit and decoding stays unambiguous.",
             st,
             ["Runs longer than 9 split (12 A's → 9A3A)", "Flush the final run after the loop", "Digits in the input"],
             "Twelve A's must become nine A three A, not twelve A. And don't forget to flush the last run after the loop.",
             ["Explain why the cap avoids ambiguity", "Follow-up: write the decoder"],
             "Explain why the cap avoids ambiguity, and be ready to write the decoder.",
             ["We scan from index one, counting the current run. When the character changes or the run reaches nine, we append the count and the previous character, then reset. After the loop we flush the final run."])

def Semordnilap():
    words = ["diaper", "abc", "test", "cba", "repaid"]; seen = set(words); pairs = []; st = []
    for w in words:
        rv = w[::-1]
        if rv in seen and rv != w:
            pairs.append([w, rv]); seen.discard(w); seen.discard(rv)
            st.append(S("Worked example", [A(words, hl={words.index(w): "ok", words.index(rv): "ok"}, idx=False), TX([f"reverse('{w}') = '{rv}' ✓", f"pairs = {pairs}"])], f"'{w}' ↔ '{rv}'", f"The reverse of {w} is {rv}, which is in the set. Record the pair and remove both so it isn't counted twice."))
        elif w in seen:
            st.append(S("Worked example", [A(words, hl={words.index(w): "bad"}, idx=False), TX([f"reverse('{w}') = '{rv}' ✗"])], f"'{rv}' not present", f"The reverse of {w}, {rv}, isn't in the list."))
    return E(["Brute force: compare every pair → O(n²·m)", "Optimal: hash set of words → O(n·m)", "Remove both words once paired"],
             "Comparing every pair of words is quadratic. With a hash set, each word checks for its reverse in constant time, so the whole thing is linear in the total characters.",
             st,
             ["Palindromes like 'aba' don't pair with themselves", "Remove matched words to avoid duplicate pairs", "Order of output pairs"],
             "A palindrome would match itself, so skip that case. Removing matched words prevents duplicate pairs.",
             ["Follow-up: count pairs, or allow duplicates"],
             "Follow-ups include counting pairs or handling duplicate words.",
             ["We put all words in a set. For each word, we reverse it; if the reverse is in the set and differs from the word, we add the pair and remove both words."])
