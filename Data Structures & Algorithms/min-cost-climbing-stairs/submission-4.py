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

O(1)sapce solution

At index n-2: there's only one way off that step — jump to the top (i+1, which is n-1, cost 0). No i+2 option exists (out of bounds). 
So the total cost to finish from there is forced to be just cost[n-2] + 0 = cost[n-2]. Nothing to compare, nothing to update.
At index n-3: now you genuinely have two options —
take an i+1 jump: land on n-2, then pay whatever it costs from there → cost[n-3] + cost[n-2]
take an i+2 jump: land on n-1 (the top), skipping n-2 entirely → cost[n-3] + cost[n-1]
These two paths can differ, so you take the min of them. That's the first spot in the array (scanning backward) where a real decision exists.

So your instinct is correct: the reason n-2 needs no update isn't about a preference between i+1/i+2 — it's that i+2 isn't even a legal move from there. 
n-3 is the first index where both moves are legal and can lead to different total costs, which is why that's where the backward loop starts making comparisons.
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n=len(cost)

        for i in range(n-3,-1,-1):
            cost[i]=min(cost[i]+cost[i+1],cost[i]+cost[i+2])
        
        return min(cost[1],cost[0])

        