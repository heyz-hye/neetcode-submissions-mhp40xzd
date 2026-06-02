'''
sort the list in ascending order
we should have a left and right pointer, with left pointing to the lightest and the right pointing
to the heaviest.
match the heaviest to the lightest if that doesn't work then the heaviest should be on the boat on its own
then we move to the second heaviest, if they match we should count them as one boat. move both pointer
if the list ever come together on the same index, then we run out of element to match and we break out of the
while loop
sorted dont modify original list while sort does.

'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left=0
        right=len(people)-1
        count=0

        people.sort()

        while left<=right:
            if people[left]+people[right]<=limit:
                right-=1
                left+=1
                count+=1
            elif left==right:
                count+=1
                break
                
            else:
                right-=1
                count+=1

        return count
            
        