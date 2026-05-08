#max function doesnt support tuple and it return error for list that is empty

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0

        for i, h in enumerate(heights):
            start=i

            while stack and h<stack[-1][1]:
                index, height=stack.pop()
                max_area=max(max_area, height*(i-index))
                start=index
            stack.append((start,h))
        #however you can enumerate a tuple in a stack
        for i,h in (stack):
            max_area=max(max_area, h*(len(heights)-i))


        return max_area

        #enumerate a stack create another indexing of the stack [index,height] cant compare int and tuple
        