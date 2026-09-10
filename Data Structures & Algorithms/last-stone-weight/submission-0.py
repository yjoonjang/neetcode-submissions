import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for stone in stones:
            heapq.heappush(hq, -stone)
        while len(hq) >= 2:
            stone1 = heapq.heappop(hq)
            stone2 = heapq.heappop(hq)
            newStone = stone1 - stone2
            if newStone != 0:
                heapq.heappush(hq, newStone)
        if len(hq) == 1:
            return -hq[0]
        else:
            return 0
        