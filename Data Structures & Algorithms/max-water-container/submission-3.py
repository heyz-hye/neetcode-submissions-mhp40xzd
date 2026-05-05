class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maximum=[]


        while left <right:
            if heights[left]<heights[right]:
                h=heights[left]
            else:
                h=heights[right]

            w=right-left

            area=h*w

            if heights[left]<heights[right]:
                left+=1

            else:
                right-=1
    
            maximum.append(area)
        
        return max(maximum)
        