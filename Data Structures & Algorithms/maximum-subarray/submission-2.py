'''
I want to the maximum sum of subarray. I know that by add a number I can increase the sum or decrease, now along the way I will encounter
positive numbers and negative numbers. But I know that if the sum I have by adding through the for loop is negative it is definitely not helpful to me sum
so if it is negative or less than 0 I want to reset my partial sum to zero and add the current number in the for loop. The sum of the number 
will be compare through the for loop every time we encounter a number.
We choose the first index of the subarray as a placeholder so it can be compare throughout the for loop

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsubarray=nums[0]
        partial_sum=0

        for i in nums:
            if partial_sum < 0:
                partial_sum=0 #reset this because the sum is not contributing to our overall max sum
            
            partial_sum=partial_sum+i
            maxsubarray=max(maxsubarray,partial_sum)

        return maxsubarray