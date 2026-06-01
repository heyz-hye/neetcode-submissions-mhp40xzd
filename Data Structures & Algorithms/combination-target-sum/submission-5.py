'''
when we do backtracking we gotta know our stop condition and our forward conditions
our stop condition should be:
1.when the sum of the cur list is greater than the nums
2.when the i index of the list we move is out of bound
3.also when the sum of our cur list that we are constantly modifying found its target 
3.5: when we found the solution we want to copy a copy of cur list because list is pass
by reference, and since we are always modifying it we dont want our answer to constantly change.
Note:also by the end of the dfs algorithm every element in the list should be popped because we visited
every possible combination iteration of nums already.
when we hit our first two stop condition we just simply return

we going for a depth first search approach as the we keep add the current index i until 
it hits our stop statements.
if the current index doesnt work we return and pop it from our list and move i forward.
by moving i forward we can effectively avoid duplicates in our solution.


'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i>=len(nums) or total>target:
                return
            
            cur.append(nums[i]) #we keep adding the same index until it doesnt work
            total=total+nums[i]
            dfs(i,cur,total)
            cur.pop() #when we return our index doesnt work so we pop it
            total=total-nums[i] # when you pop your total should also decrement
            dfs(i+1,cur,total) #increment our index by one to avoid duplicates and to go down the list


        dfs(0,[],0) # we start with index 0 and total being zero
        return res

        