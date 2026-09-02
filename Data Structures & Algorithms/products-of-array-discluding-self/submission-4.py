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



# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         output = []
#         all_product = 1
#         for i in range(nums):
#             output[i] = all_product * nums[0:i]
