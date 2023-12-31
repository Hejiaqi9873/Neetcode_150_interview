from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return  mid
            if target > nums[mid]:
                if target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

            else: # target < nums[mid]
                if target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

if __name__ == "__main__":
    solution = Solution().search(nums = [5,1,3], target = 3)
    print(solution)
