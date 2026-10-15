class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming_trust = defaultdict(int)
        outgoing_trust = defaultdict(int)

        for person, tr in trust:
            outgoing_trust[person] += 1
            incoming_trust[tr] += 1

        for person in range(1, n+1):
            if incoming_trust[person] == (n-1) and outgoing_trust[person] == 0:
                return person

        return -1
