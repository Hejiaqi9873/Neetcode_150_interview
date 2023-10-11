# 121. Best Time to Buy and Sell Stock
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_min = prices[0]
        slow, fast = 0, 1
        while slow < len(prices) and fast < len(prices):
            if prices[fast] - prices[slow] > profit:
                profit = prices[fast] - prices[slow]
                fast += 1
                continue
            else:
                if prices[fast] < cur_min:
                    cur_min = prices[fast]
                    slow = fast
                    fast += 1
                    continue
            fast += 1


        return profit

if __name__ == "__main__":
    solution = Solution().maxProfit(prices = [7,6,4,3,1])
    print(solution)
