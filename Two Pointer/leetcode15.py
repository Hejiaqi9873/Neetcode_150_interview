# 15. 3Sum
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. sort the nums
        sorted_nums = sorted(nums)
        output = []
        # use loop to get the answers
        previous = sorted_nums[0]
        for i in range(len(sorted_nums)):
            if i != 0 and sorted_nums[i] == previous:
                continue
            else:
                # 1. update previous
                previous = sorted_nums[i]
                # use method two sum to find b or c
                left = i + 1
                right = len(sorted_nums) - 1
                while left < right:
                    if sorted_nums[left] + sorted_nums[right] == -previous:
                        output.append([previous, sorted_nums[left], sorted_nums[right]])
                        left += 1
                        while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                            left += 1
                    elif sorted_nums[left] + sorted_nums[right] > -previous:
                        right -= 1
                    else:
                        left += 1

        return output

if __name__ == '__main__':
    solution = Solution().threeSum(nums = [-1,0,1,2,-1,-4])
    print(solution)