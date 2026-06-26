class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table={"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res=[]
        def dfs(i, subset):
            if len(subset)==len(digits):
                res.append("".join(subset))
                return
            
            for c in table[digits[i]]:
                subset.append(c)
                dfs(i+1,subset)
                subset.pop()
        if digits:
            dfs(0,[])

        return res
        
