'''
can use a dfs approach every time you move see an element you 

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        self.subset=[]
        def dfs(i):
            if i>=len(nums):
                self.ans.append(self.subset.copy())
                return
            self.subset.append(nums[i])
            dfs(i+1)
            self.subset.pop()
            dfs(i+1)
        dfs(0)
        return self.ans




        

        