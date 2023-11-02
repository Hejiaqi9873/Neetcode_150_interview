# 424. Longest Repeating Character Replacement
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count = defaultdict(int)
        max_length = 0
        window_len = 1
        prev_right = -1
        while left < len(s) and right < len(s):
            if right != prev_right:
                cur = s[right]
                count[cur] += 1

            # find the max value in count
            max_value = max(count.values())
            if window_len - max_value <= k:
                if window_len > max_length:
                    max_length = window_len
                prev_right = right
                right += 1
                window_len += 1
            else:
                cur_item = s[left]
                count[cur_item] -= 1
                left += 1
                window_len -= 1
                prev_right = right
        return max_length

if __name__ == '__main__':
    solution = Solution().characterReplacement(s = "ABABBAAA", k = 2)
    print(solution)
    