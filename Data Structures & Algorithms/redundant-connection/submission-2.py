class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent={}
        def find(x)->int:
            if parent[x]!=x:
                return find(parent[x])
            else:
                return x
        
        for u,v in edges:
            parent[u]=u
            parent[v]=v
        
        for u,v in edges:
            if find(u)!=find(v):
                parent[find(u)]=find(v)
            else:
                return [u,v]

            

        