class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dig_to_let = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        def backtrack(start, path):
            if len(path) == len(digits):
                res.append(''.join(path[:]))
                return

            for i in range(start, len(digits)):
                letters = dig_to_let[digits[i]]
                for ch in letters:
                    path.append(ch)
                    backtrack(i+1, path)
                    path.pop()

        backtrack(0, [])
        return res