class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles) #fastest rate you can eat
        l=1

        
        res=m

     
        while l<=m:
            mid=(l+m)//2

            hour=0
            for i in piles:
                hour+=math.ceil(i/mid) # can i eat slower while still achieveing the hours
            
            if hour<=h:
                res=min(res,mid) #update if the hour spent is less than hour require, compare mid
                m=mid-1
            
            else:
                l=mid+1
        
        return res
        