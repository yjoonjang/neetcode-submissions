class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        
        # for i in range(len(sorted_nums)):
        #     for j in range(i+1, len(sorted_nums)):
        #         for k in range(j+1, len(sorted_nums)):
        #             print(sorted_nums[i] + sorted_nums[j] + sorted_nums[k])
        #             if (sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0):
        #                 triple = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
        #                 if triple not in result:
        #                     result.append(triple)
        
        # return result
        for i, num in enumerate(sorted_nums):
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                three_sum = num + sorted_nums[l] + sorted_nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    triplet = [num, sorted_nums[l], sorted_nums[r]]
                    if triplet not in result:
                        result.append([num, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1

    
        return result
