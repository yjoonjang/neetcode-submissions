class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort(reverse=False)
        cnt = 1

        consecutive_seq_counts = []
        for i in range(len(nums)):
            if i != 0:
                if (nums[i] - nums[i-1] == 1):
                    cnt += 1

                if (i >= 2) and (nums[i] - nums[i-1] != 1) and (nums[i-1] - nums[i-2] == 1) or i == len(nums) - 1:
                    consecutive_seq_counts.append(cnt)
                    cnt = 1
        
        if len(consecutive_seq_counts) == 0:
            return 1
        return max(consecutive_seq_counts)
