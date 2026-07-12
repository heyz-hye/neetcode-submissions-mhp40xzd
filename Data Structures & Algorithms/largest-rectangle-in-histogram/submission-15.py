'''
You only push after popping everything taller than h. So at any point, 
stack heights go bottom→top from smallest to largest. 
That invariant is what makes the while condition (stack[-1][1] > h) correct 
— it's how you detect "this bar closes off a rectangle."
Why start = index matters
When you pop a bar, its rectangle's left boundary isn't index for the next comparison — 
it's whatever the popped bar's own start was. 
Bars between the popped bar's start and i are all ≥ its height (otherwise they'd have popped it already), 
so the rectangle can legally extend back that far. 
This is what replaces the need for a separate "left boundary" array that many solutions use.
The two area formulas

Mid-loop pop: (i - index) * height — width is bounded on the right by the current bar (exclusive), left by index.
Cleanup loop: (len(heights) - index) * height — width is bounded on the right by the end of the array, 
since nothing ever came along to pop it.

Operator precedence: i - index * height ≠ (i - index) * height. 
Always parenthesize the width before multiplying by height.
Off-by-one on width: the popped bar's rectangle is i - index wide, not i - index + 1 — 
because i itself is the bar that's shorter, so it's excluded.
Mutable input: the sentinel-append version (heights.append(0)) mutates the caller's list — 
fine for LeetCode's single-call harness, but worth remembering if reused.
'''
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

       
        