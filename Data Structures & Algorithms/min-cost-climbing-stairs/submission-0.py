from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        cost.append(0)
        @lru_cache(maxsize=None)
        def goingup(i):
            if i>=n:
                return 0
            
            return cost[i]+min(goingup(i+1),goingup(i+2))

        return min(goingup(0),goingup(1))

        