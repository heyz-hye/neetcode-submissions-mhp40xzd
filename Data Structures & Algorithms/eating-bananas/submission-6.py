class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        res=right


        while left<=right:
            midrate=(left+right)//2
            hour =0

            for i in piles:
                hour+=math.ceil(i/(midrate))

            if hour<=h:
                res=min(res,midrate)
                right=midrate-1

            else:
                left=midrate+1
        return res