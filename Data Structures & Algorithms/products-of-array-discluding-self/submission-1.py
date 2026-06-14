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