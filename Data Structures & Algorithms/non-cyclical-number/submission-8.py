class Solution:
    def isHappy(self, n: int) -> bool:
        smap={}
        
        while n!=1 and n not in smap:
            sum=0
            smap[n]=1
            for i in str(n):
                sum+=(int(i)%10)**2
            n=sum
                
        
        return n==1

        