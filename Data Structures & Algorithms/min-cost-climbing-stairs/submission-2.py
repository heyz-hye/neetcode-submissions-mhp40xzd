'''
You can start standing on step 0 or step 1 for free — you only pay cost[i]
when you leave step i to climb further.

Goal: reach index n (one past the last step). So the base case is i >= n,
not i == n-1, because landing on OR going past the last step both mean
you're done climbing and owe nothing more.

We take a "going up" recursive strategy: from step i, the cheapest way to
finish is cost[i] plus whichever of the next two jumps (i+1 or i+2) is cheaper.
We memoize since goingup(i) only needs to be computed once per index.

Time: O(n) — each index computed once.
Space: O(n) — memo table size + max recursion/call stack depth.
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

        