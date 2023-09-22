# 22. Generate Parentheses
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parentheses if #open < n
        # only add close parentheses if #close < #open
        # valid -> open# == close# == n
        stack = []
        res = []

        def backtracking(openN, closeN):
            # basic case
            if openN == closeN == n:
                res.append("".join(stack))
                return

            # add open parentheses
            if openN < n:
                stack.append('(')
                backtracking(openN + 1, closeN)
                # when finish need to pop the last element
                stack.pop()

            if closeN < openN:
                stack.append(')')
                backtracking(openN, closeN + 1)
                stack.pop()

        # use the function
        backtracking(0, 0)
        return res

if __name__ == "__main__":
    solution = Solution().generateParenthesis(n = 3)
    print(solution)
