class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BinarySearch(num_list, low, high, target):
            while (low <= high):
                mid = low + (high - low) // 2
                if (num_list[mid] == target):
                    return mid
                elif (num_list[mid] > target):
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        low = 0
        high = len(nums) - 1

        return BinarySearch(nums, low, high, target)