class Solution:
    @classmethod
    def canFinish(self, numCourses, prerequisites):

        # Create map of prereqs {course: [...prereqs]} and set for visited
        prerequisiteMap = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            prerequisiteMap[course].append(prerequisite)
        visited = set()

        def dfs(course):
            # base cases
            if course in visited:
                return False
            if prerequisiteMap[course]  == []:
                return True
            # dfs course prerequestites
            visited.add(course)
            for prerequisite in prerequisiteMap[course]:
                if not dfs(prerequisite): return False
            # done dfs so we can remove the course from the visited nodes
            visited.remove(course)
            # completed dfs so we don't need to visit its prereqs again
            prerequisiteMap[course] = []
            return True
        # loop through courses and run dfs on them
        for course in range(numCourses):
            if not dfs(course): return False
        return True

numCourses =  2
prerequisites = [[1,0]]
res  = Solution.canFinish(numCourses, prerequisites)
print(res)
prerequisites = [[1,0], [0,1]]
res  = Solution.canFinish(numCourses, prerequisites)
print(res)