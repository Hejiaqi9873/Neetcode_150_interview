# 853. Car Fleet

from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zip_pos_speed = list(zip(position, speed))
        sorted_item = sorted(zip_pos_speed, key=lambda x: x[0], reverse=True)
        stack = []
        for item in sorted_item:
            pos = item[0]
            sped = item[1]
            time = (target - pos) / sped
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

if __name__ == "__main__":
    solution = Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
    print(solution)
