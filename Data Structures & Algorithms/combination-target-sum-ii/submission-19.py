class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,cur,total):
            if total==target:
                res.append(list(cur))
                return

            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]+total>target:
                    break
                cur.append(candidates[j])
                dfs(j+1,cur,total+candidates[j])
                cur.pop() #this pop micmic the descision tree of chosing it and not it at the same time
        dfs(0,[],0)
        return res

        