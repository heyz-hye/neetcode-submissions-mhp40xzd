#max function doesnt support tuple and it return error for list that is empty

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0

        for i, h in enumerate(heights):
            start=i
#backward calculate popping bar from the back once encounter a shorter bar
            while stack and h<stack[-1][1]:
                index, height=stack.pop()
                max_area=max(max_area, height*(i-index))
                start=index
            stack.append((start,h))
#however you can enumerate a tuple in a stack
#backward counting from the surviving bar's height multiply length of array minus their inherited index
        for i,h in (stack):
            max_area=max(max_area, h*(len(heights)-i))


        return max_area

#enumerate a stack create another indexing of the stack [index,height] cant compare int and tuple

#you can append a sentinel value to the original array heights like heights.append(0) # The "Sentinel" - forces a final cleanup
#this will forces it go into while and calculate backward without using another for loop to calculate remaining ascending bars.
        