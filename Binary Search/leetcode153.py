# 153. Find Minimum in Rotated Sorted Array
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = float('inf')
        while left <= right:
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left += 1
            else:
                right -= 1
                if nums[mid] < res:
                    res = nums[mid]

        return res

if __name__ == "__main__":
    solution = Solution().findMin(nums = [0])
    print(solution)
