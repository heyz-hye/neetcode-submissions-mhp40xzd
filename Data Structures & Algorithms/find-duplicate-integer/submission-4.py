'''
fast and slow always start at the same position. since the elements are between 1-5 there is no way
that the first index gets referenced. This is crucial.
When fast and slow pointer intersect they are the same distance away from the duplicate than the first index
first index is p distance away from duplicate and the intersect position is x distance way from the duplicate
proof: 2(p+c-x)=p+2c-x  this turn out to p=x
so we start another slow at the beginning after we find the intersect, we keep going moving on until the 2 slow pointer and the intersect meet.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0

        while True:
            slow=nums[slow]  #this move slow pointer forward
            fast=nums[nums[fast]] #fast move twice as fast

            if fast==slow: #they interesect
                break
        
        slow2=0
        
        while True:
            slow2=nums[slow2]
            slow=nums[slow]

            if slow2==slow:
                break

        return slow #return the index of the duplicate


        