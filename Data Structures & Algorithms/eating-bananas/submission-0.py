class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_minimum_rate(piles, k):
            cnt = 0
            for pile in piles:
                if pile <= k:
                    cnt += 1
                    continue
                if pile % k == 0:
                    cnt += pile // k
                else:
                    cnt += pile // k + 1
            return cnt        


        low = 1
        high = max(piles)
        # k_list = [i for i in range(low, high+1)]

        while low < high:
            mid = low + (high - low) // 2
            if calculate_minimum_rate(piles, mid) <= h:
                high = mid
            elif calculate_minimum_rate(piles, mid) > h:
                low = mid + 1
        return low
