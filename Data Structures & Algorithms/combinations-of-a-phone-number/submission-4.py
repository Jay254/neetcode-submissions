class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digs = {
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

        def traverse(idx, path):
            if len(path) == len(digits):
                res.append(path)
                return

            for ch in digs[digits[idx]]:
                traverse(idx+1, path+ch)

        traverse(0, '')
        return res