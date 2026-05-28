class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # graph = defaultdict(list)
        # email_to_name = {}

        # for acc in accounts:
        #     name = acc[0]
        #     primary = acc[1]
        #     for email in acc[1:]:
        #         graph[primary].append(email)
        #         graph[email].append(primary)
        #         email_to_name[email] = name

        # def dfs(email, comp):
        #     visited.add(email)
        #     comp.append(email)
        #     for neighbor in graph[email]:
        #         if neighbor not in visited:
        #             dfs(neighbor, comp)

        # visited = set()
        # res = []

        # for email in graph:
        #     if email not in visited:
        #         comp = []
        #         dfs(email, comp)
        #         res.append([email_to_name[email]] + sorted(comp))

        # return res
        parent = {}

        def find(x):
            parent.setdefault(x,x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                union(first_email, email)
                email_to_name[email] = name

        roots = {}
        for email in email_to_name:
            root = find(email)
            roots.setdefault(root,[]).append(email)
        
        res = []
        for root_email, emails in roots.items():
            res.append([email_to_name[root_email]] + sorted(emails))

        return res

