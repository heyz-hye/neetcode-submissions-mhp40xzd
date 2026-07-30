class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool: #make sure all node is connected no loop and also reach every node, two separate tree is bad
        self.table=defaultdict(list)
        visit=set()

        if n==1:
            return len(edges)==0 #node is valid even if it is one, one node 0 edges
        
        if len(edges)+1!=n: #mistake here just because there is n-1 edges for n node doesnt mean it is a valid there can still be a loop
            return False
        
        for u,v in edges:
            self.table[u].append(v) #if key dont exist default dict automatically create initiate a key:val for us
            self.table[v].append(u)
        
        def dfs(node,parent)->bool:
            if node in visit:
                return False
            visit.add(node)
            for neigh in self.table[node]:
                if neigh==parent:
                    continue
                if not dfs(neigh,node): #circuit break to exit the if there is a loop exisitng in one of the path
                    return False
            return True #if no loop exist within the neighbor's path return True

        return dfs(0,-1) and len(visit)==n
                

        
        
        