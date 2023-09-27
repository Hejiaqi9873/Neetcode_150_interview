# 167. Two Sum II - Input Array Is Sorted
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        output = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                output.append(left + 1)
                output.append(right + 1)
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return output
if __name__ == "__main__":
    solution = Solution().twoSum(numbers = [2,7,11,15], target = 9)
    print(solution)