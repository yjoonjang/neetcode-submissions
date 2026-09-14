class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        sorted_nums = sorted(nums)
        
        for i in range(len(sorted_nums)):
            anchor = sorted_nums[i]
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                if anchor + sorted_nums[l] + sorted_nums[r] < 0:
                    l += 1
                elif anchor + sorted_nums[l] + sorted_nums[r] > 0:
                    r -= 1
                elif anchor + sorted_nums[l] + sorted_nums[r] == 0:
                    triplet = [sorted_nums[i], sorted_nums[l], sorted_nums[r]]
                    if triplet not in output:
                        output.append(triplet)
                    l += 1
                    r -= 1
        
        return output
            