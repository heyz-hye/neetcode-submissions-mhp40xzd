class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            if self.stack[-1][1]<val:
                self.stack.append((val,self.stack[-1][1]))
            else:
                self.stack.append((val,val))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:

        return self.stack[-1][1]

       
