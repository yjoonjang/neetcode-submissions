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

        

# from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         return [num for num, _ in count.most_common(k)]

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        
        arr.sort()
        res_temp = arr[-k:]
        res = []
        for entry in res_temp:
            res.append(entry[1])


        return res
