class Solution:
    def BinarySearch(self, low, high, nums, target):
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            if nums[mid] > target:
                high = mid - 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        # fin min first and sort
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        minValIdx = high

        if nums[minValIdx] == target:
            return minValIdx
        if minValIdx >= 1 and nums[minValIdx-1] == target:
            return minValIdx - 1

        if nums[minValIdx] <= target <= nums[-1]:
            index = self.BinarySearch(minValIdx, len(nums)-1, nums, target)
            return index
        else:
            index = self.BinarySearch(0, len(nums) - 1 - minValIdx, nums, target)
            return index

