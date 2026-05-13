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

        #you can do for digit in str(n) to extract each digit. and then type cast int on each digit and square it.
        #you can also do this n = sum(int(digit) ** 2 for digit in str(n))
        #two condtion if n!=1 and n not in set, set=()return n==1, this condition evaluate to true if n is one false if n is not 1