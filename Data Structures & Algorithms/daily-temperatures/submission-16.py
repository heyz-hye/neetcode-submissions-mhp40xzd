class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Maintain a monotonically decreasing stack, 
        #temp = [30,38,30,36,35,40,28]
        #index = [5,6]
        res = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                res[top] = i-top

            stack.append(i)

        return res

        
        