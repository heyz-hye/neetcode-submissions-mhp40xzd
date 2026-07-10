'''
you take the annswer from class schedule and make some changes to it.
In this dfs solution when you reach the end of the path you append the course
and also you append the course when you finish all its prerequistes, when the course explore every possible neighbor
from this path you append it 
when there exist a loop you return an empty list

mistakes:
you need to loop through every single course because some course doesn;t show up in the prerequsites relation list
since you loop through numCourses instead of first element in every prerequisites relation tuple
you need to add the course to the safe set so it doesn't re explore the same path thus adding duplicate elements to your answer

'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        completed=0
        table={}
        degree={}
        q=deque()
        res=[]

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
                res.append(course)
                completed+=1
                for c in table[course]:
                    degree[c]-=1 #check after degree for this course decremented
                    if degree[c]==0:
                        q.append(c)
        if completed==numCourses:
            return res
        else:
            return []
        