'''
This solution uses the Prefix and Suffix Product approach. The core idea is that the product of an array except for self at any given index i is simply the product of all numbers to the left of i multiplied by the product of all numbers to the right of i.

By pre-calculating these left and right products into separate arrays, we can avoid using division (which is usually a strict constraint for this problem) and solve it efficiently in linear time.

    Time Complexity: O(N) because we iterate through the array three separate times (which simplifies to O(N)).

    Space Complexity: O(N) because we create two additional arrays (left and right) of size N to store our intermediate products.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        l=1
        r=1
        ans=[]

        for i in range(len(nums)):
            if i==0:
                left.append(1)
                continue
            l=l*nums[i-1]
            left.append(l)
        
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right.append(1)
                continue
            r=r*nums[i+1]
            right.append(r)

        for i in range(len(nums)):
            product=left[i]*right[len(nums)-1-i]
            ans.append(product)
        
        return ans