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
        
        for ind,hei in stack: # you cannot do enumerate stack in this case because what you are essentially saying is give me the stack's index and the value inside the stack
            maxarea=max(maxarea,(len(heights)-ind) * hei) #list itself (hei) in this case already contains index and height for that stack layer
                                                         #you are multiplying a list with an int and then compare int with the list is bad.
                                                         #also wrong calculation for ind because index of stack vs index of the heights store in the stack is not the same
        
        return maxarea


       
        