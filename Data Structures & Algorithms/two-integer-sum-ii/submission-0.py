class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(numbers):
            remainder = target - num
            if remainder in seen:
                return [seen[remainder]+1, index+1]
            else:
                seen[num] = index