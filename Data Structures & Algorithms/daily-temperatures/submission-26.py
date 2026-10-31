class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature=[0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]:
                ind,val=stack.pop()
                day=i-ind
                temperature[ind]=day
            
            stack.append([i,temperatures[i]])
        return temperature