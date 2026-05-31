'''
if the number repeat it is cyclic which mean it return False if it is acyclic it return True. Only case if it is repeat and is True if it is repeating 1
to check if a number repeat we can use hashmap for  O(1) access time
to get the sum of each digit we need to convert the number to str and do a for loop for every digit
we then cast int of the letter and square it to add to the sum
every time the sum is calculated for a for loop it must also be resetted
if we see the sum in the hashmap we return false
if we see the su

'''


class Solution:
    def isHappy(self, n: int) -> bool:
        table={}
        sum=0

        while n:
            sum=0
            for i in str(n):
                sum+=int(i)**2
            if sum==1:
                return True
            if sum in table:
                return False
            table[sum]=1
            n=sum
        return True
        