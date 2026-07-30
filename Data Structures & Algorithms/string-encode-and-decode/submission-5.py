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

several mistakes:
we are returning a string in encode, string have no append method 
you need to use += and also type cast length of the individual word from int to string to concatenate or else you
will run into an error

if s[j] is not a hashtag we need to keep increment j by j+=1 and also use a while loop instead of a if statement

time compleixty:
O(N) where N is the total number of characters across all strings — this part's right for both encode and decode
worst case i is a bunch of individual characters

space complexity:
O(N) for res in encode because res is made up of n character 
O(N) for every string append to the list

you cant concatenate list to string also if you cast str to list you will make the list with the brackets as a string
both are O(N)
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
            
            length=int(s[i:j]) #you can do only s[j-1] because your encoding string can have a long int like 10#iloveubaby, you need 1 number to capture the full length.
            res.append(s[j+1:j+1+length]) #not including j because j is at postion of the hashtag, so stop before it
            i=j+1+length
        return res


