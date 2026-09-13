class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # deduplicated_nums = sorted(list(set(nums)))
        nums_set = set(nums)
        deduplicated_nums = sorted(list(nums_set))
        
        max_count = 0
        cnt = 1
        for num in deduplicated_nums:
            if num+1 in nums_set:
                cnt += 1
            else:
                if cnt > max_count:
                    max_count = cnt
                cnt = 1
        
        return max_count
