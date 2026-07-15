'''
Problem: find the edge that introduces a cycle into this graph. If multiple
edges would each individually complete a cycle, return the one that appears
last in the input list.

First approach (buggy): build an adjacency table from all edges, then DFS
from a starting node. Whenever DFS revisits an already-visited node, append
[parent, node] to a results list. Problem: this has no way to stop the moment
a cycle is confirmed, and since the whole graph (already containing the
cycle) is built before searching, DFS can report back-edges that aren't
necessarily the actual last redundant edge in input order -- it depends on
traversal order, not list order. Needed a different algorithm.

Union-Find approach:
Process edges one at a time, in input order. For each edge (u, v), find the
root ("ultimate ancestor") of u and of v.
  - If they have different roots, u and v aren't connected yet -- this edge
    is a legitimate tree edge. Union them by pointing one root at the other.
  - If they already share the same root, u and v were already connected
    *before* this edge was added -- so this edge is the one that creates the
    cycle. Return it immediately.
Because we scan in input order and return on the first cycle-closing edge we
find, this is automatically the *last* redundant edge overall (any earlier
edge that also happened to close a cycle would already have been returned
before we got here) -- no need for a second, reverse pass like the DFS
approach attempted.

time complexity:
- First loop (initialize parent[node] = node for every node): O(n).
- Second loop: n edges, and each does up to 2 calls to find(). find() walks
  up parent pointers to the root, costing O(h) where h is the current height
  of that node's tree. Since this implementation has no path compression
  (find() recomputes the root each call but never shortcuts it), h can grow
  to O(n) in the worst case (e.g. edges chain nodes into one long line
  before merging), making a single find() call O(n) and the whole loop
  O(n^2) worst case.
  Improvement: add path compression --
      parent[x] = find(parent[x])   (store the result, don't just return it)
  This flattens the tree as you go, so future find() calls on the same
  branch become close to O(1), bringing total time down to nearly O(n) in
  practice (technically O(n * alpha(n)) with union-by-rank too, where
  alpha is the inverse Ackermann function -- effectively constant).

space complexity:
table store O(n) and the call stack of find function is also at worst(O(N))

'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent={}
        def find(x)->int:
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        for u, v in edges:
            parent[u]=u
            parent[v]=v
        
        for u,v in edges:
            if find(u)!=find(v):
                parent[find(v)]=find(u)
            else:
                return [u,v]



            

        