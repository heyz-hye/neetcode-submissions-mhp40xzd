'''
PROBLEM: Determine if n nodes + edges form a valid tree
(all nodes connected, no cycles)

===========================================
EDGE CASES / PRE-CHECKS
===========================================
1. A tree has EXACTLY n-1 edges (not "at least 4" — always n-1,
   scales with n). 
   - Too few edges -> guaranteed disconnected
   - Too many edges -> guaranteed cycle
   - if len(edges) != n - 1: return False

2. Special case n == 1: a single node with no edges is a valid
   tree. Must handle BEFORE touching edges[0], since edges[0]
   on an empty list throws IndexError.
   - if n == 1: return len(edges) == 0

===========================================
BUILDING THE GRAPH
===========================================
Edges are undirected, so each pair must be added to the table
in BOTH directions:
   table[u].append(v)
   table[v].append(u)

===========================================
CYCLE DEFINITION
===========================================
An edge creates a cycle if it connects two nodes that are
ALREADY reachable from each other through existing edges.
(Not "same level," not "triangle only" — those are just
special cases of this general rule.)

===========================================
WHY NO SAFE SET NEEDED (undirected + parent-tracking)
===========================================
In a directed graph, you need visit/safe (3-state) because a
"cross edge" to an already-finished node is NOT necessarily a
cycle (only a back-edge to a node still on the current path is).

In an UNDIRECTED graph, once you track parent and skip walking
back along the edge you just came from, this distinction
disappears: any neighbor still in `visit` when you reach it
MUST be a real cycle. So a single `visit` set is enough.

(This is a different reason than connectivity — see below.)

===========================================
WHY len(visit) == n IS STILL NEEDED
===========================================
DFS from one starting node can only prove things about the
component it actually reached. It has no way of knowing there's
more graph it never touched. Example: n=4, edges=[[0,1],[2,3]]
— two separate valid mini-trees. DFS from node 0 finds no cycle
and returns True without ever seeing nodes 2/3.

This is a SEPARATE check from cycle detection:
   - cycle check -> "is there a loop where I did go?"
   - len(visit)==n -> "did I reach everyone?"
Both must pass.

===========================================
DFS LOGIC
===========================================
Call dfs(edges[0][0], -1) — first node, parent = -1 (sentinel,
no real parent).

For each neighbor of node:
   - if neighbor == parent: skip (we just came from there,
     bidirectional edge would falsely look like a cycle otherwise)
   - if neighbor in visit: cycle found -> return False
   - else: recurse

Return True if the whole reachable subgraph explored with no
cycle found.

Final answer = dfs(...) result AND len(visit) == n

===========================================
DEAD CODE CHECK: table.get(node, []) == []
===========================================
This check is UNREACHABLE, and here's the proof:
1. First call: edges[0][0] is guaranteed to have at least one
   neighbor in table (it came from edges[0] itself).
2. Every recursive call: dfs(neighbor, node) only happens if
   neighbor appeared in table[node] — and since the table is
   built bidirectionally, table[neighbor] is guaranteed to
   contain node. So neighbor can never be empty either.

Conclusion: with len(edges) == n-1 enforced AND bidirectional
table-building, no node can ever reach dfs() with an empty
adjacency list. Safe to delete.

===========================================
COMPLEXITY
===========================================
Time:  O(V + E)
   - each node visited once (guarded by visit set) -> O(V)
   - each edge traversed at most twice, once per direction
     in the bidirectional table -> O(E)
   - these are additive (not O(V*E) — we never re-scan all
     edges per node, only each node's own adjacency list once)

Space: O(V + E)
   - table (adjacency list): O(V + E)
   - visit set: O(V)
   - recursion call stack: O(N) depth
   (all three contribute — not just the call stack)

'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit=set()
        table={}
        if n==1:
            return len(edges)==0
        if len(edges)!=n-1:
            return False
        for i in range(len(edges)):
            if edges[i][0] not in table:
                table[edges[i][0]]=[edges[i][1]]
            else:
                table[edges[i][0]].append(edges[i][1])
            if edges[i][1] not in table:
                table[edges[i][1]]=[edges[i][0]]
            else:
                table[edges[i][1]].append(edges[i][0])
        
        def dfs(node, parent)->bool:
            if node in visit:
                return False
            
            visit.add(node)
            for neighbors in table[node]:
                if neighbors==parent:
                    continue
                if not dfs(neighbors,node):
                    return False
            return True

        if dfs(edges[0][0],-1) and len(visit)==n:
            return True
        else:
            return False



        
         

        
        