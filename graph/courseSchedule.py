from collections import defaultdict


class Solution:
    @classmethod
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


numCourses = 2
prerequisites = [[1, 0]]
res = Solution.canFinish(numCourses, prerequisites)
print(res)
prerequisites = [[1, 0], [0, 1]]
res = Solution.canFinish(numCourses, prerequisites)
print(res)
