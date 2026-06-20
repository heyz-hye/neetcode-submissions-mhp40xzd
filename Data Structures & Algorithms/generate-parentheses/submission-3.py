class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        if n<1:
            return res
        
        def dfs(subset,counto,countc):
            if counto==n and countc==n:
                res.append(''.join(subset))
                return

            if counto>countc:
                subset.append(')')
                dfs(subset,counto,countc+1)
                subset.pop()

            if counto<n:
                subset.append('(')
                dfs(subset,counto+1,countc)
                subset.pop()

            
        dfs([],0,0)
        return res