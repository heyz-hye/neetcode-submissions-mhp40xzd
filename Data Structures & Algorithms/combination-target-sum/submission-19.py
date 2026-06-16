'''
we will use a dfs in this case, since we can repeat the same any amount of times unless it is greater than the sum we can just keep calling the same
number, if it is greater than the target we can return and choose another path increment the index, finally after the first index primary call has
being exhausted we move up to the second index which exclude the current index completely so we get unique combinations.

our base case should be if index i is out of bound we return or if our target is lower than the sum of subsets. we should also return when we find 
a valid solution or else it will drastically slow down your code because even though your second base condtion guard against index out of bound or 
target out of bound you create an extra recursive call by not returning so it waste time recursively calling. if the target is equal equal to the
sum of subarray any elements added to it will immediatly make greater than the target unless it is zero.

sum(self.subset) is O(N) runtime this slow down our code, so we should be passing sum along the function call so we  don't calculate it every time

When you pass total into a function call, Python creates a brand new, isolated copy of that variable for that specific step of the recursion.

'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.subset=[]
        def dfs(i,total):
            
            if total==target:
                self.res.append(self.subset.copy())
                return
            
            if total>target or i>=len(nums):
                return
            
            self.subset.append(nums[i])
          
            dfs(i,total+nums[i]) #we can pass total within every function call scope, because of that when we pop an element we dont have to worry about
                                #decrementing nums[i] from the total, # <-- We pass a LARGER total to the NEXT call
            self.subset.pop()
            dfs(i+1,total) #pass in total here because we have append the number into our subset yet, if we add without append it will mess up calculation
                            ## <-- The original 'total' here is completely untouched!
        dfs(0,0)
        return self.res
        