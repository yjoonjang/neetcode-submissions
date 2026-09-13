class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1
        suffix_product = 1
        output = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            output[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]
            # prefix = nums[:i]
            # if i <= len(nums) - 1:
            #     suffix = nums[i+1:]
            # else:
            #     suffix = []
            
            # product = 1
            # for pre in prefix:
            #     product *= pre
            # for suf in suffix:
            #     product *= suf
            
            # output.append(product)


        return output