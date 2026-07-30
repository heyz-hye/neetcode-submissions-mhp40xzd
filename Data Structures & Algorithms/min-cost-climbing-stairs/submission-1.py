'''
take nothing to be at stair 0,1 but you still have to pay the cost at that index to move up
you need to be at the index by the last index

we can take a going up stategy and start from index 0 or 1 we can see which jump we can take to get the minimal cost
if we went past or arrive at the top we return 0 because they is no point for us to go further hence we don't pay the cost
at that index
'''

from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        @lru_cache(maxsize=None)
        def goingup(i):
            if i>=n:
                return 0
            
            return cost[i]+min(goingup(i+1),goingup(i+2))

        return min(goingup(0),goingup(1))

        