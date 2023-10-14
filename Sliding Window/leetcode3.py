# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        right = 1
        queue_item = [s[0]]
        max_len = 1
        while right < len(s):
            if s[right] not in queue_item:
                queue_item.append(s[right])
                right += 1
                if len(queue_item) > max_len:
                    max_len = len(queue_item)
            else:
                if len(queue_item) > max_len:
                    max_len = len(queue_item)
                index = queue_item.index(s[right])
                queue_item = queue_item[index+1:]
                queue_item.append(s[right])
                right += 1


        return max_len

if __name__ == "__main__":
    solution = Solution().lengthOfLongestSubstring(s="pwwkew")
    print(solution)