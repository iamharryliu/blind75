class Solution:
    @classmethod
    def canFinish(self, numCourses, prerequisites):
        adj_list = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj_list[a].append(b)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True

            visited.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adj_list[course] = []
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
