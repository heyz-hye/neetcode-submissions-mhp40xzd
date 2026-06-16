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

why dont we append before i+1 recursive call
self.subset.append(nums[i + 1]) # ❌ Don't do this
dfs(i + 1, total + nums[i + 1])
Let's look at a concrete example. Suppose nums = [2, 3] and target = 3.

    Start at dfs(0, 0): You are looking at nums[0] (which is 2).

    Left Branch (Choice 1): You append 2. Your subset is [2]. You call dfs(0, 2).

    Right Branch (Choice 2): You decide not to take 2. Your subset stays empty []. You call dfs(1, 0) to move on and see what you can make using only the number 3.

If you had appended 3 before going to the right branch, your subset would have become [3], and you would have completely missed the branch where the subset is empty [].


2. The Broken Approach (Forcing nums[i + 1] on the Right)

Now, let's look at what happens to the tree if you force-append the next number before calling dfs(i + 1):
Python

# The Broken Logic:
self.subset.append(nums[i + 1]) 
dfs(i + 1, total + nums[i + 1])

Look at the right branch now:

    The Trapped State: By forcing nums[1] (which is 3) into the subset immediately, your subset becomes [3].

    The Missing Path: You have completely deleted the possibility of the subset being empty [] at index 1.

Why this causes a crash (IndexOutOfBounds):

Look closely at the bottom-right of the broken tree. When the code is at index 1, it tries to look ahead to i + 1 (which is 1 + 1 = 2).
It evaluates nums[i + 1], which translates to nums[2]. Since our list only has indexes 0 and 1, Python immediately crashes with an IndexError: list index out of range.
Summary

The two branches must represent a pure binary decision:

    Left: "Give me the current number." (append → dfs(i))

    Right: "I don't want the current number, show me what the world looks like without it." (dfs(i + 1) with no append).

If you append on the right branch, you are forcing the algorithm to take a number it might want to skip, while simultaneously peeking into an index that might not even exist yet!
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
        