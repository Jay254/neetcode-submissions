class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        char_dic = {}
        max_len = 0
        max_count = 0

        while right < len(s):
            char = s[right]

            char_dic[char] = char_dic.get(char,0) + 1

            max_count = max(max_count, char_dic[char])

            window = right - left + 1

            if window - max_count > k:
                char_dic[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right-left+1)

            right += 1

        return max_len
