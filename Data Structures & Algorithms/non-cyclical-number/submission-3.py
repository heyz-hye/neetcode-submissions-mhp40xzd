class Solution:
    def isHappy(self, n: int) -> bool:
        map={}
        
        while n!=1:
            sum=0
            if n not in map:
                map[n]=1
                for i in range(len(str(n))):
                    sum+=(n%10)**2
                    n=n//10
                n=sum
            else:
                return False

        return True