class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the graph and compute in-degrees
        graph = defaultdict(list)
        in_degree = [0] * numCourses  # Initialize all in-degrees to 0

        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course
            in_degree[course] += 1  # Increase the in-degree of the course
        
        # Step 2: Initialize the queue with courses having no prerequisites (in-degree = 0)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Step 3: Process the courses in the queue
        taken_courses = 0
        
        while queue:
            course = queue.popleft()
            taken_courses += 1
            
            # For each course that depends on this course, reduce the in-degree
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:  # If in-degree is 0, it's available to take
                    queue.append(next_course)
        
        # Step 4: If we have taken all courses, return True
        return taken_courses == numCourses