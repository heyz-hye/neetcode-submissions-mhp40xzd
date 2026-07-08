'''
bfs solution, this is very emmeory efficient as you only store the degrees and the table hashmap
it is basically a better version of dfs with equivalent in time comeplexity
so in this solution you map it coursee that ever exisit to two hashmap
one that record its neighbors it must map prerequisites to courses(unlike dfs,)
one that record the amount of neightbors a course have
we also have variable that keep track of completion of each course fully by satisfying its requirement
each course start off with a degree of zero

for any course that have a degree of zero we append to the queue
we will pop it from the queue and increment the complete counter by one
for each course we pop we explore the degree of its courses/neighbors and minus its degrees
we check for any neightbors that have a degree of zero after the pop we append it back to the queue
if we exit the queue we check if the complete variable is equal to the number of courses and return 
a boolean value

the first set of courses we append to q is the courses with zero degree
this problem can't map course as key to prereq because this algorithm behave in a way that is like peeling
a onion you have to peel all the outter layer skin before we can peel the inner layers
(you have to go from bottom up).
t's not quite that "courses with no prerequisites aren't mapped to a neighbor" — 
those courses have degree 0 either way, they'd still get into the initial queue fine. 
The actual break is: once you pop a course, you need to know what does finishing this unlock, 
so you can decrement those neighbors. If table[course] holds "my prerequisites" instead, 
then when you pop course and look at table[course], 
you're looking at things that must happen before course — decrementing their degree makes no sense, 
because they're not waiting on course at all, course was waiting on them. 
You'd be decrementing the wrong nodes' degrees entirely, not just failing to traverse.
to, hence the algorithm fails.
however for dfs the graph can go birection because going backward and forward don't make any difference
dfs only care if there is a cycle


'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        completed=0
        table={}
        degree={}
        q=deque()

        for t in range(numCourses):
            degree[t]=0
            table[t]=[]
        
        for i in range(len(prerequisites)):
            course,pre=prerequisites[i][0],prerequisites[i][1]
            table[pre].append(course)
            degree[course]+=1
            

        for e in range(numCourses):
            if degree[e]==0:
                q.append(e)
        

    
        while q:
            for j in range(len(q)):
                course=q.popleft()
                completed+=1
                for c in table[course]:
                    degree[c]-=1 #check after degree for this course decremented
                    if degree[c]==0:
                        q.append(c)
        return completed==numCourses
            

                    
            

                
        






        



        