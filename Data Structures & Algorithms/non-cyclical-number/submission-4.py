class Solution:
    def isHappy(self, n: int) -> bool:
        map={}
        
        while n!=1:
            sum=0 # this rest the sum so it don't carry over when squared
            if n not in map:
                map[n]=1
                for i in range(len(str(n))):
                    sum+=(n%10)**2
                    n=n//10 # use double // to separate each integer ending, because floor giving all number before last
                n=sum
            else:
                return False

        return True