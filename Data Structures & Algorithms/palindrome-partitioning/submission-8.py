class Solution:
    def validpalindrome(self,s):
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1

            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res=[]

        def dfs(i,part):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.validpalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1,part)
                    part.pop()
        dfs(0,[])
        return res
        
        