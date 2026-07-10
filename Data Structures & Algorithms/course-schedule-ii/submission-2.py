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
        visit=set()
        safe=set()
        table={}
        self.res=[]

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in table:
                table[prerequisites[i][0]]=[prerequisites[i][1]]
            else:
                 table[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(prerequisites)->bool:
            if prerequisites in safe:
                return True
            if table.get(prerequisites,[])==[]:
                self.res.append(prerequisites)
                safe.add(prerequisites)
                return True
            if prerequisites in visit:
                return False
            visit.add(prerequisites)
            for i in table[prerequisites]:
                if not dfs(i):
                    return False
            self.res.append(prerequisites)
            visit.remove(prerequisites)
            safe.add(prerequisites)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
   
        return self.res
        