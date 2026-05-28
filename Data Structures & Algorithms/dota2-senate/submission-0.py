class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        rQ = deque()
        dQ = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                rQ.append(i)
            else:
                dQ.append(i)

        while rQ and dQ:
            r = rQ.popleft()
            d = dQ.popleft()

            if r < d:
                rQ.append(r+n)
            else:
                dQ.append(d+n)

        return 'Radiant' if rQ else 'Dire'