class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        stack=[]

        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                maxarea=max(maxarea,(i-index)*height)
                start=index
            stack.append([start,h])

        for t in range(len(stack)):
            index,height=stack.pop()
            maxarea=max(maxarea,(len(heights)-index)*height)
        
        return maxarea

       
        