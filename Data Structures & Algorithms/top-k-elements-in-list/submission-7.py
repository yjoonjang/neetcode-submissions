from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        nums_count = Counter(nums)
        heap = []

        for num in nums_set:
            count = nums_count[num]
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif heap[0][0] < count:
                heapq.heapreplace(heap, (count, num))
        
        return [num for c, num in heap]