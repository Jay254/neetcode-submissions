class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(rem, start, path):
            nonlocal res
            
            if rem == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if rem - candidates[i] >= 0:
                    path.append(candidates[i])
                    backtrack(rem-candidates[i], i+1, path)
                    path.pop()


        backtrack(target, 0, [])

        return res