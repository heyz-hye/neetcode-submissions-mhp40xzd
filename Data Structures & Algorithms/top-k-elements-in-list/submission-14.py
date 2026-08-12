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
if you initiate an empty list inside a list fill with None like this [[None]*len(array)] you will get list within list that have length of 1 because it has None in it
also you cannot do [[]*len(nums)+1], python think it is string concatenation so nono you can only do [[] for e in range(len(nums)+1] also because a number can have frequency of 0
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        freq=[[] for e in range(len(nums)+1)]
        c=0
        res=[]
        
        for val,f in count.items():
            freq[f].append(val)
        

        for i in range(len(freq)-1,-1,-1):
            for val in freq[i]:
                res.append(val)
                c+=1
                if c==k:
                    return res


            


        
            
        