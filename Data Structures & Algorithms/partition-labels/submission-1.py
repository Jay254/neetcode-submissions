class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {char: idx for idx,char in enumerate(s)}

        start = end = 0
        res = []

        for i, ch in enumerate(s):
            end = max(end,last[ch])
            if i == end:
                res.append(end-start+1)
                start = i+1

        return res