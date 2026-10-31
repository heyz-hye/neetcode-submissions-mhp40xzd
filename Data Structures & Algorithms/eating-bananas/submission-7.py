class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m=max(piles)
        l=1

        
        res=m

     
        while l<=m:
            mid=(l+m)//2

            hour=0
            for i in piles:
                hour+=math.ceil(i/mid)
            
            if hour<=h:
                res=min(res,mid)
                m=mid-1
            
            else:
                l=mid+1
        
        return res
        