class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # val : index
        
        for i, val in enumerate(nums):
            complement = target - val
            
            if complement in seen:
                return [seen[complement], i]
            
            # Store the current number so we can find it later
            seen[val] = i