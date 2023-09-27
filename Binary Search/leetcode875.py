# 875. Koko Eating Bananas
from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_item = float('inf')
        # get the left and right pointer
        max_number = max(piles)
        min_number = 1
        flag = True
        while min_number <= max_number:
            # get the mid pointer
            mid_number = (max_number + min_number) // 2
            # check time
            time = 0
            for item in piles:
                time = time + ceil(item / mid_number)

            if time > h:
                min_number = mid_number + 1
            else:
                if mid_number < min_item:
                    min_item = mid_number
                max_number = mid_number - 1

        return min_item

if __name__ == '__main__':
    solution = Solution().minEatingSpeed(piles = [3,6,7,11], h = 8)
    print(solution)