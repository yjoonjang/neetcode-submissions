class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        # for i in range(len(heights)-1):
        #     l = i
        #     for j in range(len(heights)-1):
        #         r = len(heights) - 1 - j
        #         if l >= r:
        #             break
        #         width = r - l
        #         height = min(heights[r], heights[l])
        #         if max < width * height:
        #             max = width * height
        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            if max < width * height:
                max = width * height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        
        return max