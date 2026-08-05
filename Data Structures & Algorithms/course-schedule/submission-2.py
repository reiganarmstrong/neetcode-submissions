class Solution:
    # 1-n courses
    # fail case cycle
    # all prereqs in 0 <= i < numCourses
    # dfs?
    # if cycle detected, return False
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjList
        adjList = collections.defaultdict(list)
        for i in range(numCourses):
            adjList[i]
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        confirmed = set()
        def dfs(course, visited = set()):
            if course in visited:
                return False
            if course in confirmed:
                return True

            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq, visited):
                    return False
            visited.remove(course)
            return True
        for course in adjList:
            if not dfs(course):
                return False
        return True