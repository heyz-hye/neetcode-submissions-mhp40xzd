'''
base on the position of the car, the distance between the card and the target will be different
the speed of the car can determine if the car will catch up with the other fleet side by side
car cannot surpass car ahead of it can only do side by side and travel at the same speed of the car
beside it, there I think i need to check when will the car meet side by side so I can increase count by one
for fleet if the car fleet never catch up then they will be individual car fleet of themselves.

use stack approach
the stack will start out empty, the stack will store index of the car

we can use a for loop to go through the entire postion array, and since the length of
two array are equal we only need to loop through one of the array

if remainding distance/speed of the stack is less than or equal to the remainding distance/speed then we
we have a car fleet so we append index to the stack

else we don't append but we keep a paramter call count and increment it

return count+len(stack)

try sorting
'''



class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Combine position and speed, then sort by position in descending order
        # This allows us to process cars from closest to the target, to furthest.
        #in python 3 zip return an iterable for memory efficiency it unpacks on the go
        #.sort() can only be use in list and don't return anything
        #sorted()work on any iterable and returns
        #reverse is true just make sure that it sort from last to first , greatest to lowest in this case
        #in letter case from Z to A, it also sort base on first index of the tuple
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for p, s in cars:
            # Calculate the time it takes for the current car to reach the target
            time = (target - p) / s
            stack.append(time)
            
            # If there are at least 2 cars, check if the car we just added catches up 
            # to the car ahead of it.
            # stack[-1] is the car behind, stack[-2] is the car ahead.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # The car behind catches up! They form a fleet.
                # We pop the current car's time because the fleet's arrival 
                # is dictated by the slower car ahead of it.
                stack.pop()
                
        # The number of items left in the stack represents the number of distinct fleets
        return len(stack)


        