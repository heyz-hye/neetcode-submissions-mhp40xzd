'''
This doesn't do what you think. [] * len(nums) is just [] (multiplying an empty list by n is still empty), 
so this whole line evaluates to [[]] — a list containing one empty list. You need:
pythonfrequency = [[] for _ in range(len(nums) + 1)]

The core lesson: when you're accumulating toward a target count across a nested loop, 
check the stopping condition at the innermost point where the count actually changes — not one level up. 
Checking it between buckets assumed the count would increase by exactly 1 each time you could check, 
but a bucket can hold multiple elements, so the count can skip right past your target.

 # MISTAKE (fixed): originally checked `if count==k` only BETWEEN
                    # buckets (before entering inner loop), not after each individual append.
                    # If a bucket had multiple elements, appending all of them could jump
                    # count past k in one shot, so `count==k` would never be true again ->  
                    # the function keep looping but the conditions never become true since no matter how you increment count it is already blow past k (bigger than k)
                    # loops finish, function falls through with no return -> returns None. even though res has valid results
                    # Fix: check len(res)==k right after EVERY append, so we return the exact
                    # moment res reaches size k, even mid-bucket.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        frequency=[[] for i in range(len(nums)+1)]
        res=[]
    
        for val,freq in count.items():
            frequency[freq].append(val)
        
     
        for i in range(len(frequency)-1,-1,-1):
            for e in frequency[i]:
                res.append(e)
                if len(res)==k:
                    return res

            
        