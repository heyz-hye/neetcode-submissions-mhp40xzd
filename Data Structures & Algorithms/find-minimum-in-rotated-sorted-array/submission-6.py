'''
LC 153: Find Minimum in Rotated Sorted Array

Key idea: a rotated sorted array is two increasing runs glued together
(e.g. [4,5,6,1,2,3] = [4,5,6] then [1,2,3]). The minimum is the single
point where the array "drops" -- the start of the second run.

Binary search on nums[mid] vs nums[right]:
- if nums[mid] > nums[right]:
    the drop point is somewhere in mid+1..right (mid is still in the
    first/left run, so the minimum can't be at or before mid)
    -> left = mid + 1
- else (nums[mid] <= nums[right]):
    mid is already in the second/right run (or the array isn't rotated
    at all), so mid itself could be the minimum
    -> right = mid  (keep mid in the search space)

Loop while left < right (not <=) since we never want left/right to
cross without converging -- when left == right, that index IS the
minimum, so we stop and return nums[left].

Time: O(log n), Space: O(1)
If nums[mid] <= nums[right]: the rotation point has already happened at or before mid — 
everything from mid to right is one clean ascending stretch with no drop in it. 

So the minimum is at mid or earlier.
If nums[mid] > nums[right]: the rotation point hasn't happened yet — it's still somewhere ahead of mid, 
between mid+1 and right. So the minimum is strictly after mid.

'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        

        while left<right:
            mid=(left+right)//2

            if nums[right]<nums[mid]:
                left=mid+1

            else:
                right=mid
                

        return nums[left]
        