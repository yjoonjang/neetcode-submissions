from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        unique_num_counts = list(counts.values())
        hasDuplicateNum = False
        for count in unique_num_counts:
            if count != 1:
                hasDuplicateNum = True
        return hasDuplicateNum