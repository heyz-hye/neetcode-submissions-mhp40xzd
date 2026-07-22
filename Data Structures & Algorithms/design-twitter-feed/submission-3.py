'''
"""
LeetCode 355 - Design Twitter

Approach: heap (for k-most-recent merge) + hashmap for per-user tweets + set for follows.

MISTAKES MADE DURING THIS PROBLEM (for future review):

1. Tried to use self.userId.tweet / self.followerId.followlist
   - userId/followerId are just local int params, not attribute names.
   - Python doesn't let you dynamically turn a variable's VALUE into an attribute name
     via dot notation. Needed per-user storage instead -> use a dict keyed by userId
     (defaultdict(list) for tweets, defaultdict(set) for follows).

2. Used tweetId itself as the recency/sort key
   - Problem only guarantees tweetIds are unique, NOT that they increase over time.
   - Needed a separate monotonically increasing global counter (self.time),
     incremented once per postTweet call, stored alongside the tweetId.
   - Lesson: "unique" != "ordered". Don't conflate an ID with a timestamp.

3. Stored tweets as self.userbase[userId].append([tweetId]) -- wrapped in an extra list
   - Made the loop variable `i` a list instead of a number, so `-i` threw
     TypeError: bad operand type for unary -: 'list'

4. Wrote `for t self.userId.followlist:` -- missing `in` -> SyntaxError

5. Used a list for self.following instead of a set
   - follow() called twice on same followeeId -> duplicate entries -> duplicate
     tweets counted twice in the heap.
   - unfollow() using list.remove(x) raises ValueError if x isn't present.
   - Fixed with set: O(1) add/discard, naturally dedups, and .discard() is a
     no-op if the element isn't there (no crash).

6. `selftime += 1` instead of `self.time += 1`
   - Missing the dot means Python treats `selftime` as a brand new local variable,
     not an attribute -> UnboundLocalError since it was never defined before.

7. Used bare `time` instead of `self.time` when appending to userbase
   - Referenced an undefined name (or the wrong `time` if the time module was
     ever imported) instead of the instance's counter.

8. Pushed only the timestamp onto the heap, discarding the tweetId
   - `maxheap.append(-tim)` -> heap had no way to know which tweetId the
     timestamp belonged to. Needed to push [-tim, id] (or a tuple) together,
     so the tweetId can be recovered after popping.

9. After fixing #8, forgot to update the return line to match
   - Kept doing `-heapq.heappop(maxheap)` on what was now a [-tim, id] pair,
     which tries to negate an entire list -> TypeError.
   - Needed heapq.heappop(maxheap)[1] to pull out just the id.

10. Applied the negation AFTER indexing instead of only negating the timestamp
    - Wrote `-heapq.heappop(maxheap)[1]`, which evaluates as
      -(heappop(maxheap)[1]) -- negates the tweetId itself (e.g. 42 -> -42).
    - The negation trick (heapq is a min-heap, so store -timestamp to simulate
      max-heap behavior) only ever applies to the timestamp, index [0].
      The tweetId at index [1] should come out untouched.
    - Fix: heapq.heappop(maxheap)[1]  (no leading minus at all)

CORE TAKEAWAYS:
- self.<param_name> is never valid; params are just values, not attribute paths.
- ID uniqueness =/= chronological order; track time explicitly when order matters.
- When negating for a min-heap-as-max-heap trick, only negate the sort key,
  not the payload you're carrying along in the tuple/list.
- Set > list for membership/removal when duplicates would break correctness
  and O(1) is available.
"""

solution approach:
since the userid and tweetid are all int they cannot be use as name as self.
you will need two table:
1.map each user to tweet
2.map user to their following person
then you need a time counter that can be reference through the function call to keep track of recency
because the problem doesn't say that you can you can compare the recency of tweet through value of tweetid
every time a tweet is send then you can increment the time counter, you need to append tweet id and time into the userbase table

gets newfeed implementation:
you want to use maxheap that heapify the time,tweetid as a pair because the most recent tweet is the latest time
before you actually heapify you want to append all the user tweet to maxheap
and append all of their following person's tweet into the heap as well, if the following set is not empty and list exist you append
then you call heapify on maxheap, you return 10 most recent tweetid if the length of the maxheap is equal to or greater than 10
else you return the existing length of the maxheap in order of recent to latest

you map int to set for following table because if a person following multiple person once it should have the effect of following that person
once also the remove have O(1) time complexity. There is two edge cases when handling the last two function
the first edge case:
what is the person is following themselves?
you shouldnt return duplicate tweets, therefore you don't allow the person to follow himself
what if you try to unfollow someone but you never have followed that userid in the first place? you get an error
remove only if the userid exist in the set already, you use the discard function call instead of remove, discard handle the issue perfectly

TIME COMPLEXITY

Let:
  U = number of users
  M = max number of tweets any single user has posted
  F = number of people a user follows (followees)
  T = total tweets across the user + all their followees combined
      (this is the real driver of getNewsFeed's cost, not U or F alone)

postTweet(userId, tweetId):        O(1)
    - append to a list, increment a counter -- both constant time.

follow(followerId, followeeId):    O(1)
    - set.add() is O(1) average.

unfollow(followerId, followeeId):  O(1)
    - set.discard() is O(1) average, and never raises if absent.

getNewsFeed(userId):                O(T)
    - Appending the user's own tweets + all followees' tweets to maxheap: O(T)
      (you touch every relevant tweet exactly once)
    - heapq.heapify(maxheap): O(T)
      (heapify is linear in the number of elements -- NOT T log T;
       that complexity belongs to pushing elements one at a time with
       heappush, which we are not doing here)
    - Popping up to 10 items: O(log T) per pop -> O(10 log T) = O(log T)
      since 10 is a constant
    - Overall: O(T) dominates, so getNewsFeed is O(T)


SPACE COMPLEXITY

userbase (tweets):   O(U * M)  worst case
    - U users, each storing up to M tweets as [tweetId, timestamp] pairs.

following:            O(E)
    - E = total follow edges across all users (at most U^2 in the
      worst case where everyone follows everyone, but realistically
      much sparser).

maxheap (per call):   O(T)
    - temporary space used inside a single getNewsFeed call, released
      after the function returns -- not persistent storage.

Overall persistent space: O(U*M + E)
Overall space during a getNewsFeed call: O(U*M + E + T)

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

        
