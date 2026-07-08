'''
In this problem you are checking if you finish all the courses, not learning one course 
can finish all the courses.
what you can do you can use a hashmap to map courses and its prerequisites. by mapping
we can go through every single prerequsiteis in the courses.

dfs solution:
if the course have no prerequsites we map it to an empty bracket, if we reach that course then we know
we learn that course, then we can return True, if the once we finish all the course's prerequsites we 
can safely return true because there is no cycle.

a cycle exist if along the path we are exploring we encounter a loop, for this we use a set to see if the
prerequsites we are encountering happens to be the course we called earlier, if there are no cycle then we
remove the course that was called from the set

we loop through the prerequisites lists and callled dfs on every single list so that there is no courses and
cycles left unchecked.

this is the raw solution, not optimize, because we are calling every single element in the list, every
time we call dfs, we have to perform dfs on its prerequisites. The built up the run time combinatorically.

btw maping course to prerequistes key to value
have the same correct solution as mapping prerequsites to course
because when we explore the prerequisites become the course, vice versa
we are trying to explore

optimization: we can perform a safe check, we can use a set to check
if the prerequisites we just explore is safe, so that we don't have to reexplore
again this cut down on the run time tremedously, so every time we finish a course's list
of prerequisites we can add that course to safe set().

if one of the path that we explore in the set have a loop we want to stop exploring and just return false
if all the courses are explored along with all the prerequisites we can return true.

the runtimes of the optimize code will have O(m+n) 
The bound comes from memoization ensuring each node and edge is processed exactly once, total, 
across the entire algorithm — 
regardless of whether the graph is one connected blob or many disconnected pieces.

without menmolization the run time is 2^d where d is the depth of the graph
and d can  be as large can v in the worst case

space complexity is going to be the depth of the search and the size of the visit and safe
set until it covers all the courses and prerequsites.

Driving loop — looping over prerequisites and using prerequisites[t][1] 
means you only ever start DFS from courses that appear as a prerequisite's dependency. 
Courses that never appear this way just get skipped (harmless here since they can't be part of a cycle), 
but it's cleaner and more correct in general to loop over range(numCourses) so every course actually gets visited/marked safe.
tips:
alway check visit set before you append to the visit set so you can start you dfs search and not immediately 
return False
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        safe=set()
        table={}
     

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in table:
                table[prerequisites[i][0]]=[prerequisites[i][1]]
            else:
                 table[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(prerequisites)->bool:
            if prerequisites in safe:
                return True
            if table.get(prerequisites,[])==[]:
                return True
            if prerequisites in visit:
                return False
            visit.add(prerequisites)
            for i in table[prerequisites]:
                if not dfs(i):
                    return False
            visit.remove(prerequisites)
            safe.add(prerequisites)
            return True
        
        for i in range(len(prerequisites)):
            if not dfs(prerequisites[i][0]):
                return False
   
        return True






        



        