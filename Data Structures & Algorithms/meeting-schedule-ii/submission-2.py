"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_room=0
        start=[]
        end=[]
        for interval in intervals: #interval is holding interval objects so it need access its field via the object way and not the standard for loop unpacking way
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        i=j=0
        room=0
        while i<len(start):
            if start[i]<end[j]:
                room+=1
                max_room=max(room, max_room)
                i+=1
            
            else:
                room-=1
                j+=1
        return max_room
        