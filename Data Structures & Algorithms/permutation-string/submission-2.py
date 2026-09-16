from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2):
            if s1 == s2:
                return True
        window_len = len(s1)
        s1_counts = Counter(s1)
        for i in range(len(s2)-1):
            s2_substring = s2[i:i+window_len]
            s2_substring_counts = Counter(s2_substring)
            if s1_counts == s2_substring_counts:
                return True
        
        return False

            