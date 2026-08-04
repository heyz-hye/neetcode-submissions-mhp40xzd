'''
# ============================================================================
# LeetCode 269 - Alien / Foreign Dictionary
# Pattern: Graph construction + Topological Sort (DFS, 3-state cycle detection)
# ============================================================================
#
# ---------------------------------------------------------------------------
# APPROACH
# ---------------------------------------------------------------------------
# 1. Every unique char is a NODE. Build adj = {char: set()} for ALL chars
#    up front (comprehension over every word) so isolated letters still
#    appear in the output.
# 2. Edges come ONLY from comparing ADJACENT words. For each pair (w1, w2),
#    walk until the FIRST differing char -> that gives edge w1[j] -> w2[j],
#    then BREAK. Everything after the first mismatch is unconstrained.
# 3. Prefix conflict: if w1 is longer than w2 AND w2 is a prefix of w1
#    (e.g. ["abc","ab"]) -> invalid, return "".
# 4. Topological sort via DFS. Use 3-state visit map:
#       c not in visit -> unseen
#       visit[c] == False -> on current path (GRAY)  -> cycle if revisited
#       visit[c] == True  -> fully done (BLACK)
#    Post-order append, then reverse = topo order.
#
# ---------------------------------------------------------------------------
# MISTAKES I MADE (watch for these)
# ---------------------------------------------------------------------------
# [1] CORE MISCONCEPTION: order of letters INSIDE one word means nothing.
#     "wrt" does NOT imply w < r < t. All ordering info comes from comparing
#     adjacent words. -> Deleted my entire "intra-word" first loop.
#
# [2] defaultdict(str) CANNOT hold a graph. A node points to MANY successors,
#     but table[a] = b overwrites. -> Must use defaultdict(set) / dict of sets.
#     (This is my recurring bug: defaultdict(str) instead of defaultdict(set).)
#
# [3] continue vs break: after finding the first differing char I must BREAK,
#     not continue. Continuing adds fake edges from later positions.
#     (Also a recurring one: missing break after first differing character.)
#
# [4] IndexError: comparing words[e][i] vs words[e+1][i] blows up when the
#     words differ in length. Only loop up to min(len(w1), len(w2)).
#
# [5] Prefix check was wrong: `set(w2) in set(w1)` is NOT a subset test and
#     sets discard position anyway. Correct: len(w1) > len(w2) and prefix match.
#
# [6] DFS started from only ONE node (words[0][0]) -> misses isolated letters
#     and other components. Must DFS from EVERY node in adj.
#     (Recurring: DFS starting from only one node rather than all nodes.)
#
# [7] Cycle detection needs 3 states. A plain visit SET cannot distinguish
#     "still on the current path" from "already finished" -> can't catch a->b->a.
#
# [8] Output format: LC 269 wants letters concatenated, "".join(...) NOT
#     " ".join(...).
#
# [9] Typos that crash: `word[e+1]` (NameError, should be words) and
#     `range(len(words[i]))` where i was still bound to the last word string.
#
# ---------------------------------------------------------------------------
# COMPLEXITY
# ---------------------------------------------------------------------------
# Let C = total number of characters across all words,
#     U = number of unique characters (<= 26),
#     E = number of edges (<= U^2, i.e. <= 26^2).
#
# Time:  O(C) to build the graph (scan every char once) + O(U + E) for the
#        DFS topological sort. Since U, E are bounded by the alphabet (<=26,
#        <=26^2 = constant), this is effectively O(C).  -> O(C)
# Space: O(U + E) for the adjacency map, visit map, and recursion stack,
#        bounded by the alphabet size -> effectively O(1) w.r.t. alphabet,
#        or O(U + E) in general terms.
# ============================================================================
'''


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for word in words for c in word}


        if not words:
            return ""
        
        
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minlength=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlength]==w2[:minlength]:
                return ""
            
            for j in range(minlength):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                
            
        visited = set()
        path = set()
        res = []

        def dfs(c)->bool:
            if c in visited:
                return True
            if c in path:
                return False
            path.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            path.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""

        return "".join(res[::-1])


        
        
        