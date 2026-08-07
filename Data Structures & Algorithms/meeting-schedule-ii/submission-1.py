'''
my approach is a two pointer approach:
first i will parse out the interval from the list, record the start time and end time in 
each separate list
we are going sorted the start and end list because we want to get earliest end time of the
meeting to see if there is any overlap between multiple early start time for meeting is there
is a overlap that mean we have increase the room, if there is no overlap that mean we can
subtract a room from use because we can obviously dedicated that room to the specific
start time for a meeting.
if the meeting takes up room we need a variable call room to keep track of how many rooms
we need at any specific time
we want to constanly get the max amount of room there is because that will be the minimum amount of room we need
therefore we only compare when we increase the room amount we need for minroom

edgecase:
if a starting time for a room overlapping with an ending time of a room, we do not consider it a conflict, therefore we can set up our condition, if the startting time is smaller
that the sorted ending time that mean we require more room and we need to compare, however
if the starting time is equal to the ending time or greater than it, that mean that room 
is at a different starting time and the current end time for the room dont have worry about it.

also if no intervals no room require

time complexity:
O(N)iterate through all the intervals and also we iterate through each components of
the interval.
O(NlogN)for sorting the star and en list, we do it two times, maybe we can improve by zipping then sorting to improve the amount of sorting we need
O(N)to go through the entire loop starting time.

space complexity
O(N) for star and en table

'''

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        star=[]
        en=[]
        minroom=0
        room=0
        for interval in intervals:
            star.append(interval.start)
            en.append(interval.end)
        
        star.sort()
        en.sort()
        i=0
        j=0

        while i<len(star):
            if star[i]<en[j]:
                room+=1
                minroom=max(room,minroom)
                i+=1
            elif star[i]>=en[j]:
                room-=1
                j+=1
        
        return minroom


            
        
        