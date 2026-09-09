class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_col = [mat[0] for mat in matrix]

        low, high, row = 0, len(matrix) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if first_col[mid] <= target:
                row = mid
                low = mid + 1
            else:
                high = mid - 1
            
        if row == -1:
            return False
        
        arr = matrix[row]
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
        
        return False
