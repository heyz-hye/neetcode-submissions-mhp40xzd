class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Loop through every number
        for i in range(len(nums)):
            # Loop through every number AFTER the current one
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]