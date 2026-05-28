class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(chs):
            l, r = 0, len(chs)-1
            while l <= r:
                if chs[l] != chs[r]:
                    return False
                l += 1
                r -= 1
            return True


        def backtrack(start, path):
            nonlocal res
            if start == len(s):
                res.append(path[:])

            for i in range(start, len(s)):
                if is_palindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtrack(i+1,path)
                    path.pop()


        backtrack(0, [])
        return res