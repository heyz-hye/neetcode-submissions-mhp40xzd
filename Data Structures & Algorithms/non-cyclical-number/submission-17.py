class Solution:
    def isHappy(self, n: int) -> bool:
        table={}
        

        while n!=1:
            sum=0
            for i in str(n):
                sum+=int(i)**2
            if sum in table:
                return False
            table[sum]=1
            n=sum
        return True
        