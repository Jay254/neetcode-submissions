class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #order doesn't matter -> permutations
        res = []
        candidates.sort()
        def backtrack(n, start, path):
            nonlocal res
            if n == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if n - candidates[i] < 0:
                    break
                path.append(candidates[i])
                backtrack(n-candidates[i], i+1, path)
                path.pop()

        backtrack(target, 0, [])

        return res