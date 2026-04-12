class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}

        for i, value in enumerate(nums):
            complement=target-value
            if complement in seen:
                return [seen[complement], i]

            seen[value]=i
