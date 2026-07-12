'''
this problem is similar to valid tree graph except we don't care if the graph is a tree
we want the number of components

edge case: if the edge is empty list then we just return n since there is no edges

dfs function logic:
if we encounter a node in visit we just return because it creates infinite recursion/loop
if the neighbors equal to the parent we continue
this stops you from immediately walking back the edge you just came from
once all the neighbors have been explore and added to the visit set we just return

visit set can never reach the keys that doesn't exist in the table by looping through the keys in the table
we need to figure out how many are isolated. we subtract the n by the length of the table to see how 
many isolated keys we have. Then we set up our while condition 
where the length of the visit set plus number of isolated must equal to n
then we loop through each keys in the table and call dfs on it if it doesn't exist in the visit set yet
every time we call we form one component by default. whatever remainings not in the visit set dictates
the minimum number of time we still need to call dfs to traverse.

time complexity:
each node is visited once (O(V)), 
and since the graph is undirected each edge appears twice in table and gets checked twice across all dfs calls, 
so total work is O(V+E)

space complexity:
O(v) for number of nodes in visits 
O(v) for the depth of the call stack since there can be only n nodes long if every node is connected
since stack depth is bounded by the number of nodes in the longest path of a single component, 
not edge count. Also worth noting table itself is O(V+E) space (n keys worst case, 
2 times edges total entries across adjacency lists), not just O(n).
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit=set()
        count=0
        table=defaultdict(list) #assumes empty list for key that doesn't exist
        if len(edges)==0:
            return n
        for u,v in edges:
            table[u].append(v)
            table[v].append(u)

        def dfs(node,parent):
            if node in visit:
                return
            visit.add(node)

            for neighbors in table[node]:
                if neighbors==parent:
                    continue
                dfs(neighbors,node)
            return
        isolated=n-len(table)
        while len(visit)+isolated!=n:
            for key in table:
                if key not in visit:
                    dfs(key,-1)
                    count+=1
        return count+isolated



        