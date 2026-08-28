class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = collections.defaultdict(list)
        for c, prereq in prerequisites:
            adjList[c].append(prereq)
            adjList[prereq]
        
        # run dfs on every node
        # if we hit a node we already visited in current run, return false
        # if we hit a node we already visisted in previous run, return true
        allVisited = set()
        visited = set()
        def dfs(c, visited):
            if c in visited:
                return False
            if c in allVisited:
                return True
            
            visited.add(c)
            for prereq in adjList[c]:
                if not dfs(prereq, visited):
                    return False
                allVisited.add(prereq)
            visited.remove(c)
            return True
        
        for c in adjList:
            if not dfs(c, visited):
                return False
            allVisited.add(c)
        
        return True

