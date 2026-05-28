class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
            
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, preq in prerequisites:
            indegree[course] += 1
            graph[preq].append(course)

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []

        while queue:
            course = queue.popleft()
            res.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return len(res) == numCourses

        