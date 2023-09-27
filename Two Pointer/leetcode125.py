# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # create a left pointer and a right pointer
        p1 = 0
        p2 = len(s) - 1
        # use a while loop
        while p1 < p2:
            while p1 < p2 and s[p1].isalnum() == False:
                p1 += 1
            while p2 > p1 and s[p2].isalnum() == False:
                p2 -= 1
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True


if __name__ == "__main__":
    solution = Solution().isPalindrome(s = ".,")
    print(solution)