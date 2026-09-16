from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        last = defaultdict(int)
        ch_count = defaultdict(int)
        start = 0
        best = 0

        for i, ch in enumerate(s):
            ch_count[ch] += 1
            ch_count_sorted_by_count = sorted(ch_count.items(), key=lambda kv: (-kv[1], kv[0]))
            while (i - start + 1 - ch_count_sorted_by_count[0][1] > k):
                ch_count[s[start]] -= 1
                start += 1
            best = max(best, i - start + 1)
        
        return best