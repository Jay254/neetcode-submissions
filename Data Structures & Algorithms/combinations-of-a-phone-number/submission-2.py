class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dig_str = {
            '2' : 'ABC',
            '3' : 'DEF',
            '4' : 'GHI',
            '5' : 'JKL',
            '6' : 'MNO',
            '7' : 'PQRS',
            '8' : 'TUV',
            '9' : 'WXYZ'
        }

        res = []
        def backtrack(start, path):
            if start == len(digits):
                res.append(''.join(path).lower())
                return

            letters = dig_str[digits[start]]
            for ch in letters:
                path.append(ch)
                backtrack(start+1,path)
                path.pop()


        backtrack(0, [])
        return res