class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0) # The "Sentinel" - forces a final cleanup
        stack = [] # (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index # Update start to the oldest index we just popped
            stack.append((start, h))
    
        return max_area
        