class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        array=[0]*len(temperatures)

        if len(temperatures)==1 or len(temperatures)==0:
            return [0]

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                    x=stack.pop()
                    array[x]=i-x

            stack.append(i)
            
        return array
                    

   
        
        
        