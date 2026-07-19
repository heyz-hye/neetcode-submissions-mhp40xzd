'''
This doesn't do what you think. [] * len(nums) is just [] (multiplying an empty list by n is still empty), 
so this whole line evaluates to [[]] — a list containing one empty list. You need:
pythonfrequency = [[] for _ in range(len(nums) + 1)]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        frequency=[[] for i in range(len(nums)+1)]
        res=[]
    
        for val,freq in count.items():
            frequency[freq].append(val)
        
        count=0
        for i in range(len(frequency)-1,-1,-1):
            if count==k:
                return res
            for e in frequency[i]:
                res.append(e)
                count+=1

            
        