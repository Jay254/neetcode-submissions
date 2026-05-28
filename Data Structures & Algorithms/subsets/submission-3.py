class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []

        # def backtrack(start, path):
        #     nonlocal res
        #     res.append(path[:])

        #     for i in range(start, len(nums)):
        #         path.append(nums[i])
        #         backtrack(i+1, path)
        #         path.pop()


        # backtrack(0, [])

        # return res
        res = []

        def backtrack(start, path):
            nonlocal res
            if start == len(nums):
                res.append(path[:])
                return

            backtrack(start+1, path + [nums[start]])
            backtrack(start+1, path)

            # for i in range(start, len(nums)):
            #     path.append(nums[i])
            #     backtrack(i+1, path)
            #     path.pop()

        backtrack(0, [])

        return res