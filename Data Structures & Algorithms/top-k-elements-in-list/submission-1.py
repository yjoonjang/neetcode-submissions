# from collections import defaultdict

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         nums_deduplicated = list(set(nums))
#         hash = defaultdict(list)

#         for num in nums_deduplicated:
#             hash[num] = nums.count(num)
        
#         output = []
#         for _ in range(k):
#             max_value = max(hash.values())
#             output.append(list(hash.keys())[list(hash.values()).index(max_value)])
#             hash.pop(list(hash.keys())[list(hash.values()).index(max_value)])
        
#         return output

        

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num, _ in count.most_common(k)]