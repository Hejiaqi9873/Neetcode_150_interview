# 11. Container With Most Water
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxarea = 0
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            if cur > maxarea:
                maxarea = cur
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

if __name__ == "__main__":
    solution = Solution().maxArea(height = [1,8,6,2,5,4,8,3,7])
    print(solution)