'''
I have no idea how to do this until i watch neetcode.

approach:
encode:
you can put a hashtag beore a string and state the length of the string to append. The reason why we choose 4#tace
is because you might have string with hashtag as a part of the string and that mess up our encoding.

decode:
you initiate with an i pointer to go through the encode string
you read the first number you encounter until you hit a hashtag which mean that part of the string will be your length,
so you have to append length of the string after the hashtag
then you set your i pointer to the index after the string is finished

time compleixty:
O(N) encode and decode since you only go throug the string once

space complexity:
O(1) for res in encode
O(N) for every string append to the list
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i=j+1+length

        return res


