class Solution:
    def findMinIdx(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return high

    def binarySearch(self, nums, low, high, target):
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        minIdx = self.findMinIdx(nums)
        if minIdx == 0:
            return self.binarySearch(nums, 0, len(nums)-1, target)
        if target >= nums[0]:
            return self.binarySearch(nums, 0, minIdx - 1, target)
        else:
            return self.binarySearch(nums, minIdx, len(nums) - 1, target)
        
        


