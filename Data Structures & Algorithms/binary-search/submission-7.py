class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1

        while low<=high:
            midpoint=(low+high)//2
            if nums[midpoint]==target:
                return midpoint

            if target>nums[midpoint]:
                low=midpoint+1
            else:
                high=midpoint-1

        return -1
        