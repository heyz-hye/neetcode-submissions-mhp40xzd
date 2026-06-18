class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        candidates.sort()
      

        def tree(i,cur,total):
            if total==target:
                self.res.append(list(cur))
                return
            
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if total+candidates[j]>target:
                    break
                
                cur.append(candidates[j])
                tree(j+1,cur,total+candidates[j])
                cur.pop()
        tree(0,[],0)

        return self.res

