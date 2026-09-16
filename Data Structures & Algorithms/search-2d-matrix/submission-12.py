class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        headers = [row[0] for row in matrix]
        row_idx = len(matrix) - 1
        for i in range(len(headers) - 1):
            if headers[i] <= target < headers[i+1]:
                row_idx = i
                break
        
        new_matrix = matrix[row_idx]
        low = 0
        high = len(new_matrix) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if new_matrix[mid] == target:
                return True
            if new_matrix[mid] > target:
                high = mid - 1
            if new_matrix[mid] < target:
                low = mid + 1
        return False
