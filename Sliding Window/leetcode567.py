# 567. Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(len(s1Count)):
            if s1Count[i] == s2Count[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True


            index_left = ord(s2[left]) - ord('a')

            s2Count[index_left] -= 1
            if s2Count[index_left] == s1Count[index_left]:
                matches += 1
            elif s1Count[index_left] - 1 == s2Count[index_left]:
                matches -= 1
            left += 1

            index_right = ord(s2[right]) - ord('a')
            s2Count[index_right] += 1
            if s2Count[index_right] == s1Count[index_right]:
                matches += 1
            elif s1Count[index_right] + 1 == s2Count[index_right]:
                matches -= 1

        if matches == 26:
            return True

        return False

if __name__ == "__main__":
    solution = Solution().checkInclusion(s1 = "abc", s2 = "bbbca")
    print(solution)