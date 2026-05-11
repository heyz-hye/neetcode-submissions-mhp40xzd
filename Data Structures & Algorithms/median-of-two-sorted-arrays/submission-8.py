'''
merge the two sorted array and find median
but runtime will be O(m+n)

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i=0
        j=0
        n=len(nums1)
        m=len(nums2)
        cur=0
        prev=0

        for k in range(((n+m)//2)+1):
            prev=cur

            if i<n and(j>=m or nums1[i]<nums2[j]):
                cur=nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1

        if (n+m)%2==1:
            return float(cur)

        else:
            return (prev+cur)/2.0
        
        