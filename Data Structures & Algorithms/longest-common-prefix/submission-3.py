class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars = strs[0]
        for s in strs[1:]:
            while not s.startswith(chars):
                chars = chars[:-1]
            
        return chars