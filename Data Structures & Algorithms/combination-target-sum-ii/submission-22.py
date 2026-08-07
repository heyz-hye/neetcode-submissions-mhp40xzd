class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        

        def dfs(i,total,part):
            if total==target:
                res.append(part.copy())
                return
            if i>=len(candidates):
                return
            
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                elif total+candidates[j]>target:
                    break
                
                part.append(candidates[j])
                dfs(j+1,total+candidates[j],part)
                part.pop()
        
        dfs(0,0,[])
        return res


        