class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumArea = 0
        # for i in range(len(heights)):
        l_idx = 0
        r_idx = len(heights) - 1
        while l_idx < r_idx:
            width = r_idx - l_idx
            height = min(heights[l_idx], heights[r_idx])
            area = width * height
            if area > maximumArea:
                maximumArea = area

            if heights[l_idx] <= heights[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
            
            # r_idx -= 1
            # l_idx += 1
        return maximumArea


