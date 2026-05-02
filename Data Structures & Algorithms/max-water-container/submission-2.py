class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        left=0
        right=len(heights)-1
        while left<right:
            if heights[left]<heights[right]:
                h=heights[left]
            else:
                h=heights[right]

            w=right-left
            
            area=w*h

            if max<area:
                max=area
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1

        return max


            
             

            
        