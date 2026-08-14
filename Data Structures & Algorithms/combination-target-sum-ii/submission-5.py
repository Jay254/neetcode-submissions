class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def traverse(start, path, remainder):
            nonlocal res
            if remainder == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                if remainder - candidates[i] >= 0:
                    path.append(candidates[i])
                    traverse(i+1, path, remainder - candidates[i])
                    path.pop()

        traverse(0, [], target)
        return res