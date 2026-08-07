class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]
        subset=[]
        def valid(s)->bool:
            l=0
            r=len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
    
            return True

        def dfs(i):
            if i>=len(s):
                res.append(subset.copy())
                return
            
            for j in range(i,len(s)):
                if valid(s[i:j+1]):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()
            return
        dfs(0)
        return res