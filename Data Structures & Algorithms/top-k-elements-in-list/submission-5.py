from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = Counter(nums)
        count_num_list = []
        for num, count in num_counts.items():
            count_num_list.append((count, num))
        
        count_num_list.sort()
        output = []
        for (count, num) in count_num_list[-k:]:
            output.append(num)
        return output