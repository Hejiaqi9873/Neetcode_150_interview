# 704. Binary Search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid_index = (left + right) // 2
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < target:
                left = mid_index + 1
            else:
                right = mid_index - 1
        return -1

if __name__ == "__main__":
    solution = Solution().search(nums = [1], target = 1)
    print(solution)
