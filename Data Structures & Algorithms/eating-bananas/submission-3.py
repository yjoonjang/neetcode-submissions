class Solution:
    def getEatingTime(self, piles, k):
        res = 0
        for pile in piles:
            res += math.ceil(pile / k)
        return res
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ks = []
        while low <= high:
            mid = low + (high - low) // 2
            if self.getEatingTime(piles, mid) <= h:
                ks.append(mid)
                high = mid - 1
            if self.getEatingTime(piles, mid) > h:
                low = mid + 1

        return min(ks)
