'''
this problem is similar to valid tree graph except we don't care if the graph is a tree
we want the number of componenets

dfs function logic:
if we encounter a cycle we just return,
if the neighbors equal to the parent we continue
once all the neighbors have been explore and added to the visit set we just return
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



        