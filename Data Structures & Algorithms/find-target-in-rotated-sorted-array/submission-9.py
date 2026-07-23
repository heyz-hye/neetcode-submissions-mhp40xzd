'''
There are 2 branches (left sorted / right sorted), decided by comparing nums[mid] vs nums[l].
Edge case: when nums[mid] == nums[l] (happens when the window has shrunk to 1 or 2 elements, so mid == l), 
the left side is trivially sorted — must use >= not >, or you'll misroute into the wrong half and lose the target.
Mistake I made: used > instead of >=, which fails exactly on these small-window edge cases (e.g. [3,1], target=1).

When l == mid, the "left half" is just the single element nums[l] itself (a subarray of length 1). A single element is trivially sorted — there's nothing to be out of order with. So logically it belongs in the "left half is sorted" branch.

The problem is only how you detect which branch to go into. You're using nums[mid] vs nums[l] as a proxy for "is the left half sorted?" 
But when l == mid, that comparison becomes nums[mid] vs itself — 
always equal, never >. So a strict > check will always kick this case into the else (right-sorted) branch, which is wrong, 
since it's not that the right half is sorted for any real reason — you just failed to detect the left half's (trivial) sortedness.

since you have a middle index to see which side is sorted,
from the perspective of the left index(if it happen to middle at the same time),
one index is still sorted itself
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid=(l+r)//2

            if nums[mid]==target:
                return mid

            if nums[mid]>=nums[l]: #
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                
                else:
                    l=mid+1
            
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                
                else:
                    r=mid-1

        return -1
        