class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        # Edge case: if s1 is longer than s2, we can't find a permutation
        if s1_len > s2_len:
            return False
        
        # Count frequencies of characters in s1
        s1_count = Counter(s1)
        
        # Initialize a sliding window count for the first window of size s1_len in s2
        window_count = Counter(s2[:s1_len])
        
        # Slide the window across s2
        for i in range(s1_len, s2_len):
            # If the window count matches s1_count, return True
            if window_count == s1_count:
                return True
            
            # Slide the window: add one character and remove the leftmost one
            window_count[s2[i]] += 1
            window_count[s2[i - s1_len]] -= 1
            
            # Clean up zero-count keys to ensure proper comparison
            if window_count[s2[i - s1_len]] == 0:
                del window_count[s2[i - s1_len]]
        
        # Final check after the loop
        return window_count == s1_count