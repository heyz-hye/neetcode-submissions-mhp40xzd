'''
edge case:
in order to have all nodes connected, you need atleast 4 edges and a tree have exactly n-1 edges
we don't need a safe set because to be a tree that have undirected edges one node
must able to traverse to all the other node

doubly directional, if a traingle exist that mean a loop

an edge creates a cycle if it connects two nodes that are already reachable from each other through existing edges.

if an node have no neighbor it is disconnected




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
            if table.get(node,[])==[]:
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



        
         

        
        