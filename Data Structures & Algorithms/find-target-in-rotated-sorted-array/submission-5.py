class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid

            if nums[mid]>=nums[left]:
                if nums[left]<=target<nums[mid]: # there are cases where the target is at the exact left of the divided array
                    right=mid-1 #what we are saying essentially is that if the target is to the left of this mid include left endpoint itself but no mid, we bring right to mid -1
                else:
                    left=mid+1

            else:
                if nums[right]>=target>nums[mid]: # there are cases where the target is is at the exact right of the array
                    left=mid+1 #same as above if target is in right portion of mid which include the right endpoint exclude the left we go left=mid+1

                else:
                    right=mid-1

        return -1
        