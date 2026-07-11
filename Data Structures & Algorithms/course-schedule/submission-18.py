class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        safe=set()
        table={}

        #need to populate the table before we call anything
        for i in range(len(prerequisites)):
            if prerequisites[i][1] not in table:
                table[prerequisites[i][1]]= [prerequisites[i][0]]
            else:
                table[prerequisites[i][1]].append(prerequisites[i][0])

        def dfs(course)->bool:
            if course in safe:
                return True
            if course in visit:
                return False
            if table.get(course,[])==[]:
                return True
                safe.add(course) #you don't have to add to safe because this check is o(1) and also you loop
                                #through prerequsitites instad of numCourses
                                #in a directed graph a triangle connected relation doesn't always mean a loop
            visit.add(course)

            for i in table[course]:
                if not dfs(i):
                    return False
            visit.remove(course)
            safe.add(course)
            return True
        
        for t in range(len(prerequisites)):
            if not dfs(prerequisites[t][1]):
                return False
        return True



        