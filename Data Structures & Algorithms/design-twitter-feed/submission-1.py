'''
posttweet function generate a tweetid for the userid

get news feed return 10 most recent item post by user or people user follower, so this should pull up all the user and the person they
follow's tweet and rank them in recent
tweet Id are all unique
follow connect user id with another user id
use set for follow to look up,O(1), use list even longer to loopup and remove
unfollow disconnect 
'''
class Twitter:

    def __init__(self):
        self.userbase=defaultdict(list)
        self.following=defaultdict(set)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userbase[userId].append([tweetId,self.time])
        self.time+=1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap=[]
        if self.userbase[userId]:
            for id,tim in self.userbase[userId]:
                maxheap.append([-tim,id])
        if self.following[userId]:
            for t in self.following[userId]:
                if self.userbase[t]:
                    for Id,Tim in self.userbase[t]:
                        maxheap.append([-Tim,Id])
        heapq.heapify(maxheap)

        if len(maxheap)>=10:
            return [heapq.heappop(maxheap)[1] for n in range(10)]
        else:
            return [heapq.heappop(maxheap)[1] for n in range(len(maxheap))]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

        
