class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src,dest in tickets:
            graph[src].append(dest)

        for src in graph:
            graph[src].sort(reverse=True)

        itinerary = ["JFK"]

        total_tickets = len(tickets)

        def backtrack():
            if len(itinerary) == total_tickets + 1:
                return True

            last_stop = itinerary[-1]
            if last_stop not in graph:
                return False

            for i in range(len(graph[last_stop])-1,-1,-1):
                next_stop = graph[last_stop].pop(i)
                itinerary.append(next_stop)
                if backtrack():
                    return True

                itinerary.pop()
                graph[last_stop].insert(i,next_stop)


            return False


        backtrack()
        return itinerary