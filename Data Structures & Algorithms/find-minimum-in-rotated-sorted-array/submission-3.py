'''
can use a for loop if previous less than current we continue to traverse, if that pattern holds return index 0
else as current element is less than previous element return current

use bst
set left=0
right=len(nums)-1

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1

        while left<right:
            if nums[left]>nums[right]:
                left+=1

            else:
                right-=1

        return nums[left]
        