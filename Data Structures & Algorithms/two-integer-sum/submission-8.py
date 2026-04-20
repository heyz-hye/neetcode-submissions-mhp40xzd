class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for index, x in enumerate(nums):
            complement=target-x

            if complement in seen:
                return [seen[complement],index]

            seen[x]=index

