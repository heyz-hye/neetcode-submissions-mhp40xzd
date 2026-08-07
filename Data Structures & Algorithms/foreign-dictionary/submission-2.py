class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for word in words for c in word}
        res=[]

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minlength=min(len(w1),len(w2))

            if len(w1)>len(w2) and w1[:minlength]==w2[:minlength]:
                return ""
            for e in range(minlength):
                if w1[e]!=w2[e]:
                    adj[w1[e]].add(w2[e])
                    break
        path=set()
        visited=set()
        def dfs(c)->bool:
            if c in path:
                return False
            if c in visited:
                return True
            path.add(c)
            for neigh in adj[c]:
                if not dfs(neigh):
                    return False
            res.append(c)
            path.remove(c)
            visited.add(c) #only when all the possibility of going from that node is fully explore then we add to the visited and res.
            return True
        for c in adj:
            if not dfs(c):
                return ""
    
        return "".join(res[::-1])
            

        