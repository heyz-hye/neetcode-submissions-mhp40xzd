class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.subset=[]
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                self.res.append(self.subset.copy())
                return
            self.subset.append(nums[i])
            dfs(i+1)
            self.subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return self.res