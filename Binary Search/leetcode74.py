# 74. Search a 2D Matrix
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        # use binary search to find the row of target in
        # Time Complexity: O(logm)
        cer_row = 0
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                cer_row = mid
                break
        # then, still use binary search to find the target in that certain row
        # Time Complexity: O(logn)
        left, right = 0, len(matrix[cer_row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[cer_row][mid] < target:
                left = mid + 1
            elif matrix[cer_row][mid] > target:
                right = mid - 1
            else:
                return True
        # Time Complexity of this algorithm: O(logm + logn) = O(logm*n)
        return False

if __name__ == "__main__":
    solution = Solution().searchMatrix(matrix = [[1], [3]], target = 13)
    print(solution)
