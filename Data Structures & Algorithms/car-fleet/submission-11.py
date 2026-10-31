class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        t=sorted(zip(position,speed), reverse=True)

        for p, s in t:
            time=(target-p)/s
            stack.append(time) # you add to the stack no matter what
            if len(stack)>=2 and stack[-1]<=stack[-2]: # lesser time to go to the target the better. that is why you pop
                stack.pop()

        return len(stack)

        