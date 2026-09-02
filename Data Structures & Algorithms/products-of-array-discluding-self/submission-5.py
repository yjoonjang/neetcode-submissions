class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        zero_count = 0
        isAllZero = False

        for num in nums:
            if num == 0:
                zero_count += 1
        
        if zero_count == len(nums):
            isAllZero = True
        
        for num in nums:
            if num != 0:
                all_product *= num
        
        if isAllZero or zero_count >= 2:
            all_product = 0
        
        output = []
        if zero_count >= 1:
            for num in nums:
                if num != 0:
                    output.append(0)
                else:
                    output.append(all_product)
        else:
            for num in nums:
                output.append(all_product // num)

        return output



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix 
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output

