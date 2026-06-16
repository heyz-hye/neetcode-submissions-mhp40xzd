'''
we will use a dfs in this case, since we can repeat the same any amount of times unless it is greater than the sum we can just keep calling the same
number, if it is greater than the target we can return and choose another path increment the index, finally after the first index primary call has
being exhausted we move up to the second index which exclude the current index completely so we get unique combinations.

'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.subset=[]
        def dfs(i):
            
            if sum(self.subset)==target:
                self.res.append(self.subset.copy())
                return
            
            if sum(self.subset)>target or i>=len(nums):
                return
            
            self.subset.append(nums[i])
            dfs(i)
            self.subset.pop()
            dfs(i+1)

        dfs(0)
        return self.res
        