class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_i = {ch:i for i,ch in enumerate(s)}
        start = 0
        end = 0
        res = []

        for i,ch in enumerate(s):
            end = max(end, last_i[ch])
            if i == end:
                res.append(end-start+1)
                start = end+1

        return res
