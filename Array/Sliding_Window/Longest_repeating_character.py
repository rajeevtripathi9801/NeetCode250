"""
Bruute Force is just create all the 4
"""
class Solution:
    """
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        for current1 in range(0, len(s)):
            count, maxf = {}, 0
            for current2 in range(current1, len(s)):
                count[s[current2]] = 1 + count.get(s[current2], 0)
                maxf = max(maxf, count[s[current2]])

                if (current2 - current1 + 1) - maxf <= k:
                    result = max(result, current2 - current1 + 1)

        return result
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        left = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result

if __name__ == "__main__":
    s = "ABABABAB"
    k = 2
    solution = Solution()
    res = solution.characterReplacement(s, k)
    print(res)