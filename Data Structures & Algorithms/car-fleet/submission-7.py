class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        car=sorted(zip(position,speed),reverse=True)


        for p,s in car:
            time=(target-p)/s
            stack.append(time)

            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)
        