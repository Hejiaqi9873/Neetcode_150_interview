# 739. Daily Temperatures

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair [number, index]

        for i, t in enumerate(temperatures):
            # check if the stack is empty or not
            if stack:
                # if cur number > last element of stack number
                while stack and t > stack[-1][0]:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                # after that, there is no element bigger than before
                stack.append([t, i])
            else:
                # add current to the first element of stack
                stack.append([t, i])
        return res

if __name__ == "__main__":
    solution = Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
    print(solution)