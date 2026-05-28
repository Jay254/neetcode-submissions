class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = {i:[] for i in range(numCourses)}

        for u,v in prerequisites:
            graph[v].append(u)

        def dfs(target,cur, visited):
            # print(cur, target)
            if cur == target:
                return True
            visited.add(cur)
            for neighbor in graph[cur]:
                if neighbor not in visited and dfs(target, neighbor, visited):
                    return True

            return False


        res = []
        for a,b in queries:
            can_finish = dfs(a,b, set())
            res.append(can_finish)

        return res